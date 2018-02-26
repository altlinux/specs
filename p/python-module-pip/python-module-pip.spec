%define version 1.0
%define release alt1
%setup_python_module pip

Summary: pip installs packages.  Python packages.  An easy_install replacement
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename.tar
License: MIT
Group: Development/Python
BuildArch: noarch
URL: http://www.pip-installer.org
Packager: Sergey Alembekov <rt@altlinux.ru>

BuildRequires: python-module-setuptools

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- new version
- spec fixes

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt1
- initial build for ALTLinux
