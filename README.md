report_plugin
============
settings.py配置说明：

	CELERY_BACKEND = "amqp://"
	
	CELERY_RABBITMQ_REPORT = (
        "uureport",
        "amqp://rabbit:***@uureport_rabbitmq:5672//uureport"
    )
    
    REPORT_TASK_NAME = "reports.tasks.save_report"
