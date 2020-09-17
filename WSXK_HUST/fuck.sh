touch /tmp/fuck.log
while true
do
    sleep 0.2
	./fuck_one_course.sh > /tmp/fuck.log
	if grep '选课失败，课堂人数已满！' /tmp/fuck.log
	then
		echo 'Failed'
	else
		echo 'Success'
	fi
done
