%def_enable snapshot

%define _name openaptx
Name: lib%_name
Version: 0.2.0
Release: alt1
Epoch: 1

Summary: Open Source implementation of aptX codec
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/pali/libopenaptx

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/pali/libopenaptx.git
Source: %name-%version.tar
%endif
Patch: libopenaptx-0.2.0-alt-rpath.patch

%description
This is Open Source implementation of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

%package tools
Summary: aptX tools
Group: Sound
Requires: %name = %EVR

%description tools
This package provides command line utilities openaptxenc and openaptxdec
for encoding and decoding operations.

%package devel
Summary: aptX header files
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides files needed to develop programms which use %name.

%prep
%setup
%patch
# don't strip binaries
sed -i '/^LDFLAGS = -s/d' Makefile

%build
%define _optlevel 3
%make CC=%__cc CFLAGS="%optflags_default" default

%install
%makeinstall_std PREFIX=%_prefix LIBDIR=%_lib

%files
%_libdir/%name.so.*
%doc README

%files tools
%_bindir/%{_name}dec
%_bindir/%{_name}enc

%files devel
%_includedir/%_name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%exclude %_libdir/%name.a

%changelog
* Wed Feb 10 2021 Yuri N. Sedunov <aris@altlinux.org> 1:0.2.0-alt1
- updated to 0.2.0-3-g5eb14ed from original libopenaptx repo

* Thu Dec 10 2020 L.A. Kostis <lakostis@altlinux.ru> 1.2.0-alt1
- 1.2.0.
- use ffmpeg for encoding.

* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.gebcf004
- Initial build for ALTLinux.

