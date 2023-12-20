%define modulename unrardll
Name: python3-module-unrardll
Version: 0.1.7
Release: alt1

Summary: Python wrapper for the UnRAR DLL

Url: https://github.com/kovidgoyal/unrardll
License: BSD 3-Clause New or Revised License
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kovidgoyal/unrardll/archive/v%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libunrar libunrar-devel
BuildRequires: rpm-build-intro gcc-c++

%description
Python wrapper for the UNRAR DLL.

%prep
%setup -n %modulename-%version
sed -i "s|unrar/dll.hpp|libunrar/dll.hpp|" src/unrardll/wrapper.cpp

%build
%python3_build

%install
%python3_install

%check
# will failed with LANG=C
export LANG=en_US.UTF8
%python3_check test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 0.1.7-alt1
- Build new version.

* Wed May 25 2022 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.3-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Sisyphus

