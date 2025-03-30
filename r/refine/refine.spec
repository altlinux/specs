%define _unpackaged_files_terminate_build 1

Name: refine
Version: 0.5.5
Release: alt1

Summary: Tweak various aspects of GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
URL: https://gitlab.gnome.org/TheEvilSkeleton/Refine

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: /usr/bin/appstreamcli
BuildRequires: pkgconfig(blueprint-compiler)

Requires: typelib(XdpGtk4)

Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%meson \
       -Dexec_name_as_base_id=true
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %name.lang
%doc COPYING README.md
%_bindir/*
%_desktopdir/*
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml

%changelog
* Sun Mar 31 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.5-alt1
- Initial build for Sisyphus
