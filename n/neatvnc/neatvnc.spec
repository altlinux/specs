%def_enable jpeg
%def_enable gbm
%def_enable h264
%def_enable check

Name: neatvnc
Version: 0.7.1
Release: alt1

Summary: A liberally licensed VNC server library with a clean interface
License: ISC
Group: System/Libraries
Url: https://github.com/any1/neatvnc

Vcs: https://github.com/any1/neatvnc.git
Source: https://github.com/any1/neatvnc/archive/v%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libaml-devel
BuildRequires: libgnutls-devel
BuildRequires: libpixman-devel libpng-devel zlib-devel
%{?_enable_jpeg:BuildRequires: pkgconfig(libturbojpeg)}
%{?_enable_gbm:BuildRequires: libdrm-devel libgbm-devel}
%{?_enable_h264:BuildRequires: libavcodec-devel libavfilter-devel libavutil-devel}

%description
%summary

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
This package contains shared Neat VNC library.

%package -n lib%name-devel
Summary: Neat VNC development file
Group: Development/C
Requires: lib%name = %EVR
Requires: libaml-devel

%description -n lib%name-devel
This package contains header files required to develop
Neat VNC based software.

%prep
%setup

%build
%meson \
%{?_disable_jpeg:-Djpeg=disabled} \
%{?_disable_gbm:-Dgbm=disabled} \
%{?_disable_h264:-Dh264=disabled} \
%{?_enable_check:-Dtests=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Nov 09 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus

