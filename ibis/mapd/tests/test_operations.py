import ibis
import numpy as np
import pytest

from pytest import param

pytestmark = pytest.mark.mapd
pytest.importorskip('pymapd')


@pytest.mark.parametrize(('result_fn', 'expected'), [
    param(
        lambda t: t[t, ibis.literal(1).degrees().name('n')].limit(1)['n'],
        57.2957795130823,
        id='literal_degree'
    ),
    param(
        lambda t: t[t, ibis.literal(1).radians().name('n')].limit(1)['n'],
        0.0174532925199433,
        id='literal_radians'
    ),
    param(
        lambda t: t.double_col.corr(t.float_col),
        1.000000000000113,
        id='double_float_correlation'
    ),
    param(
        lambda t: t.double_col.cov(t.float_col),
        91.67005567565313,
        id='double_float_covariance'
    )
])
def test_operations_scalar(alltypes, result_fn, expected):
    result = result_fn(alltypes).execute()
    np.testing.assert_allclose(result, expected)
