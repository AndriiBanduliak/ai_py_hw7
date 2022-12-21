import view
import logger as lg
import adding as add

if __name__ == "__main__":
    lg.logging.info('Start')
    add.init_data_base('base_phone.csv')
    view.ls_menu()