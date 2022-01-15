Name: waybar
Version: 0.9.9
Release: alt1
License: MIT
Summary: Highly customizable Wayland bar for Sway and Wlroots based compositors
URL: https://github.com/Alexays/Waybar.git
Group: Graphical desktop/Other

Source: %name-%version.tar
Source1: xkb-layout.py
Source2: clock.py

Patch0: waybar-config.patch

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake meson
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel-static
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(spdlog)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)

# language module
BuildRequires: pkgconfig(xkbregistry)

# sni module
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: pkgconfig(gio-unix-2.0)

# pulseaudio module
BuildRequires: pkgconfig(libpulse)

# backlight
BuildRequires: pkgconfig(libudev)

# network module
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libnl-genl-3.0)

# mpd module
# BuildRequires: libmpdclient-devel

%define _libexecdir %_prefix/libexec
%define helperdir %_libexecdir/%name

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson \
	-Drfkill=enabled \
	-Dgtk-layer-shell=disabled \
	-Dsystemd=disabled
%meson_build

%install
%meson_install

mkdir -p -- %buildroot/%helperdir
install -m 755 -- %SOURCE1 %buildroot/%helperdir/
install -m 755 -- %SOURCE2 %buildroot/%helperdir/

%check
%meson_test

%files
%_bindir/%name
%dir %_xdgconfigdir/%name
%config(noreplace) %_xdgconfigdir/%name/config
%config(noreplace) %_xdgconfigdir/%name/style.css
%helperdir
%_man5dir/*

%changelog
* Sat Jan 15 2022 Alexey Gladkov <legion@altlinux.ru> 0.9.9-alt1
- New version (0.9.9).

* Tue Oct 05 2021 Alexey Gladkov <legion@altlinux.ru> 0.9.8-alt1
- New version (0.9.8).

* Sat May 08 2021 Alexey Gladkov <legion@altlinux.ru> 0.9.7-alt2
- Add rpm-build-python3 BR.

* Tue Apr 27 2021 Alexey Gladkov <legion@altlinux.ru> 0.9.7-alt1
- New version (0.9.7)
- Update buildrequires.

* Fri Jan 08 2021 Alexey Gladkov <legion@altlinux.ru> 0.9.5-alt1
- New version (0.9.5)
- Replace clock module by custom version.

* Sat Dec 28 2019 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt1
- New version (0.9.0)
- Add xkb-layout module

* Thu Aug 08 2019 Alexey Gladkov <legion@altlinux.ru> 0.7.2-alt1
- New version (0.7.2)

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sat May 18 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Apr 02 2019 Alexey Gladkov <legion@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Thu Jan 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt1
- Initial build.
