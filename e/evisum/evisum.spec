%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define _name enigmatic
%define libname lib%_name

Name: evisum
Version: 2.0.12
Release: alt1

Summary: Evisum - An Enlightened System Monitor
Group: Graphical desktop/Enlightenment
License: ISC
Url: https://enlightenment.org

Vcs: https://git.enlightenment.org/enlightenment/evisum.git

%if_disabled snapshot
Source: https://download.enlightenment.org/rel/apps/%name/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define efl_ver 1.27.0
Requires: %_name = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libelementary-devel >= %efl_ver

%description
System and process monitor for Enlightenment.

%package -n %_name
Summary: Enigmatic client
Group: System/Libraries
Requires: %libname = %EVR

%description -n %_name
This package contains Enigmatic client required Evisum to work.

%package -n %libname
Summary: Enigmatic shared library
Group: System/Libraries

%description -n %libname
This package contains shared library required Evisum to work.

%package -n %libname-devel
Summary: Development files for Enigmatic library
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
This package contains development files for Enigmatic shared library.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*.png
%doc AUTHORS NEWS README*

%files -n enigmatic
%_bindir/%_name
%_bindir/%{_name}_client
%_bindir/%{_name}_start

%files -n %libname
%_libdir/%{libname}_client.so.*

%files -n %libname-devel
%_includedir/%_name/
%_libdir/%{libname}_client.so
%_pkgconfigdir/%{_name}_client.pc


%changelog
* Mon Jul 06 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.12-alt1
- 2.0.12

* Fri Jun 05 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.11-alt1
- 2.0.11

* Fri May 22 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.10-alt1
- 2.0.10

* Sat May 16 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.9-alt1
- 2.0.9

* Sat May 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.8-alt1
- 2.0.8

* Fri May 01 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Apr 28 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Mon Apr 20 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Apr 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Apr 01 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Mar 26 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Mar 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Fri Mar 21 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Fri Aug 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Dec 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sun Apr 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.13-alt1
- 0.5.13

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.12-alt1
- 0.5.12

* Thu Feb 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt1
- 0.5.11

* Mon Feb 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.10-alt1
- 0.5.10

* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- 0.5.9

* Mon Nov 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Thu Sep 17 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Mon Aug 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Fri Aug 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Wed Jul 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Jul 07 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (v0.5.0-2-gd71b1a2)


