class Aggregator():
    def __init__(self) -> None:
        # config = configparser.ConfigParser()
        # config.read('../config_exp0.ini')

        # group = 'UFL_'

        # self.trainer_ip = ast.literal_eval(config['DISTRIBUTION']['TRAINER_IP'])
        # self.num_communication_rounds = int(config['TRAINING']['NUM_COMMUNICATION_ROUNDS'])
        # hostname = socket.gethostname()
        # logging.basicConfig(filename="%s_log.txt"%hostname, level=logging.DEBUG, format="%(asctime)s - %(message)s")           
        # logging.info("[START] INIT MODEL")
        # init_model = utils.model_init()
        # init_model.save_weights('aggregated_models/model_ep%d.h5'%(0))
        # while not os.path.exists('aggregated_models/model_ep%d.h5'%(0)):
        #     time.sleep(10)
        # logging.info("[COMPLETE] INIT MODEL")

        # logging.info("[START] RECEIVE INIT MODEL")
        # while not os.path.exists('aggregated_models/model_ep%d.h5'%(0)):
        #     time.sleep(5)
        # logging.info("[COMPLETE] RECEIVE INIT MODEL")

        # logging.info("[START] BROADCAST INIT MODEL")
        # utils.broadcast_model(self.trainer_ip,'aggregated_models/model_ep%d.h5'%(0), 'aggregated_models')
        # logging.info("[COMPLETE] BROADCAST INIT MODEL")
        pass
    
    
    def rollup_round(self, data:int):
        result = data*2
        return result

    # @app.task
    # def rollup(self):
    #     for e in range(self.num_communication_rounds):

    #         logging.info("[START] RECEIVE TRAINED MODEL IN EP%d"%e)
    #         while True:
    #             if len(glob.glob('trained_models/*_ep%d.h5'%(e))) == len(self.trainer_ip):
    #                 break
    #         logging.info("[COMPLETE] RECEIVE TRAINED MODEL IN EP%d"%e)
            
    #         logging.info("[START] AGGREGATING TRAINED MODEL IN EP%d"%e)
    #         arr = []
    #         while True:
    #             print('aa')
    #             try:
    #                 print('bb')
    #                 model = utils.model_init()
    #                 model.load_weights('aggregated_models/model_ep%d.h5'%(e))
    #                 break
    #             except:
    #                 print('cc')
    #                 pass
    #         arr.append('aggregated_models/model_ep%d.h5'%(e))
    #         for p in glob.glob('trained_models/*_ep%d.h5'%(e)):
    #             # while not os.path.exists(p):
    #             #     time.sleep(5)
    #             while True:
    #                 print('a',p)
    #                 try:
    #                     print('b',p)
    #                     model = utils.model_init()
    #                     model.load_weights(p)
    #                     break
    #                 except:
    #                     print('c',p)
    #                     pass
    #             arr.append(p)
    #         aggregated_model = utils.aggregated(arr)
    #         aggregated_model.save_weights('aggregated_models/model_ep%d.h5'%(e+1))

    #         while not os.path.exists('aggregated_models/model_ep%d.h5'%(e+1)):
    #                 time.sleep(5)
    #         time.sleep(5)
    #         logging.info("[COMPLETE] AGGREGATING TRAINED MODEL IN EP%d"%e)

    #         logging.info("[START] BROADCAST AGGREGATED MODEL IN EP%d"%e)
    #         utils.broadcast_model(self.trainer_ip,'aggregated_models/model_ep%d.h5'%(e+1), 'aggregated_models')
    #         logging.info("[COMPLETE] BROADCAST AGGREGATED MODEL IN EP%d"%e)