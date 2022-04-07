#Step:1 import the libraries for visulization
import seaborn as sns
import matplotlib.pyplot as plt


#Step 2: set the theme
sns.set_theme(style="ticks",color_codes=True)   

#Step 3: Import dataset
kashti = sns.load_dataset("titanic")

# Step 4: plot basic graph with one varibales
# p = sns.countplot(x="sex",data=kashti)
# print(kashti)
# plt.show() 


# # Step 5: plot basic graph with two variable
# p = sns.countplot(x="sex",data=kashti, hue="class")
# print(kashti)
# plt.show() 

# Step 6: plot basic graph with two variable and titles
p = sns.countplot(x="sex",data=kashti, hue="class")
p.set_title("Plot for Basic Count")
print(kashti)
plt.show() 