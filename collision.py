def check_collision(*hitboxes) -> bool:
    if len(hitboxes) < 2:
        return False

    hitboxes_sets = [object.points_set for object in hitboxes]
    hitboxes_sets_sum = set()
    for hitbox_points_set in hitboxes_sets:
        hitboxes_sets_sum = hitboxes_sets_sum | hitbox_points_set

    hitboxes_points_len = sum(map(len, hitboxes_sets))
    if len(hitboxes_sets_sum) == hitboxes_points_len:
        return False

    return True


def check_collision_first(mainhb, hitboxes) -> bool:
    mainset = mainhb.points_set
    hitbox_fst_len = len(mainset)
    cnt = 0
    for hitbox in hitboxes:
        hbset = hitbox.points_set
        hitbox_sec_len = len(hbset)
        hitboxes_sets_sum = hitbox_fst_len + hitbox_sec_len
        hitboxes_setsf_sum = len(mainset | hbset)
        if hitboxes_sets_sum != hitboxes_setsf_sum:
            cnt += 1
    return bool(cnt)


class Hitbox:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.points_set = set()
        for column in range(h):
            for row in range(w):
                self.points_set.add(tuple([row + x, column + y]))

    @property
    def up(self):
        return self.y

    @property
    def down(self):
        return self.y + self.h

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w


def main():
    hb1 = Hitbox(x=0, y=0, w=2, h=2)
    hb2 = Hitbox(x=0, y=2, w=2, h=2)
    print(check_collision_first(hb1, hb2, hb2, hb2, hb1))


if __name__ == '__main__':
    main()
