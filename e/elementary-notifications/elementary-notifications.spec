%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.notifications

Name: elementary-notifications
Version: 8.1.0
Release: alt1

Summary: Gtk Notifications Server
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/notifications

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: vapi(granite)
BuildRequires: vapi(libcanberra)

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

%files -f %appname.lang
%doc LICENSE README.md
%_bindir/%appname
%_bindir/%{appname}.demo
%_desktopdir/%{appname}.demo.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- Initial build for Sisyphus
