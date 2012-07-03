
%define req_design_graphics design-graphics >= 3.1.4
%def_disable kappfinder
%def_disable userpasswd

%add_findpackage_path %_kde4_bindir

%define rname kdebase
%define major 4
%define minor 8
%define bugfix 4
Name: kde4base
Version: %major.%minor.%bugfix
Release: alt2

Group: Graphical desktop/KDE
Summary: K Desktop Environment 4 - Core Files
Url: http://www.kde.org/
License: GPLv2

Requires: %name-dolphin        = %version-%release
%if_enabled kappfinder
Requires: %name-kappfinder     = %version-%release
%endif
Requires: %name-kdepasswd      = %version-%release
Requires: %name-kdialog        = %version-%release
Requires: %name-keditbookmarks = %version-%release
Requires: %name-kfind          = %version-%release
Requires: %name-konqueror      = %version-%release
Requires: kde4-konsole
Requires: kde4-kwrite
Requires: %name-nsplugins      = %version-%release
Requires: %name-plasma-applets = %version-%release

Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.tar
Patch4: kdebase-4.3.3-alt-userpasswd.patch
Patch5: kdebase-4.3.1-alt-nsplugins-paths.patch
Patch6: kdebase-4.8.0-alt-faces-dir.patch
Patch7: kdebase-4.3.0-alt-def-nsplugins.patch
Patch8: kdebase-4.3.3-alt-chfn.patch
Patch9: kdebase-4.3.3-alt-passwd-len.patch
Patch10: kdebase-4.4.1-alt-dolphin-toolbar.patch
Patch11: kdebase-4.4.1-alt-konqueror-toolbar.patch
Patch12: kdebase-4.5.3-alt-dolphin-prefer.patch
Patch13: kdebase-4.7.3-alt-copy-first.patch
# upstream

BuildRequires(pre): kde4libs-devel
BuildRequires: libalternatives-devel
BuildRequires: bzlib-devel gcc-c++ libjpeg-devel libpcre-devel libtidy-devel
BuildRequires: libqimageblitz-devel soprano soprano-backend-redland libsoprano-devel libstrigi-devel
BuildRequires: libungif-devel xml-utils glib2-devel
BuildRequires: kde4libs-devel >= %version
BuildRequires: kde4pimlibs-devel
BuildRequires: kde4base-workspace-devel >= %version
BuildRequires: desktop-file-utils

%description
Core runtime requirements and applications for the K Desktop Environment 4.
This package does not include the KDE 4 versions of applications which are
provided by KDE 3 because of file and configuration setting conflicts.

%package devel
Group: Development/KDE and QT
Summary: Header files for %name
Requires: kde4libs-devel kde4pimlibs-devel kde4-kate-devel
Requires: %name-common = %version-%release
%description devel
Header files for developing applications using %name.

%package common
BuildArch: noarch
Group: Graphical desktop/KDE
Summary: Common files for %name package
Requires: kde-common >= %major.%minor
Conflicts: kdebase-common <= 3.5.12-alt2
%description common
Common files for %name package

%package dolphin
Group: File tools
Summary: The file manager for KDE
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
%description dolphin
Dolphin is a file manager for KDE focusing on usability.
The main features of Dolphin are:
- Navigation bar for URLs, which allows to navigate quickly
     through the file hierarchy.
- View properties are remembered for each folder.
- Split of views is supported.
- Network transparency.
- Undo/redo functionality.
- Renaming of a variable number of selected items in one step.

Dolphin is not intended to be a competitor to Konqueror: Konqueror
acts as universal viewer being able to show HTML pages, text documents,
directories and a lot more, whereas Dolphin focuses on being only a file
manager. This approach allows to optimize the user interface for the task
of file management.

%package kappfinder
Group: Graphical desktop/KDE
Summary: Applications finding tool
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
%description kappfinder
Utility to find applications not included to menu

%package kdepasswd
Group: Graphical desktop/KDE
Summary: User account configuration
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
Requires: shadow-change
%if_enabled userpasswd
Requires: userpasswd
%else
Requires: passwd
%endif
%description kdepasswd
User account configuration

%package kdialog
Group: Graphical desktop/KDE
Summary: Utility to display GUI dialog boxes from shell scripts
Requires: %name-common = %version-%release
%description kdialog
kdialog allows you to display dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%package keditbookmarks
Group: Graphical desktop/KDE
Summary: Utility to edit KDE bookmarks
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
%description keditbookmarks
Utility to edit KDE bookmarks

%package kfind
Group: File tools
Summary: KDE utility to find files
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
%description kfind
KDE utility to find files

%package kinfocenter
Group: Graphical desktop/KDE
Summary: System information center for KDE
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
%description kinfocenter
System information center for KDE

%package konqueror
Group: Networking/WWW
Summary: The file manager and web browser for KDE
PreReq(post,preun): alternatives >= 0.2
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
Requires: indexhtml
#Requires: %req_design_graphics
Provides: webclient %_bindir/xbrowser %_bindir/x-www-browser
Provides: kde4-konqueror-plugins = %version-%release
Obsoletes: kde4-konqueror-plugins < %version-%release
#Provides: kde4-konqueror-plugins-common = %version-%release
#Obsoletes: kde4-konqueror-plugins-common < %version-%release
Provides:  kde4-konqueror-plugins-adblock = %version-%release      kde4-konqueror-plugins-akregator = %version-%release
Obsoletes: kde4-konqueror-plugins-adblock < %version-%release     kde4-konqueror-plugins-akregator < %version-%release
Provides:  kde4-konqueror-plugins-autorefresh = %version-%release  kde4-konqueror-plugins-babelfish = %version-%release
Obsoletes: kde4-konqueror-plugins-autorefresh < %version-%release  kde4-konqueror-plugins-babelfish < %version-%release
Provides:  kde4-konqueror-plugins-dirfilter = %version-%release    kde4-konqueror-plugins-domtreeviewer = %version-%release
Obsoletes: kde4-konqueror-plugins-dirfilter < %version-%release    kde4-konqueror-plugins-domtreeviewer < %version-%release
Provides:  kde4-konqueror-plugins-fsview = %version-%release       kde4-konqueror-plugins-imagerotation = %version-%release
Obsoletes: kde4-konqueror-plugins-fsview < %version-%release       kde4-konqueror-plugins-imagerotation < %version-%release
Provides:  kde4-konqueror-plugins-htmlsettings = %version-%release kde4-konqueror-plugins-imgallery = %version-%release
Obsoletes: kde4-konqueror-plugins-htmlsettings < %version-%release kde4-konqueror-plugins-imgallery < %version-%release
Provides:  kde4-konqueror-plugins-minitools = %version-%release    kde4-konqueror-plugins-rellinks = %version-%release
Obsoletes: kde4-konqueror-plugins-minitools < %version-%release    kde4-konqueror-plugins-rellinks < %version-%release
Provides:  kde4-konqueror-plugins-searchbar = %version-%release    kde4-konqueror-plugins-uachanger = %version-%release
Obsoletes: kde4-konqueror-plugins-searchbar < %version-%release    kde4-konqueror-plugins-uachanger < %version-%release
Provides:  kde4-konqueror-plugins-validators = %version-%release   kde4-konqueror-plugins-webarchiver = %version-%release
Obsoletes: kde4-konqueror-plugins-validators < %version-%release   kde4-konqueror-plugins-webarchiver < %version-%release
%description konqueror
The file manager and web browser easy for use.

%package kwrite
Group: Editors
Summary: Text editor for KDE
Requires: kde4base-runtime-core
Requires: %name-common = %version-%release
%description kwrite
Text editor for KDE

%package nsplugins
Group: Graphical desktop/KDE
Summary: Netscape(R) browser plugins support for KDE
Requires: %name-common = %version-%release
%description nsplugins
Tools used to utilize Netscape(R) browser plugins in KDE

%package plasma-applets
Group: Graphical desktop/KDE
Summary: Plasma applets
Requires: %name-common = %version-%release
Provides: kde4base-plasma < %version-%release
Obsoletes: kde4base-plasma < %version-%release
%description plasma-applets
Various Plasma applets

%package -n libdolphinprivate4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libdolphinprivate4
KDE 4 library.

%package -n libkonq4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
Obsoletes: %name-libkonq < %version-%release
%description -n libkonq4
KDE 4 library.

%package -n libkonqsidebarplugin4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkonqsidebarplugin4
KDE 4 library.

%package -n libkonquerorprivate4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkonquerorprivate4
KDE 4 library.

%package -n libkbookmarkmodel4_private
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkbookmarkmodel4_private
KDE 4 library.

%prep
%setup -q -n %rname-%version
rm -rf runtime workspace
%if_enabled userpasswd
%patch4 -p2
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p2
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

cp -ar altlinux/places plasma/applets/
echo "add_subdirectory(places)" >> plasma/applets/CMakeLists.txt


%build
%K4build \
    -DKDE4_ENABLE_FPIE:BOOL=ON
#    -DKDE4_ENABLE_FINAL:BOOL=ON \

%install
%K4install

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde4-konqueror <<__EOF__
%ifdef _kde4_alternate_placement
%_bindir/xbrowser       %_kde4_bindir/konqueror      40
%_bindir/x-www-browser       %_kde4_bindir/konqueror      40
%else
%_bindir/xbrowser       %_K4bindir/konqueror      60
%_bindir/x-www-browser       %_K4bindir/konqueror      60
%endif
__EOF__

# terminate nspluginviewer
install -d %buildroot/%_sysconfdir/cron.daily/
cat > %buildroot/%_sysconfdir/cron.daily/kde4-nsplugins <<__EOF__
#!/bin/sh
killall nspluginviewer >/dev/null 2>&1 ||:
sleep 3s
killall -9 nspluginviewer >/dev/null 2>&1 ||:
__EOF__
chmod 0755 %buildroot/%_sysconfdir/cron.daily/kde4-nsplugins

# add mime types categories
desktop-file-install --mode=0755 --dir %buildroot%_K4xdg_apps \
    --remove-key=StartupNotification \
    --add-mime-type=x-scheme-handler/http \
    --add-mime-type=x-scheme-handler/https \
    %buildroot%_K4xdg_apps/kfmclient_html.desktop
desktop-file-install --mode=0755 --dir %buildroot%_K4xdg_apps \
    --remove-key=StartupNotification \
    --add-mime-type=x-scheme-handler/ftp \
    --add-mime-type=x-scheme-handler/trash \
    --add-mime-type=x-scheme-handler/network \
    --add-mime-type=x-scheme-handler/remote \
    --add-mime-type=x-scheme-handler/programs \
    --add-mime-type=x-scheme-handler/applications \
    --add-mime-type=x-scheme-handler/desktop \
    %buildroot%_K4xdg_apps/kfmclient_dir.desktop
desktop-file-install --mode=0755 --dir %buildroot%_K4xdg_apps \
    --add-mime-type=x-scheme-handler/ftp \
    --add-mime-type=x-scheme-handler/trash \
    --add-mime-type=x-scheme-handler/network \
    --add-mime-type=x-scheme-handler/remote \
    --add-mime-type=x-scheme-handler/programs \
    --add-mime-type=x-scheme-handler/applications \
    --add-mime-type=x-scheme-handler/desktop \
    %buildroot%_K4xdg_apps/dolphin.desktop
# add desktop categories
desktop-file-install --mode=0755 --dir %buildroot%_K4xdg_apps --add-category=X-PersonalSettings %buildroot%_K4xdg_apps/kdepasswd.desktop

%files
%files common
%_K4tmpl/*.desktop
%_K4tmpl/.source/*
%dir %_K4apps/khtml/kpartplugins
%dir %_K4apps/kwebkitpart
%dir %_K4apps/kwebkitpart/kpartplugins

%files plasma-applets
%_K4lib/plasma_applet_folderview.so
%_K4lib/plasma_applet_places.so
%_K4srv/plasma-applet-folderview.desktop
%_K4srv/plasma-applet-places.desktop

%files dolphin
%_K4bindir/dolphin
%_K4bindir/servicemenudeinstallation
%_K4bindir/servicemenuinstallation
%_K4libdir/libkdeinit4_dolphin.so
%_K4lib/dolphinpart.so*
%_K4lib/kcm_dolphin*.so*
%_K4lib/kio_filenamesearch.so
%_K4xdg_apps/dolphin.desktop
%_K4apps/dolphin/
%_K4apps/dolphinpart/
%_K4srv/dolphinpart.desktop
%_K4srv/kcmdolphin*.desktop
%_K4srv/filenamesearch.protocol
%_K4cfg/dolphin_*.kcfg
%_K4conf/servicemenu.knsrc
%_K4doc/en/dolphin/

%files konqueror
%config /%_sysconfdir/alternatives/packages.d/kde4-konqueror
%_K4bindir/kfmclient
%_K4bindir/konqueror
%_K4libdir/libkdeinit4_kfmclient.so
%_K4libdir/libkdeinit4_konqueror.so
%_K4lib/kcm_history.so
%_K4lib/kcm_kio.so
%_K4lib/kcm_konqhtml.so
%_K4lib/kcm_konq.so
%_K4lib/kcm_kurifilt.so
%_K4lib/kcm_performance.so
%_K4lib/kded_konqy_preloader.so
%_K4lib/khtmlkttsdplugin.so
%_K4lib/konq_aboutpage.so
%_K4lib/konq_shellcmdplugin.so
%_K4lib/konq_sidebar.so
%_K4lib/konq_sidebartree_bookmarks.so
%_K4lib/konq_sidebartree_dirtree.so
%_K4lib/konqsidebar_history.so
%_K4lib/konqsidebar_places.so
%_K4lib/konqsidebar_tree.so
%_K4lib/konqsidebar_web.so
%_K4xdg_apps/Home.desktop
%_K4xdg_apps/kfmclient.desktop
%_K4xdg_apps/kfmclient_dir.desktop
%_K4xdg_apps/kfmclient_html.desktop
%_K4xdg_apps/kfmclient_war.desktop
%_K4xdg_apps/konqbrowser.desktop
%_K4xdg_apps/konquerorsu.desktop
%_K4conf_update/kfmclient_3_2.upd
%_K4conf_update/kfmclient_3_2_update.sh
%_K4apps/kcmcss/
%_K4apps/kcontrol/pics/onlyone.png
%_K4apps/kcontrol/pics/overlapping.png
%_K4apps/khtml/kpartplugins/*
%_K4apps/kwebkitpart/kpartplugins/*
%_K4apps/konqsidebartng/
%_K4apps/konqueror/*
%exclude %_K4apps/konqueror/pics/arrow_*.*
%_K4start/konqy_preload.desktop
%_K4cfg/konqueror.kcfg
%_K4conf/konqsidebartngrc
%_K4iconsdir/hicolor/*/apps/konqueror.*
%_K4srv/cache.desktop
%_K4srv/cookies.desktop
%_K4srv/ebrowsing.desktop
%_K4srv/file*.desktop
%_K4srv/kcmhistory.desktop
%_K4srv/kcmkonqyperformance.desktop
%_K4srv/kcmperformance.desktop
%_K4srv/kded/konqy_preloader.desktop
%_K4srv/khtml_*.desktop
%exclude %_K4srv/khtml_plugins.desktop
%_K4srv/konq*.desktop
%_K4srv/netpref.desktop
%_K4srv/proxy.desktop
%_K4srv/smb.desktop
%_K4srv/useragent.desktop
%_K4srv/useragentstrings/
%_K4srvtyp/fileviewversioncontrolplugin.desktop
%_K4srvtyp/konqaboutpage.desktop
%_K4srvtyp/konqdndpopupmenuplugin.desktop
%_K4srvtyp/uasprovider.desktop
%_K4doc/en/konqueror/
#
%_K4lib/kded_favicons.so*
%_K4lib/konq_sound.so*
%_K4apps/kbookmark/directory_bookmarkbar.desktop
%_K4conf_update/favicons.upd
%_K4conf_update/move_favicons.sh
%dir %_K4apps/konqueror/
%dir %_K4apps/konqueror/pics/
%_K4apps/konqueror/pics/arrow_*.*
%_K4srv/kded/favicons.desktop
%_K4srvtyp/konqpopupmenuplugin.desktop
# konq-plugins
%_K4bindir/fsview
%_K4lib/adblock.so
%_K4lib/akregatorkonqfeedicon.so
%_K4lib/autorefresh.so
%_K4lib/babelfishplugin.so
%_K4lib/dirfilterplugin.so
%_K4lib/domtreeviewerplugin.so
%_K4lib/fsviewpart.so
%_K4lib/khtmlsettingsplugin.so
%_K4lib/kimgallery.so
%_K4lib/minitoolsplugin.so
%_K4lib/rellinksplugin.so
%_K4lib/searchbarplugin.so
%_K4lib/uachangerplugin.so
%_K4lib/validatorsplugin.so
%_K4lib/webarchiverplugin.so
%_K4lib/webarchivethumbnail.so
%_K4iconsdir/hicolor/*/apps/fsview.*
%_K4iconsdir/oxygen/*/actions/babelfish.*
%_K4iconsdir/oxygen/*/actions/cssvalidator.*
%_K4iconsdir/oxygen/*/actions/htmlvalidator.*
%_K4iconsdir/oxygen/*/actions/imagegallery.*
%_K4iconsdir/oxygen/*/actions/validators.*
%_K4iconsdir/oxygen/*/actions/webarchiver.*
%_K4apps/akregator/pics/feed.png
%_K4apps/domtreeviewer
%_K4apps/fsview
%_K4cfg/validators.kcfg
%_K4conf/translaterc
%_K4srv/ServiceMenus/imageconverter.desktop
%_K4srv/fsview_part.desktop
%_K4srv/webarchivethumbnail.desktop

%if_enabled kappfinder
%files kappfinder
%_K4bindir/kappfinder
%_K4xdg_apps/kappfinder.desktop
%_K4apps/kappfinder/
%_K4iconsdir/hicolor/*/apps/kappfinder.*
#
%_K4iconsdir/oxygen/*/apps/abiword.*
%_K4iconsdir/oxygen/*/apps/aim.*
%_K4iconsdir/oxygen/*/apps/alevt.*
%_K4iconsdir/oxygen/*/apps/antivirus.*
%_K4iconsdir/oxygen/*/apps/applixware.*
%_K4iconsdir/oxygen/*/apps/assistant.*
%_K4iconsdir/oxygen/*/apps/blender.*
%_K4iconsdir/oxygen/*/apps/bluefish.*
%_K4iconsdir/oxygen/*/apps/browser.*
%_K4iconsdir/oxygen/*/apps/camera.*
%_K4iconsdir/oxygen/*/apps/clanbomber.*
%_K4iconsdir/oxygen/*/apps/clock.*
%_K4iconsdir/oxygen/*/apps/core.*
%_K4iconsdir/oxygen/*/apps/designer.*
%_K4iconsdir/oxygen/*/apps/dia.*
%_K4iconsdir/oxygen/*/apps/display.*
%_K4iconsdir/oxygen/*/apps/download_manager.*
%_K4iconsdir/oxygen/*/apps/eclipse.*
%_K4iconsdir/oxygen/*/apps/emacs.*
%_K4iconsdir/oxygen/*/apps/email.*
%_K4iconsdir/oxygen/*/apps/evolution.*
%_K4iconsdir/oxygen/*/apps/gabber.*
%_K4iconsdir/oxygen/*/apps/gaim.*
%_K4iconsdir/oxygen/*/apps/galeon.*
%_K4iconsdir/oxygen/*/apps/gimp.*
%_K4iconsdir/oxygen/*/apps/gnomemeeting.*
%_K4iconsdir/oxygen/*/apps/gnucash.*
%_K4iconsdir/oxygen/*/apps/gnumeric.*
%_K4iconsdir/oxygen/*/apps/gv.*
%_K4iconsdir/oxygen/*/apps/gvim.*
%_K4iconsdir/oxygen/*/apps/licq.*
%_K4iconsdir/oxygen/*/apps/linguist.*
%_K4iconsdir/oxygen/*/apps/lyx.*
%_K4iconsdir/oxygen/*/apps/netscape.*
%_K4iconsdir/oxygen/*/apps/opera.*
%_K4iconsdir/oxygen/*/apps/pan.*
%_K4iconsdir/oxygen/*/apps/penguin.*
%_K4iconsdir/oxygen/*/apps/personal.*
%_K4iconsdir/oxygen/*/apps/pinguin.*
%_K4iconsdir/oxygen/*/apps/plan.*
%_K4iconsdir/oxygen/*/apps/planner.*
%_K4iconsdir/oxygen/*/apps/pybliographic.*
%_K4iconsdir/oxygen/*/apps/realplayer.*
%_K4iconsdir/oxygen/*/apps/shell.*
%_K4iconsdir/oxygen/*/apps/sodipodi.*
%_K4iconsdir/oxygen/*/apps/staroffice.*
%_K4iconsdir/oxygen/*/apps/terminal.*
%_K4iconsdir/oxygen/*/apps/tux.*
%_K4iconsdir/oxygen/*/apps/wp.*
%_K4iconsdir/oxygen/*/apps/xawtv.*
%_K4iconsdir/oxygen/*/apps/xcalc.*
%_K4iconsdir/oxygen/*/apps/xchat.*
%_K4iconsdir/oxygen/*/apps/xclipboard.*
%_K4iconsdir/oxygen/*/apps/xclock.*
%_K4iconsdir/oxygen/*/apps/xedit.*
%_K4iconsdir/oxygen/*/apps/xemacs.*
%_K4iconsdir/oxygen/*/apps/xeyes.*
%_K4iconsdir/oxygen/*/apps/xfig.*
%_K4iconsdir/oxygen/*/apps/xfmail.*
%_K4iconsdir/oxygen/*/apps/xload.*
%_K4iconsdir/oxygen/*/apps/xmag.*
%_K4iconsdir/oxygen/*/apps/xmms.*
%_K4iconsdir/oxygen/*/apps/xosview.*
%_K4iconsdir/oxygen/*/apps/xpaint.*
%_K4iconsdir/oxygen/*/apps/xv.*
#%_K4doc/en/kappfinder/
%endif

%files kdepasswd
%_K4lib/kcm_useraccount.so*
%_K4cfg/kcm_useraccount.kcfg
%_K4srv/kcm_useraccount.desktop
%_K4cfg/kcm_useraccount_pass.kcfg
%if_enabled userpasswd
%else
%_K4bindir/kdepasswd
%_K4xdg_apps/kdepasswd.desktop
%_K4doc/en/kdepasswd
%endif

%files kdialog
%_K4bindir/kdialog

%files keditbookmarks
%_K4bindir/kbookmarkmerger
%_K4bindir/keditbookmarks
%_K4libdir/libkdeinit4_keditbookmarks.so
%_K4xdg_apps/keditbookmarks.desktop
%_K4apps/keditbookmarks/
%_K4cfg/keditbookmarks.kcfg
%_K4srv/bookmarks.desktop
%_man1dir/kbookmarkmerger.*

%files kfind
%_K4bindir/kfind
#%_K4lib/libkfindpart.so
%_K4xdg_apps/kfind.desktop
%_K4iconsdir/hicolor/*/apps/kfind.*
#%_K4srv/kfindpart.desktop
#%_K4srvtyp/findpart.desktop
%_K4doc/en/kfind/
%_man1dir/kfind.*

%files nsplugins
%config(noreplace) %_sysconfdir/cron.daily/kde4-nsplugins
%_K4bindir/nspluginscan
%_K4bindir/nspluginviewer
%_K4lib/libkcminit_nsplugins.so
%_K4lib/libnsplugin.so
%_K4apps/nsplugin/
%_K4srv/khtml_plugins.desktop

%files -n libdolphinprivate4
%_K4libdir/libdolphinprivate.so.*

%files -n libkonq4
%_K4libdir/libkonq.so.*

%files -n libkonqsidebarplugin4
%_K4libdir/libkonqsidebarplugin.so.*

%files -n libkonquerorprivate4
%_K4libdir/libkonquerorprivate.so.*

%files -n libkbookmarkmodel4_private
%_K4libdir/libkbookmarkmodel_private.so.*

%files devel
%_K4link/lib*.so
%_K4includedir/*
%_K4dbus_interfaces/*
###
%exclude %_K4apps/kdm/pics/users/*


%changelog
* Thu Jun 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Thu Jan 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version
- add x-www-browser alternative

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Wed Nov 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Mon Nov 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- move "copy" item upper then "move" in popups

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Mon Sep 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1.M60P.1
- built for M60P

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- add more x-scheme-handler-s

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt0.M60P.1
- built for M60P

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt0.M60P.1
- built for M60P

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- fix build requires

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Tue Mar 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- fix conflict with kde4-konqueror-plugins-common

* Tue Mar 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Fri Feb 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- move to standart place

* Fri Jan 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Fri Nov 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt2
- prefer dolphin to open inode/directory

* Tue Nov 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Fri Oct 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt2
- move templates to common subpackage

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Wed Aug 04 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Fri Jun 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1.M51.1
- built for M51

* Fri Jun 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- allow to drop files onto places widget

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Sat May 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Thu Mar 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt3
- add root profile to konsole

* Wed Mar 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt2
- add usable buttons to dolphin and konqueror toolbars by default

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Wed Jan 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Thu Nov 26 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.2
- built for M51

* Thu Nov 26 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt2
- turn off userpasswd support

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Mon Nov 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Thu Oct 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt4
- fix default netscape plugins search paths

* Thu Sep 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt3
- fix allow keys on numpad to work with numlock off (svn r925604) (ALT#20709)

* Thu Sep 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- add konsole part detection patch (ALT#21368)

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Thu Aug 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- denice nspluginviewer by default
- terminate nspluginviewer nightly

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Thu Jul 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- fix default user faces dir

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Mon May 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- fix netscape plugins defaut search paths
- add some upstram fixes

* Fri Apr 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Wed Mar 25 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt3
- fix konsole double-clicking selection

* Tue Mar 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt2
- use konsole color scheme Linux by default
- don't harcode Shift+Arrow keys (https://bugs.kde.org/show_bug.cgi?id=59256)

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Jan 15 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- remove deprecated macroses from specfile

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Mon Oct 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Thu Sep 04 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Thu Jul 31 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Wed May 28 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Mon Apr 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt2
- use userpasswd instead of kdepasswd

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Tue Mar 11 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt3
- clean requires

* Fri Mar 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt2
- fix build requires

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- new version

* Mon Feb 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- built for ALT

