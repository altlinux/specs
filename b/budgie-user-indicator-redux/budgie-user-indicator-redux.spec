%define _unpackaged_files_terminate_build 1

Name: budgie-user-indicator-redux
Version: 1.0.2
Release: alt1

Summary: Manage your user session from the Budgie panel
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/EbonJaeger/budgie-user-indicator-redux

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(budgie-1.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(vapigen)
BuildRequires: sassc

%description
This project is born from the changes to the User Indicator applet
shipped with Budgie. Since it simply opens the Budgie Power Dialog, 
it was figured out that people might still want the old menu.

This applet gives them that option. The design is largely inspired from
Elementary's Wingpanel session indicator, with some bits of the old
Budgie user indicator mixed in, with options to show/hide items in
the menu.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %{name}.lang
%doc CHANGELOG.md LICENSE README.md
%dir %_libdir/budgie-desktop/plugins/com.github.EbonJaeger.user-indicator-redux
%_libdir/budgie-desktop/plugins/com.github.EbonJaeger.user-indicator-redux/*
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/metainfo/*.appdata.xml

%changelog
* Tue Mar 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
