Name: libutfcpp
Version: 3.2.2
Release: alt1

Summary: A library for handling UTF-8 encoded strings

License: BSL-1.0
Group: Development/C++
Url: https://github.com/nemtrif/utfcpp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/nemtrif/utfcpp/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/nemtrif/ftest/archive/refs/heads/master.zip
Source1: %name-ftest-%version.tar

BuildRequires(pre): cmake gcc-c++

%description
A C++ header only library for handling UTF-8 encoded strings.

See https://github.com/ledger/utfcpp also.

%prep
%setup -a1

%build
%cmake
%cmake_build

%install
cd source
install -d %buildroot/%_includedir/utf8/
install -m0644 utf8.h %buildroot/%_includedir
install -m0644 utf8/*.h %buildroot/%_includedir/utf8

%check
cd %_host_alias/tests
./apitests
./cpp11
./cpp17
./noexceptionstests

%package devel
Summary: A library for handling UTF-8 encoded strings
Group: Development/C++

%description devel
A library for handling UTF-8 encoded strings.

%files devel
%doc README.md
%_includedir/utf8/
%_includedir/utf8.h

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.2.2-alt1
- new version 3.2.2 (with rpmrb script)

* Fri Jul 16 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- real build 3.2.1 from new upstream (all 3.x updates here really were 2.3.4)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt1
- new version 3.1.2 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- initial build for ALT Linux Sisyphus

* Thu Jan 15 2015 jmatejka@suse.cz
- Initial package version 2.3.4
