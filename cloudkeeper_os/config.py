# -*- coding: utf-8 -*-

# Copyright 2017 CNRS and University of Strasbourg
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Cloudkeeper-os configuration options.
"""

from oslo_config import cfg
from oslo_log import log

log.register_options(cfg.CONF)

DEFAULT_OPTS = [
    cfg.PortOpt('grpc_port',
                default=50051,
                help='The port on which the server will listen.'),
    cfg.StrOpt('mapping_file',
               default='/etc/cloudkeeper-os/mapping.json',
               help='Directory where the cloud credentials for each VO '
                    'are stored.'),
    cfg.StrOpt('tempdir',
               default='/tmp',
               help='Directory where the images are downloaded'),
    cfg.StrOpt('image_visibility',
               default='private',
               choices=['public', 'private', 'shared', 'community'],
               help='Visibility of images uploaded to OpenStack'),
    cfg.StrOpt('endpoint_type',
               default=None,
               choices=['internal', 'public'],
               help='This value indicates the endpoint type to use to connect '
                    'the Glance endpoint.'),
]

cfg.CONF.register_opts(DEFAULT_OPTS)

AUTHTOKEN_OPTS = [
    cfg.StrOpt('username',
               default='cloudkeeper',
               help="Username"),
    cfg.StrOpt('password',
               secret=True,
               help="User's password"),
    cfg.StrOpt('user_domain_name',
               default='default',
               help="User's domain name"),
    cfg.StrOpt('project_domain_name',
               default='default',
               help="Domain name containing project"),
    cfg.StrOpt('auth_url',
               default=None,
               help='Complete public Identity API endpoint.'),
]

AUTHTOKEN_GROUP = 'keystone_authtoken'
cfg.CONF.register_opts(AUTHTOKEN_OPTS, AUTHTOKEN_GROUP)


def parse_args(argv, default_config_files=None):
    """Parse arguments
    """
    cfg.CONF(argv[1:],
             project='cloudkeeper-os',
             default_config_files=default_config_files)


def list_opts():
    """List options
    """
    return [
        ('DEFAULT', DEFAULT_OPTS),
        (AUTHTOKEN_GROUP, AUTHTOKEN_OPTS)
    ]
