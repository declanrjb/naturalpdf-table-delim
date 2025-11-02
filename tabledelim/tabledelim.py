import natural_pdf
from natural_pdf import PDF
import pandas as pd
import re
import math

__all__ = ['table_delim', 'find_by_regex', 'delineate_regions', 'slice_fitting_elem']

# accepts left, top, right, bottom
def sort_elems_by_dim(elems, dim):
    sorted_elems = []

    bb_ind = {
        'left': 0,
        'top': 1,
        'right': 2,
        'bottom': 3
    }[dim]

    while len(elems) > 0:
        cand_min = math.inf
        cand_elem = None
        for elem in elems:
            if elem.bbox[bb_ind] <= cand_min:
                cand_min = elem.bbox[bb_ind]
                cand_elem = elem
        sorted_elems.append(cand_elem)
        elems.remove(cand_elem)
    return sorted_elems

def intersection(page, regions):
    return page.create_region(
        max([region.bbox[0] for region in regions]),
        max([region.bbox[1] for region in regions]),
        min([region.bbox[2] for region in regions]),
        min([region.bbox[3] for region in regions])
    )

def find_by_regex(region, pattern):
    elems = region.find_all('text')
    return [elem for elem in elems if re.match(pattern, elem.text) is not None]

def delineate_regions(page, bbox, delims, direction='row'):
    if direction == 'row':
        return [page.create_region(
            bbox['left'],
            delims[i].bbox[1],
            bbox['right'],
            delims[i+1].bbox[1] - 1 if i < (len(delims) - 1) else delims[i].bbox[3]
        ) for i in range(0, len(delims))]
    elif direction == 'col':
        return [page.create_region(
            delims[i].bbox[0],
            bbox['top'],
            delims[i+1].bbox[0] - 1 if i < (len(delims) - 1) else delims[i].bbox[2],
            bbox['bottom']
        ) for i in range(0, len(delims))]
    else:
        raise ValueError("Please pass exactly one of 'row' or 'col' to param direction.")

def slice_fitting_elem(page, elem, direction='row'):

    if type(elem) == str:
        elem = page.find(elem)

    if direction == 'row':
        return page.create_region(
            0,
            elem.bbox[1],
            page.width,
            elem.bbox[3]
        )
    elif direction == 'col':
        return page.create_region(
            elem.bbox[0],
            0,
            elem.bbox[2],
            page.height
        )
    else:
        raise ValueError('Please pass exactly one of row, col to param direction.')

def table_delim(page, rows, cols, bbox={}):
    bbox = {
        'left': 0,
        'top': 0,
        'right': page.width,
        'bottom': page.height
    } | bbox

    if type(rows) == str:
        rows = page.find_all(rows)
    
    if type(cols) == str:
        cols = page.find_all(cols)

    rows = sort_elems_by_dim(rows, dim='top')
    cols = sort_elems_by_dim(cols, dim='left')

    rows = delineate_regions(page, bbox, rows, direction='row')
    cols = delineate_regions(page, bbox, cols, direction='col')

    df = pd.DataFrame([
        [intersection(page, [row, col]).extract_text() for col in cols]
        for row in rows
    ])

    return df