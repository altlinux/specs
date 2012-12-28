%define modulename progressbar

Name: python-module-progressbar
Version: 2.3
Release: alt1

Summary: Text progressbar library for python

Group: Development/Python
License: LGPLv2+
Url: http://code.google.com/p/python-progressbar

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %modulename-%version.tar

%setup_python_module %modulename

BuildRequires: python-module-distribute

%description
This library provides a text mode progress bar. This is typically used to
display the progress of a long running operation, providing a visual clue that
processing is under way.

The progressbar module is very easy to use, yet very powerful. And
automatically supports features like auto-resizing when available.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README.txt LICENSE.txt
%python_sitelibdir/%{modulename}*

%changelog
* Fri Dec 28 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3-alt1
- New version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1.1
- Rebuild with Python-2.7

* Thu Mar 11 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Linux Sisyphus
