%define oname sphinx_testing

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1.git20150823
Summary: Testing utility classes and functions for Sphinx extensions
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-testing
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sphinx-doc/sphinx-testing.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-sphinx
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-sphinx
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires sphinx six

%description
sphinx-testing provides testing utility classes and functions for Sphinx
extensions.

%if_with python3
%package -n python3-module-%oname
Summary: Testing utility classes and functions for Sphinx extensions
Group: Development/Python3
%py3_provides %oname
%py3_requires sphinx six

%description -n python3-module-%oname
sphinx-testing provides testing utility classes and functions for Sphinx
extensions.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test -v
export PYTHONPATH=$PWD/src
nosetests -vv --with-coverage --cover-package=%oname
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD/src
nosetests3 -vv --with-coverage --cover-package=%oname
popd
%endif

%files
%doc AUTHORS Sphinx-AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS Sphinx-AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150823
- Initial build for Sisyphus

