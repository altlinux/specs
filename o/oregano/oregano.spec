Name: oregano
Version: 0.84.43
Release: alt2

Summary: A GUI to simulate electronic circuit

License: GPLv2+
Group: Graphics
Url: https://github.com/drahnr/oregano

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/drahnr/oregano/archive/v%version.tar.gz
Source: %name-%version.tar

Patch: oregano-0.70-sfmt.patch
Patch1: oregano-0.70-linkage.patch

BuildRequires: groff-base intltool libgoocanvas2-devel libgtksourceview3-devel libxml2-devel perl-Encode-JP
BuildRequires: waf python3


%description
Oregano is an application for schematic capture and simulation of
electrical circuits. For the actual simulation, Oregano acts as a
front-end for SPICE, which is more or less the industry standard for
circuit simulation.

Recommended: gnucap ngspice

%prep
%setup
rm -v ./waf
waf distclean || true

%build
CFLAGS="%optflags" waf -v configure --destdir="%buildroot" --prefix="%prefix" --sysconfdir="%_sysconfdir" build

%install
waf install --destdir="%buildroot" --prefix="%prefix" --sysconfdir="%_sysconfdir"
rm -f %buildroot%_bindir/microtests/
#rm -rfv %buildroot%_datadir/glib-2.0/schemas/

%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS
%_bindir/*
%_man1dir/*
%_datadir/oregano
%_desktopdir/*
%_iconsdir/hicolor/*/apps/oregano.png
%_iconsdir/hicolor/scalable/apps/oregano.svg
%_datadir/mime/packages/*.xml
%_datadir/mime-info/oregano.keys
%_datadir/glib-2.0/schemas/*

%changelog
* Wed Jul 26 2023 Vitaly Lipatov <lav@altlinux.ru> 0.84.43-alt2
- build with external waf

* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 0.84.43-alt1
- new version 0.84.43 (with rpmrb script)

* Sat Apr 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.84.41-alt1
- new version 0.84.41 (with rpmrb script)

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.84.22-alt1
- switch to https://github.com/drahnr/oregano
- new version 0.84.22 (with rpmrb script)

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.82-alt1
- initial build for ALT Sisyphus

* Fri Jun 27 2014 Alex Burmashev <alex.burmashev@rosalab.ru> 0.70-2
+ Revision: 03f78bc
- MassBuild#440: Increase release tag


