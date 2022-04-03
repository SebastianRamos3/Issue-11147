# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.bigquery.dataexchange.common",
    manifest={
        "Category",
    },
)


class Category(proto.Enum):
    r"""Listing categories."""
    CATEGORY_UNSPECIFIED = 0
    CATEGORY_OTHERS = 1
    CATEGORY_ADVERTISING_AND_MARKETING = 2
    CATEGORY_COMMERCE = 3
    CATEGORY_CLIMATE_AND_ENVIRONMENT = 4
    CATEGORY_DEMOGRAPHICS = 5
    CATEGORY_ECONOMICS = 6
    CATEGORY_EDUCATION = 7
    CATEGORY_ENERGY = 8
    CATEGORY_FINANCIAL = 9
    CATEGORY_GAMING = 10
    CATEGORY_GEOSPATIAL = 11
    CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE = 12
    CATEGORY_MEDIA = 13
    CATEGORY_PUBLIC_SECTOR = 14
    CATEGORY_RETAIL = 15
    CATEGORY_SPORTS = 16
    CATEGORY_SCIENCE_AND_RESEARCH = 17
    CATEGORY_TRANSPORTATION_AND_LOGISTICS = 18
    CATEGORY_TRAVEL_AND_TOURISM = 19


__all__ = tuple(sorted(__protobuf__.manifest))
