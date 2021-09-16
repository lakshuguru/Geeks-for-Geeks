'''perform this task of removing tuples using various methods and ways in Python.
Examples:

Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('', '')]

Input : tuples = [('','','8'), (), ('0', '00', '000'), 
                 ('birbal', '', '45'), (''), (),  ('',''),()]
Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '', 
          '45'), ('', '')]'''

t= [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
for i in t:
    if(i==()):
        t.remove(i)
print(t)                                    