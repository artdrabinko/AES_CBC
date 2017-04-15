if __name__ == '__main__':

    import time
    import aes128
   
    
    
    def print_byte_of_array(byte_array):
        message_of_array = ''
        i_array = 0
        while i_array < len(byte_array):
            message_of_array = message_of_array + str(chr(byte_array[i_array])) 
            i_array = i_array + 1
        return message_of_array
    
    def logical_xor(data_byte_arry_for_xor,Ci):
        i_xor = 0
        while i_xor < len(data_byte_arry_for_xor):
            #print str(data_byte_arry_for_xor[i_xor])  + " xor  " + str(Ci[i_xor])
            data_byte_arry_for_xor[i_xor] = data_byte_arry_for_xor[i_xor] ^ Ci[i_xor]
            #print str(data_byte_arry_for_xor[i_xor])
            i_xor = i_xor + 1
        #print print_byte_of_array(data_byte_arry_for_xor)   
        return data_byte_arry_for_xor
    
    #Adds bytes to the block if the size is less than 16 bytes
    def block_check_for_min_size(check_block):
        if 0 < len(check_block) < 16:
                empty_spaces = 16 - len(check_block)
                for i in range(empty_spaces - 1):
                    check_block.append(0)
                check_block.append(1)
        #print print_byte_of_array(check_block) + '1'
        return check_block

    
    
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
    m = raw_input('Input message there: ')
    data = bytearray(m)
    
    #First step cod
    C = bytearray('qwertyuiopasdfgh')
     
    

    if way == '1':
        
        crypted_data = []
        
        crypted_part = C 


        temp = []
        i_counter = 1
        for byte in data:
            temp.append(byte)
	    #print str(len(temp))
            if len(temp) == 16:

                if i_counter < 2:
                    print str(i_counter) + ' part message == 16 bytes'
                    crypted_part = aes128.encrypt(logical_xor(crypted_part,temp), key)
                    print str(i_counter) + ' crypted part with IV ' + str(crypted_part) + '\n'
                else:
                    print str(i_counter) + ' part message also == 16 bytes'
                    print str(i_counter) + ' crypted (part - 1) ' + str(crypted_part)
                    crypted_part = aes128.encrypt(logical_xor(crypted_part,temp), key)
                    print str(i_counter) + ' crypted part ' + str(crypted_part) + '\n'
                
                #crypted_part = aes128.encrypt(temp, key)
                crypted_data.extend(crypted_part)
                
                i_counter = i_counter + 1
                del temp[:]
        else:
            if 0 < len(temp) < 16:
                print str(i_counter) + ' part message < 16 bytes' 
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                print str(i_counter) + ' crypted (part - 1) ' + str(crypted_part)
                crypted_part = aes128.encrypt(logical_xor(crypted_part,temp), key)
                print str(i_counter) + ' crypted part ' + str(crypted_part) + '\n'
                crypted_data.extend(crypted_part)
                
                i = i + 1

     
    print str(crypted_data) + 'lol 2'
    # Ounput data
   

	# if way == '2'
    if(way == '1'): 
        decrypted_data = []
        IV = bytearray('qwertyuiopasdfgh')
        C = IV
        C_min_1 = []
        decrypted_part = C
        temp = []
        i_dec = 1
        for byte in crypted_data:
            temp.append(byte)
	    #print str(len(temp))
            if len(temp) == 16:
                
                if i_dec < 2:
                    C_min_1.extend(temp)
                    print C_min_1
                    print key
                    print str(aes128.decrypt(temp, key))
                    decrypted_part = logical_xor(C,aes128.decrypt(temp, key))
                    #C_min_1 = aes128.decrypt(temp, key)
                    #print print_byte_of_array(C_min_1)
                    print '1'
                    print print_byte_of_array(decrypted_part)
                    print C_min_1
                    
                else:
                    print aes128.decrypt(temp, key)
                    #print 'zdy change!'
                    print C_min_1
                    decrypted_part = logical_xor(C_min_1,aes128.decrypt(temp, key))
                    print C_min_1
                    print str(C_min_1) + " " + str(aes128.decrypt(temp, key))
                    #C_min_1 = aes128.decrypt(temp, key)
                    #del C_min_1[:]
                    #C_min_1.extend(temp)
                    print '2'
                    print print_byte_of_array(decrypted_part)

                decrypted_data.extend(decrypted_part)
                del C_min_1[:]
                C_min_1.extend(temp)
                i_dec = i_dec + 1
                del temp[:]
            
        #else:
            #padding v1
            # decryptsed_data.extend(temp)
            
            # padding v2
           #if 0 < len(temp) < 16:
               # empty_spaces = 16 - len(temp)
                #for i in range(empty_spaces - 1):
                    #temp.append(0)
                #temp.append(1)
                #decrypted_part = aes128.encrypt(temp, key)
                #decrypted_data.extend(crypted_part) 
                

    
    print 'Out  message there: ' + print_byte_of_array(decrypted_data)

    
