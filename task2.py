def common_topics(first, second):
    common = set(first) & set(second)
    return sorted(common)
def all_topics(first, second):
    everything = set(first) | set(second)
    return sorted(everything)
if __name__ == '__main__':
    first  = ['python', 'sql', 'git', 'python']
    second = ['sql', 'git', 'linux', 'java']
    print('Общие темы: ', common_topics(first, second))
    print('Все темы: ', all_topics(first, second))
    print('Пустые списки: ', common_topics([], []))
    print('Нет пересечений: ', common_topics(["a"], ["b"]))
