%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name:    kbfx
Version: 0.4.9.3.1
Release: alt10

Summary: KBFX is an alternative to the classical K-Menu button and it's menu
Summary(ru_RU.UTF-8): Альтернативное меню KDE
License: GPL
Group:   Graphical desktop/KDE
URL:     http://sourceforge.net/projects/kbfx/ 

Packager: Andrey Cherepanov <cas@altlinux.ru>

Source:  %name-%version.tar.bz2
Source1: kbfxconfigapp.desktop
Source2: kbfx_theme.desktop

Patch0:  %name.patch
Patch1:  %name-build-fix.patch
Patch2:  %name-new-kde3-placemenet-build.patch
Patch3:  %name-0.4.9.3.1-alt-DSO.patch
Patch4:  %name-0.4.9.3.1-alt-noplugins_crash.patch

BuildRequires(pre): rpm-macros-kde-common-devel
BuildRequires: gcc-c++ cmake
BuildRequires: kdelibs-devel libqt3-devel libjpeg-devel

%description
KBFX is an alternative to the classical K-Menu button and it's menu.
It improves the user experience by enabling the user to set a bigger (and
thus more visible) start button and by finally replacing the Win95-like
K-Menu with the Spinx bar.
If you still want the old menu, because you're used to it, it is still
available as an option in kbfx.

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p2
%patch2 -p2
##%patch3 -p2
%patch4
cp -a %SOURCE1 configdialog/kbfxconfigapp.desktop
cp -a %SOURCE2 configdialog/kbfx_theme.desktop
subst "s,QPixmap::QPixmap,QPixmap,g" `find . -name '*.cpp'`

%build
export QTDIR=%qtdir
export KDEDIR=%prefix
export PATH=%qtdir/bin:%kdedir/bin:$PATH

%K3cmake -DDESTINATION=%buildroot
%K3make

%install
%K3install
%K3find_lang --with-kde kbfxconfigapp

rm -f %buildroot%_K3libdir/kde3/libkbfx*.la
rm -f %buildroot%_K3libdir/kbfx/plugins/*.la
rm -f %buildroot%_K3libdir/libkbfx*.la

%files -f kbfxconfigapp.lang
%doc doc/*
%doc %_K3doc/en/common/*
%_K3bindir/kbfxconfigapp
%_K3libdir/libkbfx*.so
%_K3libdir/kde3/libkbfx*.so
%_K3libdir/kbfx/plugins/*
%_K3libdir/libkbfx*.so
%_K3includedir/kbfx/*
%_K3apps/kbfx/*
%_K3apps/kbfxconfigapp/*
%_K3apps/kicker/applets/*.desktop
%_K3apps/konqueror/servicemenus/*.desktop
%_K3xdg_apps/*.desktop
%_K3mimelnk/*
%_iconsdir/hicolor/128x128/apps/*
%_niconsdir/*
%_miconsdir/*

%changelog
* Fri Jun 22 2012 Roman Savochenko <rom_as@altlinux.ru> 0.4.9.3.1-alt10
- Rebuild for TDE 3.5.13 release.
- Plugins place and translations is fixed.

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9.3.1-alt9.1
- Fixed build

* Thu Mar 01 2012 Andrey Cherepanov <cas@altlinux.org> 0.4.9.3.1-alt9
- Build for new KDE 3.5.13

* Wed Apr 13 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.9.3.1-alt8
- Migration on new KDE3 placement

* Thu Feb 03 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.9.3.1-alt7
- Rebuild with KDE 3.5.12
- Clear spec file

* Wed Jan 19 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.9.3.1-alt6
- fix build in Sisyphus

* Fri Nov 21 2008 Andrey Cherepanov <cas@altlinux.org> 0.4.9.3.1-alt5
- Remove deprecated update-desktop-database and update-menus macros 
- Remove deprecated ldconfig call in post
- Fix desktop files

* Wed Apr 16 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.9.3.1-alt4
- Fix post_ldconfig/postun_ldconfig

* Fri Feb 29 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.9.3.1-alt3
- Fix icon pathes

* Mon Oct 22 2007 Andrey Cherepanov <cas@altlinux.ru> 0.4.9.3.1-alt2
- Fix icon pathes

* Sat Jun 09 2007 Andrey Cherepanov <cas@altlinux.ru> 0.4.9.3.1-alt1
- New version

* Thu May 10 2007 Andrey Cherepanov <cas@altlinux.ru> 0.4.9.2rc4-alt2
- Fix build (update menus)

* Mon May 07 2007 Andrey Cherepanov <cas@altlinux.ru> 0.4.9.2rc4-alt1
- Initial implementation
