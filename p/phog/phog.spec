%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define rdn_name org.mobian.phog

%def_enable check

Name: phog
Version: 0.1.5
Release: alt0.2

Summary: Phone Greeter
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.com/mobian1/phog

Vcs: https://gitlab.com/mobian1/phog.git

%if_disabled snapshot
Source: https://gitlab.com/mobian1/phog/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
# fix DEFAULT_MAX_UID detection
Patch1: %name-0.1.5-alt-fix-min-max-uid.patch

%define phoc_ver 0.33

Requires: greetd dconf osk-wayland font(lato)
Requires: phoc >= %phoc_ver /usr/bin/phoc

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= 2.62
BuildRequires: pkgconfig(gcr-3) >= 3.7.5
BuildRequires: pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires: pkgconfig(libhandy-1) >= 1.1.90
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0) >= 43
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libnm) >= 1.14
BuildRequires: pkgconfig(upower-glib) >= 0.99.1
BuildRequires: pkgconfig(libsystemd) >= 241
%{?_enable_check:BuildRequires: at-spi2-core xvfb-run}

%description
A greetd-compatible greeter for mobile devices like Purism's Librem 5
and Pine64's PinePhone.

%prep
%setup -n %name-%version
%patch1 -p2 -b .uid

%build
%meson
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name
%dir %_datadir/%name
%_datadir/%name/phoc.ini
%_datadir/glib-2.0/schemas/%rdn_name.enums.xml
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%doc README*

%changelog
* Thu Dec 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt0.2
- src/greetd.c:
  fixed DEFAULT_MAX_UID detection if /etc/login.defs unaccessible (antohami@)

* Thu Dec 07 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt0.1
- first preview for Sisyphus (0.1.5-5-g199ac78a)



