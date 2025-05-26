consequentes = {
    "f_Sobe_abruptamente" :  {'p': 3, 'q':0}, #f
    "h_Desce_abruptamente" : {'p': -1.3, 'q':1.93}, #h    # Comportamentos Menos Abruptos (transições moderadas)
    "i_Desce_Menos_Abruptamente" : {'p': -1.76, 'q': 2.27}, #i
    "j_Sobe_menos_abruptamente" : {'p': 0, 'q': 1.83}, #j  #Cobre 1.5-2  
    "k_Desce_Menos_Abruptamente_2" : {'p':1.804, 'q': -3.345}, #k #Cobre 2-2.5    # Comportamentos Suaves
    "l_Desce_muito_suavemente" : {'p':-1.73, 'q':5.5}, #l # Cobre 2.5-3
    "m_Desce_Abruptamente" : {'p': -1.78, 'q': 5.57}, #m  # Cobre 3-3.5
    "n1_Desce_muito_muito_suavemente_2" : {'p': -0.593 , 'q': 1.45}, #n1
    "n2_Sobe_suavemente_2" : {'p': 0.607, 'q': -3.058 },#n2
    "o_Sobe" : {'p': 0.945, 'q':-4.398}, #o modificado
    "p1_plato" : {'p': 0.292, 'q': -1.471}, #p1 modificado
    "p2_desce_muito_suavemente_2" : {'p': -0.427, 'q': 1.915}, #p2 modificado
    "q_desce_suavemente" : {'p': -0.728, 'q': 3.393}, #q
    "r_Sobe_suavemente_3" :{'p': 0.48, 'q': -3.27}, #r
    "s_Sobe_abruptamente" : {'p':1.3, 'q': -8.17}, #s
    "t_Sobe_suavemente_3" :{'p': 0.48, 'q': -3.27}, #t
    "u_Sobe_abruptamente" : {'p':1.3, 'q': -8.17}, #u
    "v_Sobe_suavemente_3" :{'p': -0.062, 'q': 0.8}, #v
    "w_Sobe_abruptamente" : {'p':0.307, 'q': -2.148}, #w
    "a_Sobe_suavemente_3" :{'p': -0.198, 'q': 2.19}, #a
    "b_Sobe_abruptamente" : {'p':-0.8804, 'q': 8.302}, #b
    "c_Sobe_abruptamente" : {'p':-0.675, 'q': 6.318}, #c
}


def saida_do_consequente(p, x, q):
    return (p*x)+ q