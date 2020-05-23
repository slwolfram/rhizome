from . import extract


def _next_level(db, result, user_id, depth):
    return [(r.update(shoots=get_shoots(db, user_id, r.shoot_id, depth - 1)))
            for r in result]


def get_user_roots(db, user_id, depth):
    with db.cursor() as c:
        c.execute('''SELECT * from rhizome.root r
                        join rhizome.shoot s 
                            on r.shoot_sk=s.shoot_id
                        join rhizome.user_path up
                            on (up.shoot_sk=s.shoot_id and
                                up.user_sk=%s and
                                up.is_authorized=true)
                                ''' % str(user_id))
        result = list(extract(c))
        return (result
                if not depth else
                _next_level(db, result, user_id, depth))


def get_roots(db, depth):
    with db.cursor() as c:
        c.callproc('QRY_ROOTS')
        result = list(extract(c))
        return (result
                if not depth or not result else
                _next_level(db, result, None, depth))


def get_shoots(db, user_id, root_id, depth):
    with db.cursor() as c:
        if user_id:
            c.execute('''SELECT * from rhizome.shoot s 
                            join rhizome.user_paths up
                                on (up.shoot_sk=s.shoot_id and
                                    up.user_sk=%s
                                    up.is_authorized=true)
                            where s.root_sk=%s
                            ''' % (user_id, root_id))
        else:
            c.execute('''SELECT * from rhizome.shoot s
                         where s.root_sk=%s
                         ''' % root_id)
        result = list(extract(c))
        return (result
                if not depth else
                _next_level(db, result, user_id, depth))


def create_shoot(db, shoot):
    with db.cursor() as c:
        cols = ', '.join(f"{k}" for k in shoot.keys())
        vals = ', '.join(f"'{v}'" for v in shoot.values())
        c.execute('''INSERT into rhizome.shoot
                     (%s)
                     VALUES (%s) 
                     ''' % (cols,
                            vals))
        return c.rowcount()


def create_root(db, shoot):
    create_shoot(db, shoot)
    with db.cursor() as c:
        shoot_id = str(db.insert_id())
        c.execute(
            '''INSERT into rhizome.root
                (shoot_sk)
                VALUES (%s)
            ''' % str(shoot_id))
        return c.rowcount()


def update_shoot(db, shoot):
    with db.cursor() as c:
        c.execute('''UPDATE rhizome.shoot
                     SET %s
                     WHERE shoot_id=%s
                     ''' % (' AND '.join([f"{k}='{v}'" for k, v in zip(shoot._fields, shoot)]),
                            str(shoot.shoot_id)))
        return c.rowcount()
