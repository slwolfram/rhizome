ins_root = (lambda shoot_id: (
            '''INSERT into rhizome.root
                (shoot_sk)
                VALUES (%s)
            ''' % str(shoot_id)))


