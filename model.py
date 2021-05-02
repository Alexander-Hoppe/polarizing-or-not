""" Analyze, whether the content of a given social media webpage could
 potentially polarize a user or not
"""

def calc_polarizing_probability(domain, content):
    """ Returns a probability that the content of a domain will polarize users
    Parameters
--------------------------------------------------------------------------------
    domain: str
	domain name of the social media webpage
    content: str
        outer html of the given domain/page

    Returns
-------------------------------------------------------------------------------- 
    probability: float
        the probability that the content of the page will polarize a user, where 
    0 is the minimum probability and 1 is the maximum probability
    """
    
    probability = .6

    return probability

