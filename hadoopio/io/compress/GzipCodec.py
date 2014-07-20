#!/usr/bin/env python
# ========================================================================
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gzip

from hadoopio.io.InputStream import DataInputBuffer
from io import StringIO

class GzipCodec:
    
    hadoop_module_name = 'org.apache.hadoop.io.compress'
    hadoop_class_name = 'GzipCodec'
    
    def compress(self, data):
        ioObj = StringIO.StringIO()
        f = gzip.GzipFile(fileobj = ioObj, mode='wb')
        f.write(data)
        f.close()
        return ioObj.getValue()

    def decompress(self, data):
        ioObj = StringIO.StringIO(data)
        f = gzip.GzipFile(fileobj = ioObj, mode='rb')
        d = f.read()
        f.close()
        return d

    def decompressInputStream(self, data):
        return DataInputBuffer(self.decompress(data))
