%def_enable jpeg
%def_enable gbm
%def_enable h264
%def_enable tls
%def_enable nettle
%def_enable check

Name: neatvnc
Version: 1.0.0
Release: alt1

Summary: A liberally licensed VNC server library with a clean interface
License: ISC
Group: System/Libraries
Url: https://github.com/any1/neatvnc

Vcs: https://github.com/any1/neatvnc.git

Source: https://github.com/any1/neatvnc/archive/v%version/%name-%version.tar.gz

%define aml_ver 1.0.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(aml1) >= %aml_ver
BuildRequires: libpixman-devel libpng-devel zlib-devel
%{?_enable_jpeg:BuildRequires: pkgconfig(libturbojpeg)}
%{?_enable_gbm:BuildRequires: libdrm-devel libgbm-devel}
%{?_enable_h264:BuildRequires: libavcodec-devel libavfilter-devel libavutil-devel}
%{?_enable_tls:BuildRequires: libgnutls-devel}
%{?_enable_nettle:BuildRequires: libnettle-devel libgmp-devel}
%{?_enable_check:BuildRequires: /usr/bin/openssl}

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
Requires: pkgconfig(aml1) >= %aml_ver

%description -n lib%name-devel
This package contains header files required to develop
Neat VNC based software.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_feature jpeg jpeg} \
    %{subst_enable_meson_feature gbm gbm} \
    %{subst_enable_meson_feature h264 h264} \
    %{subst_enable_meson_feature nettle nettle} \
    %{subst_enable_meson_feature tls tls} \
    %{subst_enable_meson_bool check tests}
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
* Fri May 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Apr 26 2026 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Wed Jul 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Wed Jun 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1.1
- enabled nettle support (ALT #54823)

* Tue Mar 04 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4

* Tue Feb 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Thu Dec 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Wed Sep 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sat Feb 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Nov 09 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Thu May 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus

