from ansible.errors import AnsibleFilterError

def transform_dict_var3(dict_var):
    try:
                result = {}
                for key, value in dict_var.items():
                        interface = key.split('/')[0]
                        vpc_temp = str(value)
                        vpc = vpc_temp[:2]
                        result = {}
                        if interface not in result:
                                result[interface] = []
                        if vpc not in result[interface] and len(result[interface]) == 0:
                                result[interface].append(vpc)
                        if vpc not in result[interface] and len(result[interface]) != 0:
                                result[interface] = ['9999']
                return result
    except Exception as e:
        raise AnsibleFilterError('Error occurred while transforming the dict_var: {}'.format(e))

class FilterModule(object):
    ''' Query filter '''

    def filters(self):
        return{
            'transform_dict_var3' : transform_dict_var3
        }
