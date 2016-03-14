%define oname clyde
Name: python3-module-%oname
Version: 0.8.0
Release: alt1.git20141130.1.1
Summary: Command line interface designer
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/clyde/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/clyde-hub/clyde.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-sugarbowl python3-module-jinja2
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python-module-sphinx-devel python3-module-sphinx
#BuildPreReq: python3-module-sphinx-settings
#BuildPreReq: python3-module-sphinx_rtd_theme

%py3_provides %oname
%py3_requires sugarbowl jinja2

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-sphinx_rtd_theme python3-module-sugarbowl xz
BuildRequires: python3-module-coverage python3-module-html5lib python3-module-jinja2-tests python3-module-nose python3-module-setuptools-tests python3-module-sphinx-settings rpm-build-python3 time

%description
Clyde is a command line interface designer.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
pushd docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
popd

%check
python3 setup.py test

%files
%doc *.rst demo docs/_build/html
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20141130.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20141130.1
- NMU: Use buildreq for BR.

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141130
- Initial build for Sisyphus

