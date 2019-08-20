# SPDX-License-Identifier: EPL-1.0
##############################################################################
# Copyright (c) 2019 The Linux Foundation and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
##############################################################################

"""Read the Docs interface."""


import logging
from pprint import pformat

import click

from lftools.api.endpoints import readthedocs

log = logging.getLogger(__name__)


@click.group()
@click.pass_context
def rtd(ctx):
    """Read the Docs interface."""
    pass


@click.command(name='project-list')
@click.pass_context
def project_list(ctx):
    """Get a list of Read the Docs projects.

    Returns a list of RTD projects for the account whose
    token is configured in lftools.ini. This returns the
    slug name, not the pretty name.
    """
    r = readthedocs.ReadTheDocs()
    for project in r.project_list():
        log.info(project)


@click.command(name='project-details')
@click.argument('project-slug')
@click.pass_context
def project_details(ctx, project_slug):
    """Retrieve project details."""
    r = readthedocs.ReadTheDocs()
    data = r.project_details(project_slug)
    log.info(pformat(data))


@click.command(name='project-version-list')
@click.argument('project-slug')
@click.pass_context
def project_version_list(ctx, project_slug):
    """Retrieve project version list."""
    r = readthedocs.ReadTheDocs()
    data = r.project_version_list(project_slug)

    for version in data:
        log.info(version)


@click.command(name='project-version-details')
@click.argument('project-slug')
@click.argument('version-slug')
@click.pass_context
def project_version_details(ctx, project_slug, version_slug):
    """Retrieve project version details."""
    r = readthedocs.ReadTheDocs()
    data = r.project_version_details(project_slug, version_slug)
    log.info(pformat(data))


@click.command(name='project-create')
@click.argument('project-name')
@click.argument('repository-url')
@click.argument('repository-type')
@click.argument('homepage')
@click.argument('programming-language')
@click.argument('language')
@click.pass_context
def project_create(ctx, project_name, repository_url, repository_type,
                   homepage, programming_language, language):
    """Create a new project."""
    r = readthedocs.ReadTheDocs()
    data = r.project_create(project_name, repository_url, repository_type,
                            homepage, programming_language, language)
    log.info(pformat(data))


@click.command(name='project-build-list')
@click.argument('project-slug')
@click.pass_context
def project_build_list(ctx, project_slug):
    """Retrieve a list of a project's builds."""
    r = readthedocs.ReadTheDocs()
    data = r.project_build_list(project_slug)
    log.info(pformat(data))


@click.command(name='project-build-details')
@click.argument('project-slug')
@click.argument('build-id')
@click.pass_context
def project_build_details(ctx, project_slug, build_id):
    """Retrieve specific project build details."""
    r = readthedocs.ReadTheDocs()
    data = r.project_build_details(project_slug, build_id)
    log.info(pformat(data))


@click.command(name='project-build-trigger')
@click.argument('project-slug')
@click.argument('version-slug')
@click.pass_context
def project_build_trigger(ctx, project_slug, version_slug):
    """Trigger a new build."""
    r = readthedocs.ReadTheDocs()
    data = r.project_build_trigger(project_slug, version_slug)
    log.info(pformat(data))


rtd.add_command(project_list)
rtd.add_command(project_details)
rtd.add_command(project_version_list)
rtd.add_command(project_version_details)
rtd.add_command(project_create)
rtd.add_command(project_build_list)
rtd.add_command(project_build_details)
rtd.add_command(project_build_trigger)