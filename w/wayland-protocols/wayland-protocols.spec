%define ver_major 1.5

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

%check
%make check

%find_lang %name

%files -f %name.lang
%_datadir/%name/
%_datadir/pkgconfig/%name.pc
%doc README

%changelog
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

