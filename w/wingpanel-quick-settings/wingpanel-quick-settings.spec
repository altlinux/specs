%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.quick-settings

Name: wingpanel-quick-settings
Version: 1.4.0
Release: alt1.git.ddb7019

Summary: Access frequently used settings and system actions
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/quick-settings

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gdk-wayland-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(packagekit-glib2)
BuildRequires: pkgconfig(wingpanel-9)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: vapi(granite)

%description
WingPanel Quick Settings Indicator

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
%doc LICENSE README.md
%_libdir/wingpanel-9/libquick-settings.so
%_datadir/glib-2.0/schemas/quick-settings.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Tue Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.0-alt1.git.ddb7019
- Initial build for Sisyphus
