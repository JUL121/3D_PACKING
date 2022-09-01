# Copyright 2022 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

settings = [
    {
        'name': 'Choose input type', 'type': 'menu', 'id': 'input_type',
        'options': ['Random', 'File upload'], 'value': 'Random',
    },
    {
        'name': 'Input file', 'type': 'text', 'id': 'data_filepath',
        'options': [],
        'value': 'input/sample_data_1.txt',
        'display': 'none',
    },
    {
        'name': 'Number of bins', 'type': 'number', 'id': 'num_bins',
        'options': [],
        'value': 1,
    },
    {
        'name': 'Number of cases', 'type': 'number', 'id': 'num_cases',
        'options': [],
        'value': 20,
    },
    {
        'name': 'Case dimension minimum', 'type': 'number',
        'id': 'case_size_range_min',
        'options': [],
        'value': 5,
        'display': 'none',
    },
    {
        'name': 'Case dimension maximum', 'type': 'number',
        'id': 'case_size_range_max',
        'options': [],
        'value': 15,
        'display': 'none'
    },
    {
        'name': 'Bin Dimensions (LxWxH)', 'type': 'text', 'id': 'bin_dimensions',
        'options': [],
        'value': '50x50x50',
    },
    {
        'name': 'Bin length', 'type': 'number', 'id': 'bin_length',
        'options': [],
        'value': 50,
        'display': 'none',
    },
    {
        'name': 'Bin width', 'type': 'number', 'id': 'bin_width',
        'options': [],
        'value': 50,
        'display': 'none',
    },
    {
        'name': 'Bin height', 'type': 'number', 'id': 'bin_height',
        'options': [],
        'value': 50,
        'display': 'none',
    },
]


_options = ['Constrained Quadratic Model', 'CBC (Python-MIP)', "DQM"]
settings_solve = [
    {
        'name': 'Solver', 'type': 'menu', 'id': 'solver',
        'options': _options,
        'value': _options[1],
    },
    {
        'name': 'Hybrid solver time(s)', 'type': 'number', 'id': 'time_limit',
        'options': [],
        'value': 20,
    },
]
