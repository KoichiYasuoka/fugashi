from fugashi import Tagger
import pytest

WAKATI_TESTS = (
        ("すももももももももの内", 'すもも も もも も もも の 内'),
        ("日本語ですよ", '日本 語 です よ'),
        ("深海魚は、深海に生息する魚類の総称。", '深海 魚 は 、 深海 に 生息 する 魚類 の 総称 。'),
        )

TOKENIZER_TESTS = (
        ('あなたは新米の魔女。', ['あなた', 'は', '新米', 'の', '魔女', '。']),
        ('パートナーである猫と共に、見知らぬ町へやってきたばかりです。', ['パートナー', 'で', 'ある', '猫', 'と', '共', 'に', '、', '見知ら', 'ぬ', '町', 'へ', 'やっ', 'て', 'き', 'た', 'ばかり', 'です', '。']),

        )

@pytest.mark.parametrize('text,wakati', WAKATI_TESTS)
def test_wakati(text, wakati):
    tagger = Tagger('-Owakati')
    assert tagger.parse(text) == wakati

@pytest.mark.parametrize('text,saved', TOKENIZER_TESTS)
def test_tokens(text, saved):
    # testing the token objects is tricky, so instead just check surfaces
    #TODO: maybe save serialized nodes to compare?
    tagger = Tagger()
    tokens = [str(tok) for tok in tagger.parseToNodeList(text)]
    assert tokens == saved
