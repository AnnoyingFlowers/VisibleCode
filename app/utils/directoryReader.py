import os


def read_directory(path, result):
    paths = os.listdir(path)
    for i, item in enumerate(paths):
        sub_path = os.path.join(path, item)
        if os.path.isdir(sub_path):
            result.append(dict(
                name=item,
                value=max(os.path.getsize(sub_path) // 1024, 1),
                path=path,
                children=[]
            ))
            read_directory(sub_path, result[-1]['children'])
        else:
            result.append(dict(
                name=item,
                value=max(os.path.getsize(sub_path) // 1024, 1),
                path=path
            ))
