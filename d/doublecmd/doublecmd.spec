Name:		doublecmd
Summary:	Twin-panel (commander-style) file manager (GTK2 and QT4)
Version:	0.7.8
Release:	alt1
Url:		http://doublecmd.sourceforge.net

Packager:	Motsyo Gennadi <drool@altlinux.ru>

Source0:	%name-%version.tar
Source1:	%name-qt.desktop
License:	GPLv2
Group:		File tools

BuildRequires: fpc >= 2.6.2 fpc-src glib2-devel libgtk+2-devel lazarus >= 1.0.10 libQt4Pas5-devel >= 2.5 /usr/bin/convert
BuildRequires: libncurses-devel
BuildRequires: libdbus-devel
BuildRequires: bzlib-devel
BuildRequires: gdk-pixbuf-devel
BuildRequires: xorg-proto-devel
BuildRequires: xorg-xtrans-devel

%description
Double Commander (GTK2 and QT4 versions) is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package -n %name-gtk
Summary:	Twin-panel (commander-style) file manager (GTK2)
Group:		File tools
Requires:	%name-common
Provides:	%name
Obsoletes:	%name < 0.6.1

%description -n %name-gtk
Double Commander GTK is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package -n %name-qt
Summary:	Twin-panel (commander-style) file manager (Qt4)
Group:		File tools
Requires:	%name-common

%description -n %name-qt
Double Commander QT4 is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%package -n %name-common
Summary:	Common files for Double Commander
Group:		File tools

%description -n %name-common
Common files for Double Commander

%prep
%setup

%build
./build.sh beta qt
mv ./%name ./%name-qt && mv ./%name.zdli ./%name-qt.zdli
./clean.sh
./build.sh beta gtk2

# To fix ... "oblom" ... when processing install ;)
%set_verify_elf_method textrel=relaxed

%install
install/linux/install.sh --install-prefix=%buildroot
install ./%name-qt %buildroot%_libdir/%name/%name-qt
install -m 0644 ./%name-qt.zdli %buildroot%_libdir/%name/%name-qt.zdli
ln -s ../%_lib/%name/%name-qt %buildroot%_bindir/%name-qt
install -m 0644 %SOURCE1 %buildroot%_desktopdir/%name-qt.desktop

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 pixmaps/mainicon/alt/256px-dcfinal.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 pixmaps/mainicon/alt/256px-dcfinal.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 pixmaps/mainicon/alt/256px-dcfinal.png %buildroot%_miconsdir/%name.png

%files -n %name-gtk
%_bindir/%name
%_libdir/%name/%name
%_libdir/%name/%name.zdli
%_desktopdir/%name.desktop

%files -n %name-qt
%_bindir/%name-qt
%_libdir/%name/%name-qt
%_libdir/%name/%name-qt.zdli
%_desktopdir/%name-qt.desktop

%files -n %name-common
%exclude %_libdir/%name/%name
%exclude %_libdir/%name/%name-qt
%exclude %_libdir/%name/%name.zdli
%exclude %_libdir/%name/%name-qt.zdli
%exclude %_bindir/%name
%exclude %_bindir/%name-qt
%_libdir/%name
%_datadir/%name
%_man1dir/%name.*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Mon Feb 27 2017 Motsyo Gennadi <drool@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Mon Dec 26 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Fri Dec 02 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Mon May 30 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Thu Mar 31 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Thu Mar 17 2016 Motsyo Gennadi <drool@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sat Oct 17 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sun Aug 16 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Jul 14 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Mon Jun 15 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Tue May 12 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Fri May 08 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.1-alt2
- fix BuildRequires

* Fri May 01 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6.1-alt1
- 0.6.1
- build Qt4 version

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version

* Mon Dec 30 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.8-alt0.rev.5390
- build for Sisyphus (thank for src.rpm to Anatoly Chernov)

* Sat Sep 28 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.7-alt0.rev.5310
- build for Sisyphus (thank for src.rpm to Anatoly Chernov)

* Tue Mar 26 2013 Andrey Cherepanov <cas@altlinux.org> 0.5.4-alt2
- Fix build by commented out unused assignment

* Wed Feb 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.4-alt1
- build for Sisyphus

* Mon Oct 22 2012 - Anatoly Chernov <aichernov@umail.ru>
- New beta release 0.5.4-3.3 (beta 16.10.2012) with no problem ... :)

* Sun Jun 24 2012 - Anatoly Chernov <aichernov@umail.ru>
- Initial package, version 0.5.4 beta (with new Lazarus) and fix the problem:
- at first:... (hi!)
- /usr/bin/ld: warning: creating a DT_TEXTREL in a shared object.
- ... (skip about 3000 lines) ...
- and later on: ...
- verify-elf: ERROR: ... : TEXTREL entry found: 0x00000000
- RPM build errors: ... ;)
- ...
- assembler ... "blin"
- see http://lists.altlinux.org/pipermail/devel/2012-June/194625.html

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6
