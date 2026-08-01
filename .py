import sympy as sp

# 1. تعريف الرموز والمتغيرات
x = sp.symbols('x')
A, B, C, D, E, F = sp.symbols('A B C D E F')
variables = [A, B, C, D, E, F]

# 2. تحليل المقام وأقسامه
z = x**2 + 1
y = x**2 + sp.sqrt(3)*x + 1
v = x**2 - sp.sqrt(3)*x + 1

# 3. البسط الكلي Ln
Ln = (A*x+B)*(y*v) + (C*x+D)*(z*v) + (E*x+F)*(z*y)

# 4. تكوين المعادلات عن طريق مقارنة معاملات x من الدرجة 0 إلى 5
# بما أن البسط الأصلي للكسر هو 1، إذن الحد المطلق = 1 وباقي المعاملات = 0
equations = []
target_coefficients = [1, 0, 0, 0, 0, 0]

for i in range(len(variables)):
    coeff = Ln.coeff(x, i)
    # بنعمل المعادلة بحيث يكون المعامل بيساوي القيمة المستهدفة
    equations.append(sp.Eq(coeff, target_coefficients[i]))

# 5. تحويل المعادلات لنظام مصفوفات (A * X = b) بطريقة صحيحة ومضمونة
A_matrix, b_vector = sp.linear_eq_to_matrix(equations, variables)

# 6. حل النظام الخطي للحصول على قيم المتغيرات بدقة رمزية
solution = sp.linsolve((A_matrix, b_vector), variables)

print("قيم الثوابت (A, B, C, D, E, F) بدقة رمزية (جذور وكسور):")
sp.pprint(solution)