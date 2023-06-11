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

        let mut max_value: isize = 0;
        if max_value_tail < list[0] {
            max_value = list[0];
        } else {
            max_value = max_value_tail;
        }
        return max_value;
    }
}
