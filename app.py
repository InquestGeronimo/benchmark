import gradio as gr
from fastapi import FastAPI

from elements import TextElements as text
from benchmark import Benchmarker
from settings import Manager
    
BM = Benchmarker()
app = FastAPI()
   
def parameters():
    
    engine = gr.Radio(text.engines, value=text.engines[0], label=text.engine_label)
    batch = gr.Slider(minimum=1, maximum=128, step=1, value=5, label=text.batch_label, interactive=True)
    time = gr.Slider(minimum=1, maximum=60, step=2, value= 5, label=text.time_label, interactive=True)
    scenario = gr.Radio(text.scenarios, value=text.scenarios[0], label=text.scenario_label)
    
    button = gr.Button(text.button_label)
    output = gr.Textbox(label=text.output_label)
    
    button.click(
        fn=BM.get_benchmarks, 
        inputs=[model, engine, batch, time, scenario], 
        outputs=output
    )


with gr.Blocks() as demo:
    
    gr.Markdown(text.md_title)

    with gr.Row():
        
        with gr.Column():
            
            gr.HTML(value=text.embd_video)
            gr.Markdown(text.md_body)   
            
        with gr.Column():
                
            with gr.Tab(text.image_detection_tab):
                
                model = gr.Radio(
                    choices=text.image_detection_models, 
                    value=text.image_detection_models[0],
                    label=text.model_label
                )
                parameters()
                
            with gr.Tab(text.image_classification_tab):
                
                model = gr.Radio(
                    choices=text.image_classification_models, 
                    value=text.image_classification_models[0],
                    label=text.model_label
                )
                parameters()
                
            with gr.Tab(text.image_segmentation_tab):
                
                model = gr.Radio(
                    choices=text.image_segmentation_models, 
                    value=text.image_segmentation_models[0],
                    label=text.model_label
                )
                parameters()
                
            with gr.Tab(text.sentiment_analysis_tab):
                
                model = gr.Radio(
                    choices=text.sentiment_analysis_models, 
                    value=text.sentiment_analysis_models[0],
                    label=text.model_label
                )
                parameters()

            with gr.Tab(text.question_answering_tab):
                
                model = gr.Radio(
                    choices=text.question_answering_models, 
                    value=text.question_answering_models[0],
                    label=text.model_label
                )
                parameters()
                
            with gr.Tab(text.token_classification_tab):
                
                model = gr.Radio(
                    choices=text.token_classification_models, 
                    value=text.token_classification_models[0],
                    label=text.model_label
                )
                parameters()            
                
            with gr.Tab(text.document_classification_tab):
                
                model = gr.Radio(
                    choices=text.document_classification_models, 
                    value=text.document_classification_models[0],
                    label=text.model_label
                )
                parameters()   
                
            with gr.Tab(text.multi_label_classification_tab):
                
                model = gr.Radio(
                    choices=text.multi_label_classification_models, 
                    value=text.multi_label_classification_models[0],
                    label=text.model_label
                )
                parameters()  
                
            with gr.Tab(text.masked_language_modeling_tab):
                
                model = gr.Radio(
                    choices=text.masked_language_modeling_models, 
                    value=text.masked_language_modeling_models[0],
                    label=text.model_label
                )
                parameters()

app = gr.mount_gradio_app(app, demo, path=Manager.route)        
                        
if __name__ == "__main__":
    demo.launch(share=True)