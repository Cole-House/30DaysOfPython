dream_companies = ['Google', 'Apple', 'Facebook', 'Amazon', 'Microsoft']
dream_companies.append('Spotify')
print(dream_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
dream_companies[5] = dream_companies[5].upper();
print(dream_companies)
# Convert all elements to strings and join
result = "# ".join(map(str, dream_companies));
print(result)
dream_companies.sort()
print(dream_companies)
dream_companies.sort(reverse=True);
print(dream_companies)
slice_1=dream_companies[0:3];
print(slice_1);
slice_2=dream_companies[3:6];
print(slice_2);
middle_index = len(dream_companies) // 2
# Remove the middle IT company or companies from the list
dream_companies.pop(middle_index);
print(dream_companies);
dream_companies.pop();
print(dream_companies);
dream_companies.clear();
print(dream_companies);
del dream_companies;

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end);
print(front_end);
full_stack = front_end.copy()
print(full_stack);  
