from coursesSite.manager.requestOps import RequestsOps
import coursesSite.manager.Endpoints as endpoints_list

endpoints = endpoints_list.Endpoints

session = RequestsOps('admin', 'adminadmin')

request = session.get(endpoints.COURSE.value)
if request.status_code == 200:
    print (request.content)
