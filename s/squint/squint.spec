%define _unpackaged_files_terminate_build 1

Name: squint
Version: 0.9.0
Release: alt1

Summary: Duplicate an X11 monitor into a window
License: GPL-3.0
Group: System/X11
Url: https://github.com/a-ba/squint

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)
BuildRequires: /usr/bin/txt2tags

%description
%summary

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
desktop-file-install --dir=%buildroot%_datadir/applications squint.desktop

%files
%doc LICENSE NEWS README TODO
%_bindir/*
%_desktopdir/%{name}.desktop
%_man1dir/*
%dir %_datadir/squint
%_datadir/squint/*

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus
