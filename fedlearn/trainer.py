from fedlearn.utils import MAX_TRAINING_ROUNDS


class Trainer():
    def __init__(self) -> None:
        super().__init__()
        self.trainer_ip = "10.10.100.13"
        self.trainer_port = 5682
        self.round = 0

    def training_round(self, data=None):
        if not data:
            data = 1
        else:
            data += 1
        return data
    
    
    
    # @app.task(bind=True)
    # def add(self, x, y):
    #     try:
    #         # if self.attempts == 0:
    #         #     self.attempts +=1
    #         #     raise RuntimeWarning("retry operatin")
    #         # else:
    #         #     self.attempts = 0
    #         #     return x + y
    #         return x + y
    #     except RuntimeWarning as exc:
    #         raise self.retry(exc=exc)




        # num_samples = int(config["TRAINING"]["NUM_SAMPLES"])
        # local_batch_size = int(config["TRAINING"]["LOCAL_BATCH_SIZE"])
        # local_epochs = int(config["TRAINING"]["LOCAL_EPOCHS"])

        # model = utils.model_init()
        # model.load_weights("aggregated_models/model_ep%d.h5" % (iteration))
        # x_train, y_train = utils.sampling_data(num_samples)
        # model.compile(
        #     optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"]
        # )
        # model.fit(
        #     x_train,
        #     y_train,
        #     epochs=local_epochs,
        #     batch_size=local_batch_size,
        #     verbose=1,
        #     validation_split=0.2,
        # )
        # model.save_weights(
        #     "trained_models/%s_ep%d.h5" % (self.trainer_ip + ":" + self.trainer_port, iteration)
        # )
        # logging.info("[COMPLETE] TRAIN LOCAL MODEL IN EP%d" % iteration)
