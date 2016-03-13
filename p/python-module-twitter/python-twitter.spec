%define oname twitter

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt2.1
Summary: Python Interface for Twitter API

Group: Development/Python
License: Apache License 2.0
Url: http://code.google.com/p/python-twitter/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif
%py_requires rfc822 requests requests_oauthlib

%description
This library provides a pure python interface for the Twitter API.

%package -n python3-module-%oname
Summary: Python Interface for Twitter API
Group: Development/Python3
%py3_requires rfc822py3 requests requests_oauthlib
%py3_provides %oname

%description -n python3-module-%oname
This library provides a pure python interface for the Twitter API.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
find ../python3 -type f -name '*.py' -exec sed -i 's|rfc822|rfc822py3|g' '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
%python3_build
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

%files
%doc *.rst CHANGES COPYING LICENSE NOTICE doc/twitter.html examples/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst CHANGES COPYING LICENSE NOTICE doc/twitter.html examples/
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added %%py3_provides for Python 3 module

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Version 2.0
- Added module for Python 3

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2
- Rebuild with Python-2.7

* Sun Mar 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Apr 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1
- Initial
