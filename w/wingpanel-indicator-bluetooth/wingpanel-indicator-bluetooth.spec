%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.bluetooth

Name: wingpanel-indicator-bluetooth
Version: 8.0.0
Release: alt1.git.cccfecd

Summary: Wingpanel Bluetooth Indicator
License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/panel-bluetooth

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libnotify)
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
%_libdir/wingpanel-9/libbluetooth.so
%_datadir/metainfo/io.elementary.wingpanel.bluetooth.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.0.0-alt1.git.cccfecd
- Initial build for Sisyphus
