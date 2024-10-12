%define ver_major 1.38

%if "%__gcc_version_major" < "11"
%ifarch ppc64le
%def_disable check
%endif
%endif

Name: wayland-protocols
Version: %ver_major
Release: alt1

Summary: Wayland protocols
License: MIT
Group: System/X11
Url: https://wayland.freedesktop.org/

Vcs: https://gitlab.freedesktop.org/wayland/wayland-protocols.git
Source: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/%version/downloads/%name-%version.tar.xz
#Source: https://wayland.freedesktop.org/releases/%name-%version.tar.xz

BuildArch: noarch

%define wayland_ver 1.20

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ libwayland-client-devel >= %wayland_ver libwayland-server-devel

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in wayland-protocols.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_datadir/%name/
%_includedir/%name/
%_datadir/pkgconfig/%name.pc
%doc README.md GOVERNANCE* MEMBERS*

%changelog
* Sat Oct 12 2024 Yuri N. Sedunov <aris@altlinux.org> 1.38-alt1
- 1.38

* Sat Aug 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.37-alt1
- 1.37

* Fri Apr 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.36-alt1
- 1.36

* Wed Apr 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.35-alt1
- 1.35

* Thu Mar 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.34-alt1
- 1.34

* Sat Jan 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.33-alt1
- 1.33

* Mon Jul 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.32-alt1
- 1.32

* Tue Nov 29 2022 Yuri N. Sedunov <aris@altlinux.org> 1.31-alt1
- 1.31

* Mon Nov 21 2022 Yuri N. Sedunov <aris@altlinux.org> 1.30-alt1
- 1.30

* Mon Nov 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.29-alt1
- 1.29

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.28-alt1
- 1.28

* Mon Oct 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.27-alt1
- 1.27

* Fri Jul 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.26-alt1
- 1.26

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 1.25-alt1
- 1.25

* Wed Dec 29 2021 Yuri N. Sedunov <aris@altlinux.org> 1.24-alt1.1
- disabled broken %%check for ppc64le with gcc < 11

* Tue Nov 23 2021 Yuri N. Sedunov <aris@altlinux.org> 1.24-alt1
- 1.24

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.23-alt1
- 1.23

* Wed Sep 01 2021 Yuri N. Sedunov <aris@altlinux.org> 1.22-alt1
- 1.22 (ported to Meson build system)

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.21-alt1
- 1.21

* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.20-alt1
- 1.20

* Fri Jul 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.18-alt1
- 1.18

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.17-alt1
- 1.17

* Tue Jul 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.16-alt1
- 1.16

* Fri Jul 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.15-alt1
- 1.15

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14-alt1
- 1.14

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13-alt1
- 1.13

* Wed Dec 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt1
- 1.12

* Tue Oct 17 2017 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1
- 1.11

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Fri Aug 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- 1.7

* Sat Jul 23 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Fri Mar 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Feb 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Thu Nov 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus

