%def_enable snapshot

%define _name seahorse
%define ver_major 3.11
%def_enable libnotify

Name: %_name-nautilus
Version: %ver_major.92
Release: alt2

Summary: PGP encryption and signing for Nautilus
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Seahorse

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires: meson rpm-build-gnome
BuildRequires: libgtk+3-devel libnautilus-devel libcryptui-devel libgpgme-devel
BuildRequires: libgnome-keyring-devel libdbus-glib-devel gnupg2-gpg gcr-libs-devel
%{?_enable_libnotify:BuildPreReq: libnotify-devel >= 0.7.2}

%description
This package provides extension for Nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%prep
%setup

%build
%meson \
    %{?_enable_libnotify:-Dlibnotify=true}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%_name-tool
%nautilus_extdir/libnautilus-seahorse.so
%_desktopdir/seahorse-pgp-encrypted.desktop
%_desktopdir/seahorse-pgp-keys.desktop
%_desktopdir/seahorse-pgp-signature.desktop
%_datadir/glib-2.0/schemas/org.gnome.seahorse.nautilus.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.seahorse.nautilus.window.gschema.xml
%_man1dir/%_name-tool.1.*
%doc AUTHORS NEWS README*

%changelog
* Fri Jan 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt2
- updated to 3.11.92-42-g0b57f04

* Sun Mar 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Thu Oct 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.5-alt1
- 3.7.5

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Apr 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- first build for Sisyphus

