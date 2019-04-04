def calculate_elo(winner,loser, k_winner, k_loser):
    
    trans_winner = 10**(winner/400)
    trans_loser = 10**(loser/400)

    ex_score_winner = trans_winner / (trans_winner+trans_loser)
    ex_score_loser = trans_loser / (trans_winner+trans_loser)

    new_winner = winner + k_winner * (1 - ex_score_winner)
    new_loser = loser + k_loser * (0 - ex_score_loser)

    return {"winner" : new_winner, "loser" : new_loser}

