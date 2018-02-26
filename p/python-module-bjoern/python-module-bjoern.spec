%define version 1.2
%define release alt1
%setup_python_module bjoern

Summary: A screamingly fast Python WSGI server written in C.
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename.tar
License: BSD
Group: Development/Python
URL: https://github.com/jonashaag/bjoern
Packager: Sergey Alembekov <rt@altlinux.ru>

BuildRequires: python-module-setuptools libev-devel

%description
%summary

%prep
%setup -q -n %modulename

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Thu Jun 09 2011 Sergey Alembekov <rt@altlinux.ru> 1.2-alt1
- initial build for ALTLinux.
