%define oname oauth2

Name: python3-module-%oname
Version: 1.9
Release: alt2
Summary: Library for OAuth version 1.0a (forked from python-oauth)

Group: Development/Python3
License: MIT
Url: https://github.com/simplegeo/python-oauth2
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
BuildArch: noarch

Source: oauth2-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%description
python-oauth2 implements OAuth, which is an open protocol to allow API
authentication in a simple and standard method from desktop and web 
applications. This was forked from python-oauth.

%prep
%setup -n oauth2-%version

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install
rm -rf %buildroot/%python3_sitelibdir/tests

%files
%doc LICENSE.txt README.md example/
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.9-alt2
- Drop python2 support.

* Thu Mar 22 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9-alt1
- Version 1.9

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.211-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.211-alt1
- Version 1.5.211
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.170-alt2
- Rebuild with Python-2.7

* Mon Jun 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.170-alt1
- 1.5.170

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.165-alt1
- Initial
