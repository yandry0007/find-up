url = "https://nodejs-yampier.c9users.io/pag/?nombreb=yandry&data=5&a=0005&long=0008"

def parse(req):
	arreglo_parametros = []
	parametros = {};
	try:
		if (req.find("?") > 0 ):
			url_data = req.split("?");
			arreglo_parametros = url_data[1].split("&") 
			for i in range(len(arreglo_parametros)):
				parametro = arreglo_parametros[i]
				param_data = parametro.split("=")
				parametros[param_data[0]] = param_data[1]
	except Exception, e:
		pass
	return parametros

param = parse(url)
print param