Name: python-module-twitter
Version: 0.8.2
Release: alt1
Summary: Python Interface for Twitter API

Group: Development/Python
License: Apache License 2.0
Url: http://code.google.com/p/python-twitter/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-dev

%description
This library provides a pure python interface for the Twitter API.

%prep
%setup -q

%build
%python_build

%install
chmod a-x README
%__python setup.py install --skip-build --root %buildroot

%files
%doc PKG-INFO README CHANGES COPYING LICENSE doc/twitter.html examples/
# For noarch packages: sitelib
%python_sitelibdir/*

%changelog
* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2
- Rebuild with Python-2.7

* Sun Mar 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Apr 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1
- Initial
