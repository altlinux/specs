%undefine __libtoolize
%define unstable 0
%define _optlevel s
%define glibc_core_ver %{get_version glibc-core}
%define _keep_libtool_files 1

%define qtdir %_qt3dir
%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libkde

Name: kdeaccessibility
Version: 3.5.13
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - accessibility programs
License: GPL
URL: http://www.kde.org

Requires: %name-kmag = %version-%release
Requires: %name-kmousetool = %version-%release
Requires: %name-kmouth = %version-%release
Requires: %name-icon-theme-mono
#Requires: %name-ksayit = %version-%release
Requires: %name-ktts = %version-%release
Requires: %name-kbstate = %version-%release

Source: %name-%version.tar

# Automatically added by buildreq on Fri Mar 05 2004 (-bi)
BuildRequires: gcc-c++
BuildRequires: kdelibs-devel libjpeg-devel libpng-devel libqt3-devel
BuildRequires: libstdc++-devel qt3-designer xml-utils zlib-devel
BuildRequires: kdemultimedia-devel kde-common-devel
BuildRequires: libacl-devel libattr-devel libalsa-devel
BuildRequires: libXtst-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
K Desktop Environment - accessibility programs

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
#
%description common
Common empty package for %name

%package kmag
Summary: A screen magnifier for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmag
Kmag is a KDE screen magnifier for the visually impaired.

%package kmousetool
Summary: KDE mouse manipulation tool
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmousetool
Kmousetool  is  a KDE mouse manipulation tool aimed to help
aid disabled people but useful for  many.   It  includes  features  and
options  that  provide artificial intelligence on common mouse gestures
to perform actions.

%package kmouth
Summary: A type and say KDE front end for speech synthesizers
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmouth
Kmouth is a type and say KDE front end for speech synthesizers.

%package icon-theme-mono
Summary: Monochrome icon theme for KDE
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: kde-icon-theme-mono = %version-%release
#
%description icon-theme-mono
Monochrome icon theme for KDE

%package ksayit
Summary: Text-to-Speech Frontend for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksayit
Text-to-Speech Frontend for KDE

%package ktts
Summary: Text-to-speech system for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ktts
Text-to-speech system for KDE

%package kbstate
Summary: Keyboard status applet
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kbstate
Panel applet that shows the state of the modifier keys


%prep
%setup -q
cp -ar altlinux/admin ./

sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in

find ./ -type f -name Makefile.am | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lkdefx -lDCOP -lkdeinit_kded \$(LIB_KPARTS) \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%K3configure \
    --disable-gcc-hidden-visibility \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-ksayit-audio-plugins \
    --disable-kttsd-gstreamer \
    --enable-kttsd-command \
    --enable-kttsd-epos \
    --enable-kttsd-festivalint \
    --enable-kttsd-flite \
    --enable-kttsd-freetts

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%if %unstable
%set_strip_method none
%endif
export PATH=%_bindir:$PATH

%K3install


%files
%files common
%_K3conf/*

%files kmag
%_K3bindir/kmag
%_K3apps/kmag
%_kde3_iconsdir/*/*/apps/kmag.png
%doc %_K3doc/en/kmag
%_K3applnk/Applications/kmag.desktop

%files kmousetool
%_K3bindir/kmousetool
%_K3apps/kmousetool
%_kde3_iconsdir/*/*/apps/kmousetool.png
%doc %_K3doc/en/kmousetool
%_K3applnk/Applications/kmousetool.desktop

%files kmouth
%_K3bindir/kmouth
%_K3apps/kmouth
#/usr/share/config/kmouthrc
%doc %_K3doc/en/kmouth
%_kde3_iconsdir/*/*/apps/kmouth.png
%_K3applnk/Applications/kmouth.desktop

%files icon-theme-mono
%_iconsdir/mono/

#%files ksayit
#%_K3includedir/ksayit_fxplugin.h
#
#%_K3bindir/ksayit
#%_K3lib/libFreeverb_plugin.*
#%_K3apps/ksayit/
#%_K3srv/ksayit_libFreeverb.desktop
#%_K3srvtyp/ksayit_libFreeverb_service.desktop
#%_kde3_iconsdir/hicolor/*/apps/ksayit.*
#%_kde3_iconsdir/hicolor/*/apps/ksayit_*.*
#%_K3xdg_apps/ksayit.desktop


%files ktts
#%_K3includedir/kparts/kttsjobmgr.h
#
%_K3bindir/kttsd
%_K3bindir/kttsmgr
#%_K3libdir/libKTTSD_Lib.so*
%_K3libdir/libkttsd.so*
%_K3lib/kcm_kttsd.*
%_K3lib/ktexteditor_kttsd.*
%_K3lib/libkttsd_*plugin.*
%_K3lib/libkttsjobmgrpart.*
%_K3apps/ktexteditor_kttsd
%_K3apps/kttsd/
#%_K3apps/kttsjobmgr/
%_K3srv/ktexteditor_kttsd.desktop
%_K3srv/kttsd.desktop
%_K3srv/kttsd_*plugin.desktop
%_K3srv/kttsjobmgr.desktop
%_K3srvtyp/kttsd_audioplugin.desktop
%_K3srvtyp/kttsd_filterplugin.desktop
%_K3srvtyp/kttsd_synthplugin.desktop
#%_kde3_iconsdir/crystalsvg/*/apps/kttsd.*
%_kde3_iconsdir/*/*/actions/female.*
%_kde3_iconsdir/*/*/actions/male.*
%_kde3_iconsdir/*/*/actions/nospeak.png
%_kde3_iconsdir/*/*/actions/speak.png
%_K3doc/en/kttsd
%_K3xdg_apps/kcmkttsd.desktop
%_K3xdg_apps/kttsmgr.desktop

%files kbstate
%_K3lib/kbstate_panelapplet.*
%_K3apps/kbstateapplet/
%_K3apps/kicker/applets/kbstateapplet.desktop

%changelog
* Sun Jun 17 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt3.1
- Removed bad RPATH

* Tue Sep 20 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt3
- fix conflict with kde-4.7

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- remove xorg-x11-devel requirement

* Thu Feb 24 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Wed Dec 22 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu Aug 09 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- move keyboard status applet to kbstate subpackage

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- remove patch against text relocations 

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version
- fix text relocations; thanks Alexey Morozov

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Tue Apr 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Thu Dec 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Sat Oct 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Tue Apr 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Fri Mar 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- initial spec
