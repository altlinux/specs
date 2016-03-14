BuildRequires(pre): rpm-build-python3
%define oldname python-module-alterator
Name: python3-module-alterator
Version: 0.1
Release: alt1.1

Summary: Python module for writing backends for ALTLInux Alterator framework

Group: Development/Python
License: GPL
URL: http://www.aspirinka.net/alterator
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: python-alterator-%version.tar.bz2

BuildArch: noarch
BuildRequires: python3-devel

%define modulename alterator
%description
This module can be used to write backends for ALTLinux Alterator system.


%prep
%setup -n python-%modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/%modulename/

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt0.1.1
- python3 copycat update

