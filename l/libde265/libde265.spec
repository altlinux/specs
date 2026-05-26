Name: libde265
Version: 1.1.0
Release: alt1
Summary: Open H.265 video codec implementation
License: LGPLv3
Group: System/Libraries
Url: https://github.com/strukturag/libde265
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake gcc-c++

%description
libde265 is an open source implementation of the H.265 video codec.
It is written from scratch in plain C for simplicity and efficiency.
Its simple API makes it easy to integrate it into other software.

%package devel
Group: Development/C++
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup -q
%patch -p1

%build
%cmake \
	-DENABLE_SHERLOCK265=off \
	-DENABLE_DECODER=off

%cmake_build

%install
%cmake_install

%files
%_libdir/%name.so.*

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name

%changelog
* Tue May 26 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed May 20 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Wed Jun 18 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Mon Dec 25 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15

* Mon Nov 27 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.0.14-alt1
- 1.0.14

* Thu Sep 14 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.0.12-alt1
- 1.0.12 (closes: #47544)

* Thu Feb 09 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Fri Nov 18 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Thu Sep 24 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Mon Aug 31 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Fri Feb 28 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Dec 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- initial release

