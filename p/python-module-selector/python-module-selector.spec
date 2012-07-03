%define version 0.8.11
%define release alt1
%setup_python_module selector

Summary: WSGI delegation based on URL path and method.
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename.tar
License: LGPL
Group: Development/Python
BuildArch: noarch
URL: http://lukearno.com/projects/selector/
Packager: Sergey Alembekov <rt@altlinux.ru>

BuildRequires: python-module-setuptools python-module-resolver

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
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.11-alt1.1
- Rebuild with Python-2.7

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.8.11-alt1
- initial build for ALTLinux
