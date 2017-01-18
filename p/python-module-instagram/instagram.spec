%define _unpackaged_files_terminate_build 1
%define oname instagram

Name: python-module-%oname
Version: 1.3.2
Release: alt1
Summary: Instagram API client
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-instagram/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Instagram/python-instagram.git
Source0: https://pypi.python.org/packages/35/a9/c33c2224e4bbc8579940199c98cc980ee5424623f72e142612ba03c567ea/python-%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
Python Client for Instagram API
http://instagram.com/developers/

%prep
%setup -q -n python-%{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1
- automated PyPI update

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20140805
- Initial build for Sisyphus

