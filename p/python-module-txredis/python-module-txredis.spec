%define version 0.1.2
%define release alt1
%define origname txredis
%setup_python_module txredis

Summary: Python/Twisted client for Redis key-value store
Name: %packagename
Version: %version
Release: %release.1
Source0: %origname-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://ooici.net/packages/txredis/
Packager: Sergey Alembekov <rt@altlinux.org>

BuildPreReq: %py_dependencies setuptools

%description
%summary

%prep
%setup -n %origname-%version

%build
%python_build

%install
mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.1
- Rebuild with Python-2.7

* Mon Nov 29 2010 Sergey Alembekov <rt@altlinux.ru> 0.1.2-alt1
- initial build for ALTLinux
