%define _unpackaged_files_terminate_build 1

Name: budgie-user-indicator-redux
Version: 1.1.0
Release: alt2

Summary: Manage your user session from the Budgie panel
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/EbonJaeger/budgie-user-indicator-redux

ExcludeArch: %ix86

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(budgie-3.0)
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
# Update to budgie-3.0 API
sed -i "s/budgie-2\.0/budgie-3.0/" meson.build

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
* Mon Jan 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- rebuild with budgie-3.0 API for Budgie 10.10
- add ExcludeArch: ix86

* Fri Dec 19 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Tue Mar 18 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
