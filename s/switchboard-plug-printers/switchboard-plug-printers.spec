%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.printers

Name: switchboard-plug-printers
Version: 8.0.1
Release: alt1

Summary: Switchboard Printers Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-printers

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(cups)

%description
Printers plug for Switchboard.
This plug configures all available printers.

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
%_libdir/switchboard-3/hardware/libio.elementary.settings.printers.so
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
