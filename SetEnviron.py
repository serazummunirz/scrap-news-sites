import os


def SetEnviron():
    
    with open('.env', 'r') as f:
        all_environs = f.readlines()
        for env in all_environs:
            key = env.split("=")[0].strip()
            value = env.split("=")[1].strip()

            if key == "DATE" and len(value) < 2:
                value = f"0{value}"

            if key == "MONTH":
                value = value.upper()[:3]

            if key == "KEYWORD":
                value = value.lower()

            os.environ[key] = value