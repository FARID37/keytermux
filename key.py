B
    ���\!  �               @   sx  d dl Z d dlZd dlZd dlmZ dZdZdZdZdZdZ	d	Z
d
ZdZdZdZdZdZdZdZdZdZdZdZdZdd� Ze �d� ed Zee� eed � ed� ed� ed� ed� ye �d� W n   Y nX ed � ed!� ed"� ed#� d$Zed%d&�Z e �!e� e �"�  ed#� ed'� ed� ed(� ed� e �d)� ed*� ed+� e �d,� e �d-� dS ).�    N)�sleepz[32;1mz[01;32mz[34;1mz[36;1mz[31;1mz[0mz[37;1mz[35;1mz[3;1mz[33;1mz[0;33mz[30;1mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mc             C   s6   x0| d D ]$}t j�|� t j��  t�d� q
W d S )N�
gl�l��?)�sys�stdout�write�flush�timer   )�s�c� r   �key.py�
slowprints   s    
r   �cleara@  
==============================================
      _____ _    ____  ___ ____ __________
    _|  ___/ \  |  _ \|_ _|  _ \___ /___  |
   (_) |_ / _ \ | |_) || || | | ||_ \  / (_)
  _ _|  _/ ___ \|  _ < | || |_| |__) |/ / _ _
(_|_)|_|/_/   \_\_| \_\___|____/____//_/ (_|_)
==============================================
� z
Press enter to continue...�   z)[!] Making Termux Properties directory...�   z(/data/data/com.termux/files/home/.termuxz/[!] Success Making Termux Properties directory!�   z[!] Making Setup file...�   ziextra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]z:/data/data/com.termux/files/home/.termux/termux.properties�wz [!] Success Making Setup file...z
[!] Setting up setup file...ztermux-reload-settingsz.[!] Successfully !! Making Termux Shortcut KeyzC[!] Terima Kasih Sudah Menggunakan Script Ini, Don't Recoded Pleasezrm -f key.py�exit)#�osr   r   r   �g�gtZbt�b�mr
   �p�u�M�kZkt�a�W�R�G�O�B�P�CZGRr   �systemZfarid37�print�input�mkdirZshortcutkey�openZscriptr   �closer   r   r   r   �<module>   sn   




