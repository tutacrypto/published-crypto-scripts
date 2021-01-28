import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
sample_transport=RequestsHTTPTransport(
   url='https://api.thegraph.com/subgraphs/name/aave/protocol-v2',
   verify=True,
   retries=5,
)
client = Client(
   transport=sample_transport
)


# some tokens ids on aave
yfi_reserve_id = '0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e0xb53c1a33016b2dc2ff3653530bff1848a515c8c5'
wbtc_reserve_id = '0x2260fac5e5542a773aa44fbcfedf7c193bc2c5990xb53c1a33016b2dc2ff3653530bff1848a515c8c5'


def get_name(reserve):
  query = gql('''
  query 
  {
    reserve (id: "'''+ reserve + '''") {
      id
      name
    }
  }

  ''')
  response = client.execute(query)
  name = response['reserve']['name']
  return name


def get_info_asset(reserve):
  query = gql('''
  query 
  {
    reserve (id: "'''+ reserve + '''") {
      id
      name
      variableBorrowRate
      utilizationRate
      liquidityRate
    }
  }

  ''')
  response = client.execute(query)
  return response


def get_varBorrowRate(reserve):
  query = gql('''
  query 
  {
    reserve (id: "'''+ reserve + '''") {
      id
      name
      variableBorrowRate
      utilizationRate
      liquidityRate
    }
  }

  ''')
  response = client.execute(query)
  name = response['reserve']['name']
  variableBorrowRate = response['reserve']['variableBorrowRate']
  variableBorrowRate = int(variableBorrowRate)
  variableBorrowRate = variableBorrowRate / (1000000000000000000000000000)
  daily_rate = (variableBorrowRate + 1) ** (1/365)
  return variableBorrowRate


def get_liquidityRate(reserve):
  query = gql('''
  query 
  {
    reserve (id: "'''+ reserve + '''") {
      id
      name
      variableBorrowRate
      utilizationRate
      liquidityRate
    }
  }

  ''')
  response = client.execute(query)
  name = response['reserve']['name']
  liquidityRate = response['reserve']['liquidityRate']
  liquidityRate = int(liquidityRate)
  liquidityRate = liquidityRate / (1000000000000000000000000000)
  daily_rate = (liquidityRate + 1) ** 1/365
  return liquidityRate



# Examples
# querying info on YFI asset
print(get_name(yfi_reserve_id), get_info_asset(yfi_reserve_id))

# querying lending rate of WBTC
print(get_name(wbtc_reserve_id), get_liquidityRate(wbtc_reserve_id))

# querying variable borrowing rate of WBTC
print(get_name(wbtc_reserve_id), get_varBorrowRate(wbtc_reserve_id))













