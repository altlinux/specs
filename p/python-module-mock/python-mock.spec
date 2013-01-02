Name: python-module-mock
Version: 0.8.0
Release: alt1
Summary: A Python mock object library

Group: Development/Python
License: Apache License 2.0
Url: http://code.google.com/p/mock/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-dev

%description
mock is a Python module that provides a core Mock class. It is intended to
reduce the need for creating a host of trivial stubs throughout your test suite.
After performing an action, you can make assertions about which methods /
attributes were used and arguments they were called with. You can also specify
return values and set needed attributes in the normal way.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc README.txt html/
# For noarch packages: sitelib
%python_sitelibdir/*

%changelog
* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt2
- Rebuild with Python-2.7

* Mon Oct 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt1
- Initial
