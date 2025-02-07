%define _unpackaged_files_terminate_build 1

Name: caja-seahorse
Version: 1.18.5
Release: alt1

Summary: Caja extension to encrypt/decrypt OpenPGP files using GnuPG
License: GPLv2
Group: Graphical desktop/MATE
Url: https://github.com/darkshram/seahorse-caja

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: mate-common
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gcr-3)
BuildRequires: gnupg2
BuildRequires: gpgme libgpgme-devel
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(cryptui-0.0)
BuildRequires: pkgconfig(libnotify)

Requires: /usr/bin/caja
Requires: seahorse

%description
Seahorse Caja is an extension for Caja which allows encryption and
decryption of OpenPGP files using GnuPG. It is integrated into the Caja
right-click menu, but can also be used from the command line. It's based
on seahorse-nautilus.

%prep
%setup

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static \
  --disable-gpg-check
%make_build

%install
%makeinstall_std

find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %name --all-name

%files -f %name.lang
%doc NEWS ChangeLog COPYING README.md AUTHORS THANKS
%_bindir/*
%_man1dir/*
%_libdir/caja/extensions-2.0/*.so
%_datadir/applications/*.desktop
%dir %_datadir/seahorse-caja/
%_datadir/seahorse-caja/*
%_datadir/glib-2.0/schemas/org.mate.seahorse.caja.*gschema.xml

%changelog
* Fri Feb 07 2025 Nikolay Strelkov <snk@altlinux.org> 1.18.5-alt1
- Initial build for Sisyphus
