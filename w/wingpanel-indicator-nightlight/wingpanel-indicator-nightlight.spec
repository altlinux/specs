%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.nightlight

Name: wingpanel-indicator-nightlight
Version: 2.1.3
Release: alt1.git.14cdc69

Summary: A Wingpanel indicator for Night Light
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/panel-nightlight

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(granite)
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
%_libdir/wingpanel-9/libnightlight.so
%_datadir/metainfo/io.elementary.panel.nightlight.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 2.1.3-alt1.git.14cdc69
- Initial build for Sisyphus
