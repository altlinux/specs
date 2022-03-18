%def_disable snapshot
%define ver_major 1.5
%def_enable x11
%def_enable glx
%def_enable egl
%def_disable docs
%def_enable check

Name: libepoxy
Version: %ver_major.10
Release: alt1

Summary: Direct Rendering Manager runtime library
Group: System/Libraries
License: MIT
Url: https://github.com/anholt/libepoxy

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://github.com/anholt/libepoxy.git
Source: %name-%version.tar
%endif

BuildRequires(pre): meson >= 0.54
BuildRequires: python3 libglvnd-devel libGL-devel
%{?_enable_x11:BuildRequires: libX11-devel xorg-util-macros}
%{?_enable_egl:BuildRequires: libEGL-devel}
%{?_enable_docs:BuildRequires: doxygen}

%description
A library for handling OpenGL function pointer management.

%package devel
Summary: Development files for libepoxy
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development files for libepoxy
Group: Development/Documentation
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name.

%prep
%setup

%build
%meson \
	%{?_disable_x11:-Dx11=false} \
	%{?_enable_glx:-Dglx=yes} \
	%{?_enable_egl:-Degl=yes} \
	%{?_enable_docs:-Ddocs=true}
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot/%_libdir
%meson_test

%files
%_libdir/%name.so.*
%doc README.md COPYING

%files devel
%_includedir/epoxy/
%_libdir/%name.so
%_pkgconfigdir/epoxy.pc

%if_enabled docs
%files devel-doc
%_datadir/doc/epoxy/
%endif


%changelog
* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.10-alt1
- 1.5.10

* Sat Aug 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.9-alt1
- 1.5.9

* Fri May 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.8-alt1
- 1.5.8

* Sat May 01 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- 1.5.7

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.6-alt1
- updated to 1.5.6-2-g1403303

* Tue Dec 22 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4 (ported to Meson build system)

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun May 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Jun 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Feb 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Sat Jul 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release

