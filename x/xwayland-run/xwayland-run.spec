%define _unpackaged_files_terminate_build 1

Name: xwayland-run
Version: 0.0.4
Release: alt1

Summary: Set of utilities to run X/Wayland headless
License: GPL-2.0
Group: System/X11
Url: https://gitlab.freedesktop.org/ofourdan/xwayland-run

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires: meson

Requires: xorg-xwayland
Requires: xauth
Requires: /usr/bin/dbus-run-session

%description
xwayland-run contains a set of small utilities revolving around running
Xwayland and various Wayland compositor headless.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/wlheadless-run
%_bindir/xwayland-run
%_bindir/xwfb-run
%_man1dir/wlheadless-run.*
%_man1dir/xwayland-run.*
%_man1dir/xwfb-run.*
%dir %_datadir/wlheadless/
%_datadir/wlheadless/*
%python3_sitelibdir/wlheadless

%changelog
* Sat May 24 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus
