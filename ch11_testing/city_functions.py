def cc_formatting(city, country, population=''):
    if population:
        return(f'{city}, {country}, '.title() + f'population - {population}')
    else:
        return(f'{city}, {country}'.title())


