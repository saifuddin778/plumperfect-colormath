plumperfect-colormath
=====================

REST interface for colormath's color conversion and color distance calculation methods.

####The REST Interface
From root, run:
```
> python manage.py runserver
```
#####Color Distance:
To calculate distance between two urls:
```
http://localhost:5000/distance/?type=cmc&c1=(1,2,3)&c2=(1,2,3)
```
Following are the parameters:
* `c1` first color - to be provided as `(float, float, float)`
* `c2` second color - to be provided as  `(float, float, float)`
* `type` type of distance (can be `cie1976`, `cie1994`, `cie2000` or `cmc`)

#####Color Conversion:
To convert a color of one type to another:
```
http://localhost:5000/convert/?input_type=rgb&output_type=hsl&color=(1,2,3)
```
Following are the parameters:
* `input_type` input type of the color to be converted (can be `rgb`, `hsl` or `lab`)
* `output_type` output type desired (can be `rgb`, `hsl` or `lab`)
* `color` the color to be converted - to be provided as `(float, float, float)`

####To use as Module
```python
>>> from manage import convert, distance
```
#####Color Distance:
```python
>>> distance(type='cie1994', c1=(3,4,5), c2=(0.1,2,3))
>>> {'status': True, 'output': 3.6429623555473025}
```
#####Color Conversion:
```python
>>> convert(input_type='hsl', output_type='lab', color=(0.1,0.3,.045))
>>> {'status': True, 'output': {'lab_l': 2.647575713442098, 'lab_a': 1.982241536185203, 'lab_b': 0.702864107468909}}
```
####To Use from Command Line
From root, run:

#####Color Distance:
```
> python manage.py distance --c1="(1,2,3)" --c2="(10,2.0, 0.3)" --type=cmc
> {'status': True, 'output': 9.520307223878351}
```

#####Color Conversion:
```
> python manage.py convert --input_type=rgb --output_type=hsl --color="(1, 2, 10)"
> {'status': True, 'output': {'hsl_l': 5.5, 'hsl_h': 233.33333333333334, 'hsl_s': -1.0}}
```
