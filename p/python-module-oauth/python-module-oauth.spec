Name: python-module-oauth
Version: 1.0.1
Release: alt1.1
Summary: Library for OAuth version 1.0a

Group: Development/Python
License: MIT
Url: http://code.google.com/p/oauth/

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
%summary

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/oauth*
%doc LICENSE.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.1-alt1
- initial build

