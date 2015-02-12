%define oname pytvrage

%def_without python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20120917
Summary: Python client for the tvrage.com XML API
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-tvrage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ckreutzer/python-tvrage.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-BeautifulSoup
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-BeautifulSoup
%endif

%py_provides %oname tvrage
%py_requires BeautifulSoup
Conflicts: python-module-tvrage

%description
python-tvrage is a python based object oriented client interface for
tvrage.com's XML based api feeds.

%package -n python3-module-%oname
Summary: Python client for the tvrage.com XML API
Group: Development/Python3
%py3_provides %oname tvrage
%py3_requires BeautifulSoup
Conflicts: python3-module-tvrage

%description -n python3-module-%oname
python-tvrage is a python based object oriented client interface for
tvrage.com's XML based api feeds.

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

%files
%doc AUTHORS NEWS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20120917
- Initial build for Sisyphus

