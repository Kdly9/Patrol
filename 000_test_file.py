from transports import get_transport
from status import Status
 
def main(db, control_id, scan_date):
	try:
        print('Test started')
    	result, options, transport_name = get_transport('SSH')
 
    	command = result.exec('ls -la')
 
    	if 'testfile.txt' in command:
            status_info = Status.STATUS_COMPLIANT.name
    	else:
            status_info = Status.STATUS_NOT_COMPLIANT.name
 
        transport_id = db.db_transport_select(transport_name)
 
        db.add_control(control_id,
                       scan_date,
                       status_info,
                       transport_id,
                       str(options))  # Добавляем результат сканирования в базу
    	print('End of test')
	except:
    	pass
