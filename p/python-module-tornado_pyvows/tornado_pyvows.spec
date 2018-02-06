%define _unpackaged_files_terminate_build 1
%define oname tornado_pyvows

%def_disable check

Name: python-module-%oname
Version: 0.6.1
Release: alt1.1
Summary: tornado_pyvows are pyvows extensions to tornado web framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tornado_pyvows/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rafaelcaricio/tornado_pyvows.git
Source0: https://pypi.python.org/packages/1c/2a/da02e0db7106f7209bb20414d885b0a66684446cbc13a1c0c65252e3dc0b/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-mock
BuildPreReq: python-module-pyvows-tests python-module-tornado
BuildPreReq: python-module-pycurl python-module-urllib3
BuildPreReq: python-module-gevent python-module-unidecode

%py_provides %oname

%description
This project contains extensions to test Tornado apps under pyvows.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
%make test

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- automated PyPI update

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.git20141008
- Initial build for Sisyphus

