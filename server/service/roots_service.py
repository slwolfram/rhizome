from ..repository import roots_repo as repo
from . import transaction


@transaction
def create_root(root, **kwargs):
    rowcount = repo.create_root(kwargs['db'], root)
    return rowcount


@transaction
def create_shoot(shoot, **kwargs):
    rowcount = repo.create_shoot(kwargs['db'], shoot)
    return rowcount


@transaction
def get_roots(depth, **kwargs):
    result = repo.get_roots(kwargs['db'], depth)
    return result
