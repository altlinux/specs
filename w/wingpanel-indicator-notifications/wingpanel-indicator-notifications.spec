%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.panel.notifications

Name: wingpanel-indicator-notifications
Version: 7.1.1
Release: alt1.git.10cd1d5

Summary: Wingpanel Notifications Indicator
License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/wingpanel-indicator-notifications

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: libwingpanel-devel
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libadwaita-1)
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
%_libdir/wingpanel-9/libnotifications.so
%_datadir/glib-2.0/schemas/io.elementary.panel.notifications.gschema.xml
%_datadir/metainfo/io.elementary.panel.notifications.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 7.1.1-alt1.git.10cd1d5
- Initial build for Sisyphus
