from ..repository import post_repo as repo
from . import transaction


@transaction
def create_post(post, **kwargs):
    rowcount = repo.create_post(kwargs['db'], post)
    return rowcount


@transaction
def update_post(post, **kwargs):
    rowcount = repo.update_post(kwargs['db'], post)
    return rowcount


@transaction
def get_roots(depth, **kwargs):
    result = repo.get_roots(kwargs['db'], depth)
    return result


@transaction
def get_post(depth, **kwargs):
    result = repo.get_post(kwargs['db'], depth)
    return result
