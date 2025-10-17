%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.power

%define _libexecdir %_prefix/libexec

Name: switchboard-plug-power
Version: 8.0.1
Release: alt1

Summary: Switchboard Power Plug
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-power

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(switchboard-3)

%description
Power plug for Switchboard.
This plug configures system power consumption.

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
%_libdir/switchboard-3/hardware/libpower.so
%_libexecdir/io.elementary.logind.helper
%_datadir/dbus-1/system-services/io.elementary.logind.helper.service
%_datadir/dbus-1/system.d/io.elementary.logind.helper.conf
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/polkit-1/actions/%{appname}.policy

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
