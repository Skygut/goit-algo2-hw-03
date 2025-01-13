# goit-algo2-hw-03

## Завдання 1:
### 1. **Які термінали забезпечують найбільший потік товарів до магазинів?**
   - Згідно з розрахунками потоків:
     - **"Термінал 1"** забезпечує найбільший потік товарів до магазинів завдяки високій пропускній здатності з'єднань із складами (наприклад, "Склад 1", "Склад 2") та прямим шляхам до багатьох магазинів.
     - **"Термінал 2"** також робить суттєвий внесок, але його потік обмежений через вузькі місця на певних маршрутах, наприклад, через "Склад 4".

### 2. **Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік?**
   - Маршрути з найменшою пропускною здатністю:
     - **"Склад 4" → "Магазин 13" (5 одиниць)**.
     - **"Термінал 2" → "Склад 2" (10 одиниць)**.
   - Ці низькопропускні маршрути значно обмежують потік від "Терміналу 2" до магазинів, створюючи вузькі місця, які заважають використовувати повний потенціал терміналу.

### 3. **Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів?**
   - Магазини, які отримали найменше товарів:
     - **"Магазин 13" (5 одиниць)** через низьку пропускну здатність маршруту "Склад 4" → "Магазин 13".
     - **"Магазин 5" (10 одиниць)** через обмеження на маршруті "Склад 2".
   - Збільшення постачання можливе шляхом підвищення пропускної здатності таких маршрутів:
     - **"Склад 4" → "Магазин 13"**.
     - **"Склад 2" → "Магазин 5"**.

### 4. **Чи є вузькі місця, які можна усунути для покращення ефективності логістичної мережі?**
   - Основні вузькі місця:
     - **"Склад 4" → "Магазин 13" (5 одиниць)**, який повністю завантажений і обмежує потік.
     - **"Термінал 2" → "Склад 2" (10 одиниць)**, що зменшує внесок "Терміналу 2".
   - Для покращення ефективності необхідно:
     - Збільшити пропускну здатність цих маршрутів.
     - Оптимізувати розподіл потоків, щоб уникнути перевантаження певних маршрутів і недовикористання інших.


## Завдання 2

На основі отриманих результатів порівняльного аналізу продуктивності **OOBTree** і **dict** для діапазонних запитів можна зробити наступні висновки:

1. **Час виконання діапазонних запитів**:
   - **OOBTree**: Загальний час виконання 100 запитів склав **1.694532 секунд**.
   - **Dict**: Загальний час виконання 100 запитів склав **0.368792 секунд**.

2. **Продуктивність**:
   - **Dict** значно перевершує **OOBTree** для даного сценарію, оскільки його час виконання майже в 4.6 разів менший.
   - Це можна пояснити тим, що для `dict` діапазонні запити реалізовані через лінійний пошук, який може бути ефективним на невеликому обсязі даних.

3. **Структура даних**:
   - **OOBTree** є більш ефективною структурою для роботи з великими обсягами даних, особливо якщо дані вже відсортовані або потрібна часта вибірка в діапазоні. Однак у цьому випадку невеликий обсяг даних та високі накладні витрати на роботу з деревом зробили цю структуру менш ефективною.

## Підсумок:
- Використовувати **OOBTree** доцільно у випадках, коли потрібно обробляти великий обсяг даних і виконувати багато діапазонних запитів.
- Для невеликих наборів даних **dict** забезпечує кращу продуктивність і простоту використання. 
