def get_winner(x: int) -> str:
    ''' Outputs the winner for a given category (x: [0,5)), it gets
    the scores and number of evaluations for every film, then gets
    the winner following the hierarchy: score > number of evaluations.
    '''
    winner_score = 0
    winner_evaluations = 0
    for i in film_scores:
        if film_scores[i][x] > winner_score:
            winner_score = film_scores[i][x]
            winner_evaluations = N_evaluations[i][x]
            winner = i
        elif film_scores[i][x] == winner_score:
            if N_evaluations[i][x] > winner_evaluations:
                winner_evaluations = N_evaluations[i][x]
                winner = i
    winners[winner] += 1
    return winner


def get_worst() -> str:
    ''' Outputs the winner for the worst movie, it gets the number
    of times that every movie won any category, then gets the winner
    by the hierarchy: number of awards won > combined score.
    '''
    winner_wins = 0
    winner_score = 0
    combined_scores = {}
    for i in film_scores:
        combined_scores[i] = (film_scores[i][0] + film_scores[i][1]
        + film_scores[i][2] + film_scores[i][3] + film_scores[i][4])
    for i in film_scores:
        if winners[i] > winner_wins:
            winner_wins = winners[i]
            winner_score = combined_scores[i]
            winner = i
        elif winners[i] == winner_wins:
            if combined_scores[i] > winner_score:
                winner_score = combined_scores[i]
                winner = i
    return winner


def get_best() -> str:
    ''' Outputs films that shouldn't be in the competition.
    The function iterates throught all the movies then notes
    which weren't voted for any category, then returns a string
    with those numbers if any were found, if not returns the
    string: "sem ganhadores".
    '''
    best_films = []
    combined_scores = {}
    for i in film_scores.keys():
        combined_scores[i] = (film_scores[i][0] + film_scores[i][1]
         + film_scores[i][2] + film_scores[i][3] + film_scores[i][4])
    for i in winners:
        if combined_scores[i] == 0:
            best_films.append(i)
    if len(best_films) == 0:
        return "sem ganhadores"
    else:
        return ", ".join(best_films)


if __name__ == "__main__":
    N_films = int(input())
    film_scores = {}
    N_evaluations = {}
    winners = {}
    for i in range(N_films):
        film = input()
        film_scores[film] = [0, 0, 0, 0, 0]
        N_evaluations[film] = [0, 0, 0, 0, 0]
        winners[film] = 0
    evaluations = int(input())
    for i in range(evaluations):
        evaluation_parameters = input().split(",")
        evaluation_parameters[3] = evaluation_parameters[3].lstrip( )
        evaluation_parameters[2] = evaluation_parameters[2].lstrip( )
        evaluation_parameters[1] = evaluation_parameters[1].lstrip( )
        if (evaluation_parameters[1] == "filme que causou mais bocejos"):
            film_scores[evaluation_parameters[2]][0] += int(evaluation_parameters[3])
            N_evaluations[evaluation_parameters[2]][0] += 1
        elif(evaluation_parameters[1] == "filme que foi mais pausado"):
            film_scores[evaluation_parameters[2]][1] += int(evaluation_parameters[3])
            N_evaluations[evaluation_parameters[2]][1] += 1
        elif(evaluation_parameters[1] == "filme que mais revirou olhos"):
            film_scores[evaluation_parameters[2]][2] += int(evaluation_parameters[3])
            N_evaluations[evaluation_parameters[2]][2] += 1
        elif(evaluation_parameters[1] == "filme que não gerou discussão nas redes sociais"):
            film_scores[evaluation_parameters[2]][3] += int(evaluation_parameters[3])
            N_evaluations[evaluation_parameters[2]][3] += 1
        elif(evaluation_parameters[1] == "enredo mais sem noção"):
            film_scores[evaluation_parameters[2]][4] += int(evaluation_parameters[3])
            N_evaluations[evaluation_parameters[2]][4] += 1
    for i in film_scores.keys():
        for j in range(5):
            if N_evaluations[i][j] != 0:
                film_scores[i][j] = film_scores[i][j]/N_evaluations[i][j]
    #print(film_scores)
    #print(N_evaluations)
    print("#### abacaxi de ouro ####\n\ncategorias simples")
    print("categoria: filme que causou mais bocejos\n-", get_winner(0))
    print("categoria: filme que foi mais pausado\n-", get_winner(1))
    print("categoria: filme que mais revirou olhos\n-", get_winner(2))
    print("categoria: filme que não gerou discussão nas redes sociais\n-", get_winner(3))
    print("categoria: enredo mais sem noção\n-", get_winner(4))
    #print(winners)
    print("\ncategorias especiais")
    print("prêmio pior filme do ano\n-", get_worst())
    print("prêmio não merecia estar aqui\n-", get_best())