%def_enable snapshot
%define ver_major 1.15
%define rdn_name com.github.phase1geo.minder

%def_enable check

Name: minder
Version: %ver_major.6
Release: alt1

Summary: Mind-mapping application
License: GPL-3.0
Group: Office
Url: https://github.com/phase1geo/Minder

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/phase1geo/Minder.git
Source: %name-%version.tar
%endif

%define glib_ver 2.68
%define gtk_ver 3.22

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libmarkdown)
BuildRequires: pkgconfig(granite)
BuildRequires: vapi(granite)

%description
Quickly create visual mind-maps using the keyboard and automatic layout.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
#%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%_datadir/mime/packages/%rdn_name.xml
%doc AUTHORS* README*


%changelog
* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.6-alt1
- first build for Sisyphus (1.15.6-2-g3a35139)


