class test_enum:
    testinfo = 'testinfo'  # 测试用例
    id = 'id'        #测试用例 id
    title = 'title'     #测试用例标题
    info='info'        #信息


    testcase = 'testcase'  #测试流程
    element_info ='element_info'  #元素信息
    find_type='find_type' #元素类型
    operate_type='operate_type'#操作

    check = 'check'   #检查测试用例
    check_type='check_type'   #检查类型

    msg = 'msg'   #错误信息

class find_type:

    find_element_by_id = 'id'
    find_element_by_xpath='xpath'
    find_element_by_class_name='class_name'
    find_element_by_tag_name='tag_name'
    find_element_by_link_text='text'

    find_elements_by_id='id_list'
    find_elements_by_xpath='xpath_list'
    find_elements_by_class_name='class_name_list'
    find_elements_by_tag_name='tag_name_list'
    find_elements_by_link_text='text_list'

    # w.find_element_by_id()
    # w.find_element_by_xpath()
    # w.find_element_by_class_name()
    # w.find_element_by_tag_name()
    # w.find_element_by_link_text()
    #
    # w.find_elements_by_xpath()
    # w.find_elements_by_xpath()
    # w.find_elements_by_class_name()
    # w.find_elements_by_tag_name()
    # w.find_elements_by_link_text()

class operate_type:
    click='click'
    send_keys='send_keys'
    get_value='get_value'
    get_text='get_text'
    move_to_elemrnt='move_to_element'

    get_list = 'get_list'
    get_driver='get_driver'

    switch_window='switch_window'
    scroll_down='scroll_down'
    scroll_up='scroll_up'
    close_window='close_window'
    change_size ='change_size'

    #实践
    refresh='refresh'
    sleep='sleep'

class Eunms:

    WAIT_TIME = 20

    # 检查点
    DEFAULT_CHECK = "default_check"  # 默认检查点，就是查找页面元素
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在

    CONTRARY_COMPARE = "contrary_compare"  # 检查点关键字contrary_getval: 如果查找元素存在历史数据则失败
    COMPARE = "compare"  # 历史数据和实际数据对比 ：如果不在历史数据，就是失败

    RE_CONNECT = 1  # 是否打开失败后再次运行一次用例

    # 文件名字
    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"

    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"
    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"