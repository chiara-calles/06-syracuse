#### Fonctions secondaires
"""
Calcule et affichage des suites de syracuse
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche le graphique de la suite de Syracuse donnée.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    #return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l=[]
    l.append(n)

    #tant qu'on n'est pas arrivé à 1
    while n!= 1:
        if n % 2 == 0:    #n est pair
            n = n // 2
        else:
            n = 3*n + 1
        l.append(n)

    return l


def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # le temps de vol c'est la longueur -1
    n = len(l) - 1
    return n


def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # altitude = quand la valeur > valeur initiale
    n = 0
    debut = l[0]

    for valeur in l[1:]:
        if valeur > debut:
            n = n+1
        else:
            # si valeur <= au début, le vol en altitude est fini, on arrête
            break

    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
   """
    return max(l)


#### Fonction principale


def main():
    """
    Fonction principale qui appelle les fonctions secondaires pour la démonstration
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
