import Pyro5.api

@Pyro5.api.expose
class calc():
    def soma(self, v1, v2):
        return v1 + v2


    def sub(self, v1, v2):
        return v1 - v2


    def mult(self, v1, v2):
        return v1 * v2

    def expo(self, v1, v2):
        return v1 ** v2

    def div(self, v1, v2):
        return v1/v2

    
daemon =Pyro5.api.Daemon()
uri = daemon.register(calc)
print(uri)
ns = Pyro5.api.locate_ns()
ns.register("calc", uri)
daemon.requestLoop()




