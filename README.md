# Value Stream Mapper

![Output example](https://raw.github.com/vitkhab/value_stream_mapper/master/examples/development.png) 

## Usage
`python3 main.py examples/development.yml examples/development.png`

## Input file
Input file contains list of elements in YAML format. Each element has attributes:
* `name` - a name of a step in value stream.
* `lead` -  overall time spent on this step.
* `value` - time spent on activities adding value to product.
* `accepted` - number of pieces of work accepted from previous step on first try.
* `completed` - number of produced pieces of work on previous step.
```
- name: Analyze
  lead: 80
  value: 10
  accepted: 100
  completed: 100
  ```