'use strict';

const fs = require('fs');
const d = require('../tmp/data.js')


let data = JSON.stringify(d.data['state']);
fs.writeFileSync('tmp/raw_5lab.json', data);