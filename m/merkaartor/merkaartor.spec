Name: merkaartor
Version: 0.16.1
Release: alt1
Packager: Egor Glukhov <kaman@altlinux.org>

Summary: an OpenStreetMap editor
License: LGPL
Group: Sciences/Geosciences
Url: http://www.merkaartor.org/

Source: %name-%version.tar

BuildRequires: boost-devel gcc-c++ git-core glibc-devel-static
BuildRequires: libgdal-devel libqt4-devel

%description
Merkaartor is an openstreetmap mapping program.
Merkaartor focuses on providing a visually pleasing but performant
editing environment for free geographical data.

%prep
%setup

%build
lupdate-qt4 Merkaartor.pro
lrelease-qt4 Merkaartor.pro
qmake-qt4 PREFIX=%_prefix NODEBUG=1 TRANSDIR_MERKAARTOR=%_datadir/%name/translations/ Merkaartor.pro
%make_build

%install
LIB_SUFFIX=
%ifarch x86_64
LIB_SUFFIX=64
%endif
%make_install INSTALL_ROOT=%buildroot LIB_SUFFIX=$LIB_SUFFIX install

%files
%_bindir/merkaartor
%_datadir/%name/
%_libdir/%name/
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Wed Aug 11 2010 Egor Glukhov <kaman@altlinux.org> 0.16.1-alt1
- 0.16.1

* Thu Aug 13 2009 Grigory Batalov <bga@altlinux.ru> 0.14-alt1
- New upstream release.

* Tue Apr 28 2009 Grigory Batalov <bga@altlinux.ru> 0.13.2-alt2
- Own directory with translations.

* Tue Apr 28 2009 Grigory Batalov <bga@altlinux.ru> 0.13.2-alt1
- New upstream release (OSM API 0.6).

* Thu Apr 23 2009 Grigory Batalov <bga@altlinux.ru> 0.13.1-alt1
- New upstream release.

* Tue Nov 11 2008 Grigory Batalov <bga@altlinux.ru> 0.0.13-alt0.r11862
- New SVN version.
- Translations included (thanks to Maks Vasilev <max@stranger-team.ru>).

* Tue May 27 2008 Grigory Batalov <bga@altlinux.ru> 0.0.11-alt0.r7914
- New SVN version.

* Fri Apr 25 2008 Grigory Batalov <bga@altlinux.ru> 0.0.10-alt1
- Build for ALT Linux.
