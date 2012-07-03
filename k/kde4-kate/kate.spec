
%add_findpackage_path %_kde4_bindir

%ifarch arm
%def_disable desktop
%else
%def_enable desktop
%endif

%define rname kate
%define major 4
%define minor 8
%define bugfix 4
Name: kde4-kate
Version: %major.%minor.%bugfix
Release: alt2

Group: Editors
Summary: Advanced text editor
Url: http://www.kde.org/
License: GPLv2

Requires: kde4-icon-theme
Requires: %name-core = %version-%release
Provides: kde4sdk-kate = %version-%release
Obsoletes: kde4sdk-kate < %version-%release

Source: %rname-%version.tar
Patch1: kate-4.8.0-alt-acomment-shared.patch

# Automatically added by buildreq on Fri Sep 16 2011 (-bi)
# optimized out: automoc cmake cmake-modules desktop-file-utils docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-mime-info xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ glib2-devel zlib-devel kde-common-devel desktop-file-utils

%description
A fast and advanced text editor with nice plugins

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdesdk-common <= 3.5.12-alt1
Conflicts: kdebase-common <= 3.5.12-alt2
%description common
Common empty package for %rname

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: kde4libs >= %{get_version kde4libs}
%description core
Core files needed for %rname

%package -n kde4-kwrite
Group: Editors
Summary: Text editor for KDE
Requires: kde4-icon-theme
Requires: %name-core = %version-%release
Provides: kde4base-kwrite = %version-%release
Obsoletes: kde4base-kwrite < %version-%release
%description -n kde4-kwrite
Text editor for KDE

%package -n libkateinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkateinterfaces4
%name library.

%package -n libkatepartinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkatepartinterfaces4
%name library.

%package -n libktexteditor4_codesnippets_core
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libktexteditor4_codesnippets_core
%name library.

%package -n libacomment4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libacomment4
%name library.

%package devel
Summary: Header files for %rname
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
This package includes the header files you will need to compile
applications for %rname.


%prep
%setup -q -n %rname-%version
%patch1 -p1


%build
%K4build


%install
%K4install

kde4_add_text_mimes() {
desktop-file-install --mode=0755 --dir %buildroot%_K4xdg_apps \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	$1
}

kde4_add_text_mimes %buildroot%_K4xdg_apps/kate.desktop
kde4_add_text_mimes %buildroot%_K4xdg_apps/kwrite.desktop


%files common
%_K4conf/artisticcommentrc

%files core
%_K4lib/katepart.so
%_K4lib/ktexteditor_*.so
%_K4apps/ktexteditor_*/
%_K4apps/katepart
%_K4conf/katemoderc
%_K4conf/katepartpluginsrc
%_K4conf/ktexteditor_codesnippets_core.knsrc
%_K4srv/katepart.desktop
%_K4srv/ktexteditor_*.desktop
%_K4iconsdir/hicolor/*/apps/ktexteditorautobrace.*
%_K4iconsdir/oxygen/*/actions/debug.*
%_K4iconsdir/oxygen/*/actions/repoadd.*
%_K4iconsdir/oxygen/*/actions/repomanage.*
%_K4iconsdir/oxygen/*/actions/snippetadd.*
%_K4iconsdir/oxygen/*/actions/snippetedit.*

%files
%if_enabled desktop
%_K4conf/katefiletemplates.knsrc
%_K4lib/katefiletemplates.so
%_K4srv/katefiletemplates.desktop
%endif
%_K4bindir/kate
%_K4bindir/ktesnippets_editor
%_K4xdg_apps/kate.desktop
%_K4xdg_apps/ktesnippets_editor.desktop
%_K4apps/kate/
%_K4apps/katexmltools
%_K4conf_update/kate-2.4.upd
%_K4conf/katerc
%_K4libdir/libkdeinit4_kate.so
%_K4lib/katetabifyplugin.so
%_K4lib/katexmltoolsplugin.so
#%_K4lib/kateexternaltoolsplugin.so
%_K4lib/katefilebrowserplugin.so
#%_K4lib/katefindinfilesplugin.so
%_K4lib/katekonsoleplugin.so
%_K4lib/katemailfilesplugin.so
%_K4lib/kateopenheaderplugin.so
%_K4lib/katequickdocumentswitcherplugin.so
%_K4lib/katesymbolviewerplugin.so
%_K4lib/katetabbarextensionplugin.so
%_K4lib/katetextfilterplugin.so
%_K4lib/plasma_applet_katesession.so
%_K4lib/katebacktracebrowserplugin.so
%_K4lib/katebuildplugin.so
%_K4lib/katectagsplugin.so
%_K4lib/kate_kttsd.so
%_K4lib/katexmlcheckplugin.so
%_K4lib/katesnippets_tngplugin.so
%_K4lib/katefiletreeplugin.so
%_K4lib/kategdbplugin.so
%_K4lib/katesqlplugin.so
%_K4lib/katesearchplugin.so
#%_K4srv/kateexternaltoolsplugin.desktop
%_K4srv/katefilebrowserplugin.desktop
#%_K4srv/katefindinfilesplugin.desktop
%_K4srv/katekonsoleplugin.desktop
%_K4srv/katemailfilesplugin.desktop
%_K4srv/kateopenheader.desktop
%_K4srv/katequickdocumentswitcher.desktop
%_K4srv/katesymbolviewer.desktop
%_K4srv/katetabbarextension.desktop
%_K4srv/katetextfilter.desktop
%_K4srv/katebacktracebrowserplugin.desktop
%_K4srv/katebuildplugin.desktop
%_K4srv/katectagsplugin.desktop
%_K4srv/plasma-applet-katesession.desktop
%_K4srv/kate_kttsd.desktop
%_K4srv/katexmlcheck.desktop
%_K4srv/katesnippets_tngplugin.desktop
%_K4srv/katetabifyplugin.desktop
%_K4srv/katexmltools.desktop
%_K4srv/katefiletreeplugin.desktop
%_K4srv/kategdbplugin.desktop
%_K4srv/katesql.desktop
%_K4srv/katesearch.desktop
%_K4srvtyp/kateplugin.desktop
#%_K4doc/*/kate-plugins
%_K4doc/*/kate
%_K4iconsdir/hicolor/*/apps/kate.*
%_K4xdg_mime/ktesnippets.xml

%files -n kde4-kwrite
%_K4bindir/kwrite
%_K4libdir/libkdeinit4_kwrite.so
%_K4xdg_apps/kwrite.desktop
%_K4apps/kwrite/
%_K4doc/en/kwrite/

%files -n libkateinterfaces4
%_K4libdir/libkateinterfaces.so.*
%files -n libkatepartinterfaces4
%_K4libdir/libkatepartinterfaces.so.*
%files -n libktexteditor4_codesnippets_core
%_K4libdir/libktexteditor_codesnippets_core.so.*
%files -n libacomment4
%_K4libdir/libacomment.so.*

%files devel
%_K4includedir/kate/
%_K4includedir/ktexteditor_codesnippets_core/
%_K4includedir/kate_*.h
%_K4includedir/artisticcomment.h
%_K4link/lib*.so

%changelog
* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.2
- rebuilt

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- fix kwrite startup without kate

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1.M60T.1
- built for M60T

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- fix requires (ALT#26424)

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
