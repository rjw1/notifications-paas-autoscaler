import app


class App:
    def __init__(self, name, scalers, **scaler_details):
        self.name = name
        self.scaler_details = scaler_details
        self.scaler_details['app_name'] = name
        self.scalers = []
        for scaler in scalers:
            scaler_cls = getattr(app, scaler)
            self.scalers.append(scaler_cls(**self.scaler_details))

    def query_scalers(self):
        desired_instance_counts = []
        for scaler in self.scalers:
            desired_instance_counts.append(scaler.get_desired_instance_count())
        return desired_instance_counts

    def get_desired_instance_count(self):
        return max(self.query_scalers())

    def refresh_cf_info(self, cf_attributes):
        self.cf_attributes = cf_attributes
