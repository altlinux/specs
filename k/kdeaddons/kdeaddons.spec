%undefine __libtoolize
%define unstable 0
%define _optlevel s
%define _keep_libtool_files 1

%define qtdir %_qt3dir
%def_without knewsticker
%def_without vim
%def_without noatun
%def_without xmms
%def_without atlantik

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libkde

Name: kdeaddons
Version: 3.5.13
Release: alt1.2

Group: Graphical desktop/KDE
Summary: KDE addons
License: GPL

Source0: kdeaddons-%version.tar

# ALT
Patch100: 3.5.12-alt-disable-konq-rellinks.patch
Patch101: 3.5.12-alt-fix-linking.patch
Patch102: 3.5.0-alt-noatun-plugins-fix-linking.patch
Patch103: 3.5.10-alt-fix-compile.patch

Requires: %name-akregator = %version-%release
%if_with atlantik
Requires: %name-atlantik-designer = %version-%release
%endif
Requires: %name-kaddressbook = %version-%release
Requires: %name-kate = %version-%release
Requires: %name-kfile = %version-%release
Requires: %name-kicker = %version-%release
%if_with knewsticker
Requires: %name-knewsticker = %version-%release
%endif
Requires: %name-konqueror = %version-%release
Requires: %name-ksig = %version-%release
%if_with noatun
Requires: %name-noatun = %version-%release
%endif
%if_with vim
Requires: %name-vim = %version-%release
%endif
#Requires: %name-kontact = %version-%release

# Automatically added by buildreq on Mon Apr 12 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs esound fontconfig freetype2 gcc-c++ gcc-g77 glib-devel glib2 gtk+-devel kde-settings kdebase-devel kdebase-konqueror kdebase-libkonq kdebase-wm kdegames-atlantik kdegames-devel kdegames-libs kdelibs-devel kdemultimedia-arts kdemultimedia-devel kdemultimedia-noatun kdepim-devel kdepim-kaddressbook kdepim-kontact kdepim-libs libSDL-devel libarts-devel libarts-qt libjpeg-devel libpng-devel libqt3-devel libstdc++-devel libxmms-devel menu-devel perl-Finance-Quote perl-MIME-tools perl-NNTPClient perl-URI perl-libwww-perl python qt3-designer xml-utils zlib-devel
BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++
#libssl-devel
BuildRequires: kdebase-devel >= %version
BuildRequires: kdemultimedia-devel >= %version kdepim-devel >= %version
BuildRequires: libSDL-devel libjpeg-devel libpng-devel
BuildRequires: libqt3-devel libstdc++-devel menu-devel
BuildRequires: perl-Finance-Quote perl-MIME-tools perl-NNTPClient perl-URI perl-libwww-perl
BuildRequires: qt3-designer xml-utils zlib-devel python
BuildRequires: libacl-devel libattr-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version
BuildRequires: kdebase-devel >= %version
%if_with xmms
BuildRequires: libxmms-devel
%endif
%if_with atlantik
Requires: kdegames-devel >= %version
%endif


%description
Plugins for some KDE applications.
%name extends the functionality of the following applications:
    * Konqueror
%if_with noatun
    * Noatun (media player)
%endif
    * Kate (text editor)
    * Kicker (some applets)
%if_with knewsticker
    * Knewsticker
%endif

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kde-common >= 3.2
Conflicts: kdeaddons <= 3.0
#
%description common
Common empty package for %name

%package akregator
Summary: Plugin for aKregator
Group: Networking/News
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: kdepim-akregator
#
%description akregator
Add Feed to aKregator

%package kaddressbook
Summary: KAB KWorldClock XXPort Plugin
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: kdepim-kaddressbook
#
%description kaddressbook
KAB KWorldClock XXPort Plugin

%package kontact
Summary: KNewsTicker plugin for Kontact
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: kdepim-kontact
#
%description kontact
KNewsTicker plugin for Kontact

%package ksig
Summary: Graphical tool for managing multiple email signatures
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksig
Graphical tool for managing multiple email signatures

%package vim
Summary: Vim component for KDE
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: vim-X11-gtk2
#
%description vim 
The Vim component may need to be configured before it can be used.
This configuration can be done through the KDE Components section
of the KDE Control Center.

%package atlantik-designer
Summary: Designer for atlantik monopoly game client
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description atlantik-designer
This is designer for atlantik - monopoly like game client

%package kate
Summary: Plugins for the Kate text editor
Group: Editors
Requires: %{get_dep kdelibs}
Requires: kdebase-kate
Requires: %name-common = %version-%release
#
%description kate
%name-kate contains plugins extending the functionality of the Kate
(KDE Advanced Text Editor) editor.
%name-kate adds, among other things, DCOP support, project management
and text filtering capabilities.

%package kicker
Summary: Plugins and additional applets for Kicker (the KDE panel)
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: kdebase-wm
Requires: %name-common = %version-%release
#
%description kicker
Plugins and additional applets for Kicker (the KDE panel)

%package kfile
Summary: 	KDE file dialog plugins for text files and folders
Group:		Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: kdebase-konqueror
Requires: %name-common = %version-%release
#
%description kfile
This is a collection of plugins for the KDE file dialog.  These plugins
extend the file dialog to offer advanced meta-information for text,
HTML and desktop files, as well as for folders.
This package is part of the KDE add-ons module.

%package knewsticker
Summary: Scripts extending the functionality of KNewsTicker
Group: Networking/Other
Requires: kdenetwork-knewsticker
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description knewsticker
Scripts extending the functionality of KNewsTicker

%package konqueror
Summary: Plugins extending the functionality of Konqueror
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: kdebase-konqueror
Provides: metabar = 0.8
Obsoletes: metabar < 0.8
#
%description konqueror
Plugins extending the functionality of Konqueror.
%name-konqueror contains, among other things, plugins for translating web
pages, checking web pages for valid HTML code, and viewing the DOM tree of
web pages.

%package noatun
Summary: Plugins extending the functionality of the noatun media player
Group: Sound
Requires: kdemultimedia-noatun
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description noatun
Plugins extending the functionality of the noatun media player

%prep
%setup  -q -nkdeaddons-%version
cp -ar altlinux/admin ./
#
%patch100 -p1
%patch101 -p1
# %patch102 -p1
# %patch103 -p1


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
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lDCOP \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done
for d in kate
do
    find $d -type f -name Makefile.am
done | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lkatepartinterfaces -lktexteditor \2|' $f
done
for d in konq-plugins
do
    find $d -type f -name Makefile.am
done | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= \$(LIB_KUTILS) \$(LIB_KPARTS) \2|' $f
done


make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR%_lib:$KDEDIR%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%if_without knewsticker
DO_NOT_COMPILE+=" knewsticker"
%endif
%if_without noatun
DO_NOT_COMPILE+=" noatun"
%endif
%if_without vim
DO_NOT_COMPILE+=" vim"
%endif
%if_without xmms
DO_NOT_COMPILE+=" xmms"
%endif
%if_without atlantik
DO_NOT_COMPILE+=" atlantik"
%endif
export DO_NOT_COMPILE

%K3configure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-final

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install
%if %unstable
%set_strip_method none
%endif

%K3install
#K3install -C atlantikdesigner


%files
%files common
%_K3cfg/*
%_K3conf/*

%files akregator
%_K3lib/libakregatorkonqfeedicon.*
%_K3lib/libakregatorkonqplugin.*
%_K3apps/akregator/pics/rss.png
%_K3srv/akregator_konqplugin.desktop

%files kaddressbook
%_K3lib/libkaddrbk_geo_xxport.*
%_K3lib/libkaddrbk_gmx_xxport.*
%_K3apps/kaddressbook
%_K3srv/kaddressbook

#%files kontact
#%_K3lib/kcm_kontactknt.*
#%_K3lib/libkontact_newstickerplugin.*
#%_K3srv/kcmkontactknt.desktop
#%_K3srv/kontact

%files ksig
%_K3bindir/ksig
%_K3apps/ksig/ksigui.rc
%_kde3_iconsdir/*/*/apps/ksig.png
%_K3xdg_apps/ksig.desktop
%doc %_K3doc/en/ksig

%if_with vim
%files vim
%_libdir/libxvim.so*
%_K3lib/kcm_vim.*
%_K3lib/libvimpart.*
%_K3apps/kcontrol/pics/kvim.png
%_K3apps/vimpart
%_K3srv/vimpart.desktop
%_K3xdg_apps/kcmvim.desktop
%endif

%if_with atlantik
%files atlantik-designer
%_K3bindir/atlantikdesigner
%_K3apps/atlantikdesigner
%_K3iconsdir/crystalsvg/*/apps/atlantikdesigner.png
%_K3xdg_apps/atlantikdesigner.desktop
%endif

%files kate
#%_K3bindir/dcop_kate
#%_K3bindir/testor
%_K3lib/libkatetabbarextensionplugin.*
%_K3lib/kate*.*
%_K3apps/kate/
%_K3apps/katepart/syntax/katetemplate.xml
%_K3apps/katexmltools
%_K3srv/kate*.desktop
%doc %_K3doc/en/kate-plugins
%_K3applnk/.hidden/katefll.desktop

%files kicker
%_K3lib/math_panelapplet.*
%_K3lib/ktimemon*.*
%_K3lib/kolour*.*
%_K3lib/mediacontrol_panelapplet.*
%_K3lib/kbinaryclock_panelapplet.*
%_K3iconsdir/crystalsvg/*/apps/ktimemon.*
%_kde3_iconsdir/*/*/apps/ktimemon.*
%_K3apps/kicker/applets
%_K3apps/mediacontrol
%doc %_K3doc/en/kicker-applets

%files kfile
%_K3lib/kfile_*.*
%_K3lib/libren*
%_K3srv/kfile_*
%_K3srv/ren*
#%doc %_K3doc/en/kdeaddons-kfile-plugins

%if_with knewsticker
%files knewsticker
%_K3apps/knewsticker/scripts/*
%endif

%files konqueror
%_K3bindir/kio_media_realfolder
%_K3bindir/fsview
%_K3bindir/jpegorient
#%_K3lib/librellinksplugin.*
%_K3lib/libadblock.*
%_K3lib/libsearchbarplugin.*
%_K3lib/libarkplugin.*
%_K3lib/libautorefresh.*
%_K3lib/libbabelfishplugin.*
%_K3lib/libcrashesplugin.*
%_K3lib/libdirfilterplugin.*
%_K3lib/libdomtreeviewerplugin.*
%_K3lib/libfsviewpart.*
%_K3lib/libkhtmlsettingsplugin.*
%_K3lib/libkimgallery.*
%_K3lib/libkuickplugin.*
%_K3lib/libminitoolsplugin.*
%_K3lib/libmfkonqmficon.*
%_K3lib/librsyncplugin.*
%_K3lib/libuachangerplugin.*
%_K3lib/libvalidatorsplugin.*
%_K3lib/libwebarchiverplugin.*
%_K3lib/kcm_kuick.*
%_K3lib/konqsidebar_delicious.*
%_K3lib/konqsidebar_metabar.*
%_K3lib/konq_sidebarnews.*
#%_K3lib/konqsidebar_mediaplayer.*
%_K3lib/webarchivethumbnail.*
%_K3apps/domtreeviewer
%_K3apps/imagerotation/
%_K3apps/imagerotation/exif.py
%_K3apps/imagerotation/orient.py
%_K3apps/fsview
%_K3apps/khtml/kpartplugins
%_K3apps/konqiconview
%_K3apps/konqlistview
%_K3apps/konqsidebartng
%_K3apps/konqueror/kpartplugins
%_K3apps/konqueror/servicemenus
%_K3apps/konqueror/icons/*/*/*/*.*
%_K3apps/metabar/
%_K3apps/microformat/
#%_K3mimelnk/application/*webarchive*.desktop
%_K3srv/ark_plugin.desktop
#%_K3srv/dirfilterplugin.desktop
%_K3srv/fsview_part.desktop
%_K3srv/kuick_plugin.desktop
%_K3srv/webarchivethumbnail.desktop
%_K3iconsdir/crystalsvg/*/actions/babelfish.png
%_K3iconsdir/crystalsvg/*/actions/cssvalidator.png
%_K3iconsdir/crystalsvg/*/actions/domtreeviewer.png
%_K3iconsdir/crystalsvg/*/actions/htmlvalidator.png
%_K3iconsdir/crystalsvg/*/actions/imagegallery.png
%_K3iconsdir/crystalsvg/*/actions/validators.png
%_K3iconsdir/crystalsvg/*/actions/webarchiver.png
%_K3iconsdir/crystalsvg/*/actions/minitools.*
%_kde3_iconsdir/*/*/apps/autorefresh.*
%_kde3_iconsdir/*/*/apps/fsview.png
%_K3iconsdir/crystalsvg/*/apps/konqsidebar_*.png
%_kde3_iconsdir/*/*/apps/metabar.*
%_K3iconsdir/crystalsvg/*/actions/remotesync.*
%_K3iconsdir/crystalsvg/*/actions/remotesyncconfig.*
%_K3applnk/.hidden/arkplugin.desktop
%_K3applnk/.hidden/kcmkuick.desktop
%_K3applnk/.hidden/crashesplugin.desktop
%_K3applnk/.hidden/dirfilterplugin.desktop
%_K3applnk/.hidden/fsview.desktop
%_K3applnk/.hidden/khtmlsettingsplugin.desktop
%_K3applnk/.hidden/kimgalleryplugin.desktop
%_K3applnk/.hidden/kuickplugin.desktop
#%_K3applnk/.hidden/mediaplayerplugin.desktop
%_K3applnk/.hidden/plugin_babelfish.desktop
%_K3applnk/.hidden/plugin_domtreeviewer.desktop
%_K3applnk/.hidden/plugin_validators.desktop
%_K3applnk/.hidden/plugin_webarchiver.desktop
%_K3applnk/.hidden/uachangerplugin.desktop
%_K3applnk/.hidden/rsyncplugin.desktop
%doc %_K3doc/en/konq-plugins
# lnkforward
%_K3bindir/lnkforward
%_K3mimelnk/application/x-win-lnk.desktop
%_K3applnk/.hidden/lnkforward.desktop

%if_with noatun
%files noatun
%_K3bindir/noatun*
%_K3lib/noatun*.*
%_K3apps/noatun/*
#%_K3apps/dub
%_K3iconsdir/crystalsvg/*/apps/synaescope.png
%endif

%changelog
* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.13-alt1.2
- fixed build with recent automake
- restored build with rpm optflags

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt2.2
- Removed bad RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.12-alt2.1.1
- Rebuild with Python-2.7

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- remove xorg-x11-devel requirement

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Mon Nov 29 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Wed Nov 24 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt3
- fix compile
- don't build atlantik designer

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- fix compile with new autotools
- remove deprecated macroses from specfile

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Fri Jul 13 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- build without noatun
- add webarchiver archive filename filtering fix from KUbintu
- spec improvement; thanks morozov@alt

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Tue Mar 27 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- add patch for setup improved http caching

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Tue Jun 27 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt3
- add libssl-devel to BuildRequires

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- bump release to push incoming@ALT

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Tue Jan 10 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- obsolete metabar by %name-konqueror

* Tue Dec 13 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Wed Jun 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Thu May 05 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt2
- fix default icon for searchbar

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Wed Mar 16 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- remove update rellinks plugin

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

* Fri May 14 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt2
- fix ksig description

* Mon Apr 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Wed Mar 10 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Thu Jan 29 2004 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt3
- fix quoting filename in webarchiving

* Fri Dec 05 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- remove *.la files

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Wed Aug 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Tue Jul 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- update code from cvs

* Wed May 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update from cvs KDE_3_1_RELEASE

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update from cvs KDE_3_1_RELEASE
- add MDK patches

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update from cvs KDE_3_1_RELEASE

* Fri Mar 14 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt0.1
- update from cvs KDE_3_1_RELEASE

* Thu Jan 30 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update from cvs KDE_3_1_RELEASE

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs

* Thu Nov 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Tue Oct 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.2
- update from cvs

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- rebuild with gcc 3.2 && objprelink

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix menu items

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-3mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- fix build requires for 8.0

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Mon Feb 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.3mdk
- Fix BuildRequires for 8.2

* Sat Feb 08 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.2mdk
- Fix BuildRequires on 8.0 PPC
- Fix ./configure
- Add missing files
- Set unstable macro to 1

* Thu Feb 07 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-2mdk
- kde 3.0 beta1

* Sat Nov 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0
