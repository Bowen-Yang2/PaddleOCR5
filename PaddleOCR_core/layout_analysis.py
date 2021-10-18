def lay_out_analysis(save_folder,img_path,font_path,image_save):
    import os
    import cv2
    from paddleocr import PPStructure,draw_structure_result,save_structure_res
    table_engine = PPStructure(show_log=True, use_gpu=False)
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder,os.path.basename(img_path).split('.')[0])
    for line in result:
        line.pop('img')
        print(line)
    from PIL import Image
    #font_path = './fonts/simfang.ttf'
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    #image_save='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/output/table/result.jpg'
    im_show.save(image_save)


if __name__ == '__main__':
    lay_out_analysis(save_folder='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/output/table',
    img_path='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/table/be_kind_to_address_fear.jpg',
    font_path='./fonts/simfang.ttf',
    image_save='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/output/table/result.jpg')




'''
lay_out_analysis(save_folder='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/output/table',
img_path='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/table/be_kind_to_address_fear.jpg',
font_path='./fonts/simfang.ttf',
image_save='C:/Users/YANGB43/OneDrive - Pfizer/try/ppocr_img/output/table/result.jpg')
'''