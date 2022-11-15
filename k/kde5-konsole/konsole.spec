%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define rname konsole

%_K5if_ver_gteq %ubt_id M100
%def_enable obsolete_kde4
%else
%def_disable obsolete_kde4
%endif

%define sover 1
%define libkonsoleprivate libkonsoleprivate%sover
%define libkonsoleapp libkonsoleapp%sover

Name: kde5-%rname
Version: 22.08.3
Release: alt2
%K5init %{?_enable_obsolete_kde4:no_altplace} %{?_enable_obsolete_kde4:appdata}%{!?_enable_obsolete_kde4:no_appdata}

Group: Terminals
Summary: Terminal emulator for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires(post,preun): alternatives >= 0.2
Provides: xvt, %_x11bindir/xvt
#Requires: fonts-bitmap-misc
%if_enabled obsolete_kde4
Provides: kde4-konsole = %version-%release
Obsoletes: kde4-konsole < %version-%release
%endif

Source: %rname-%version.tar
Source10: profiles.tar
Patch12: alt-def-font.patch
Patch13: alt-def-colors.patch
Patch14: alt-fix-empty-profile.patch
Patch15: alt-disable-colorfilter.patch
Patch16: alt-new-tab-button.patch

# Automatically added by buildreq on Mon Apr 27 2015 (-bi)
# optimized out: alternatives cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdb4-devel libxkbfile-devel python-module-google qt5-script-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: libalternatives-devel
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-script-devel
BuildRequires: libdb4-devel zlib-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-sonnet-devel kf5-knewstuff-devel kf5-kglobalaccel-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel
BuildRequires: libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel

%description
As well as being a standalone program, it is also used by other KDE programs
such as the Kate editor and KDevelop development environment to provide easy
access to a terminal window. Konsole's features and usage are explained and
illustrated in the Konsole handbook, which can be accessed by browsing to
"help:/konsole" in Konqueror.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkonsoleprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkonsoleprivate
%name library

%package -n %libkonsoleapp
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkonsoleapp
%name library

%prep
%setup -q -n %rname-%version -a10
#patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
%K5build \
%if_disabled obsolete_kde4
    -DDATA_INSTALL_DIR=%_K5data \
%endif
    #

%install
%K5install
%if_disabled obsolete_kde4
%K5install_move data konsole khotkeys knsrcfiles kio kconf_update
%endif

# install profiles
KONSOLE_DATA_DIR=%buildroot/%_K5data/konsole/
%if_enabled obsolete_kde4
KONSOLE_DATA_DIR=%buildroot/%_datadir/konsole/
%endif
for f in profiles/*.profile ; do
    install -m 0644 $f $KONSOLE_DATA_DIR
done

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde5-konsole <<__EOF__
%_x11bindir/xvt %_K5bin/konsole        55
%_x11bindir/x-terminal-emulator %_K5bin/konsole        55
__EOF__

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories5/*.*categories

%files
%config %_sysconfdir/alternatives/packages.d/kde5-konsole
# konsole may problems for some reasons because sgid
#%attr(2711,root,utempter) %_K5bin/konsole
%_K5bin/konsole
%_K5bin/konsoleprofile
%_K5conf_bin/konsole_globalaccel
%_K5plug/konsole*.so
%_K5plug/konsoleplugins/
%_K5xdgapp/org.kde.konsole.desktop
%if_enabled obsolete_kde4
%_datadir/konsole/
%_datadir/kio/servicemenus/konsolerun.desktop
%_datadir/kconf_update/konsole_globalaccel.upd
%else
%_K5data/kio/servicemenus/konsolerun.desktop
%_K5data/konsole/
%_K5conf_up/konsole_globalaccel.upd
%endif
%_K5srv/*.desktop
%_K5srvtyp/*.desktop
%_K5notif/*
%if_enabled obsolete_kde4
%_datadir/knsrcfiles/*konsole*
%else
%_K5data/knsrcfiles/*konsole*
%endif
%if_enabled obsolete_kde4
%_datadir/metainfo/org.kde.konsole*.*.xml
%endif

%files -n %libkonsoleprivate
%_K5lib/libkonsoleprivate.so.*
%_K5lib/libkonsoleprivate.so.%sover

%files -n %libkonsoleapp
%_K5lib/libkonsoleapp.so.*
%_K5lib/libkonsoleapp.so.%sover

%changelog
* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt2
- add alternative for x-terminal-emulator

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Fri Feb 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt3
- update russian translation

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- improve New Tab button appearance

* Mon Jan 17 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Fri Dec 17 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt4
- update default color theme

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt3
- don't disable transparency by default
- add root shell profile by default
- don't increase default font size

* Mon Nov 29 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt2
- fix tranparency option description

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt2
- disable color filter by default

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 22 2021 Oleg Solovyov <mcpain@altlinux.org> 21.04.3-alt2
- fix empty profile when ran from desktop action

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Mon Jul 05 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt2
- resolve duplicate provides

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Mon May 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt2
- obsolete kde4-konsole

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Thu Jan 14 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Fri Dec 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Thu Nov 21 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt2
- change default colors to WhiteOnBlack

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Wed Jul 17 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt3
- don't use utempter

* Thu Jul 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt2
- using utempter

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Mon Aug 21 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt2
- fix tabdrag (ALT#33507)

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Wed Jul 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt2
- set Monospace font by default to scale with hi resolution
- intense bold fonts by default

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Thu Jan 12 2017 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt2
- update code from upstream

* Thu Nov 24 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt3
- add upstream fix for KDEBUG#367746

* Fri Sep 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt2
- disable kcrash

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Sep 08 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt2
- don't intense bold fonts by default

* Tue Sep 06 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version
- use Fixed font instead of Terminus by default

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Fri Dec 25 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt2
- fix default font

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Fri Dec 11 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt2
- set Terminus font by default

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Mon Sep 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt2
- disable transparency by default
- add profile entry for root

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Jun 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt1
- new version

* Mon Apr 27 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- initial build
