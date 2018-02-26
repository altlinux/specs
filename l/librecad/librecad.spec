Name: librecad
Version: 2.0.0
Release: alt0.alpha3

Summary: Computer-aided design (CAD) system
Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://www.librecad.org
License: GPLv2
Group: Graphics

Source: librecad-%version.tar
Patch: 0001-Adding-DXF-.desktop-file.patch
Patch1: librecad-1.0.0-mdv-desktop.patch

Requires: librecad-data
#Suggests:	librecad-doc
#Suggests:	librecad-plugins

# Removed manually: git-core glibc-devel-static 
# Automatically added by buildreq on Sat Jun 02 2012
# optimized out: fontconfig libfreetype-devel libqt4-clucene libqt4-core libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-sql libqt4-sql-sqlite libstdc++-devel
BuildRequires: boost-devel-headers gcc-c++ libmuparser-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel

%description
LibreCAD is an application for computer aided design (CAD) in two
dimensions (2D). With LibreCAD you can create technical drawings
such as plans for buildings, interiors, mechanical parts or schemas
and diagrams.

%package data
Group: Graphics
Summary: Platform independent files for %name
Requires: %name
BuildArch: noarch

%description data
Contains the platform-independent files for LibreCAD, including
fonts, patterns, translations.

#package doc
#Group:		Graphics
#Summary:	Documentation for %name
#Requires:	%name
#BuildArch:	noarch
#
#description doc
#Documentation for %name, a Qt4 application to design 2D CAD
#drawing based on the community edition of QCad.

%package plugins
Group: Graphics
Summary: Plugins libraries files for %name
Requires: %name

%description plugins
Contains the plugins files for LibreCAD.

%prep
%setup

%patch0 -p1
%patch1 -p1
find . -type f -executable -a \( -name '*.cpp' -o -name '*.h' \) | xargs -i{} chmod 644 {}

%build
export QTDIR=%_qt4dir/
export PATH=$PATH:$QTDIR/bin

%define qmake_qt4 qmake-qt4
%qmake_qt4 librecad.pro
%make_build

pushd plugins
	%qmake_qt4
	%make_build plugins.pro
popd

%install
%makeinstall INSTALL_ROOT=%buildroot

install -m 755 -d %buildroot%_datadir/%name/doc
install -m 755 -d %buildroot%_datadir/%name/fonts
install -m 755 -d %buildroot%_datadir/%name/library
install -m 755 -d %buildroot%_datadir/%name/patterns
install -m 755 -d %buildroot%_datadir/%name/qm
install -m 755 -d %buildroot%_docdir/%name
install -m 755 -d %buildroot%_libdir/%name/plugins
install -m 755 -d %buildroot%_datadir/mime/packages

#cp unix/resources/doc/* %buildroot%_datadir/%name/doc/
cp unix/resources/fonts/*.lff %buildroot%_datadir/%name/fonts/
cp -r unix/resources/library/* %buildroot%_datadir/%name/library/
cp unix/resources/patterns/*.dxf %buildroot%_datadir/%name/patterns/
cp unix/resources/qm/*.qm %buildroot%_datadir/%name/qm/
cp unix/resources/plugins/* %buildroot%_libdir/%name/plugins/
cp gpl-2.0.txt LICENSE
chmod 644 LICENSE
chmod 644 README
find %buildroot%_datadir/%name -type f -exec chmod 644 {} \;

install -Dm 755 unix/%name %buildroot%_bindir/%name
install -Dm 644 desktop/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 644 desktop/%name.sharedmimeinfo %buildroot%_datadir/mime/packages/%name.xml
install -Dm 644 desktop/graphics_icons_and_splash/Icon\ LibreCAD/Icon_Librecad.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc LICENSE README
%_bindir/%name
%_desktopdir/%name.desktop
#%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml

%files data
%dir %_datadir/%name/
%_datadir/%name/fonts/
%_datadir/%name/library/
%_datadir/%name/patterns/
%_datadir/%name/qm/

#files doc
#%_datadir/%name/doc/*

%files plugins
%_libdir/%name/plugins/

%changelog
* Sat Jun 02 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.alpha3
- build 2.0.0 alpha3

* Fri Jan 13 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jan 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:1.0.0-1
+ Revision: 759355
- add Epoch: 1
- remove Makefile and spec.in
- remove BuildRoot tag, replace spaces with tabs
- 1.0.0 final release

* Wed Aug 17 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1.99.2-1
+ Revision: 694859
- Updating to latest git snapshot

* Sat Aug 13 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1.99.1-1
+ Revision: 694367
- Adding missing source package for 1.0.0rc1.99.1
- Update to latest snapshot, still pre RC2

* Sat Aug 06 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1.99-1
+ Revision: 693531
- Updating to pre-RC2 snapshot and using new patches capabilities of gitrpm helper
- Using 'mdv' branch for desktop file
- Updating stuff for new gitrpm
- Update for latest rpm-common changes
- Introducing GitRPM funny stuff, see http://git.mandriva.com/projects/?p=users/alissy/gitrpm.git;a=summary

* Thu Jun 23 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1_55_g4f9b7c5-1
+ Revision: 686840
- Updating from 1.0.0beta5 to 1.0.0rc1

* Tue Jun 07 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0beta5_144_g0046d99-1
+ Revision: 683100
- Updating to latest git revision
- Dropping obsolete french locale patch

* Sun Jun 05 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0beta5_132_gf21f8b2-1
+ Revision: 682785
- Updating to latest git tree, and dropping merged patches.

* Thu Jun 02 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0beta5_116_g88b5983-1
+ Revision: 682483
- Fix missing BuildRequires against qt4-linguist
- Fix missing BuildRequires against qt4-assistant (providing qcollectiongenerator)
- Importing LibreCAD.
- Created package structure for librecad.

