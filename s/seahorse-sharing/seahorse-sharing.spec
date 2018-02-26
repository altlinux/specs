%define _name seahorse
%define ver_major 3.4

Name: %_name-sharing
Version: %ver_major.0
Release: alt1

Summary: PGP public key sharing using DNS-SD and HKP
License: LGPLv2+
Group: Graphical desktop/GNOME

URL: http://live.gnome.org/Seahorse
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

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
* Sun Apr 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- first build for Sisyphus

