from nipype.interfaces.broccoli import firstlevel
import os

BROCCOLI_DIR = '/home/miha/Programiranje/BROCCOLI'
OpenfMRI_DIR = '/data/miha/OpenfMRI/RhymeJudgment/ds003'
subject = 'sub001'
SUBJECT_DIR = os.path.join(OpenfMRI_DIR, subject)

firstlevel.FirstLevelAnalysis.help()
print(SUBJECT_DIR)

interface = firstlevel.FirstLevelAnalysis(
    MNI_file = BROCCOLI_DIR + '/brain_templates/MNI152_T1_2mm.nii',
    filters_parametric = BROCCOLI_DIR + '/code/Matlab_Wrapper/filters_for_parametric_registration.mat',
    filters_nonparametric = BROCCOLI_DIR + '/code/Matlab_Wrapper/filters_for_nonparametric_registration.mat',
    
    T1_file = os.path.join(SUBJECT_DIR, 'anatomy/highres001_brain.nii.gz'),
    fMRI_file = os.path.join(SUBJECT_DIR, 'BOLD/task001_run001/bold.nii.gz'),
    GLM_path = os.path.join(SUBJECT_DIR, 'model/model001/onsets/task001_run001'),
    
    opencl_device = 0,
)


results = interface.run()
print(repr(results))

