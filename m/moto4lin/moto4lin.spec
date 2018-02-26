BuildRequires: desktop-file-utils
Name: moto4lin
Version: 0.3
Release: alt7.qa1

Summary: File manager for Motorola P2K phones
Summary(ru_RU.CP1251): Программа для управления файлами на мобильных телефонах Motorola P2K
License: %gpl2plus
Group: Communications

Url: http://moto4lin.sf.net/

Source0: %name-%version.tar
Source1: %name.rules
Source2: %name.png
Patch0: %name-svn-r82-crossplatform.patch

Packager: Mobile Development Team <mobile@packages.altlinux.org>

BuildPreReq: ImageMagick gcc-c++ libusb-compat-devel
BuildPreReq: libqt3-devel >= 3.3.0
BuildRequires(pre): rpm-build-licenses

%description
File manager and seem editor for Motorola P2K phones (C3x0, C650, V300,
V500, V600, E398, T720, T722 etc.).

This is alpha version, use it at your own risk (you should backup all
files from your phone before using this program).

%description -l ru_RU.CP1251
Файловый менеджер и редактор seem для P2K-телефонов Motorola (C3x0, C650, V300,
V500, V600, E398, T720, T722 и др.).

Поскольку это альфа-версия, используйте ее на свой страх и риск. Перед
использованием рекомендуется сделать резервную копию всех файлов вашего телефона.

%prep
%setup
%patch -p1
sed -i "s,debug,," moto_ui/moto_ui.pro

%build
lrelease-qt3 moto_ui/moto_ui.pro
qmake-qt3 "CONFIG+=no_fixpath"
%make_build QMAKE=qmake-qt3
convert -border 0x8 -bordercolor none -depth 8 %SOURCE2 %name-64.png
for s in 48 36 32 24 22 16; do
    convert -depth 8 -resize ${s}x$s %name{-64,-$s}.png
done


%install
%make_install INSTALL_ROOT=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/udev/rules.d/75-%name.rules
for s in 64 48 36 32 24 22 16; do
    install -D -m 0644 {%name-$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done
install -d -m 0755 %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Version=1.0
Name=%name
GenericName=Filemanager for Motorola P2k phones
Comment=Upload ringtones and download photos.
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Qt;Utility;PDA;
__MENU__
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TelephonyTools \
	%buildroot%_desktopdir/moto4lin.desktop


%files
%_sysconfdir/udev/rules.d/*
%_bindir/*
%_datadir/%name/
%doc Changelog INSTALL README
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*


%changelog
* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.3-alt7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for moto4lin
  * postclean-03-private-rpm-macros for the spec file

* Mon Apr 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt7
- update buildreqs

* Tue Aug 19 2008 Led <led@altlinux.ru> 0.3-alt6.1
- added %name-svn-r82-crossplatform.patch
- cleaned up spec
- added ROKR E2 (22b8:3801/3802) to udev rules
- fixed License
- added %name.desktop
- added icons

* Wed Apr 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt6
- SVN r82
- add udev rules file for 22b8:4901 and 4902 to allow work without superuser
  rights

* Sun Oct 15 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt5
- SVN r79
- change Packager:

* Sat Jun 11 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt4
- package *.pat, needed for correct java upload

* Sun May 29 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt3
- CVS 20050529

* Wed Apr 20 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt2
- CVS 20050420

* Sat Mar 05 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- CVS 20050304

* Fri Feb 25 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.1-alt1
- first build
- warning: supports only 22b8:4902 (C380), connected on /dev/ttyACM0
