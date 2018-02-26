BuildRequires: desktop-file-utils
Name: qtemu
Version: 2.0
Release: alt0.1.1.qa3

Summary: QtEmu is a graphical user interface for QEMU written in Qt4
Summary(ru_RU.UTF-8): QtEmu - графический интерфейс для QEMU, написаный на Qt4
License: GPL
Group: Emulators
Url: http://qtemu.org

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar
Source1: %name.desktop
Patch0: qtemu-help-transl-alt.patch
Patch1: qtemu-alt-qt4.patch
Patch2: qtemu-alt-DSO.patch


# Automatically added by buildreq on Wed Sep 12 2007
BuildRequires: gcc-c++ libSM-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel libqt4-devel
BuildPreReq: cmake
BuildPreReq: libvncserver-devel

Requires: qemu

%description
QtEmu is a graphical user interface for QEMU written in Qt4. 

%description -l ru_RU.UTF8
QtEmu - графический интерфейс для QEMU, написаный на Qt4.   

%prep
%setup -q
%patch0 -p1
%patch1 -p2
%patch2 -p2

#subst 's|DESTINATION translations|DESTINATION %_datadir/qt4/translations/|g' CMakeLists.txt
#subst 's|DESTINATION help|DESTINATION %_docdir/%name-%version/|g' CMakeLists.txt

%build
cmake -DCMAKE_INSTALL_PREFIX=%_usr -DQT_QMAKE_EXECUTABLE=%_qt4dir/bin/qmake .
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

mkdir -p %buildroot%_desktopdir
cp %SOURCE1 %buildroot%_desktopdir/
mkdir -p %buildroot%_niconsdir
cp images/oxygen/%name.png %buildroot%_niconsdir/
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	--add-category=Emulator \
	%buildroot%_desktopdir/qtemu.desktop

%files -f %name.lang
%_bindir/*
%_datadir/%{name}/translations/*
%_datadir/%{name}/help/*
%_desktopdir/*
%_niconsdir/*
%doc COPYING CHANGELOG README help/

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt0.1.1.qa3
- Fixed build

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt0.1.1.qa2
- Fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt0.1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qtemu

* Sat Nov 28 2009 Alexey Morsov <swi@altlinux.ru> 2.0-alt0.1.1
- new version
- remove absoluted macros

* Fri Nov 16 2007 Alexey Morsov <swi@altlinux.ru> 1.0.5-alt2
- fix translations installation path (bug #13432)
- fix doc paths in CMakeLists.txt instead of manual mv

* Tue Nov 13 2007 Alexey Morsov <swi@altlinux.ru> 1.0.5-alt1
- Option for custom network settings.
- Possibility to set additional options which are not covered by QtEmu.
- Sound configuration.

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 1.0.4-alt2
- critical: fix machine starting
- fix: rebuild with full src-tree (my mistake while merge in git)

* Wed Sep 12 2007 Alexey Morsov <swi@altlinux.ru> 1.0.4-alt1
- version 1.0.4

* Wed Sep 12 2007 Terechkov Evgenii <evg@altlinux.ru> 1.0.3-alt2
- Spec cleanups
- #12748 fixed in spec

* Tue Mar 20 2007 Alexey Morsov <swi@altlinux.ru> 1.0.3-alt1
- first build for sisyphus

