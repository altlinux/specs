%define oname binaryornot

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20140505
Summary: Ultra-lightweight pure Python package to check if a file is binary or text
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/binaryornot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/audreyr/binaryornot.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-invoke python-module-flake8
BuildPreReq: python-module-autopep8 python-module-coverage
BuildPreReq: python-module-tox
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-invoke python3-module-flake8
BuildPreReq: python3-module-autopep8 python3-module-coverage
BuildPreReq: python3-module-tox
%endif

%py_provides %oname

%description
Ultra-lightweight pure Python package to guess whether a file is binary
or text, using a heuristic similar to Perl's pp_fttext and its analysis
by @eliben.

%package -n python3-module-%oname
Summary: Ultra-lightweight pure Python package to check if a file is binary or text
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Ultra-lightweight pure Python package to guess whether a file is binary
or text, using a heuristic similar to Perl's pp_fttext and its analysis
by @eliben.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Ultra-lightweight pure Python package to guess whether a file is binary
or text, using a heuristic similar to Perl's pp_fttext and its analysis
by @eliben.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Ultra-lightweight pure Python package to guess whether a file is binary
or text, using a heuristic similar to Perl's pp_fttext and its analysis
by @eliben.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20140505
- Initial build for Sisyphus

