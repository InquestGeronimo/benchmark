
class TextElements:
    
    # Markdown Text
    md_title = "# Benchmarking Sparse Models with DigitalOcean's Premium Intel CPUs!"

    md_body = '''

    ## Hello 👋
    This goal of this demo is to allow users to benchmark the DeepSparse runtime on DigitalOcean's CPUs. The screen on the right allows one to select different configurations for benchmarking select models from the Computer Vision and NLP domains:
    
    - the selection o
    
    '''
    
    # Video
    embd_video = '<iframe width="700" height="375" src="https://www.youtube.com/embed/gGErxSqf05o?autoplay=1&mute=1" \
        title="YOLOv5 on CPUs: Sparsifying to Achieve GPU-Level Performance and Tiny Footprint" frameborder="0" allow="accelerometer; \
        autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    
    # Models
    image_detection_models = ["Sparse YOLOv5s COCO", "Dense YOLOv5s COCO", "Sparse YOLOv5m COCO", "Dense YOLOv5m COCO"]
    image_classification_models = ["Sparse ResNet 50 ImageNet", "Dense ResNet 50 ImageNet", "Sparse MobileNetV1 ImageNet", "Dense MobileNetV1 ImageNet"]
    image_segmentation_models = ["Sparse YOLACT", "Dense YOLACT"]
    sentiment_analysis_models = ["Sparse DistilBERT SST2", "Dense DistilBERT SST2", "Sparse oBERT SST2", "Dense oBERT SST2"]
    question_answering_models = ["Sparse DistilBERT SQUAD", "Dense DistilBERT SQUAD", "Sparse oBERT SQUAD", "Dense oBERT SQUAD"]
    token_classification_models = ["Sparse DistilBERT CONLL", "Dense DistilBERT CONLL", "Sparse oBERT CONLL", "Dense oBERT CONLL"]
    document_classification_models = ["Sparse RoBERTa IMDB", "Dense RoBERTa IMDB", "Sparse oBERT IMDB", "Dense oBERT IMDB"]
    multi_label_classification_models = ["Sparse oBERT GOEMOTIONS", "Dense oBERT GOEMOTIONS"]
    masked_language_modeling_models = ["Sparse DistilBERT WIKI", "Dense DistilBERT WIKI", "Sparse oBERT WIKI", "Dense oBERT WIKI"]
    
    # Tasks
    image_detection_tab = "Image Detection"
    image_classification_tab = "Image Classification"
    image_segmentation_tab = "Image Segmentation"
    sentiment_analysis_tab = "Sentiment Analysis"
    question_answering_tab = "Question Answering"
    token_classification_tab = "Token Classification"
    document_classification_tab = "Document Classification"
    multi_label_classification_tab = "Multi Label Text Classification"
    masked_language_modeling_tab = "Masked Language Modeling"
    

    # Labels
    model_label = "Select Model"
    engine_label = "Select Engine"
    batch_label = "Set Batch Size"
    time_label = "Set time (secs)"
    scenario_label = "Select Inference Scenario"
    button_label = "show me the 💵"
    output_label = "Output Box"
    
    # Parameters
    batch_min = 1
    batch_max = 128
    batch_step = 1
    batch_value = 5
    
    time_min = 1
    time_max = 60
    time_step = 2
    time_value = 5
    
    engines = ["DeepSparse", "ONNX"]
    scenarios = ["sync", "async"]

    # Map
    tab_switch = {
        image_detection_tab: image_detection_models,
        image_classification_tab: image_detection_models,
        image_segmentation_tab: image_segmentation_models,
        sentiment_analysis_tab: sentiment_analysis_models,
        question_answering_tab: question_answering_models,
        token_classification_tab: token_classification_models,
        document_classification_tab: document_classification_models,
        multi_label_classification_tab: multi_label_classification_models,
        masked_language_modeling_tab: masked_language_modeling_models
    }