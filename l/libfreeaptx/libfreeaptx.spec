%def_disable snapshot

%define _name freeaptx
Name: lib%_name
Version: 0.1.1
Release: alt1

Summary: Open Source implementation of aptX codec
Group: System/Libraries
License: LGPL-2.1
Url: https://github.com/iamthehorker/libfreeaptx

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/iamthehorker/libfreeaptx.git
Source: %name-%version.tar
%endif

%description
This is Open Source implementation of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

libfreeaptx is based on version 0.2.0 of libopenaptx with the intent of continuing
under a free license without the additional license restriction added to 0.2.1. The
initial version of libfreeaptx was reset to 0.1.0 to prevent confusion between the
two projects.

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

%changelog
* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus


