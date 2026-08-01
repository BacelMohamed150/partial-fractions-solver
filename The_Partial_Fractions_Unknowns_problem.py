import sympy as sp
# بنعرف المتغيرات و مقدار اللي هنحلله
x = sp.symbols('x')
A, B, C, D, E, F, G = sp.symbols('A B C D E F G')
x_array = [A, B, C, D, E, F, G] # : دي مصفوفة المجاهيل في نظام الجبر الخطي
                       # Ax = b
l = x**7 + 1
# هنا هنجيب تحليل بجبر حقيقي للمقدار l
const, lf = sp.factor_list(l)
term1 = lf[0][0]
term2 = lf[1][0]
# هنستعمل نظرية الكسور الجزئية
expr = sp.expand(((A)*(term2))+((B*x**5 + C*x**4 + D*x**3 + E*x**2 + F*x + G)*(term1)) - 1)

A_array = [] # بنعمل مصفوفة فاضية علشان نملاها بمعاملات
for i in range(len(x_array)): # هنا بنطلب ان الكمبيوتر يعدي عدد من المرات مساوي لعدد المجاهيل لاحضار معاملات كل مقدار به
                              # for every x to the power of i ,as i is considered a period of positive intgers between 0 and 5
    coeff = expr.coeff(x,i)   # بنطلب معاملات المقدار الكبير دا
    A_array.append(sp.Eq(coeff,0)) # بنطلب ملء المصفوفة الفارغة بعناصر عبارة عن معادلات
    

sol_dic = sp.solve(A_array, x_array) # دالة الحل في المكتبة هتحولها لقاموس هنحتاج نحوله لمصفوفة
sol_mat = sp.Matrix([sol_dic[var] for var in x_array]) # كدا طلبنا تحويل قاموس المجاهيل لمصفوفة للتعامل السهل معها

print(sol_mat)







  




