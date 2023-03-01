
class TextElements:
    
    # Markdown Text
    md_title = "# Benchmarking Sparse Models on DigitalOcean's CPUs!"

    md_body = '''

    ## Hey There 👋
    
    Welcome to Neural Magic's Benchmarking Demo where you can put DeepSparse runtime on DigitalOcean's CPUs to the test! 
    Our goal is to provide an easy-to-use platform for users to benchmark select models from Computer Vision and NLP domains, 
    and to do so with a variety of different configurations.

    Whether you're an expert in the field or just getting started, our demo provides a straightforward way to put DeepSparse to the test and get valuable insights into its performance. 
    
        Step 1: Select your AI task in the tabs.
        Step 2: Select your model. You have the choice of benchmarking a sparse or dense model.
        Step 3: Select your engine.
        Step 4: Set your batch size, which refers to the number of input samples that are processed.
        Step 5: Set the time of how long the benchmarking will take.
        Step 6: Select your inference scenario. SYNC is used to simulate model latency/synchronous 
                scenarios, while ASYNC is used to simulate model throughput/asynchronous scenarios.
        
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
    batch_value = 1
    
    time_min = 1
    time_max = 60
    time_step = 2
    time_value = 5
    
    engines = ["DeepSparse", "ONNX"]
    scenarios = ["sync", "async"]

    # Map
    tab_switch = {
        image_detection_tab: image_detection_models,
        image_classification_tab: image_classification_models,
        image_segmentation_tab: image_segmentation_models,
        sentiment_analysis_tab: sentiment_analysis_models,
        question_answering_tab: question_answering_models,
        token_classification_tab: token_classification_models,
        document_classification_tab: document_classification_models,
        multi_label_classification_tab: multi_label_classification_models,
        masked_language_modeling_tab: masked_language_modeling_models
    }