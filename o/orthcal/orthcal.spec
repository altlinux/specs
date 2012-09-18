Name: orthcal
Version: 1.3
Release: alt1

Summary: Eastern Orthodox Calendar with daily Feasts

Url: https://apps.ubuntu.com/cat/applications/orthcal/
License: GPLv3
Group: Office

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

Requires: perl-DBD-SQLite

# manually removed: rpm-build-gir

# Automatically added by buildreq on Tue Sep 18 2012 (-bi)
# optimized out: fontconfig libX11-locales libgdk-pixbuf libwayland-client libwayland-server perl-Cairo perl-Carp-Clan perl-Date-Calc-XS perl-Encode perl-Glib perl-Pango python-base python-module-distribute python-module-peak python-module-zope
BuildRequires: perl-DBI perl-Date-Calc perl-Gtk2 perl-Locale-gettext python-module-mwlib python-module-paste 

%description
Eastern Orthodox Calendar with daily Feasts.

%prep
%setup
%__subst "s|/opt/extras.ubuntu.com|%_datadir|g" bin/* *.desktop

%install
make install INSTALLDIR=%buildroot%_datadir/%name DESTDIR=%buildroot
mkdir -p %buildroot%_bindir/
ln -s %_datadir/%name/bin/OrthCal.pl %buildroot%_bindir/%name

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/extras-%name.desktop

%changelog
* Tue Sep 18 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Linux Sisyphus
