for i in $(ls src/bluing/*py); do sed -i 's/bluescan/bluing/g' $i; done
for i in $(ls src/bluing/*py); do sed -i 's/lmp-feature /lmp-features/g' $i; done
for i in $(ls src/bluing/*py); do sed -i 's/lmp-featuresB/lmp-features B/g' $i; done
for i in $(ls src/bluing/*py); do sed -i "s/lmp-feature'/lmp-features'/g" $i; done
for i in $(ls src/bluing/*py); do sed -i 's/from pyclui import Logger/import logging/g' $i; done
for i in $(ls src/bluing/*py); do sed -i 's/logger = Logger(__name__, logging.INFO)/logger = logging.getLogger(__name__)/g' $i; done
sed -i 's/HCI_Cmd_LE_Read_Remote_Used_Features as HCI_Cmd_LE_Read_Remote_Features/HCI_Cmd_LE_Read_Remote_Features/' src/bluing/le_scan.py


