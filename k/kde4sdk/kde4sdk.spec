
%add_findpackage_path %_K4bindir
%add_findreq_skiplist %_K4apps/lokalize/scripts/*.py
%add_findreq_skiplist %_K4bindir/kdedoc

%define rname kdesdk
Name: kde4sdk
%define major 4
%define minor 8
%define bugfix 4
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Software Development Kit
License: GPL
Url: ftp://ftp.kde.org/pub/kde/stable/%version/src/
Packager: Sergey V Turchin <zerg at altlinux dot org>

Requires: %name-core = %version-%release
Requires: %name-lokalize = %version-%release
Requires: %name-kapptemplate = %version-%release
Requires: %name-kuiviewer = %version-%release
Requires: %name-scripts = %version-%release
#Requires: %name-kbugbuster = %version-%release
Requires: %name-strigi-analyzer = %version-%release
Requires: %name-po2xml = %version-%release
Requires: %name-umbrello = %version-%release
Requires: %name-cervisia = %version-%release
Requires: %name-kompare = %version-%release
Requires: %name-kmtrace = %version-%release
Requires: %name-kcachegrind = %version-%release
Requires: %name-dolphin = %version-%release
Requires: %name-okteta = %version-%release


Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
Patch1: kdesdk-4.0.2-alt-find-libsvn.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: libsubversion-devel perl-XML-DOM perl-Switch libldap-devel libltdl-devel gcc-c++
BuildRequires: libiberty-devel libjpeg-devel libxslt-devel bzlib-devel
BuildRequires: boost-devel libhunspell-devel desktop-file-utils
BuildRequires: kde4libs-devel >= %version kde4base-devel
BuildRequires: kde4pimlibs-devel >= %version
BuildRequires: kde4base-workspace-devel >= %version
BuildRequires: perl-Pod-Parser

%description
Software Development Kit for the K Desktop Environment.

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdesdk-common <= 3.5.12-alt1
%description common
Common empty package for %rname

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files needed for %rname

%package okteta
Summary: Byte level data editor
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Provides: kde4utils-okteta = %version-%release
Obsoletes: kde4utils-okteta < %version-%release
%description okteta
Viewing and editing of data on the byte level

%package -n libokteta1core4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libokteta1core4
KDE 4 library

%package -n libokteta1gui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libokteta1gui4
KDE 4 library

%package -n libkasten1okteta1controllers4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten1okteta1controllers4
KDE 4 library

%package -n libkasten1okteta1core4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten1okteta1core4
KDE 4 library

%package -n libkasten1okteta1gui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten1okteta1gui4
KDE 4 library

%package lokalize
Group: Development/Tools
Summary: Computer-aided translation system
Requires: %name-core = %version-%release
Provides: %name-localize = %version-%release
%description lokalize
Computer-aided translation system

%package kapptemplate
Summary: Template for KDE Application Development
Group: Development/KDE and QT
Requires: %name-core = %version-%release
%description kapptemplate
KAppTemplate is a set of modular shell scripts that will create a
framework for any number of KDE application types. At it's base
level, it handles creation of things like the automake/autoconf
framework, lsm files, RPM spec files, and po files. Then, there
are individual modules that allow you to create a skeleton KDE
application, a KPart application, a KPart plugin, or even convert
existing source code to the KDE framework.

%package kuiviewer
Summary: UI Files Viewer
Group: Development/KDE and QT
Provides: kuiviewer4
Requires: %name-core = %version-%release
%description kuiviewer
Displays Qt Designer UI files

%package scripts
Summary: Script From kdesdk
Group: Development/KDE and QT
BuildArch: noarch
Requires: %name-core = %version-%release
%description scripts
This package contains the scripts for KDE development which are
contained in the %rname module.

%package kbugbuster
Summary: kbugbuster
Group: Development/KDE and QT
Provides: kbugbuster4
Requires: %name-core = %version-%release
%description kbugbuster
Kbugbuster

%package strigi-analyzer
Summary: Strigi Analyzer
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description strigi-analyzer
Strigi analyzer

%package po2xml
Summary: Xml2po and vice versa converters
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description po2xml
An xml2po and vice versa converters.

%package devel
Summary: Header files for %rname
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kde4-kate-devel
%description devel
This package includes the header files you will need to compile
applications for %rname.

%package umbrello
Summary: UML Modeller
Group: Development/Tools
Requires: %name-core = %version-%release
%description umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%package cervisia
Summary: CVS client part
Group: Development/Tools
Requires: %name-common = %version-%release
%description cervisia
CVS client part.

%package kompare
Summary: KDE diff graphic tool
Group: Development/Tools
Requires: %name-core = %version-%release
%description kompare
kompare is a KDE diff graphic tool

%package kmtrace
Summary: Memory Allocation Debugging Tool
Group: Development/Tools
Requires: %name-core = %version-%release
%description kmtrace
Memory Allocation Debugging Tool

%package kcachegrind
Summary: KCachegrind
Group: Development/Tools
Requires: %name-core = %version-%release
%ifarch %ix86
Requires: valgrind
%endif
%description kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%package dolphin
Summary: Dolphin plugins for development
Group: Development/Tools
Requires: kde4base-dolphin
%description dolphin
Dolphin plugins for development

%package libs
Summary: %name core libraries
Group: System/Libraries
#Requires: %name-common = %version-%release
%description libs
%name core libraries

%package -n libkasten1controllers4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten1controllers4
%name library.

%package -n libkasten1core4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten1core4
%name library.

%package -n libkasten1gui4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten1gui4
%name library.

%package -n libkompareinterface4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkompareinterface4
%name library.

%package -n libktrace4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libktrace4
%name library.


%prep
%setup -q -n %rname-%version
%patch1 -p1

%build
%K4cmake \
    -DHUNSPELL_INCLUDE_DIR=%_includedir \
    -DHUNSPELL_LIBRARIES=%_libdir/libhunspell.so
%K4make


%install
%K4install

# fix scripts for strong /usr/lib/rpm/find-requires
pushd %buildroot/%_K4bindir
for f in `(file ./* | grep bash; file ./* | grep shell) | awk -F: '{print $1}' | xargs grep -l ^=head`
do
    mv "$f" "$f.tmp"
    awk 'BEGIN{found=0;} /^=head/ {if (found==0){print "cat <<\\__EOF__";found=1;};} {print} END{if (found!=0) print "__EOF__";}' <"$f.tmp" >"$f"
    rm -f "$f.tmp"
    chmod a+x $f
done
popd

# resilve conflict with subversion-tools
mv %buildroot/%_K4bindir/svn-clean %buildroot/%_K4bindir/svnclean


%files
%files libs
%files common
%files core
%_K4bindir/cvsaskpass
%_K4bindir/cvsservice
%_K4bindir/kio_svn_helper
%_K4bindir/kstartperf
%_K4bindir/kpartloader
%_K4libdir/libkdeinit4_cvsaskpass.so
%_K4libdir/libkdeinit4_cvsservice.so
%_K4lib/kio_perldoc.so
%_K4lib/kabcformat_kdeaccounts.so
%_K4lib/kstartperf.so
%_K4apps/kio_perldoc/
%_K4apps/kpartloader/
%_K4srv/perldoc.protocol
%_K4apps/kabc/formats/kdeaccountsplugin.desktop
%_K4iconsdir/locolor/*/actions/*.*
%_K4iconsdir/hicolor/*/actions/*.*
%_K4iconsdir/hicolor/*/mimetypes/application-x-uml.*

%files okteta
%_K4bindir/okteta
%_K4lib/libkbytearrayedit.so
%_K4lib/oktetapart.so
%_K4xdg_apps/okteta.desktop
%_K4apps/okteta/
%_K4apps/oktetapart/
%_K4iconsdir/hicolor/*/apps/okteta.*
%_K4srv/kbytearrayedit.desktop
%_K4srv/oktetapart.desktop
%_K4cfg/structviewpreferences.kcfg
%_K4conf/okteta-structures.knsrc
%_K4xdg_mime/okteta.xml
%_K4doc/*/okteta

%files -n libkasten1okteta1core4
%_K4libdir/libkasten1okteta1core.so.*
%files -n libkasten1okteta1gui4
%_K4libdir/libkasten1okteta1gui.so.*
%files -n libkasten1okteta1controllers4
%_K4libdir/libkasten1okteta1controllers.so.*
%files -n libkasten1controllers4
%_K4libdir/libkasten1controllers.so.*
%files -n libokteta1core4
%_K4libdir/libokteta1core.so.*
%files -n libokteta1gui4
%_K4libdir/libokteta1gui.so.*
%files -n libkasten1core4
%_K4libdir/libkasten1core.so.*
%files -n libkasten1gui4
%_K4libdir/libkasten1gui.so.*

%files dolphin
%_K4lib/fileviewgitplugin.so
%_K4lib/fileviewsvnplugin.so
%_K4lib/fileviewbazaarplugin.so
%_K4lib/fileviewhgplugin.so
%_K4cfg/fileviewsvnpluginsettings.kcfg
%_K4cfg/fileviewgitpluginsettings.kcfg
%_K4cfg/fileviewhgpluginsettings.kcfg
%_K4srv/fileviewgitplugin.desktop
%_K4srv/fileviewsvnplugin.desktop
%_K4srv/fileviewbazaarplugin.desktop
%_K4srv/fileviewhgplugin.desktop

%files lokalize
%_K4bindir/lokalize
%_K4xdg_apps/lokalize.desktop
%_K4apps/lokalize/
%_K4cfg/lokalize.kcfg
%_datadir/strigi/fieldproperties/strigi_translation.fieldproperties
%_K4iconsdir/*/*/apps/lokalize.*
%_K4doc/*/lokalize

%files kapptemplate
%_K4bindir/kapptemplate
%_K4xdg_apps/kapptemplate.desktop
#%_K4apps/kapptemplate/
%_K4apps/kdevappwizard/
%_K4cfg/kapptemplate.kcfg
%_K4iconsdir/hicolor/*/*/kapptemplate.*
%_K4doc/*/kapptemplate

%files kuiviewer
%_K4bindir/kuiviewer
%_K4libdir/kde4/kuiviewerpart.so
%_K4libdir/kde4/quithumbnail.so
%_K4xdg_apps/kuiviewer.desktop
%_K4apps/kuiviewer/
%_K4iconsdir/hicolor/*/apps/kuiviewer.png
%_K4apps/kuiviewerpart/
%_K4srv/kuiviewer_part.desktop
%_K4srv/designerthumbnail.desktop

%files scripts
%_K4bindir/adddebug
%_K4bindir/build-progress.sh
%_K4bindir/cheatmake
%_K4bindir/colorsvn
%_K4bindir/create_cvsignore
%_K4bindir/create_makefile
%_K4bindir/create_makefiles
%_K4bindir/create_svnignore
%_K4bindir/cvs-clean
#%_K4bindir/cvs2dist
%_K4bindir/cvsaddcurrentdir
%_K4bindir/cvsbackport
%_K4bindir/cvsblame
%_K4bindir/cvscheck
%_K4bindir/cvsforwardport
%_K4bindir/cvslastchange
%_K4bindir/cvslastlog
%_K4bindir/cvsrevertlast
%_K4bindir/cvsversion
%_K4bindir/cxxmetric
#%_K4bindir/extractqml
%_K4bindir/extend_dmalloc
%_K4bindir/extractattr
%_K4bindir/extractrc
%_K4bindir/findmissingcrystal
%_K4bindir/fix-include.sh
%_K4bindir/fixkdeincludes
%_K4bindir/fixuifiles
%_K4bindir/includemocs
%_K4bindir/kde_generate_export_header
%_K4bindir/kde-systemsettings-tree.py
%_K4bindir/kdedoc
%_K4bindir/kdekillall
%_K4bindir/kdelnk2desktop.py
%_K4bindir/kdemangen.pl
#%_K4bindir/kdesrc-build
%_K4bindir/krazy-licensecheck
%_K4bindir/makeobj
%_K4bindir/noncvslist
%_K4bindir/nonsvnlist
%_K4bindir/optimizegraphics
%_K4bindir/package_crystalsvg
%_K4bindir/png2mng.pl
%_K4bindir/pruneemptydirs
%_K4bindir/qtdoc
%_K4bindir/svnclean
#%_K4bindir/svn2dist
%_K4bindir/svnbackport
%_K4bindir/svnchangesince
%_K4bindir/svnforwardport
%_K4bindir/svngettags
%_K4bindir/svnintegrate
%_K4bindir/svnlastchange
%_K4bindir/svnlastlog
%_K4bindir/svnrevertlast
%_K4bindir/svnversions
%_K4bindir/wcgrep
%_K4bindir/zonetab2pot.py
#%_K4xdg_apps/kdesrc-build.desktop
#%_K4doc/*/kdesrc-build
%ifndef _kde_alternate_placement
#%_man1dir/adddebug.*
#%_man1dir/cheatmake.*
#%_man1dir/create_cvsignore.*
#%_man1dir/create_makefile.*
#%_man1dir/create_makefiles.*
#%_man1dir/cvscheck.*
#%_man1dir/cvslastchange.*
#%_man1dir/cvslastlog.*
#%_man1dir/cvsrevertlast.*
#%_man1dir/cxxmetric.*
#%_man1dir/demangle.*
#%_man1dir/extend_dmalloc.*
#%_man1dir/extractrc.*
#%_man1dir/fixincludes.*
#%_man1dir/po2xml.*
#%_man1dir/pruneemptydirs.*
#%_man1dir/qtdoc.*
#%_man1dir/reportview.*
#%_man1dir/split2po.*
#%_man1dir/swappo.*
#%_man1dir/transxx.*
#%_man1dir/xml2pot.*
#%_man1dir/zonetab2pot.py.*
%endif

#%files kbugbuster
#%_K4bindir/kbugbuster
#%_K4xdg_apps/kbugbuster.desktop
#%_K4apps/kbugbuster/
#%_K4iconsdir/*/*/*/kbugbuster*
#%_K4libdir/kde4/kcal_bugzilla.so
#%_K4srv/kresources/kcal/bugzilla.desktop

%files strigi-analyzer
%_K4libdir/strigi/strigi*

%files po2xml
#%_K4bindir/po2xml
%_K4bindir/split2po
#%_K4bindir/swappo
%_K4bindir/xml2pot

%files umbrello
%_K4bindir/umbrello
%_K4xdg_apps/umbrello.desktop
%_K4apps/umbrello/
%_K4iconsdir/hicolor/*/apps/umbrello*
%_K4doc/*/umbrello

%files cervisia
%_K4bindir/cervisia
%_K4xdg_apps/cervisia.desktop
%_K4apps/cervisia/
%_K4apps/cervisiapart/
%_K4conf_update/cervisia-change_repos_list.pl
%_K4conf_update/cervisia-normalize_cvsroot.pl
%_K4conf_update/cervisia.upd
%_K4conf_update/change_colors.pl
%_K4cfg/cervisiapart.kcfg
%_K4iconsdir/*/*/apps/cervisia.*
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsjob.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsloginjob.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsservice.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.repository.xml
%ifdef _kde_alternate_placement
%else
#%_man1dir/cervisia.*
%endif
%_K4libdir/libkdeinit4_cervisia.so
%_K4libdir/kde4/kded_ksvnd.so
%_K4libdir/kde4/kio_svn.so
%_K4libdir/kde4/cervisiapart.so
%_K4srv/ServiceMenus/subversion.desktop
%_K4srv/ServiceMenus/subversion_toplevel.desktop
%_K4srv/cvsservice.desktop
%_K4srv/kded/ksvnd.desktop
%_K4srv/svn+file.protocol
%_K4srv/svn+http.protocol
%_K4srv/svn+https.protocol
%_K4srv/svn+ssh.protocol
%_K4srv/svn.protocol
%_K4srv/cervisiapart.desktop
%_datadir/dbus-1/interfaces/org.kde.ksvnd.xml
%_K4doc/*/cervisia

%files kompare
%_K4bindir/kompare
%_K4libdir/kde4/komparenavtreepart.so
%_K4libdir/kde4/komparepart.so
%_K4libdir/libkomparedialogpages.so.*
%_K4libdir/libkomparediff2.so.*
%_K4xdg_apps/kompare.desktop
%_K4apps/kompare/
%_K4iconsdir/hicolor/*/apps/kompare.*
%_K4srv/komparenavtreepart.desktop
%_K4srv/komparepart.desktop
%_K4srvtyp/komparenavigationpart.desktop
%_K4srvtyp/kompareviewpart.desktop
%_K4doc/*/kompare

%files kmtrace
%_K4bindir/kmtrace
%_K4bindir/demangle
%_K4bindir/kminspector
%_K4bindir/kmmatch
%_K4apps/kmtrace/

%files kcachegrind
%_K4bindir/kcachegrind
%_K4bindir/dprof2calltree
%_K4bindir/hotshot2calltree
%_K4bindir/memprof2calltree
%_K4bindir/op2calltree
%_K4bindir/pprof2calltree
%_K4iconsdir/*/*/*/kcachegrind.*
%_K4apps/kcachegrind/
%_K4xdg_apps/kcachegrind.desktop
%_K4doc/*/kcachegrind

%files -n libkompareinterface4
%_K4libdir/libkompareinterface.so.*
%files -n libktrace4
%_K4libdir/libktrace.so.*

%files devel
%_K4includedir/kprofilemethod.h
%_K4includedir/ktrace.h
%_K4includedir/kompare/
%_K4includedir/okteta1
%_K4includedir/kasten1
%_K4includedir/KDE/*
%_K4link/*.so
%_K4lib/plugins/designer/*.so


%changelog
* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- built for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Thu Jun 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 4.5.3-alt1.1
- rebuilt with perl 5.12

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt2
- fix subpackages requires (ALT#23808)

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

* Tue Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
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

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- removed deprecated macroses from specfile

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Tue Jun 03 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Mon Mar 31 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt2
- fix to package main package

* Thu Mar 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- built for ALT

