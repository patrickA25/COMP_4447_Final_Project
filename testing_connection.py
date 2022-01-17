#testing connection

def testing_coin_connection(cg):
    test_con_value = cg.ping()
    if test_con_value == {'gecko_says': '(V3) To the Moon!'}:
        return 'Connection is good'
    else:
        return ['Connection not good',test_con_value]