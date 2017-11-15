%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%def_disable kworldclock
%def_enable icons
%def_enable emoticons
%def_enable wallpapers
%def_disable icewm
%ifarch %arm
# do not bother the universe trying to build 3d screensavers with GLES-flavoured qt
%def_disable screensavers3d
%else
%def_enable screensavers3d
%endif

%define rname kdeartwork
%define major 4
%define minor 14
%define bugfix 0
Name: kde4artwork
Version: %major.%minor.%bugfix
Release: alt3

Summary: K Desktop Environment - Artwork
Group: Graphical desktop/KDE
License: GPL
Url: http://www.kde.org

%if_enabled kworldclock
Requires: %name-kworldclock = %version-%release
%endif
%if_enabled emoticons
Requires: %name-emoticons = %version-%release
%endif
Requires: %name-desktopthemes = %version-%release
%if_enabled icewm
Requires: %name-styles-icewm-kwin = %version-%release
%endif
Requires: %name-styles-kde2-kwin = %version-%release
Requires: %name-styles-keramik-kwin = %version-%release
Requires: %name-styles-modernsystem-kwin = %version-%release
Requires: %name-styles-quartz-kwin = %version-%release
Requires: %name-styles-redmond-kwin = %version-%release
Requires: %name-styles-web-kwin = %version-%release
Requires: %name-screensavers = %version-%release
Requires: %name-screensavers3d = %version-%release
Requires: %name-sounds = %version-%release
Requires: %name-styles-phase-widgets = %version-%release
%if_enabled wallpapers
Requires: %name-wallpapers = %version-%release
%endif
Requires: %name-color-schemes = %version-%release
%if_enabled icons
Requires: %name-icon-theme-nuvola = %version-%release
Requires: %name-icon-theme-mono = %version-%release
%endif


Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar


BuildRequires(pre): kde4base-workspace-devel
BuildRequires: gcc-c++ eigen3 icon-naming-utils
BuildRequires: kde4base-workspace-devel kde4libs-devel >= %version kde4graphics-devel

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%package common
Summary: Common package for %name
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kde-common >= %major.%minor
%description common
Common package for %name

%package emoticons
Summary: %name emoticon themes
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
%description emoticons
Emoticon themes for KDE

%package desktopthemes
Summary: %name desktop theme
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: kde4base-workspace-core
Provides: plasma-desktoptheme-aya = %version-%release
Obsoletes: plasma-desktoptheme-aya < %version-%release
Provides: plasma-desktoptheme-clean-blend = %version-%release
Obsoletes: plasma-desktoptheme-clean-blend < %version-%release
Provides: plasma-desktoptheme-elegance = %version-%release
Obsoletes: plasma-desktoptheme-elegance < %version-%release
Provides: plasma-desktoptheme-heron = %version-%release
Obsoletes: plasma-desktoptheme-heron < %version-%release
Provides: plasma-desktoptheme-silicon = %version-%release
Obsoletes: plasma-desktoptheme-silicon < %version-%release
Provides: plasma-desktoptheme-slim-glow = %version-%release
Obsoletes: plasma-desktoptheme-slim-glow < %version-%release
%description desktopthemes
Desktop themes for KDE

%package screensavers
Summary: Sreensavers for KDE4
Group: Graphical desktop/KDE
Requires: kde4base-workspace-core
Requires: %name-common = %version-%release
Provides: kscreensaver4-asciiquarium = %version-%release
Obsoletes: kscreensaver4-asciiquarium < %version-%release
%description screensavers
Screensavers for KDE

%package screensavers3d
Summary: Additional screensavers for KDE4 with OpenGL support
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: %name-screensavers
Requires: kde4base-workspace-core
%description screensavers3d
Additional screensavers for KDE with OpenGL support

%package kworldclock
Summary: %name themes for KWorldClock
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: kde4toys-kworldclock
%description kworldclock
Themes for KWorldClock

%package sounds
Summary: Additional sounds for KDE4
Group: Sound
BuildArch: noarch
Requires: %name-common = %version-%release
%description sounds
Additional sounds for KDE

%package color-schemes
Summary: Color schemes for KDE4
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Conflicts: kde4accessibility-core < 4.7
%description color-schemes
Color schemes for KDE

%package wallpapers
Summary: Additional wallpapers for KDE4
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
%description wallpapers
Additional wallpapers for KDE

%package styles-kde2-kwin
Summary: KDE4 window manager style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description styles-kde2-kwin
KDE4 window manager style

%package styles-keramik-kwin
Summary: KDE4 window manager style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description styles-keramik-kwin
KDE4 window manager style

%package styles-modernsystem-kwin
Summary: KDE4 window manager style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description styles-modernsystem-kwin
KDE4 window manager style

%package styles-quartz-kwin
Summary: KDE4 window manager style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description styles-quartz-kwin
KDE4 window manager style

%package styles-redmond-kwin
Summary: KDE4 window manager style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description styles-redmond-kwin
KDE4 window manager style

%package styles-web-kwin
Summary: KDE4 window manager style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description styles-web-kwin
KDE4 window manager style

%package styles-icewm-kwin
Summary: %name IceWM style for KDE4 window manager
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: kde4-styles-icewm-kwin = %version-%release
Obsoletes: kde4-styles-icewm-kwin <= %version-%release
%description styles-icewm-kwin
IceWM style for KDE window manager

%package styles-phase-widgets
Summary: Phase style for KDE4 widgets
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: kde4-styles-phase-widgets = %version-%release
Obsoletes: kde4-styles-phase-widgets <= %version-%release
%description styles-phase-widgets
Phase style for KDE/QT widgets

%package icon-theme-nuvola
Summary: Nuvola icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde4-icon-theme = %version-%release
Provides: icon-theme-nuvola = %version-%release
Obsoletes: icon-theme-nuvola <= %version-%release
Provides: kde-icon-theme-nuvola = %version-%release
Obsoletes: kde-icon-theme-nuvola <= %version-%release
Provides: kde4-icon-theme-nuvola = %version-%release
Obsoletes: kde4-icon-theme-nuvola <= %version-%release
%description icon-theme-nuvola
Nuvola icons for KDE

%package icon-theme-primary
Summary: Primary icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: kde4-icon-theme = %version-%release
Provides: icon-theme-primary = %version-%release
Obsoletes: icon-theme-primary <= %version-%release
Provides: kde-icon-theme-primary = %version-%release
Obsoletes: kde-icon-theme-primary <= %version-%release
Provides: kde4-icon-theme-primary = %version-%release
Obsoletes: kde4-icon-theme-primary <= %version-%release
%description icon-theme-primary
Primary icons for KDE

%package icon-theme-mono
Summary: Mono icons for KDE
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %version-%release
Conflicts: kde4accessibility-core < 4.7
Provides: kde4-icon-theme = %version-%release
Provides: icon-theme-mono = %version-%release
Obsoletes: icon-theme-mono <= %version-%release
Provides: kde-icon-theme-mono = %version-%release
Obsoletes: kde-icon-theme-mono <= %version-%release
Provides: kde4-icon-theme-mono = %version-%release
Obsoletes: kde4-icon-theme-mono <= %version-%release
Provides: kdeaccessibility-icon-theme-mono = %version-%release
Provides: kdeaccessibility-icon-theme-mono = 3.5.12-alt2.1
Obsoletes: kdeaccessibility-icon-theme-mono <= %version-%release
%description icon-theme-mono
Mono icons for KDE

%prep
%setup -q -n %rname-%version
%if_disabled screensavers3d
sed -i 's,^if(OPENGL_FOUND AND OPENGL_GLU_FOUND AND QT_QTOPENGL_LIBRARY),if(0),' \
	kscreensaver/kdesavers/CMakeLists.txt
%endif

%build
%K4build \
    -DICON_INSTALL_DIR=%_K4iconsdir

%install
%K4install

# list scrinsavers
>lst.screensavers3d
>lst.screensavers
find %buildroot/%_K4srv/ScreenSavers -type f -name \*desktop | \
while read f
do
    NAME=`basename $f`
    EXEC=`grep 'Exec=' $f | head -n 1 | sed -e 's|.*=||' -e 's|[[:space:]].*||'`
    LIST=lst.screensavers
    if echo "$NAME" | grep -q -e "^K" -e "kpartsaver" -e "asciiquarium"; then
	if grep -q 'X-KDE-Type=OpenGL' $f; then
	    LIST=lst.screensavers3d
	else
	    LIST=lst.screensavers
	fi
    else
	echo "Unknown screensaver $NAME !!!!!!!"
	LIST=/dev/null
    fi
    echo "%%_K4srv/ScreenSavers/$NAME" >> $LIST
    echo "$EXEC" | grep -q -e '\.kss$' \
	&& echo "%%_kde4_bindir/$EXEC" >> $LIST
done

# fix icons
for n in nuvola mono
do
    pushd %buildroot/%_K4iconsdir/$n
    if grep -q "^Inherits=" index.theme; then
	sed -i "s|Inherits=.*|Inherits=oxygen,hicolor|" index.theme
    else
	sed -i "s|DisplayDepth=\(.*\)|Inherits=oxygen,hicolor\nDisplayDepth=\1|" index.theme
    fi
    find ./ -type f -name go.png| \
    while read i
    do
	n=`dirname $i`
	[ -e $n/kmenu.png ] \
	    || ln -s go.png $n/kmenu.png
    done
    popd
done

for n in nuvola mono
do
    pushd %buildroot/%_iconsdir/$n
    for sz in 16x16 22x22 32x32 48x48 64x64 128x128 256x256 scalable
    do
	if [ -d $sz ]; then
	    pushd $sz
	    for ctx in `ls -1`; do
		[ -d $ctx ] \
		    && %_libexecdir/icon-name-mapping -c $ctx
	    done
	    popd
	fi
    done
    popd
done




%files
%files common
%doc README

%if_enabled emoticons
%files emoticons
%_K4emo/*
%else
%exclude %_K4emo/*
%endif

%files desktopthemes
%_K4apps/desktoptheme/*

%if_enabled icewm
%files styles-icewm-kwin
%_K4apps/kwin/icewm-themes/*
%endif

%files styles-phase-widgets
%_K4apps/kstyle/themes/phase.themerc
%_K4lib/kstyle_phase_config.so
%_K4lib/plugins/styles/phasestyle.so

%files styles-kde2-kwin
%_K4lib/kwin3_kde2.so
%_K4lib/kwin_kde2_config.so
%_K4apps/kwin/kde2.desktop

%files styles-keramik-kwin
%_K4lib/kwin3_keramik.so
%_K4lib/kwin_keramik_config.so
%_K4apps/kwin/keramik.desktop

%files styles-modernsystem-kwin
%_K4lib/kwin3_modernsys.so
%_K4lib/kwin_modernsys_config.so
%_K4apps/kwin/modernsystem.desktop

%files styles-quartz-kwin
%_K4lib/kwin3_quartz.so
%_K4lib/kwin_quartz_config.so
%_K4apps/kwin/quartz.desktop

%files styles-redmond-kwin
%_K4lib/kwin3_redmond.so
%_K4apps/kwin/redmond.desktop

%files styles-web-kwin
%_K4lib/kwin3_web.so
%_K4apps/kwin/web.desktop

%files screensavers -f lst.screensavers
%_K4apps/kfiresaver/
%_K4apps/kscreensaver/

%files screensavers3d -f lst.screensavers3d

%if_enabled kworldclock
%files kworldclock
%_K4apps/kworldclock/maps/*
%else
#%exclude %_K4apps/kworldclock/maps/*
%endif

%files sounds
#%_K4snd/KDE_Logout_new.wav
#%_K4snd/KDE_Startup_new.wav

%files color-schemes
%_K4apps/color-schemes/

%if_enabled wallpapers
%files wallpapers
%_K4wall/*
%else
%exclude %_K4wall/*
%endif

%if_enabled icons
%files icon-theme-nuvola
%_K4iconsdir/nuvola/
%files icon-theme-mono
%_K4iconsdir/mono/
%else
%exclude %_kde4_iconsdir/*
%endif

%changelog
* Wed Nov 15 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.0-alt3
- do not build 3d screensavers on GLES-flavoured qt

* Tue Nov 14 2017 Oleg Solovyov <mcpain@altlinux.org> 4.14.0-alt2
- fix build

* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Wed Dec 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1.M60P.1
- built for M60P

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix provides

* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Thu Jun 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- fix build requires

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Thu Nov 04 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1.M51.1
- built for M51

* Mon Jul 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt2
- package icons, wallpapers

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Tue May 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Fri Oct 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Wed Jan 21 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt2
- rebuilt

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Thu Sep 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Thu May 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Mon Apr 21 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- initial build

