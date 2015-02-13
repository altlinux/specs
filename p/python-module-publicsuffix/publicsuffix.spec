%define oname publicsuffix

%def_with python3

Name: python-module-%oname
Version: 1.0.5
Release: alt1.git20150124
Summary: Get a public suffix for a domain name using the Public Suffix List
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/publicsuffix/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.tablix.org/~avian/git/publicsuffix.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
This module allows you to get the public suffix of a domain name using
the Public Suffix List from http://publicsuffix.org

%package -n python3-module-%oname
Summary: Get a public suffix for a domain name using the Public Suffix List
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module allows you to get the public suffix of a domain name using
the Public Suffix List from http://publicsuffix.org

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
%doc ChangeLog README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150124
- Initial build for Sisyphus

