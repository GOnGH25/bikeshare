import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    valid_cities = ['chicago', 'new york city', 'washington']
    while city not in valid_cities:
        city = input(
            '\nFor which of the following cities\n{}\n' \
            'would you like to get bikesharing stats?\n'.format(valid_cities)).lower()
        if city not in valid_cities:
            print('\nPlease try again with a valid city.')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    valid_months = ['all', 'january', 'february', 'march', 
                   'april', 'may', 'june']
    while month not in valid_months:
        month = input(
            '\nFor which of the following months\n{}\n' \
            'would you like to get bikesharing stats?\n'.format(valid_months)).lower()
        if month not in valid_months:
            print('\nPlease try again with a valid month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 
                   'thursday', 'friday', 'saturday', 'sunday']
    while day not in valid_days:
        day = input(
            '\nFor which day of week\n{}\n' \
            'would you like to get bikesharing stats?\n'.format(valid_days)).lower()
        if day not in valid_days:
            print('\nPlease try again with a valid day.')
    print('\n\nYou selected to see bikesharing stats with the following filter:\n' \
          'city: {}\n' \
          'month(s): {}\n' \
          'day(s) of week: {}\n'.format(city,month,day))
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 
                  'april', 'may', 'june', 
                  'july', 'august', 'september', 
                  'october', 'november', 'december']
        month = months.index(month) + 1 #need to add 1 because of zero indexing
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_commond_month = df['Start Time'].dt.month_name().mode()[0]
    print('The most common month is {}.'.format(most_commond_month))

    # TO DO: display the most common day of week
    most_commond_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}.'.format(most_commond_day))

    # TO DO: display the most common start hour
    most_commond_hour = df['start_hour'].mode()[0]
    print("The most common start hour is {} o'clock.".format(most_commond_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}.".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}.".format(most_common_end_station))
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' -> ' + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    print("The most common trip is {}.".format(most_common_trip))
    #print(df['Trip'].value_counts())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is {}.".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("The average travel time is {}.".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.keys():
        print(df['Gender'].value_counts())
    else:
        print('There is no data to the gender of users!')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.keys():
        print("The earliest year of birth is {}.".format(df['Birth Year'].min()))
        print("The most recent year of birth is {}.".format(df['Birth Year'].max()))
        print("The most common year of birth is {}.".format(df['Birth Year'].mode()[0]))
    else:
        print('There is no data to the year of birth of users!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_on_demand(df):
    """
    Print raw data of DataFrame on user request.

    """
    len_df = df.size
    i = 0
    do_print = input('\nWould you like to see the raw data? This prints the first 5 data points.\nEnter yes or no.\n')
    while (do_print.lower() == 'yes') and (i+5) < len_df:
        print(df.iloc[i:i+5])
        do_print = input('\nWould you like to see 5 more data points? Enter yes or no.\n')
        i += 5
        if do_print.lower() != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print_on_demand(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
