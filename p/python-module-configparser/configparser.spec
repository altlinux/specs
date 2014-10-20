%define oname configparser

%def_with python3

Name: python-module-%oname
Version: 3.5.0
Release: alt1.b2
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/configparser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This is a backport of those
changes so that they can be used directly in Python 2.6 - 3.5.

%package -n python3-module-%oname
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This is a backport of those
changes so that they can be used directly in Python 2.6 - 3.5.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.b2
- Initial build for Sisyphus

