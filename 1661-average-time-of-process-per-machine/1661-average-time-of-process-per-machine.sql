select machine_id,round((select avg(timestamp) from activity a1 where a1.machine_id=a.machine_id and activity_type='end') - (select avg(timestamp) from activity a2 where a2.machine_id=a.machine_id and activity_type='start'),3) as processing_time
from Activity a
group by machine_id;