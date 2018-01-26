%def_enable snapshot

%define _name seahorse
%define ver_major 3.8

Name: %_name-sharing
Version: %ver_major.0
Release: alt2

Summary: PGP public key sharing using DNS-SD and HKP
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Seahorse

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires: rpm-build-gnome intltool
BuildRequires: libgtk+3-devel libsoup-devel libgpgme-devel libavahi-glib-devel
BuildRequires: libSM-devel gnupg2-gpg

%description
This package provides extension for Nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%prep
%setup

%build
export GNUPG=/usr/bin/gpg2
%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/seahorse-sharing.desktop
%_bindir/%name
%_datadir/pixmaps/seahorse/*/*
%_man1dir/%name.1.*
%doc AUTHORS NEWS README

%changelog
* Fri Jan 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- updated to 3.8.0-22-g0370fb3

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Apr 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- first build for Sisyphus

