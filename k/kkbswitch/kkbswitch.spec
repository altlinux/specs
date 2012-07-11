%undefine __libtoolize
%define qtdir %_qt3dir
%define kdedir %_K3prefix
%define beta %nil
%define _optlevel s
%def_disable debug

Name: kkbswitch
Version: 1.4.3
Release: alt12.1

Summary: Keyboard layout indicator for KDE
Group: Graphical desktop/KDE
URL: http://kkbswitch.sourceforge.net/
License: GPL

%if_enabled debug
Requires: gdb
%endif

Source: %name-%version%beta.tar.gz
Source1: admin.tar.bz2
Patch0: acinclude.patch
Patch1: kkbswitch-1.4.3-alt-defaults.patch
Patch2: kkbswitch-1.4.3-alt-add-dcop-kscreensaver.patch
Patch3: kkbswitch.desktop.patch
Patch4: kkbswitch-1.4.3-alt-singlewindowwatcher-fixes.patch
Patch5: kkbswitch-1.4.3-alt-DSO.patch

BuildRequires: gcc-c++
BuildRequires: libjpeg-devel libpng-devel libxkbfile-devel
BuildRequires: libqt3-devel libstdc++-devel xml-utils zlib-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs-devel
#BuildRequires: kdelibs > 1 kdelibs-devel > 1

%description
KKBSwitch is a keyboard layout indicator for KDE

%prep
%setup -q -n %name-%version%beta
rm -rf admin
tar xfj %SOURCE1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2

make -f admin/Makefile.common cvs ||:

%build
%if_enabled debug
%define _optlevel 0
%add_optflags %optflags_debug
%endif

%add_optflags -I%_includedir/tqtinterface
export QTDIR=%qtdir KDEDIR=%kdedir

%K3configure \
%if_enabled debug
    --enable-debug=full \
%endif
    --disable-ru-ua-layout

%make_build

%install
%if_enabled debug
%set_strip_method none
%endif
%K3install applnkUtilitiesdir=%_K3xdg_apps

%K3find_lang --with-kde %name


%files -f %name.lang
%doc README TODO ChangeLog AUTHORS
%doc %_man1dir/*
%_K3bindir/*
%_K3apps/%name
%_K3apps/kconf_update/*
#
%_K3xdg_apps/%name.desktop
%_K3start/*.desktop

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt12.1
- Fixed build

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.4.3-alt12
- Rebuild for TDE 3.5.13 release

* Fri Apr 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt11
- fix build requires

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt10
- move to alternate place

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt9
- fix build requires

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 1.4.3-alt8
- fix to build

* Thu Nov 20 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt7
- fix crash when switch after active window closed; thanx iv@alt

* Wed Jan 16 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt6
- separate layout for each window by default

* Fri Dec 07 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt5
- fix desktop-file

* Fri Nov 23 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt4
- add kxkb-like dcop interface

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt3
- remove double of desktop-file

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt2
- fix build requires

* Fri Dec 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt1
- new version

* Fri Aug 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.4.2-alt2
- add alias for Tatar language
- don't use flags by default

* Wed Jan 19 2005 Sergey V Turchin <zerg at altlinux dot org> 1.4.2-alt1
- new version
- build with gcc3.4

* Mon Aug 23 2004 Sergey V Turchin <zerg at altlinux dot org> 1.4.1-alt1
- new version

* Wed Feb 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.3.2-alt1
- new version

* Thu Oct 23 2003 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt1
- release 1.3

* Tue Oct 21 2003 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt0.1.pre
- 1.3pre

* Fri Sep 12 2003 Sergey V Turchin <zerg at altlinux dot org> 1.2-alt2
- add autostart feature

* Tue Nov 26 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2-alt1
- new version
- fix menu item

* Fri Sep 06 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1-alt3
- rebuild with gcc 3.2

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1-alt1
- new version

* Mon Jun 03 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt4
- add popup configuration dialog by clicking in KControl

* Fri Apr 26 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt3
- build with KDE3

* Fri Mar 22 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt2
- remove Requires kdebase

* Tue Jan 22 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt1
- initial spec

