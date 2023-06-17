fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let result = sum(numbers);
    assert_eq!(result, 45);

    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let result_len = len(numbers);
    assert_eq!(result_len, 9);

    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let result_max = max(numbers);
    assert_eq!(result_max, 9);

    let numbers = vec![10, 8, 2, 6, 3, 6, 1, 4, 7, 5, 9];
    let result_max = quicksort(numbers);
    assert_eq!(result_max, vec![1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]);
}

fn sum(list: Vec<isize>) -> isize {
    if list.len() == 1 {
        return list[0];
    } else if list.len() == 0 {
        return 0;
    } else {
        let mut tail: Vec<isize> = Vec::new();
        for i in 1..list.len() {
            tail.push(list[i])
        }
        return sum(tail) + list[0];
    }
}

fn len<T>(list: Vec<T>) -> isize {
    if list.len() == 1 {
        return 1;
    } else if list.len() == 0 {
        return 0;
    } else {
        let mut tail: Vec<usize> = Vec::new();
        for i in 1..list.len() {
            tail.push(i)
        }
        return len(tail) + 1;
    }
}

fn max(list: Vec<isize>) -> isize {
    if list.len() == 1 {
        return list[0];
    } else if list.len() == 0 {
        return 0;
    } else {
        let mut tail: Vec<isize> = Vec::new();
        for i in 1..list.len() {
            tail.push(list[i])
        }

        let max_value_tail = max(tail);

        let max_value: isize;
        if max_value_tail < list[0] {
            max_value = list[0];
        } else {
            max_value = max_value_tail;
        }
        return max_value;
    }
}

fn quicksort(mut list: Vec<isize>) -> Vec<isize> {
    if list.len() < 2 {
        return list;
    } else {
        let mut head = Vec::new();
        let mut tail = Vec::new();

        let main_element = list.pop().unwrap();
        for i in list {
            if i > main_element {
                head.push(i);
            } else {
                tail.push(i);
            }
        }
        let mut result = Vec::new();
        result.extend(quicksort(tail));
        result.extend(vec![main_element]);
        result.extend(quicksort(head));
        return result;
    }
}
