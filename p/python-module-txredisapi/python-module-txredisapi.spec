%define version 20101029
%define release alt1
%define origname txredisapi
%setup_python_module txredisapi

Summary: Twisted client protocol for redis
Name: %packagename
Version: %version
Release: %release.1
Source0: %origname-%version.tar
License: Apache
Group: Development/Python
BuildArch: noarch
URL: https://github.com/fiorix/txredisapi.git
Packager: Sergey Alembekov <rt@altlinux.org>

BuildPreReq: %py_dependencies setuptools

%description
%summary

%prep
%setup -n %origname-%version

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20101029-alt1.1
- Rebuild with Python-2.7

* Tue Feb 01 2011 Sergey Alembekov <rt@altlinux.ru> 20101029-alt1
- initial build

