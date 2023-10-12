Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

Summary: Gamerzilla Integration Library
Name: libgamerzilla
Version: 0.1.3
Release: alt1_%autorelease
License: zlib
URL: https://github.com/dulsi/libgamerzilla
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libjansson-devel
BuildRequires: libcurl-devel
BuildRequires: ctest cmake
Source44: import.info

%description
Gamerzilla is trophy/achievement system for games. It integrates with a
hubzilla plugin to display your results online. Games can either connect
directly to hubzilla or connect to a game launcher with using this
library.

%package devel
Group: Development/C
Summary: Libraries and includes for Gamerzilla development
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains libraries and header files for
developing applications that use gamerzilla.

%package server
Group: Games/Other
Summary: Simple Gamerzilla server to relay information to Hubzilla

%description server
The gamerzillaserver listens for trophies awarded by games. It logs into
the user's Hubzilla server and passes on the awards.

%prep
%setup -q

%build
%{fedora_v2_cmake}
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
sed -i 's,^Version: $,Version: %version,' %buildroot%_pkgconfigdir/gamerzilla.pc

%files
%doc README
%doc --no-dereference LICENSE
%{_libdir}/libgamerzilla.so.0
%{_libdir}/libgamerzilla.so.0.1.0

%files devel
%{_includedir}/gamerzilla/
%{_libdir}/libgamerzilla.so
%{_libdir}/pkgconfig/gamerzilla.pc
%{_datadir}/vala/vapi/gamerzilla.vapi
%{_datadir}/vala/vapi/gamerzilla.deps

%files server
%{_bindir}/gamerzillaserver

%changelog
* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 0.1.3-alt1_1
- new version

