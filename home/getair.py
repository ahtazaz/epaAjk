from influxdb import InfluxDBClient
def datainput(a,b,c,d,e,f):
    a = a
    b = b
    c = c
    d = d
    e = e
    f = f
    print(a)
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('epa')
    
    json_body=[
    {
        "measurement": "air",
        "tags": {
            "air": "air",
        },        
        "fields": {
            "Carbon_Monoxide":a,
            "NOx":b,
            "SOx":c,
            "Ozone":d, 
            "Particulate_Matter":e,
            "SOx":f
            
        }
    }]
    client.write_points(json_body)