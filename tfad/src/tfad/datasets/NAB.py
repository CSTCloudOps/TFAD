# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


import os

from typing import Union
from pathlib import PosixPath

import numpy as np
import pandas as pd

from tfad.ts import TimeSeries, TimeSeriesDataset

from tqdm import tqdm


def NAB(path: Union[PosixPath, str], *args, **kwargs) -> TimeSeriesDataset:
    """

    Args:
        path : Path to the directory containing the two files (.csv and .hdf) with the dataset.

    Source:
        https://github.com/NetManAIOps/KPI-Anomaly-Detection
    """
    print("Loading KPI datasets...")
    path = PosixPath(path).expanduser()
    assert path.is_dir()

    dataset = TimeSeriesDataset()

    files_NAB = os.listdir(path)
    for file in files_NAB:
        ts_pd = pd.read_csv(os.path.join(path,file))
        ts_pd = ts_pd.fillna(0)
        dataset.append(
            TimeSeries(
                values=ts_pd['value'],
                labels=ts_pd['label']
            )
        )

    return dataset