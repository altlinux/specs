%define ver_major 1.12

Name: wayland-protocols
Version: %ver_major
Release: alt1

Summary: Wayland protocols
License: MIT
Group: System/X11
Url: http://wayland.freedesktop.org/

Source: http://wayland.freedesktop.org/releases/%name-%version.tar.xz

BuildArch: noarch
# wayland-scanner required
BuildRequires: wayland-devel

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in wayland-protocols.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%check
%make check


%files -f %name.lang
%_datadir/%name/
%_datadir/pkgconfig/%name.pc
%doc README

%changelog
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

