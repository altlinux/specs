%define mname sphinxjp.themes
%define oname %mname.revealjs

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150621
Summary: A sphinx theme for generate reveal.js presentation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxjp.themes.revealjs
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tell-k/sphinxjp.themes.revealjs.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest-cov python-module-mock
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cov python3-module-mock
BuildPreReq: python3-module-sphinx
%endif

%py_provides %oname
%py_requires %mname setuptools sphinx

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
* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150621
- Initial build for Sisyphus

