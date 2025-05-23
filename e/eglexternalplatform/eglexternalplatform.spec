# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

Name: eglexternalplatform
Version: 1.2.1
Release: alt1
Summary: EGL External Platform Interface headers
Group: System/Libraries

License: MIT
Url: https://github.com/NVIDIA
Source0: %name-%version.tar

BuildRequires: meson libglvnd-devel

%description
%summary

%package devel
Group: System/Libraries
Summary: Development files for %name

%description devel
The %name-devel package contains the header files for
developing applications that use %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
#mkdir -p %buildroot%_includedir/
#install -p -m 0644 interface/eglexternalplatform.h %buildroot%_includedir/
#install -p -m 0644 interface/eglexternalplatformversion.h %buildroot%_includedir/
#mkdir -p %buildroot%_datadir/pkgconfig/
#install -p -m 0644 eglexternalplatform.pc %buildroot%_datadir/pkgconfig/

%files devel
%doc README.md samples
%doc --no-dereference COPYING
%_includedir/*
%_datadir/pkgconfig/eglexternalplatform.pc

%changelog
* Fri May 23 2025 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Tue Oct 08 2024 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- update by mgaimport

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- new version

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0
- new version
