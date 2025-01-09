def input_columns(table):
    if not isinstance(table, str):
        raise TypeError('table is not a string')

    columns = {
        "users": ("id", "name", "age"),
        "product": ("pid", "prod", "quantity"),
        "sales": ("sid", "pid", "id")
    }

    if table not in columns:
        raise KeyError('table is not in columns')

    field = input(f"Выберите одно из полей {columns[table]} этой таблицы или введите * для выбора всех: ").strip()
    field = columns.get(field, '*')

    return f"SELECT {field} FROM {table};"


print(input_columns("users"))