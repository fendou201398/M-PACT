# ResNet50 + LSTM models
from resnet.resnet_model                     import ResNet

# I3D models
from i3d.i3d_model  			     import I3D
from i3d_cvr.i3d_cvr_model  		     import I3D_CVR
from i3d_rr.i3d_rr_model  		     import I3D_RR
from i3d_sr.i3d_sr_model  		     import I3D_SR

# C3D models
from c3d.c3d_model  			     import C3D
from c3d_cvr.c3d_cvr_model 		     import C3D_CVR
from c3d_rr.c3d_rr_model 		     import C3D_RR

class Models():
    """
    An abstraction layer to import models and keep the training file clean

    """

    def __init__(self, model_name, inputDims = 250, inputAlpha = 1.0, modelAlpha = 1.0, verbose = 1):
        self.model_name = model_name
        self.inputDims  = inputDims
        self.inputAlpha = inputAlpha 
        self.modelAlpha = modelAlpha 
        self.verbose    = verbose

    def assign_model(self):

        if self.model_name == 'resnet':
            model = ResNet(self.inputDims, 25, verbose = self.verbose)

        elif self.model_name == 'i3d':
            model = I3D(input_alpha = self.inputAlpha, verbose = self.verbose)

        elif self.model_name == 'i3d_cvr':
           model = I3D_CVR(cvr = self.modelAlpha, input_alpha = self.inputAlpha, verbose = self.verbose)

        elif self.model_name == 'i3d_rr':
           model = I3D_RR(input_alpha = self.inputAlpha, verbose = self.verbose)

        elif self.model_name == 'c3d':
            model = C3D(input_alpha = self.inputAlpha, verbose = self.verbose)

        elif self.model_name == 'c3d_cvr':
            model = C3D_CVR(cvr = self.modelAlpha, input_alpha = self.inputAlpha, verbose = self.verbose)

        elif self.model_name == 'c3d_rr':
            model = C3D_RR(input_alpha = self.inputAlpha, verbose = self.verbose)

        # END IF

        return model