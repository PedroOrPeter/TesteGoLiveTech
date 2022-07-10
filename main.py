from roboLiveTech import RoboRafael
import logging

robo = RoboRafael()
robo.correio()
log_format = '%(asctime)s'

logging.basicConfig(filename='gerador.txt',
                    filemode='a',
                    level=logging.DEBUG,
                    format=log_format)
logger = logging.getLogger('root')
logger.info(log_format)
