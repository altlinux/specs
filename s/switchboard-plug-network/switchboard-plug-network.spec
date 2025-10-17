%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.network

Name: switchboard-plug-network
Version: 8.2.0
Release: alt1

Summary: Switchboard Network Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-network

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libnma-gtk4)

%description
Manage network connections.
Switchboard plug for managing networking.

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
%_libdir/switchboard-3/network/libnetwork.so
%_datadir/metainfo/io.elementary.settings.network.metainfo.xml

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.2.0-alt1
- Initial build for Sisyphus
