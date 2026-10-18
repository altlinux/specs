%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.system

%def_with check

Name: switchboard-plug-about
Version: 8.2.3
Release: alt1

Summary: Switchboard System Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-system

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(fwupd)
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(packagekit-glib2)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(udisks2)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: vapi(appstream)

%description
System plugin for elementary System Settings.
This plugin displays information about the system.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_libdir/switchboard-3/hardware/libsystem.so
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 8.2.3-alt1
- Initial build for Sisyphus
