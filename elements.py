
class TextElements:
    
    md_title = "# Benchmarking Sparse Models with DigitalOcean's Premium Intel CPUs!"

    md_body = '''

    ### What is Deepsparse? 
    DeepSparse is Neural Magic's inference runtime offering GPU-class performance on CPUs and APIs to integrate ML into your application. It provides off-the-shelf pipelines for computer vision and NLP that wrap the model with proper pre- and post-processing to run performantly on CPUs by using sparse models.

    ## Benchmark
    To Benchmark Neural Magic's sparse models, select the Benchmarking parameters on the right and click `SUBMIT`.
    
    '''
    embd_video = '<iframe width="700" height="375" src="https://www.youtube.com/embed/gGErxSqf05o?autoplay=1&mute=1" \
        title="YOLOv5 on CPUs: Sparsifying to Achieve GPU-Level Performance and Tiny Footprint" frameborder="0" allow="accelerometer; \
        autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    
    image_detection_models = ["Sparse YOLOv5s COCO", "Dense YOLOv5s COCO", "Sparse SSD-300 ResNet-50 COCO", "Dense SSD-300 ResNet-50 COCO"]
    image_classification_models = ["Sparse ResNet 50 ImageNet", "Dense ResNet 50 ImageNet", "Sparse MobileNetV1 ImageNet", "Dense MobileNetV1 ImageNet"]
    image_segmentation_models = ["Sparse YOLACT", "Dense YOLACT"]
    sentiment_analysis_models = ["Sparse DistilBERT SST2", "Dense DistilBERT SST2", "Sparse oBERT SST2", "Dense oBERT SST2"]
    question_answering_models = ["Sparse DistilBERT SQUAD", "Dense DistilBERT SQUAD", "Sparse oBERT SQUAD", "Dense oBERT SQUAD"]
    token_classification_models = ["Sparse DistilBERT CONLL", "Dense DistilBERT CONLL", "Sparse oBERT CONLL", "Dense oBERT CONLL"]
    document_classification_models = ["Sparse RoBERTa IMDB", "Dense RoBERTa IMDB", "Sparse oBERT IMDB", "Dense oBERT IMDB"]
    multi_label_classification_models = ["Sparse oBERT GOEMOTIONS", "Dense oBERT GOEMOTIONS"]
    masked_language_modeling_models = ["Sparse DistilBERT WIKI", "Dense DistilBERT WIKI", "Sparse oBERT WIKI", "Dense oBERT WIKI"]
    
    image_detection_tab = "Image Detection"
    image_classification_tab = "Image Classification"
    image_segmentation_tab = "Image Segmentation"
    sentiment_analysis_tab = "Sentiment Analysis"
    question_answering_tab = "Question Answering"
    token_classification_tab = "Token Classification"
    document_classification_tab = "Document Classification"
    multi_label_classification_tab = "Multi Label Text Classification"
    masked_language_modeling_tab = "Masked Language Modeling"
    
    model_label = "Select Model"
    engine_label = "Select Engine"
    batch_label = "Set Batch Size"
    time_label = "Set time (secs)"
    scenario_label = "Select Inference Scenario"
    button_label = "show me the 💵"
    output_label = "Output Box"
    
    engines = ["DeepSparse", "ONNX"]
    scenarios = ["sync", "async"]
    