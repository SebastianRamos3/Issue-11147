# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from google.cloud.video.live_stream_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.livestream_service import (
    LivestreamServiceAsyncClient,
    LivestreamServiceClient,
)
from .types.outputs import (
    AudioStream,
    ElementaryStream,
    Manifest,
    MuxStream,
    PreprocessingConfig,
    SegmentSettings,
    SpriteSheet,
    TextStream,
    TimecodeConfig,
    VideoStream,
)
from .types.resources import (
    Asset,
    AudioFormat,
    AudioStreamProperty,
    Channel,
    Encryption,
    Event,
    Input,
    InputAttachment,
    InputConfig,
    InputStreamProperty,
    LogConfig,
    Pool,
    VideoFormat,
    VideoStreamProperty,
)
from .types.service import (
    ChannelOperationResponse,
    CreateAssetRequest,
    CreateChannelRequest,
    CreateEventRequest,
    CreateInputRequest,
    DeleteAssetRequest,
    DeleteChannelRequest,
    DeleteEventRequest,
    DeleteInputRequest,
    GetAssetRequest,
    GetChannelRequest,
    GetEventRequest,
    GetInputRequest,
    GetPoolRequest,
    ListAssetsRequest,
    ListAssetsResponse,
    ListChannelsRequest,
    ListChannelsResponse,
    ListEventsRequest,
    ListEventsResponse,
    ListInputsRequest,
    ListInputsResponse,
    OperationMetadata,
    StartChannelRequest,
    StopChannelRequest,
    UpdateChannelRequest,
    UpdateInputRequest,
    UpdatePoolRequest,
)

__all__ = (
    "LivestreamServiceAsyncClient",
    "Asset",
    "AudioFormat",
    "AudioStream",
    "AudioStreamProperty",
    "Channel",
    "ChannelOperationResponse",
    "CreateAssetRequest",
    "CreateChannelRequest",
    "CreateEventRequest",
    "CreateInputRequest",
    "DeleteAssetRequest",
    "DeleteChannelRequest",
    "DeleteEventRequest",
    "DeleteInputRequest",
    "ElementaryStream",
    "Encryption",
    "Event",
    "GetAssetRequest",
    "GetChannelRequest",
    "GetEventRequest",
    "GetInputRequest",
    "GetPoolRequest",
    "Input",
    "InputAttachment",
    "InputConfig",
    "InputStreamProperty",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListChannelsRequest",
    "ListChannelsResponse",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListInputsRequest",
    "ListInputsResponse",
    "LivestreamServiceClient",
    "LogConfig",
    "Manifest",
    "MuxStream",
    "OperationMetadata",
    "Pool",
    "PreprocessingConfig",
    "SegmentSettings",
    "SpriteSheet",
    "StartChannelRequest",
    "StopChannelRequest",
    "TextStream",
    "TimecodeConfig",
    "UpdateChannelRequest",
    "UpdateInputRequest",
    "UpdatePoolRequest",
    "VideoFormat",
    "VideoStream",
    "VideoStreamProperty",
)
