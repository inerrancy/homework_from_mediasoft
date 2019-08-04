from datetime import datetime


def decor(print_face):
    def timer(*args, **kwargs):
        t_before = datetime.now().timestamp()
        print(t_before)
        print_face(*args, **kwargs)
        t_after = datetime.now().timestamp()
        print(t_after)
        d_t = t_after - t_before
        print(d_t)

    return timer


@decor
def print_face():
    print("""
             ツ
            ツツ
           ツツツ
          ツツツツ
        ツツツツツツ
        """)


print_face()
