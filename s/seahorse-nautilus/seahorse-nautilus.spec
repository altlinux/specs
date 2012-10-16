%define _name seahorse
%define ver_major 3.6
%def_enable libnotify

Name: %_name-nautilus
Version: %ver_major.1
Release: alt1

Summary: PGP encryption and signing for Nautilus
License: LGPLv2+
Group: Graphical desktop/GNOME

URL: http://live.gnome.org/Seahorse
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: rpm-build-gnome intltool
BuildRequires: libgtk+3-devel libnautilus-devel libcryptui-devel libgpgme-devel
BuildRequires: libgnome-keyring-devel libdbus-glib-devel gnupg2-gpg gcr-libs-devel
%{?_enable_libnotify:BuildPreReq: libnotify-devel >= 0.7.2}

%description
This package provides extension for Nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%prep
%setup

%build
export GNUPG=/usr/bin/gpg2
%configure --disable-static \
	--disable-schemas-compile \
	%{subst_enable libnotify}

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%_name-tool
%nautilus_extdir/libnautilus-seahorse.so
%_desktopdir/seahorse-pgp-encrypted.desktop
%_desktopdir/seahorse-pgp-keys.desktop
%_desktopdir/seahorse-pgp-signature.desktop
%_datadir/%name/
%_datadir/GConf/gsettings/org.gnome.seahorse.nautilus.convert
%_datadir/glib-2.0/schemas/org.gnome.seahorse.nautilus.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.seahorse.nautilus.window.gschema.xml
%_man1dir/%_name-tool.1.*
%doc AUTHORS NEWS README

%exclude %nautilus_extdir/*.la

%changelog
* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Apr 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- first build for Sisyphus

