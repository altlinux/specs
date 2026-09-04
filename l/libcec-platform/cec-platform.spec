Name: libcec-platform
Version: 2.2.0
Release: alt1

Summary: Platform support library used by libCEC and binary add-ons for Kodi
License: GPLv2+
Group: Development/C++
URL: https://libcec.pulse-eight.com/
VCS: https://github.com/pulse-eight/platform

Source: %name-%version.tar
BuildRequires: cmake gcc-c++
%description
%summary

%package devel
Summary: %summary
Group: Development/C++

%description devel
%summary

%prep
%setup

%define optflags_lto %nil
%build
%cmake_insource -DCMAKE_INSTALL_PREFIX=%prefix
make

%install
%makeinstall_std

%files devel
%_includedir/p8-platform
%_libdir/p8-platform
%_libdir/libp8-platform.a
%_pkgconfigdir/p8-platform.pc

%changelog
* Fri Sep 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.0-alt1
- 2.2.0 released

* Wed Apr 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.0.1-alt3
- fixed FTBFS with cmake4

* Thu Jan 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0.1-alt2
- rebuilt for Leia

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0.1-alt1.1
- NMU: added URL

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0.1-alt1
- 2.1.0.1

* Thu Jul 23 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.10-alt1
- 1.0.10
