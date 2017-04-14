if __name__ == '__main__':

    import os
    import time
    import aes128
   
    
    
    def print_byte_of_array(byte_array):
        message_of_array = ''
        i_array = 0
        while i_array < len(byte_array):
            message_of_array = message_of_array +  str(chr(byte_array[i_array])) 
            i_array = i_array + 1
        return message_of_array
    
    def logical_xor(data_byte_arry_for_xor,Ci):
        i_xor = 0
        while i_xor < len(data_byte_arry_for_xor):
            data_byte_arry_for_xor[i_xor] = data_byte_arry_for_xor[i_xor] ^ Ci[i_xor]
            i_xor = i_xor + 1
        return data_byte_arry_for_xor


    
    
    print('Step 1:')
    while True:
        print('Press 1 for encription smth and 2 for decription')
        way = str(input())
        if way not in ['1', '2']:
            print('Action denied')
            continue
        else:
            break

    print('Step 3:')
    while True:
        print('Enter your Key for encription/decription. The Key must be less than 16 symbols. Please, don\'t forget it!')
        key = raw_input()
        
        if len(key) > 16:
            print('Too long Key. Imagine another one')
            continue
        
        for symbol in key:
            if ord(symbol) > 0xff:
                print('That key won\'t work. Try another using only latin alphabet and numbers')
                continue
        
        break

    print('\r\nPlease, wait...\n')

    time_before = time.time()

    # Input data
    m = raw_input()
    data = bytearray(m)
    
    #First step cod
    IV = bytearray('1234525890123456')
    C = IV
    
    
    #Adds bytes to the block if the size is less than 16 bytes
    def block_check_for_min_size(check_block):
        if 0 < len(check_block) < 16:
                empty_spaces = 16 - len(check_block)
                for i in range(empty_spaces - 1):
                    check_block.append(0)
                check_block.append(1)
        return check_block
   
    
    data = logical_xor(block_check_for_min_size(data),IV)
   
    print print_byte_of_array(data)
    
    
    

    if way == '1':
        crypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
	    #print str(len(temp))
            if len(temp) == 16:
		
                crypted_part = aes128.encrypt(temp, key)
                crypted_data.extend(crypted_part)
                del temp[:]
        else:
            #padding v1
            # crypted_data.extend(temp)

            # padding v2
            
            crypted_part = aes128.encrypt(block_check_for_min_size(temp), key)
            
		crypted_data.extend(crypted_part)

     
	
    print print_byte_of_array(crypted_data)
    # Ounput data
   

	# if way == '2'
    if(way == '1'): # if way == '2'
        decrypted_data = []
        temp = []
        for byte in crypted_data:
            temp.append(byte)
	    #print str(len(temp))
            if len(temp) == 16:
                decrypted_part = aes128.decrypt(temp, key)
                decrypted_data.extend(decrypted_part)
		del temp[:]
        else:
            #padding v1
            # decryptsed_data.extend(temp)
            
            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                decrypted_part = aes128.encrypt(temp, key)
                decrypted_data.extend(crypted_part) 

  		# decrypted_data


    
    print print_byte_of_array(decrypted_data)
    
    
    
    #C = bytearray('1234567890123456')
    
    decrypted_data = logical_xor(decrypted_data,C) 
    
    
    print print_byte_of_array(decrypted_data)
    
    print 'after XOR'

