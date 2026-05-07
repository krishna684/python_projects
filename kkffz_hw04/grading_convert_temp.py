import subprocess
def test(i, f, to, expected):
    print(f"Test case {i} -- {f}, {to}")
    p = subprocess.Popen(["python3", "convert_temp.py"], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.stdin.write((str(f)+"\n").encode())
    p.stdin.write((str(to)+"\n").encode())
    output = p.communicate()[0].decode()
    actual = output.lower()
    # Extract the last number out of the output
    if expected == "invalid":
        if "invalid" in actual:
            print("  Passed")
        else:
            print("  Failed")
            print("  Actual:", output)
            print("  Expected:", expected)
    else:
        if expected in actual:
            print("  Passed")
        else:
            print("  Failed")
            print("  Actual:", actual)
            print("  Expected:", expected)
    p.terminate()

if __name__ == "__main__":
    test(1, -500, "m", "invalid")
    test(2, -20.2, "k", "244")
    test(3, 30, "c", "-1")
    test(4, 50, "g", "invalid")
