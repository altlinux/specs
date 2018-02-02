%define mname sphinxjp.themes
%define oname %mname.revealjs

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150621.1.1.1
Summary: A sphinx theme for generate reveal.js presentation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxjp.themes.revealjs
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tell-k/sphinxjp.themes.revealjs.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-pytest-cov python-module-mock
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-pytest-cov python3-module-mock
#BuildPreReq: python3-module-sphinx
%endif

%py_provides %oname
%py_requires %mname setuptools sphinx

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme python3-module-unittest2
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest-cov python-module-setuptools python3-module-html5lib python3-module-jinja2-tests python3-module-mock python3-module-pytest-cov python3-module-setuptools python3-module-sphinx rpm-build-python3 time

%description
reveal.js style presentation theme for Sphinx.

%if_with python3
%package -n python3-module-%oname
Summary: A sphinx theme for generate reveal.js presentation
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname setuptools sphinx

%description -n python3-module-%oname
reveal.js style presentation theme for Sphinx.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD/src
%make -C docs html

%check
export LC_ALL=en_US.UTF-8
python setup.py test -v -a "--cov sphinxjp"
%if_with python3
pushd ../python3
python3 setup.py test -v -a "--cov sphinxjp"
popd
%endif

%files
%doc *.rst src/*.txt docs/_build/html
%python_sitelibdir/*.egg-info
%python_sitelibdir/sphinxjp/themes/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst src/*.txt docs/_build/html
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/sphinxjp/themes/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150621.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150621.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20150621.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150621
- Initial build for Sisyphus

