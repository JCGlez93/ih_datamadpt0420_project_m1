import argparse
from p_acquisition import m_acquisition
from p_wrangling import m_wrangling
from p_reporting import m_reporting
from p_analysis import  m_analysis
import time

def argument_parser():
    parser = argparse.ArgumentParser(description='Select a country...')
    parser.add_argument("-c", "--country" , type=str ,dest= 'country' , help='select a country in the list...')
    args= parser.parse_args()
    return args


def main(country=None):

 start = time.time()
 print(f'Starting pipeline for {country}')
 df = m_acquisition.acquire()
 print('This may take around 80 seconds..')
 wrangling_= m_wrangling.wrangle(df)
 print('Wrangling done, lets save the table')
 analysis_ =  m_analysis.analyse(wrangling_, country)
 print(analysis_)
 print(f'Task {country} done')

 end = time.time()
 print(end - start, str("seconds"))


if __name__ == '__main__':
  arguments = argument_parser()
  main(arguments.country)



