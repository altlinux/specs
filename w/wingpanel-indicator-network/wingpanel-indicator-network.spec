%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.network

Name: wingpanel-indicator-network
Version: 8.0.1
Release: alt1.git.6b1ba43

Summary: Wingpanel Network Indicator
License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/wingpanel-indicator-network

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libnma)
BuildRequires: pkgconfig(libnma-gtk4)
BuildRequires: vapi(granite)

%description
%summary

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
%_libdir/wingpanel-9/libnetwork.so
%_datadir/metainfo/io.elementary.panel.network.metainfo.xml
%_datadir/polkit-1/actions/io.elementary.panel.network.policy

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1.git.6b1ba43
- Initial build for Sisyphus
