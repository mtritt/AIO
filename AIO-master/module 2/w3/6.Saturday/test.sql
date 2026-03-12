-- subqueries 
select client_id , name 
    (slect sum(ivoice_total)
    from invoices 
    where c.client_id = client_id) as invoice_amount 
from clients c
order by invoice_amount desc 
limit 1 

-- temp table 
create temporary table temp_invoice(
    client_id int, 
    invoice_sum decimal(10 ,2) ,
    invoice_avg decimal(10 ,2) 
)

select * from temp_invoice 

-- insert into temp table 
insert into temp_invoice
select client_id 
    sum(invoice_total) as invoice_sum 
    avg(invoice_total) as invoice_avg
from invoices 
group by client_id


-- store procedures

-- trigger 

-- practice 
-- #1 
-- using the sql_hr database how would you retrieve a list of employees who earns a higher salary than their manager using sub query 
select e1.* 
from employee e1
where e1.salary > (
    select e2.salary 
    from employee e2 
    where e1.reports_to = e2.employee_id
)
-- #2 
-- create temporary table that includes first name , last name and office address for each employee 
create temporary table temp_employee as 
select e.first_name , e.last_name , o.address as office_address 
from employee e 
join offices o on e.office_id = o.office_id 
-- #3 
create procedure update_payment_invoice 
as
    @new_payment_id int , 
    @new_client_id int , 
    @new_invoice_id int , 
    @new_date int , 
    @new_amount int , 
    @new_payment_method int 
begin 
    insert into payments (payment_id , client_id , invoice_id , date , amount , payment_method)
    values (new_payment_id , new_client_id , new_invoice_id, new_date , new_amount , new_payment_method)

    update invoices 
    set payment_total = payment_total + new_amount
    where invoice_id = new_invoice_id
end 
-- #4 
create procedure find_most_payment
begin 
    select client_id , count(payment_id) as payment_count
    from payments 
    where date >= date_sub(current_date , interval 1 year)
    group by client_id 
    order by payment_count desc 
    limit 1 
end 
-- #5 
-- list the orders that have a total amount greater than the avg order amount using a subquery 
select order_id 
from orders o 
where (
    select sum(oi.quantity * oi.unit_price)
    from orders_items oi 
    where oi.order_id = o.order_id 
) > (
    select avg(order_amount)
    from(
        select oi.order_id , sum(oi.quantity * oi.unit_price) as order_amount 
        from orders_items oi 
        group by oi.order_id

    ) as avg_order 
)