-- Número total de usuários ativos no último mês
SELECT COUNT(DISTINCT user_id) as active_users
FROM user_activity_table
WHERE activity_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE();

-- Atividades mais comuns entre os usuários
SELECT activity_type, COUNT(*) as activity_count
FROM user_activity_table
GROUP BY activity_type
ORDER BY activity_count DESC;

-- Usuários que fizeram compras mas não se envolveram em outras atividades nos últimos 30 dias
SELECT user_id
FROM user_activity_table
WHERE activity_type = 'purchase'
AND user_id NOT IN (
    SELECT DISTINCT user_id
    FROM user_activity_table
    WHERE activity_type != 'purchase'
    AND activity_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE()
);

-- Usuários que visitaram mais de 10 vezes mas não fizeram nenhuma compra nos últimos 30 dias
SELECT user_id, COUNT(*) as visit_count
FROM user_activity_table
WHERE activity_type = 'visit'
AND activity_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE()
GROUP BY user_id
HAVING visit_count > 10
AND user_id NOT IN (
    SELECT DISTINCT user_id
    FROM user_activity_table
    WHERE activity_type = 'purchase'
    AND activity_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE()
);
