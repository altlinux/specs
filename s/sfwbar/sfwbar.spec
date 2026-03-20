%define _unpackaged_files_terminate_build 1

Name: sfwbar
Version: 1.0_beta17
Release: alt1

Summary: S* Floating Window Bar
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/LBCrion/sfwbar

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: meson
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libmpdclient)
BuildRequires: pkgconfig(xkbregistry)
BuildRequires: /usr/bin/rst2man

# TODO - find the exact root of the problem like
#        "lib.req: ERROR: /usr/src/tmp/sfwbar-buildroot/usr/lib64/sfwbar/alsactl.so: library libsfwbar.so not found"
#        and then remove the below hacky line
AutoReq: nolib

Requires: libgtk-layer-shell

%description
SFWBar (S* Floating Window Bar) is a flexible taskbar application for
wayland compositors, designed with a stacking layout in mind.
Originally developed for Sway, SFWBar will work with any wayland
compositor supporting layer shell protocol, the taskbar and window
switcher functionality shall work with any compositor supportinig
foreign toplevel protocol, but the pager, and window placement
functionality require sway (or at least i3 IPC support).

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %{name}.lang
%doc LICENSE README.md doc/ChangeLog
%_bindir/*
%_man1dir/*
%_datadir/icons/hicolor/scalable/apps/%{name}.svg
%dir %_datadir/%name/
%_datadir/%name/*
%dir %_libdir/%name/
%_libdir/%name/*.so

%changelog
* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 1.0_beta17-alt1
- New version 1.0_beta17.

* Thu May 08 2025 Nikolay Strelkov <snk@altlinux.org> 1.0_beta16-alt1
- Initial build for Sisyphus
