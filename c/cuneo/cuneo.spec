%define _unpackaged_files_terminate_build 1
%define xdg_name io.github.heidefinnischen.cuneo

Name:    cuneo
Version: 1.0.0
Release: alt1

Summary: A different kind of calculator
License: GPL-3.0-or-later
Group:   Sciences/Mathematics
Url:     https://github.com/heidefinnischen/cuneo
VCS:     https://github.com/heidefinnischen/cuneo

Source0: %name-%version.tar
Patch0:  %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-python3
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)

%description
Cuneo is a simple and straightforward app that lets you calculate and convert
anything you might encounter in your daily life. Being designed like a widget,
Cuneo gets out of the way and is best used floating over a maximized window
so you can focus on your actual tasks and not managing a calculation app
covering half your screen.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/cuneo
%_datadir/cuneo/
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Wed Jun 11 2025 Alexey Volkov <qualimock@altlinux.org> 1.0.0-alt1
- Initial build for ALT
