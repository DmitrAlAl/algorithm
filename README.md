algorithm
=========

Для выявления похожих людей, их можно раскидать по многомерному пространству, осями которого могут быть любимые книги, например. Для поиска близких по интересам точек, используется формула определения расстояния. На плоскости L=Корень из суммы квадратов. Для трехмерного пространства то же. И для любого многомерного...


Желательно сначала нормировать оценки, т.к. они могут быть стабильно завышенными или заниженными.

Для вычисления оптимального значения при большом количестве переменных, вводят весовые коэффициенты для каждого параметра.
optimum = сумма(весовой коэфф. на значение параметра)/делить на сумму весовых коэффициентов. Значения параметра тоже должны быть примерно одинаковыми. Желательно нормированы единицей.

Кстати, для нормализации можно разделить значение каждого конкретного параметра на сумму остальных.
