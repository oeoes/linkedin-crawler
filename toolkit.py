import os
import csv


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Membuat project baru ' + directory)
        os.makedirs(directory)
        save_crawled_data(directory)


def save_crawled_data(project_name):
    """
    Membuat inisial file, result.csv dan cached.txt
    result.csv untuk file hasil crawled
    cached.txt untuk caching data yang sudah crawlec
    :param project_name:
    :return:
    """
    urls = project_name + '/result.csv'
    cache = project_name + '/cached.txt'
    if not os.path.isfile(urls):
        with open(cache, 'w'):
            pass
        print('Cache file created.')
        with open(urls, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Occupation", "Account Url",
                             "Image Url", "Email", "Website", "Phone Number"])
        print('Init file created.')


def cached_file_to_set(filename):
    results = set()
    with open(filename, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


def set_to_cached_file(urls_set, filename):
    for url in urls_set:
        append_to_cached_file(filename, url)


def append_to_cached_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')


def append_to_file(file_name, data):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
