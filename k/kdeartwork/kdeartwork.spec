%undefine __libtoolize
%define qtdir %_qt3dir
%define unstable 0
%define _optlevel s
%define _keep_libtool_files 1
%define cmake 1

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3
%define with_xscreensaver 1

Name: kdeartwork
Version: 3.5.13
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE Artwork (empty package)
License: GPL

Requires: %name-emoticons = %version-%release
Requires: %name-icon-theme-ikons = %version-%release
Requires: %name-icon-theme-kdeclassic = %version-%release
Requires: %name-icon-theme-kids = %version-%release
Requires: %name-icon-theme-locolor = %version-%release
Requires: %name-icon-theme-slick = %version-%release
Requires: %name-styles-cde = %version-%release
Requires: %name-styles-cde-kwin = %version-%release
Requires: %name-styles-smoothblend = %version-%release
Requires: %name-styles-smoothblend-kwin = %version-%release
Requires: %name-styles-dotnet = %version-%release
Requires: %name-styles-dotnet-widgets = %version-%release
Requires: %name-styles-glow = %version-%release
Requires: %name-styles-glow-kwin = %version-%release
Requires: %name-styles-icewm = %version-%release
Requires: %name-styles-icewm-kwin = %version-%release
Requires: %name-styles-kde1 = %version-%release
Requires: %name-styles-kde1-kwin = %version-%release
Requires: %name-styles-kstep = %version-%release
Requires: %name-styles-kstep-kwin = %version-%release
Requires: %name-styles-riscos = %version-%release
Requires: %name-styles-riscos-kwin = %version-%release
Requires: %name-styles-openlook = %version-%release
Requires: %name-styles-openlook-kwin = %version-%release
Requires: %name-styles-phase = %version-%release
Requires: %name-styles-phase-widgets = %version-%release
Requires: %name-styles-system = %version-%release
Requires: %name-styles-system-kwin = %version-%release
Requires: %name-sounds = %version-%release
Requires: %name-wallpapers = %version-%release
Requires: %name-kworldclock = %version-%release
Requires: %name-screensavers = %version-%release
%if %with_xscreensaver
Requires: %name-xscreensaver = %version-%release
%endif

Source0: kdeartwork-%version.tar

Patch01: tde-3.5.13-build-defdir.patch

# Automatically added by buildreq on Wed Oct 16 2002
#BuildRequires: XFree86-devel XFree86-libs fontconfig-devel freetype2 gcc-c++ kde-common kde-config kdebase-devel kdelibs-devel libGLU-devel libart_lgpl-devel libarts-devel libexpat libjpeg-devel liblcms libmng libpng-devel libqt3-devel libstdc++-devel objprelink xscreensaver zlib-devel
BuildRequires: cmake fontconfig-devel
BuildRequires: gcc-c++ kdebase-devel
BuildRequires: libart_lgpl-devel libexpat
BuildRequires: libjpeg-devel liblcms libmng libpng-devel libqt3-devel
BuildRequires: libstdc++-devel zlib-devel
BuildRequires: libacl-devel libattr-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version
%if %with_xscreensaver
BuildRequires: xscreensaver-hacks, xscreensaver-hacks-gl
%endif

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.
This is empty package for compatibility. You don't need them.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kde-common >= 3.2
Conflicts: kdeartwork <= 3.0
Conflicts: kdeartwork-base < 3.2.99
#
%description common
Common empty package for %name

%package styles-phase
Summary: Phase style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-phase-widgets
Provides: kde-styles-phase = %version-%release
Obsoletes: kde-styles-phase <= %version-%release
%description styles-phase
Phase style for KDE

%package styles-phase-widgets
Summary: Phase style for KDE/QT widgets
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-phase-widgets = %version-%release
Obsoletes: kde-styles-phase-widgets <= %version-%release
%description styles-phase-widgets
Phase style for KDE/QT widgets

%package styles-icewm
Summary: IceWM style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-icewm-kwin
Provides: kde-styles-icewm = %version-%release
Obsoletes: kde-styles-icewm <= %version-%release
%description styles-icewm
IceWM style for KDE

%package styles-icewm-kwin
Summary: IceWM style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-icewm-kwin = %version-%release
Obsoletes: kde-styles-icewm-kwin <= %version-%release
%description styles-icewm-kwin
IceWM style for KDE window manager

%package styles-glow
Summary: Glow style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-glow-kwin
Provides: kde-styles-glow = %version-%release
Obsoletes: kde-styles-glow <= %version-%release
%description styles-glow
Glow style for KDE

%package styles-glow-kwin
Summary: Glow style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-glow-kwin = %version-%release
Obsoletes: kde-styles-glow-kwin <= %version-%release
%description styles-glow-kwin
Glow style for KDE window manager

%package styles-riscos
Summary: Risc OS style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-riscos-kwin
Provides: kde-styles-riscos = %version-%release
Obsoletes: kde-styles-glow <= %version-%release
%description styles-riscos
Risc OS style for KDE

%package styles-riscos-kwin
Summary: Risc OS style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-riscos-kwin = %version-%release
Obsoletes: kde-styles-riscos-kwin <= %version-%release
%description styles-riscos-kwin
Risc OS style for KDE window manager

%package styles-cde
Summary: CDE style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-cde-kwin
Provides: kde-styles-cde = %version-%release
Obsoletes: kde-styles-cde <= %version-%release
%description styles-cde
CDE style for KDE

%package styles-cde-kwin
Summary: CDE style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-cde-kwin = %version-%release
Obsoletes: kde-styles-cde-kwin <= %version-%release
%description styles-cde-kwin
CDE style for KDE window manager

%package styles-smoothblend
Summary: Smooth Blend style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-smoothblend-kwin
Provides: kde-styles-smoothblend = %version-%release
Obsoletes: kde-styles-smoothblend <= %version-%release
%description styles-smoothblend
Smooth Blend style for KDE

%package styles-smoothblend-kwin
Summary: Smooth Blend style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-smoothblend-kwin = %version-%release
Obsoletes: kde-styles-smoothblend-kwin <= %version-%release
%description styles-smoothblend-kwin
Smooth Blend style for KDE window manager

%package styles-kde1
Summary: KDE1 style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-kde1-kwin
Provides: kde-styles-kde1 = %version-%release
Obsoletes: kde-styles-kde1 <= %version-%release
%description styles-kde1
KDE1 style for KDE

%package styles-kde1-kwin
Summary: KDE1 style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-kde1-kwin = %version-%release
Obsoletes: kde-styles-kde1-kwin <= %version-%release
%description styles-kde1-kwin
KDE1 style for KDE window manager

%package styles-kstep
Summary: KStep style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-kstep-kwin
Provides: kde-styles-kstep = %version-%release
Obsoletes: kde-styles-kstep <= %version-%release
%description styles-kstep
KStep style for KDE

%package styles-kstep-kwin
Summary: KStep style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-kstep-kwin = %version-%release
Obsoletes: kde-styles-kstep-kwin <= %version-%release
%description styles-kstep-kwin
KStep style for KDE window manager

%package styles-openlook
Summary: OpenLook style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-openlook-kwin
Provides: kde-styles-openlook = %version-%release
Obsoletes: kde-styles-openlook <= %version-%release
%description styles-openlook
OpenLook style for KDE

%package styles-openlook-kwin
Summary: OpenLook style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-openlook-kwin = %version-%release
Obsoletes: kde-styles-openlook-kwin <= %version-%release
%description styles-openlook-kwin
OpenLook style for KDE window manager

%package styles-system
Summary: System style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-system-kwin
Provides: kde-styles-system = %version-%release
Obsoletes: kde-styles-system <= %version-%release
%description styles-system
System style for KDE

%package styles-system-kwin
Summary: System style for KDE window manager
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-system-kwin = %version-%release
Obsoletes: kde-styles-system-kwin <= %version-%release
%description styles-system-kwin
System style for KDE window manager

%package styles-dotnet
Summary: DotNet style for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: %name-styles-dotnet-widgets
Provides: kde-styles-dotnet = %version-%release
Obsoletes: kde-styles-dotnet <= %version-%release
%description styles-dotnet
DotNet style for KDE

%package styles-dotnet-widgets
Summary: DotNet style for KDE/QT widgets
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kde-styles-dotnet-widgets = %version-%release
Obsoletes: kde-styles-dotnet-widgets <= %version-%release
%description styles-dotnet-widgets
DotNet style for KDE/QT widgets

%package sounds
Summary: Additional sounds for KDE
Group: Sound
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: sounds-%name = %version-%release
Obsoletes: sounds-%name <= %version-%release
#
%description sounds
Additional sounds for KDE

%package wallpapers
Summary: Additional wallpapers for KDE
Group: Graphics
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: wallpapers-%name = %version-%release
Obsoletes: wallpapers-%name <= %version-%release
#
%description wallpapers
Additional wallpapers for KDE

%package emoticons
Summary: Emoticon themes for KDE
Group: Graphics
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: emoticons-%name = %version-%release
Obsoletes: emoticons-%name <= %version-%release
#
%description emoticons
Emoticon themes for KDE

%package icon-theme-locolor
Summary: Low-color icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde-icon-theme-locolor = %version-%release
Obsoletes: kde-icon-theme-locolor <= %version-%release
Provides: kdeartwork-locolor = %version-%release
Obsoletes: kdeartwork-locolor <= %version-%release
#
%description icon-theme-locolor
Low-color icons for KDE.
Install this package if you intend to use KDE on a display
that supports 256 or less colors.

%package icon-theme-kdeclassic
Summary: Classic icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde-icon-theme-kdeclassic = %version-%release
Obsoletes: kde-icon-theme-kdeclassic <= %version-%release
#
%description icon-theme-kdeclassic
Classic icons for KDE

%package icon-theme-ikons
Summary: Ikons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde-icon-theme-ikons = %version-%release
Obsoletes: kde-icon-theme-ikons <= %version-%release
#
%description icon-theme-ikons
Ikons for KDE

%package icon-theme-kids
Summary: Kids icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde-icon-theme-kids = %version-%release
Obsoletes: kde-icon-theme-kids <= %version-%release
#
%description icon-theme-kids
Kids icons for KDE

%package icon-theme-slick
Summary: Slick icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde-icon-theme-slick = %version-%release
Obsoletes: kde-icon-theme-slick <= %version-%release
#
%description icon-theme-slick
Slick icons for KDE

%package screensavers
Summary: Additional screensavers for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: kdebase-wm
#
%description screensavers
Additional screensavers for KDE.
kdeartwork-screensavers includes the kbanner, kblob, kbouboule, klorenz,
kmorph3d, kpartsaver, kpipes, kpolygon, kpyro, krock, kscience,
kslidescreen, kslideshow, kspace, kswarm and kvm screensavers.

%package xscreensaver
Summary: Frontend to xscreensaver screensavers
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: kdebase-wm
Requires: xscreensaver-hacks, xscreensaver-hacks-gl
#
%description xscreensaver
This package contains frontend to xscreensaver
to give additional screensavers for KDE.

%package kworldclock
Summary: Themes for KWorldClock
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: kdetoys-kworldclock
#
%description kworldclock
Themes for KWorldClock.

%prep
%setup  -q -nkdeartwork-%version

%patch01

%if %cmake
%else
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
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lDCOP -lkdefx \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

make -f admin/Makefile.common cvs ||:
%endif


%build
export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L/%_qt3dir/lib -L%_libdir -L/%_lib"

#export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
#export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%if %cmake
BD=%_builddir/%name-%version/BUILD

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake \
    -DWITH_XSCREENSAVER=ON \
    -DWITH_LIBART=ON \
    -DWITH_OPENGL=ON \
    -DWITH_ARTS=OFF \
    -DBUILD_ALL=ON
fi
%K3make

%else
# else if cmake

%K3configure \
    --with-extra-includes=%_includedir/tqtinterface \
    --without-arts \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-final

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%endif
# end if cmake

%install
%if %unstable
%set_strip_method none
%endif

%K3install

%if %cmake

make -C BUILD/emoticons DESTDIR=%buildroot install
install -dm 0755 %buildroot/%_K3emo
mv %buildroot/usr/share/kde/share/emoticons/* %buildroot/%_K3emo

make -C BUILD/kscreensaver DESTDIR=%buildroot install
install -dm 0755 %buildroot/%_K3applnk
mv %buildroot/usr/share/kde/share/applnk/* %buildroot/%_K3applnk

install -dm 0755 %buildroot/%_kde3_iconsdir

%endif

[ -d %buildroot/%_K3iconsdir/Locolor -a ! -d %buildroot/%_kde3_iconsdir/locolor ] && \
    mv %buildroot/%_K3iconsdir/Locolor %buildroot/%_kde3_iconsdir/locolor

for iconsdir in %buildroot/%_kde3_iconsdir %buildroot/%_K3iconsdir
do
    pushd $iconsdir
	find . -type d -name .xvpics | while read n; do rm -rf $n; done
	find . -type f -exec chmod a-x {} \;
	find . -type f -name index.theme -exec subst "s/^Inherits\=.*/Inherits=hicolor,default.kde/" {} \;
    popd

    find $iconsdir -type f -name go.png| \
    while read n
    do
	n=`dirname $n`
	ln -s go.png $n/kmenu.png ||:
    done
done


%files
%files common

%files styles-phase
%files styles-phase-widgets
%_K3lib/plugins/styles/phasestyle.so*
%_K3lib/kstyle_phase_config.so*
%_K3apps/kstyle/themes/phase.themerc

%files styles-icewm
%files styles-icewm-kwin
%_K3lib/kwin3_icewm.so*
%_K3lib/kwin_icewm_config.so*
%_K3apps/kwin/icewm-themes/
%_K3apps/kwin/icewm.desktop

%files styles-glow
%files styles-glow-kwin
%_K3lib/kwin3_glow.so*
%_K3lib/kwin_glow_config.so*
%_K3apps/kwin/glow-themes/
%_K3apps/kwin/glow.desktop

%files styles-cde
%files styles-cde-kwin
%_K3lib/kwin3_cde.so*
%_K3lib/kwin_cde_config.so*
%_K3apps/kwin/cde.desktop

%files styles-smoothblend
%files styles-smoothblend-kwin
%_K3lib/kwin3_smoothblend.so*
%_K3lib/kwin_smoothblend_config.so*
%_K3apps/kwin/smoothblend.desktop

%files styles-kde1
%files styles-kde1-kwin
%_K3lib/kwin3_kde1.so*
%_K3apps/kwin/kde1.desktop

%files styles-kstep
%files styles-kstep-kwin
%_K3lib/kwin3_kstep.so*
%_K3apps/kwin/kstep.desktop

%files styles-openlook
%files styles-openlook-kwin
%_K3lib/kwin3_openlook.so*
%_K3apps/kwin/openlook.desktop

%files styles-system
%files styles-system-kwin
%_K3lib/kwin3_system.so*
%_K3apps/kwin/system.desktop

%files styles-riscos
%files styles-riscos-kwin
%_K3lib/kwin3_riscos.so*
%_K3apps/kwin/riscos.desktop

%files styles-dotnet
%files styles-dotnet-widgets
%_K3lib/plugins/styles/dotnet.so*
%_K3apps/kstyle/themes/dotnet.themerc

%files sounds
%_K3snd/*.wav

%files wallpapers
%_K3wall/*.desktop
%_K3wall/*.svgz
%_K3wall/*.jpg
%_K3wall/*.png

%files emoticons
%_K3emo

%files icon-theme-kdeclassic
%_K3iconsdir/kdeclassic

%files icon-theme-ikons
%_K3iconsdir/ikons

%files icon-theme-kids
%_K3iconsdir/kids

%files icon-theme-slick
%_K3iconsdir/slick

%files icon-theme-locolor
%_kde3_iconsdir/locolor

%files screensavers
%_K3bindir/*.kss
%_K3apps/kfiresaver
%_K3apps/kscreensaver/*.png
%_K3applnk/System/ScreenSavers/K*.desktop

%if %with_xscreensaver
%files xscreensaver
%_K3bindir/kxsconfig
%_K3bindir/kxsrun
%_K3applnk/System/ScreenSavers/*.desktop
%exclude %_K3applnk/System/ScreenSavers/K*.desktop
%endif

%files kworldclock
%_K3apps/kworldclock/maps/*

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt2.2
- Removed bad RPATH

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- remove xorg-x11-devel requirement

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Mon Nov 29 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- rebuilt

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Tue Mar 28 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- rebuilt

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Thu Dec 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Tue Oct 25 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt2
- rebuilt with new xscreensaver location

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

* Mon Oct 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Fri Mar 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt2
- fix menufiles

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Mon Mar 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Thu Aug 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- update code from cvs

* Thu May 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update from cvs KDE_3_1_BRANCH

* Mon May 05 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update from cvs KDE_3_1_BRANCH

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update from cvs KDE_3_1_BRANCH

* Tue Jan 28 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update from cvs
- build without extra package

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs

* Thu Nov 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs
- add BlueSphere icons to %{name}-extra

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.11
- fix requires

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update from cvs
- increase release to upgrade Daedalus

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- build with gcc 3.2
- sync patches with cooker

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Fri Aug 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version
- update from cvs

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix menu items

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Mon Apr 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-3mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- fix spec file for 8.0

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Wed Feb 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.4mdk
- Fix BuildRequires on 8.2

* Sat Feb 09 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.3mdk
- Fix ./configure
- Set unstable macro to 1
- Enable debug

* Fri Feb 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- spec file

* Sat Feb 02 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.2mdk
- Rename to allow KDE 2 & 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1-2mdk
- kde 3.0 beta1

* Sat Nov 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

* Wed Nov 15 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2.2-1mdk
- kde 2.2.2

* Thu Oct 25 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2.1-2mdk
- Add support for Mandrake Linux 8.2
- Add Packager: Mandrake Linux KDE Team <kde@mandrakesoft.com>
- Rewrite %%configure steps
- 8.2: enable objprelink

* Thu Sep 18 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2.1-1mdk
- kde 2.2.1

* Fri Sep 14 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-6mdk
- Add description

* Thu Sep 12 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-5mdk
- Fix group name

* Wed Sep 04 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-4mdk
- Add requires kdebase

* Fri Aug 31 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-3mdk
- Rebuild with new kdelibs

* Thu Aug 16 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-2mdk
- Fix generated menu

* Mon Aug 06 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-1mdk
- kde 2.2

* Tue Aug 02 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-0.pre1.1mdk
- kde 2.2 pre 1

* Thu Jun 28 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.beta1.1mdk
- KDE 2.2.beta1
- Clean spec
- Rewrite %%files sections

* Tue Jun 02 2001 Laurent Montel <lmontel@mandrakesoft.com> 2.2-0.alpha2.1mdk
- kde2.2alpha2
