import pytest


@pytest.mark.integration
@pytest.mark.predictor
@pytest.mark.au
def test_au_in_preds(response):
    for face in response.faces:
        assert "au" in face.preds.keys()


@pytest.mark.endtoend
@pytest.mark.predictor
@pytest.mark.au
def test_lip_pucker(response, cfg):
    if "test.jpg" not in cfg.path_image:
        pytest.skip("Ony test.jpg is used for this test.")
    assert response.faces[0].preds["au"].label == "lip_pucker"
