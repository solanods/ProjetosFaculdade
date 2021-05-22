# abrir o database
use projeto_api;

# selecionar tudo
SELECT * FROM projeto_api.api_covid;

# verificar o total de mortos
select sum(deaths) from api_covid;

# verificar valores únicos em uma coluna
select distinct location from api_covid;

# selecionar mais de um campo
select deaths, location from api_covid;
select confirmed, recovered, country from api_covid;

# selecionar mais de um campo e ordenar de forma descendente
select country, recovered  from api_covid order by recovered desc ;

# selecionar a soma de mortes por localização
select sum(deaths), location from api_covid group by location;

# verificar a taxa de recuperação por país
select recovered / confirmed, country from api_covid order by recovered / confirmed desc;

#verificar a porcentagem de mortes em relação à população de cada país
select deaths / population, country from api_covid order by deaths / population desc;

# visualizar os dados juntos
select country, deaths, deaths / population, recovered / confirmed from api_covid;




