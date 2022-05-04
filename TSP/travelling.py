from pirat import Pirat
from islands import reading_txt

if __name__ == '__main__':
    n, p, k, M, islands = reading_txt(input())
    pirat_mipt, pirat_msu = Pirat(), Pirat()

    travelled = [1]
    while pirat_mipt.travelling and pirat_msu.travelling:
        pirat_mipt.travel(islands)
        pirat_msu.travel(islands)

    ans = pirat_mipt.path + pirat_msu.path[::-1]
    print(*ans)
