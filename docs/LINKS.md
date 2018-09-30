Some interesting links

Media: http://www.rtve.es/api/medios.json
Gives 851 for radio

Radio programs: http://www.rtve.es/api//medios/851/programas.json?size=20&page=4
Starting with letter: startWithLetter=f
Gives i.e. 29890 for "A compás"

Audios from "A compás": http://www.rtve.es/api/programas/29890/audios.json

Mas vistos: api.rtve.es/api/audios/mas-vistos.json
Mas populares: api.rtve.es/api/audios/mas-populares.json

POR CADENAS
http://www.rtve.es/api/cadenas.json
Gets 849 for Radio3

Audios de la cadena: http://api.rtve.es/api/cadenas/849/audios.json
Programas de la cadena: http://api.rtve.es/api/cadenas/849/programas.json


Content Tree
============

Media: radio
	- Channel
		- A-Z
			- Program 
				- All (programas/{id}/audios.json)
				- Popular (programas/{id}/audios/mas-populares.json)
				- Most seen	(programas/{id}/audios/mas-vistos.json)
			- Program
		- Popular (/cadenas/{id}/audios/mas-populares)
		- Most seen (/cadenas/{id}/audios/mas-vistos)
		- Live
	- Channel
		- Program
		- ....
