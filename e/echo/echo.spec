%def_disable snapshot

%define _name Echo
%define ver_major 1.2
%define rdn_name io.github.lo2dev.%_name

%def_disable check

Name: echo
Version: %ver_major
Release: alt1

Summary: Utility to ping websites
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/lo2dev/Echo

Vcs: https://github.com/lo2dev/Echo.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%add_python3_path %_datadir/%name

%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: dconf
#Requires: %_sysctldir/70-iputils.conf
Requires: iputils

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Echo is a simple utility to ping websites using GTK4 and Libadwaita.

NOTE: The user must be a member of the "iputils" group to use Echo.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
mv %buildroot%_bindir/%name %buildroot%_bindir/%rdn_name
sed -i 's|\(Exec=\)%name|\1%rdn_name|' %buildroot%_desktopdir/%rdn_name.desktop

%find_lang %name

%check
%__meson_test

%files -f %name.lang
%attr(755,root,iputils) %_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Tue Jul 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- first build for Sisyphus


