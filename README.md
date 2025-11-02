Proposed expansion to [natural_pdf](https://github.com/jsoma/natural-pdf) to identify tables by page elements or regular expressions. More effective in certain cases than methods reliant on OCR or page structure.

# Quickstart

Navigate to your project directory and clone this repository:

git clone https://github.com/declanrjb/naturalpdf-table-delim

Import the module in a new Python script or the interpreter:


```python
import tabledelim as td
```

For testing, you may also need to load the base natural_pdf library. (This project is in development. The goal is to incorporate these methods into natural_pdf itself.)


```python
import natural_pdf
from natural_pdf import PDF
```

# Structure

The table_delim approach to table scraping thinks of tables as structures of certain elements or patterns. Anything can be a table: not just grids of lines. The method excepts a set of elements (or specifier) that delineate rows and a set of elements (or specifier) delineate columns. The relevant regions are then calculated as the space between those elements.

Eg: Elements reading "AMERICAN AIRLINES" and "ALLEGIANT AIR" are passed as row delimiters. The first row is then a region the width of the passed bounding box with top equal to the top attribute of AMERICAN AIRLINES and bottom equal to the top attribute of ALLEGIANT AIR. Columns are calculated similarly with respect to the left and right attributes.

# Worked Examples

## Election Precinct Scraping

The inspiration for this method, which has proven able to handle precinct PDFs without rigorous visual table structure.


```python
pdf = PDF('demo/bergin_precincts.pdf')
page = pdf.pages[0]
page.show()
```




    
![png](README_files/README_9_0.png)
    




```python
left_margin = page.create_region(0, 0, 100, page.height)
rows = td.find_by_regex(left_margin, '\w+[\s0-9]*$')
```


```python
td.table_delim(page, 
    rows=rows, # text on the left hand side of the page consisting of at least one world followed by 0 or more digits
    cols='line:vertical[height>=20]', # vertical lines of height at least 20
    bbox = {
        'top': page.find('text:contains("PRESIDENT")').bottom # only apply this scrape to the part of the page below the first appearance of PRESIDENT
    })
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Allendale 1</td>
      <td>Early Voting</td>
      <td>485</td>
      <td>6</td>
      <td>1.24%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Allendale 1</td>
      <td>Election Day</td>
      <td>485</td>
      <td>82</td>
      <td>16.91%</td>
      <td></td>
      <td>6</td>
      <td>70</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>68</td>
      <td>3</td>
      <td>7</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allendale 1</td>
      <td>Mail-In</td>
      <td>485</td>
      <td>46</td>
      <td>9.48%</td>
      <td></td>
      <td></td>
      <td>41</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td>40</td>
      <td></td>
      <td>3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allendale 1</td>
      <td>Total</td>
      <td>485</td>
      <td>134</td>
      <td>27.63%</td>
      <td></td>
      <td>6</td>
      <td>116</td>
      <td>7</td>
      <td></td>
      <td></td>
      <td>114</td>
      <td>3</td>
      <td>10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allendale 2</td>
      <td>Early Voting</td>
      <td>257</td>
      <td>2</td>
      <td>0.78%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>Allendale 2</td>
      <td>Election Day</td>
      <td>257</td>
      <td>33</td>
      <td>12.84%</td>
      <td></td>
      <td></td>
      <td>29</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>29</td>
      <td>1</td>
      <td>2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>Allendale 2</td>
      <td>Mail-In</td>
      <td>257</td>
      <td>26</td>
      <td>10.12%</td>
      <td></td>
      <td></td>
      <td>23</td>
      <td>3</td>
      <td></td>
      <td></td>
      <td>23</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td>Allendale 2</td>
      <td>Total</td>
      <td>257</td>
      <td>61</td>
      <td>23.74%</td>
      <td></td>
      <td></td>
      <td>54</td>
      <td>5</td>
      <td></td>
      <td></td>
      <td>54</td>
      <td>3</td>
      <td>2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <td>Allendale 3</td>
      <td>Early Voting</td>
      <td>338</td>
      <td>2</td>
      <td>0.59%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>9</th>
      <td>Allendale 3</td>
      <td>Election Day</td>
      <td>338</td>
      <td>33</td>
      <td>9.76%</td>
      <td></td>
      <td></td>
      <td>32</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>26</td>
      <td>3</td>
      <td>3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>10</th>
      <td>Allendale 3</td>
      <td>Mail-In</td>
      <td>338</td>
      <td>43</td>
      <td>12.72%</td>
      <td></td>
      <td></td>
      <td>40</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>34</td>
      <td>3</td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>11</th>
      <td>Allendale 3</td>
      <td>Total</td>
      <td>338</td>
      <td>78</td>
      <td>23.08%</td>
      <td></td>
      <td></td>
      <td>74</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>62</td>
      <td>6</td>
      <td>7</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>12</th>
      <td>Allendale 4</td>
      <td>Early Voting</td>
      <td>501</td>
      <td>6</td>
      <td>1.20%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>13</th>
      <td>Allendale 4</td>
      <td>Election Day</td>
      <td>501</td>
      <td>45</td>
      <td>8.98%</td>
      <td></td>
      <td></td>
      <td>40</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td>41</td>
      <td>1</td>
      <td>1</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>14</th>
      <td>Allendale 4</td>
      <td>Mail-In</td>
      <td>501</td>
      <td>57</td>
      <td>11.38%</td>
      <td></td>
      <td></td>
      <td>57</td>
      <td></td>
      <td></td>
      <td></td>
      <td>49</td>
      <td>3</td>
      <td>3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>15</th>
      <td>Allendale 4</td>
      <td>Total</td>
      <td>501</td>
      <td>108</td>
      <td>21.56%</td>
      <td></td>
      <td></td>
      <td>103</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td>96</td>
      <td>4</td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>16</th>
      <td>Allendale</td>
      <td>Early Voting</td>
      <td>1581</td>
      <td>16</td>
      <td>1.01%</td>
      <td></td>
      <td></td>
      <td>15</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>16</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>17</th>
      <td>Allendale</td>
      <td>Election Day</td>
      <td>1581</td>
      <td>193</td>
      <td>12.21%</td>
      <td></td>
      <td>6</td>
      <td>171</td>
      <td>9</td>
      <td></td>
      <td></td>
      <td>164</td>
      <td>8</td>
      <td>13</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>18</th>
      <td>Allendale</td>
      <td>Mail-In</td>
      <td>1581</td>
      <td>172</td>
      <td>10.88%</td>
      <td></td>
      <td></td>
      <td>161</td>
      <td>8</td>
      <td></td>
      <td></td>
      <td>146</td>
      <td>8</td>
      <td>10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>19</th>
      <td>Allendale</td>
      <td>Total</td>
      <td>1581</td>
      <td>381</td>
      <td>24.10%</td>
      <td></td>
      <td>6</td>
      <td>347</td>
      <td>18</td>
      <td></td>
      <td></td>
      <td>326</td>
      <td>16</td>
      <td>23</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>20</th>
      <td>Alpine 1</td>
      <td>Early Voting</td>
      <td>465</td>
      <td>8</td>
      <td>1.72%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>21</th>
      <td>Alpine 1</td>
      <td>Election Day</td>
      <td>465</td>
      <td>162</td>
      <td>34.84%</td>
      <td></td>
      <td>12</td>
      <td>95</td>
      <td>20</td>
      <td>2</td>
      <td></td>
      <td>96</td>
      <td>9</td>
      <td>19</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>22</th>
      <td>Alpine 1</td>
      <td>Mail-In</td>
      <td>465</td>
      <td>30</td>
      <td>6.45%</td>
      <td></td>
      <td></td>
      <td>26</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>22</td>
      <td></td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>23</th>
      <td>Alpine 1</td>
      <td>Total</td>
      <td>465</td>
      <td>200</td>
      <td>43.01%</td>
      <td></td>
      <td>12</td>
      <td>124</td>
      <td>22</td>
      <td>2</td>
      <td></td>
      <td>123</td>
      <td>9</td>
      <td>23</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>24</th>
      <td>Alpine</td>
      <td>Early Voting</td>
      <td>465</td>
      <td>8</td>
      <td>1.72%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>25</th>
      <td>Alpine</td>
      <td>Election Day</td>
      <td>465</td>
      <td>162</td>
      <td>34.84%</td>
      <td></td>
      <td>12</td>
      <td>95</td>
      <td>20</td>
      <td>2</td>
      <td></td>
      <td>96</td>
      <td>9</td>
      <td>19</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>26</th>
      <td>Alpine</td>
      <td>Mail-In</td>
      <td>465</td>
      <td>30</td>
      <td>6.45%</td>
      <td></td>
      <td></td>
      <td>26</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>22</td>
      <td></td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>27</th>
      <td>Alpine</td>
      <td>Total</td>
      <td>465</td>
      <td>200</td>
      <td>43.01%</td>
      <td></td>
      <td>12</td>
      <td>124</td>
      <td>22</td>
      <td>2</td>
      <td></td>
      <td>123</td>
      <td>9</td>
      <td>23</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>28</th>
      <td>Bergenfield 1</td>
      <td>Early Voting</td>
      <td>426</td>
      <td>5</td>
      <td>1.17%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>29</th>
      <td>Bergenfield 1</td>
      <td>Election Day</td>
      <td>426</td>
      <td>36</td>
      <td>8.45%</td>
      <td></td>
      <td>2</td>
      <td>28</td>
      <td>5</td>
      <td></td>
      <td></td>
      <td>27</td>
      <td>3</td>
      <td>5</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>30</th>
      <td>Bergenfield 1</td>
      <td>Mail-In</td>
      <td>426</td>
      <td>32</td>
      <td>7.51%</td>
      <td></td>
      <td></td>
      <td>26</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td>24</td>
      <td>2</td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>31</th>
      <td>Bergenfield 1</td>
      <td>Total</td>
      <td>426</td>
      <td>73</td>
      <td>17.14%</td>
      <td></td>
      <td>2</td>
      <td>57</td>
      <td>10</td>
      <td></td>
      <td></td>
      <td>54</td>
      <td>5</td>
      <td>11</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>32</th>
      <td>Bergenfield 2</td>
      <td>Early Voting</td>
      <td>462</td>
      <td>1</td>
      <td>0.22%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>33</th>
      <td>Bergenfield 2</td>
      <td>Election Day</td>
      <td>462</td>
      <td>61</td>
      <td>13.20%</td>
      <td></td>
      <td>6</td>
      <td>49</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>41</td>
      <td>1</td>
      <td>16</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>34</th>
      <td>Bergenfield 2</td>
      <td>Mail-In</td>
      <td>462</td>
      <td>28</td>
      <td>6.06%</td>
      <td></td>
      <td></td>
      <td>23</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>19</td>
      <td>3</td>
      <td>3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>35</th>
      <td>Bergenfield 2</td>
      <td>Total</td>
      <td>462</td>
      <td>90</td>
      <td>19.48%</td>
      <td></td>
      <td>6</td>
      <td>73</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td>61</td>
      <td>4</td>
      <td>19</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>36</th>
      <td>Bergenfield 3</td>
      <td>Early Voting</td>
      <td>455</td>
      <td>4</td>
      <td>0.88%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>37</th>
      <td>Bergenfield 3</td>
      <td>Election Day</td>
      <td>455</td>
      <td>36</td>
      <td>7.91%</td>
      <td></td>
      <td>3</td>
      <td>30</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>26</td>
      <td>4</td>
      <td>5</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>38</th>
      <td>Bergenfield 3</td>
      <td>Mail-In</td>
      <td>455</td>
      <td>28</td>
      <td>6.15%</td>
      <td></td>
      <td></td>
      <td>22</td>
      <td>3</td>
      <td></td>
      <td></td>
      <td>23</td>
      <td>1</td>
      <td>3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>39</th>
      <td>Bergenfield 3</td>
      <td>Total</td>
      <td>455</td>
      <td>68</td>
      <td>14.95%</td>
      <td></td>
      <td>3</td>
      <td>55</td>
      <td>5</td>
      <td></td>
      <td></td>
      <td>53</td>
      <td>5</td>
      <td>8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>40</th>
      <td>Bergenfield 4</td>
      <td>Early Voting</td>
      <td>483</td>
      <td>1</td>
      <td>0.21%</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td>***</td>
      <td></td>
    </tr>
    <tr>
      <th>41</th>
      <td>Bergenfield 4</td>
      <td>Election Day</td>
      <td>483</td>
      <td>48</td>
      <td>9.94%</td>
      <td></td>
      <td>3</td>
      <td>33</td>
      <td>9</td>
      <td></td>
      <td></td>
      <td>34</td>
      <td>1</td>
      <td>6</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>42</th>
      <td>Bergenfield 4</td>
      <td>Mail-In</td>
      <td>483</td>
      <td>36</td>
      <td>7.45%</td>
      <td></td>
      <td>2</td>
      <td>31</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>26</td>
      <td>7</td>
      <td>2</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



Compared to an attempt to scrape the same page using base natural_pdf:


```python
pd.DataFrame(page.extract_table())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td></td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>None</td>
      <td></td>
      <td>Registered\nVoters</td>
      <td>Voters\nCast</td>
      <td>Turnout\n(%)</td>
      <td></td>
      <td>DEM\nBUKOVINAC\n-\nTERRISA</td>
      <td>DEM\n-\nJOSEPH\nBIDEN\nJr. R.</td>
      <td>UNCOMMITTED\nDELEGATES\nDEM\n-</td>
      <td>Write-ins</td>
      <td></td>
      <td>DEM\n-\nANDY\nKIM</td>
      <td>LAWRENCE\nHAMM DEM\n-</td>
      <td>DEM\n-\nCAMPOS- PATRICIA\nMEDINA</td>
      <td>Write-ins</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allendale 1\nAllendale 1\nAllendale 1\nAllenda...</td>
      <td>Early Voting\nElection Day\nMail-In\nTotal\nEa...</td>
      <td>485\n485\n485\n485\n257\n257\n257\n257\n338\n3...</td>
      <td>6\n82\n46\n134\n2\n33\n26\n61\n2\n33\n43\n78\n...</td>
      <td>1.24%\n16.91%\n9.48%\n27.63%\n0.78%\n12.84%\n1...</td>
      <td></td>
      <td>***\n6\n6\n***\n***\n***\n6\n6\n***\n12\n12\n*...</td>
      <td>***\n70\n41\n116\n***\n29\n23\n54\n***\n32\n40...</td>
      <td>***\n2\n4\n7\n***\n2\n3\n5\n***\n1\n1\n2\n***\...</td>
      <td>***\n***\n***\n***\n***\n2\n2\n***\n2\n2\n***\...</td>
      <td></td>
      <td>***\n68\n40\n114\n***\n29\n23\n54\n***\n26\n34...</td>
      <td>***\n3\n3\n***\n1\n2\n3\n***\n3\n3\n6\n***\n1\...</td>
      <td>***\n7\n3\n10\n***\n2\n2\n***\n3\n4\n7\n***\n1...</td>
      <td>***\n***\n***\n***\n***\n***\n***\n***\n***\n***</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alpine 1\nAlpine 1\nAlpine 1\nAlpine 1\nAlpine...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bergenfield 1\nBergenfield 1\nBergenfield 1\nB...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



## Use of Force in Vancouver

Example from jsoma's [collection of bad pdfs](https://badpdfs.com/pdfs/use-of-force-raw/).


```python
force_doc = PDF('demo/use-of-force-raw.pdf')
page = force_doc.pages[0]
page.show()
```




    
![png](README_files/README_15_0.png)
    




```python
td.table_delim(page, rows='text:contains("970")', cols=td.slice_fitting_elem(page, 'text:contains("PFEIFER, TIM")').find_all('text'))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
      <th>21</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PFEIFER, TIM</td>
      <td>12/2/2016</td>
      <td>Dec-02-2016</td>
      <td>22:30</td>
      <td>WEST</td>
      <td>23-2016-18335</td>
      <td>SOLLERS, CECIL ARTHUR</td>
      <td>M</td>
      <td>U</td>
      <td>H</td>
      <td>...</td>
      <td>FOOT PURSUIT</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>TASER, CAROTID RESTRAINT</td>
      <td>CAROTID RESTRAINT</td>
      <td>EMS AT SCENE, HOSPITAL/RELEASED</td>
      <td>YES</td>
      <td>YES</td>
      <td>SGT. GEDDRY / 1315</td>
      <td>970</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NICHOLSON, DUSTIN</td>
      <td>12/3/2016</td>
      <td>Dec-03-2016</td>
      <td>6:45</td>
      <td>WEST</td>
      <td>23-2016-18348</td>
      <td>GUTIERREZ, SAVANNAH D (DOB: Aug-14-1986)</td>
      <td>F</td>
      <td>W</td>
      <td>N</td>
      <td>...</td>
      <td>FOOT PURSUIT, FIELD CONTACT</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>TAKEDOWNS</td>
      <td>TAKEDOWNS TREATMENT REFUSED</td>
      <td>TREATMENT REFUSED</td>
      <td>YES</td>
      <td>NO</td>
      <td>SGT MARTIN /</td>
      <td>970</td>
    </tr>
    <tr>
      <th>2</th>
      <td>JENNINGS, ERIK</td>
      <td>12/7/2016</td>
      <td>Dec-07-2016</td>
      <td>13:05</td>
      <td>EAST</td>
      <td>23-2016-18571</td>
      <td>MCDONALD, ALEMAYOHU J APR-03-1996</td>
      <td>M</td>
      <td>B</td>
      <td>U</td>
      <td>...</td>
      <td>HANDCUFFING</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>TAKEDOWNS</td>
      <td>TAKEDOWNS</td>
      <td></td>
      <td>YES</td>
      <td>NO</td>
      <td>BURGARA / 1257</td>
      <td>970</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BATES, JUSTIN</td>
      <td>12/13/2016</td>
      <td>Dec-02-2016</td>
      <td>22:30</td>
      <td>WEST</td>
      <td>23-2016-18335</td>
      <td>SOLLERS, CECIL A (DOB: Sep-25-1989)</td>
      <td>M</td>
      <td>U</td>
      <td>H</td>
      <td>...</td>
      <td>FOOT PURSUIT</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>POINT TASER</td>
      <td>POINT TASER</td>
      <td>EMS AT SCENE, HOSPITAL/ADMITTED, HOSPITAL/RELE...</td>
      <td>YES</td>
      <td>YES</td>
      <td>CPL PARDUE/1219</td>
      <td>970</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GEDDRY, BLAISE</td>
      <td>12/13/2016</td>
      <td>Dec-13-2016</td>
      <td>2:35</td>
      <td>WEST</td>
      <td>23-2016-18818</td>
      <td>RENFRO, JOHN W</td>
      <td>M</td>
      <td>W</td>
      <td>U</td>
      <td>...</td>
      <td>OTHER</td>
      <td>NONE</td>
      <td>NONE MENTAL ILLNESS, ADMISSION TO FACILITY, PR...</td>
      <td>TAKEDOWNS, HANDS/FEET</td>
      <td>TAKEDOWNS, HANDS/FEET</td>
      <td>EMS AT SCENE, HOSPITAL/ADMITTED</td>
      <td>YES</td>
      <td>YES</td>
      <td>GEDDRY 1315</td>
      <td>970</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>296</th>
      <td>PARDUE, BILL</td>
      <td>1/19/2018</td>
      <td>1/19/2018</td>
      <td>1:24</td>
      <td>WEST</td>
      <td>23-2018-967</td>
      <td>RAULS, COURTNEY A</td>
      <td>F</td>
      <td>B</td>
      <td>U</td>
      <td>...</td>
      <td>FIELD CONTACT</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>TAKEDOWNS</td>
      <td>TAKEDOWNS</td>
      <td></td>
      <td>YES</td>
      <td>YES</td>
      <td>DUMAS/ 1543</td>
      <td>970</td>
    </tr>
    <tr>
      <th>297</th>
      <td>MARBACH, NICHOLAS</td>
      <td>1/20/2018</td>
      <td>1/18/2018</td>
      <td>23:20</td>
      <td>EAST</td>
      <td>23-2018-965</td>
      <td>ELLIOT, DENNIS RICHARD</td>
      <td>M</td>
      <td>U</td>
      <td>U</td>
      <td>...</td>
      <td>ESCORT, HANDCUFFING, FIELD CONTACT PRIOR TO IN...</td>
      <td></td>
      <td>BRUISES MENTAL ILLNESS, ADMISSION TO FACILITY</td>
      <td>HANDS/FEET</td>
      <td>HANDS/FEET</td>
      <td>EMS AT SCENE, HOSPITAL/ADMITTED</td>
      <td>YES</td>
      <td>YES</td>
      <td>KREBS/DAVIS #1508/1230</td>
      <td>970</td>
    </tr>
    <tr>
      <th>298</th>
      <td>MARBACH, NICHOLAS</td>
      <td>1/20/2018</td>
      <td>1/18/2018</td>
      <td>23:21</td>
      <td>EAST</td>
      <td>23-2018-965</td>
      <td>NAPOLEON, ALICE LANEY</td>
      <td>F</td>
      <td>I</td>
      <td>U</td>
      <td>...</td>
      <td>OTHER, FIELD CONTACT</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>HANDS/FEET</td>
      <td>HANDS/FEET</td>
      <td>EMS AT SCENE, SELF TREATMENT</td>
      <td>YES</td>
      <td>YES</td>
      <td>KREBS/DAVIS #1508/1230</td>
      <td>970</td>
    </tr>
    <tr>
      <th>299</th>
      <td>HEMSTOCK, STUART</td>
      <td>1/23/2018</td>
      <td>1/23/2018</td>
      <td>8:45</td>
      <td>EAST</td>
      <td>23-2018-1191</td>
      <td>KESSEL, JORDAN P</td>
      <td>M</td>
      <td>W</td>
      <td>N</td>
      <td>...</td>
      <td>HANDCUFFING, OTHER</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>CONTROL HOLDS CAUSING INJURY</td>
      <td>CONTROL HOLDS CAUSING INJURY</td>
      <td></td>
      <td>YES</td>
      <td>YES</td>
      <td>HUBERTY/1214</td>
      <td>970</td>
    </tr>
    <tr>
      <th>300</th>
      <td>HAMMOND, SCOTLAND</td>
      <td>1/27/2018</td>
      <td>1/27/2018</td>
      <td>20:20</td>
      <td>WEST</td>
      <td>23-2018-1420</td>
      <td>CONTRERAS, RICKY</td>
      <td>M</td>
      <td>W</td>
      <td>U</td>
      <td>...</td>
      <td>HANDCUFFING</td>
      <td>NONE</td>
      <td>NONE</td>
      <td>HANDS/FEET</td>
      <td>HANDS/FEET</td>
      <td>EMS AT SCENE</td>
      <td>YES</td>
      <td>YES</td>
      <td>D. KREBS / 1508</td>
      <td>970</td>
    </tr>
  </tbody>
</table>
<p>301 rows × 22 columns</p>
</div>


