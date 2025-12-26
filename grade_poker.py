card_ranks = "23456789TJQKA"
card_suits = "CDHS"
hand_size = 5

def card_rank_index(card):
    return card_ranks.index(card[0])

def card_rank_value(card):
    return card_rank_index(card) + 2

def sort_cards(cards):
    return sorted(cards, key=card_rank_index)

def card_rank_counts(cards):
    counts = [0] * len(card_ranks)
    for card in cards:
        idx = card_rank_index(card)
        counts[idx] += 1
    return counts

def is_flush(cards):
    suit = None
    for card in cards:
        if suit is None:
            suit = card[1]
            continue
        if card[1] != suit:
            return False
    return True

def is_straight_and_rank(cards):
    cards = sort_cards(cards)
    rank_seq = "".join(card[0] for card in cards)
    if rank_seq in card_ranks:
        return True, card_rank_index(cards[-1])
    elif rank_seq == card_ranks[:hand_size-1] + card_ranks[-1]:
        return True, card_rank_index(cards[-2])
    return False, 0

def evaluate_hand(cards):
    assert len(cards) == hand_size
    flush = is_flush(cards)
    straight, straight_rank = is_straight_and_rank(cards)

    card_idxs = [card_rank_index(card) for card in cards]
    card_counts = card_rank_counts(cards)
    max_count = max(card_counts)
    desc_card_idxs = sorted(card_idxs, reverse=True)

    if straight and flush:
        return 9, (straight_rank,)

    if max_count == 4:
        main_rank = card_counts.index(4)
        second_rank = card_counts.index(1)
        return 8, (main_rank, second_rank)

    if max_count == 3:
        main_rank = card_counts.index(3)
        pair_count = card_counts.count(2)
        if pair_count == 1:
            second_rank = card_counts.index(2)
            return 7, (main_rank, second_rank)
        else:
            extra_ranks = (idx for idx in desc_card_idxs if idx != main_rank)
            return 4, (main_rank, *extra_ranks)

    if flush:
        return 6, (*desc_card_idxs,)

    if straight:
        return 5, (straight_rank,)

    if max_count == 2:
        first_pair = card_counts.index(2)
        pair_count = card_counts.count(2)
        if pair_count == 2:
            second_pair = card_counts.index(2, first_pair+1)
            extra_ranks = (idx for idx in desc_card_idxs if idx not in (first_pair, second_pair))
            return 3, (second_pair, first_pair, *extra_ranks)
        else:
            extra_ranks = (idx for idx in desc_card_idxs if idx != first_pair)
            return 2, (first_pair, *extra_ranks)

    return 1, desc_card_idxs

def compare_hands(hand_1, hand_2):
    grade_1, ranks_1  = evaluate_hand(hand_1)
    grade_2, ranks_2  = evaluate_hand(hand_2)
    if grade_1 < grade_2:
        return -1
    elif grade_1 > grade_2:
        return 1
    for rank_1, rank_2 in zip(ranks_1, ranks_2):
        if rank_1 < rank_2:
            return -1
        elif rank_1 > rank_2:
            return 1
    return 0


if __name__ == "__main__":
    fname = "poker.txt"
    p_1_wins = 0
    with open(fname, "r", encoding="utf-8") as f:
        for line in f:
            cards = line.strip().split()
            hand_1 = cards[:hand_size]
            hand_2 = cards[hand_size:]
            result = compare_hands(hand_1, hand_2)
            if result > 0:
                p_1_wins += 1
    print(p_1_wins)
