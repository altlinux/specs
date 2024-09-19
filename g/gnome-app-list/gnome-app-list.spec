%def_disable snapshot

%define ver_major 1.0
%define rdn_name org.gnome.App-list

%def_enable check

Name: gnome-app-list
Version: %ver_major
Release: alt1

Summary: GNOME App List
Group: Graphical desktop/GNOME
License: LGPL-2.1
Url: https://gitlab.gnome.org/GNOME/gnome-app-list

Vcs: https://gitlab.gnome.org/GNOME/gnome-app-list.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
%{?_enable_check:BuildRequires: xmllint}

%description
This project provides app recommendation data for the GNOME project.
This AppStream data is available across the system, and is mainly used
by the Software (https://gitlab.gnome.org/GNOME/gnome-software) app.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_datadir/swcatalog/xml/%rdn_name.xml
%doc README* NEWS

%changelog
* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Tue Aug 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Mon Aug 05 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus.
