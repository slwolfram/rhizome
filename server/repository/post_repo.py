from flask import current_app


def extract_result(cursor):
    fields = [i[0] for i in cursor.description]
    for row in cursor:
        r = dict(zip(fields, row))
        yield r


def get_children(db, parent, depth):
    with db.cursor() as c:
        c.callproc('QRY_CHILD_POSTS')
        children = list(extract_result(c))
        if children and depth:
            parent.update(children=[(get_children(db, x, depth - 1))
                                    for x in children])
        else:
            parent.update(children=None)
        return parent


def get_roots(db, depth):
    with db.cursor() as c:
        c.callproc('QRY_ROOTS')
        roots = list(extract_result(c))
        current_app.logger.info('roots: {}'.format(roots))
        return (roots if not (depth or roots) else
                [get_children(db, x, depth) for x in roots])


def get_post(db, post_id, depth):
    with db.cursor() as c:
        c.callproc('QRY_POST', [post_id])
        post = list(extract_result(c))
        return (post if not (depth or post) else
                (get_children(db, post[0], depth)))


def create_post(db, post):
    with db.cursor() as c:
        if 'parent_sk' not in post:
            post['parent_sk'] = 0
        if 'rows_affected' not in post:
            post['rows_affected'] = 0
        current_app.logger.info('Inserting {}'.format(post))
        result = c.callproc('INS_POST', list(post.values()))
        current_app.logger.info('result: {}'.format(result))
        return result


def update_post(db, post):
    with db.cursor() as c:
        c.callproc('UPD_POST', list(post.values()))
        result = list(extract_result())
        print('update_post result: ' + str(result))
        return result
