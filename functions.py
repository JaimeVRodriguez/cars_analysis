import scipy.stats as stats
import numpy as np
import math


def compute_power(n, sigma, alpha, mu0, mua):
    standard_error = sigma / n**0.5
    h0 = stats.norm(mu0, standard_error)
    ha = stats.norm(mua, standard_error)
    critical_value = h0.ppf(1-alpha)
    power = 1 - ha.cdf(critical_value)

    return power



def sample_size_needed_for_power(alpha, power, mu0, mua, sigma):
    standard_normal = stats.norm(0, 1)
    beta = 1 - power
    numerator = sigma * (standard_normal.ppf(1 - alpha) - standard_normal.ppf(beta))
    denominator = (mua - mu0)
    return math.ceil((numerator / denominator) ** 2)



def sample_calcs(col1, col2='origin'):
    
    col1_df = pd.DataFrame()
    col1_df['Mean'] = cars_df.groupby(col2)[col1].mean()
    col1_df['STD'] = cars_df.groupby(col2)[col1].std()
    col1_df['Sample Size'] = cars_df.groupby(col2)[col1].count()

    return col1_df




def graph_samp_dist(mean, std, sample_size, color):

    std_error = std / np.sqrt(sample_size)
    sample_dist_mean = stats.norm(mean, std_error)  
    xs = np.linspace(mean-(4*std_error), mean+(4*std_error), 300)

    pdfs = sample_dist_mean.pdf(xs)

    ax.plot(xs, pdfs, color=color)



if __name__ == '__main__':
    pass