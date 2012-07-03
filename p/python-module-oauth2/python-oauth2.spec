Name: python-module-oauth2
Version: 1.5.170
Release: alt2
Summary: Library for OAuth version 1.0a (forked from python-oauth)

Group: Development/Python
License: MIT
Url: https://github.com/simplegeo/python-oauth2
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-dev python-module-setuptools

%description
python-oauth2 implements OAuth, which is an open protocol to allow API
authentication in a simple and standard method from desktop and web 
applications. This was forked from python-oauth.

%prep
%setup -q

%build
%python_build

%install
%__python setup.py install --skip-build --root %buildroot
rm -rf %buildroot/%python_sitelibdir/tests

%files
%doc LICENSE.txt README.md example/
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.170-alt2
- Rebuild with Python-2.7

* Mon Jun 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.170-alt1
- 1.5.170

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.165-alt1
- Initial
