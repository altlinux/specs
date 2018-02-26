%undefine __libtoolize
%define _optlevel s
%define glibc_core_ver %{get_version glibc-core}
%define _keep_libtool_files 1

%define unstable 0

%define qtdir %_qt3dir
%define kdedir %prefix
%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libkde
# textrel
%add_verify_elf_skiplist %_libdir/libkommanderwidgets.so*

Name: kdewebdev
Version: 3.5.13
Release: alt2

Group: Graphical desktop/KDE
Summary: K Desktop Environment - web development programs
License: GPL
URL: http://www.kde.org

Requires: %name-kimagemapeditor = %version-%release
Requires: %name-klinkstatus = %version-%release
Requires: %name-kommander = %version-%release
Requires: %name-kxsldbg = %version-%release
Requires: %name-quanta = %version-%release
Requires: %name-kfilereplace = %version-%release


Source: %name-%version.tar

Patch1: kommander-3.5.10-fix-compile.patch
Patch2: kommander-3.5.9-fix-linking.patch
Patch3: kxsldbg-3.5.0-fix-linking.patch
Patch4: quanta-3.5.0-fix-linking.patch
Patch5: quanta-3.5.12-no-la.patch

# security
# end security

# Automatically added by buildreq on Thu Oct 07 2004 (-bi)
#BuildRequires: fontconfig freetype2 gcc-c++ gcc-g77 kde-settings kdelibs-devel libarts-devel libbfd-devel libgpg-error libjpeg-devel libpng-devel libqt3-devel libstdc++-devel libxml2-devel libxslt-devel menu-devel python-base python-modules-compiler python-modules-encodings qt3-designer rpm-build-python xml-utils xorg-x11-devel xorg-x11-libs zlib-devel
BuildRequires(pre): kdelibs-devel
BuildRequires: fontconfig freetype2 gcc-c++
BuildRequires: kdelibs-devel libjpeg-devel libpng-devel
BuildRequires: libqt3-devel libstdc++-devel libxml2-devel libxslt-devel
BuildRequires: menu-devel qt3-designer rpm-build-python xml-utils
BuildRequires: zlib-devel libacl-devel libattr-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
K Desktop Environment - web development programs

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: quanta < 3.3.0-alt0.1
#
%description common
Common empty package for %name

%package klinkstatus
Summary: Link checker for KDE
Group: Development/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
%description klinkstatus
KLinkStatus is a link checker for KDE.
It allows you to search internal and external links in your entire web site,
just a single page and choose the depth to search.
You can also check local files, ftp, fish, etc, as KLinkStatus uses KIO.
For performance, links can be checked simultaneously.

%package kimagemapeditor
Summary: An HTML image map editor
Group: Development/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
%description kimagemapeditor
An HTML image map editor

%package kfilereplace
Summary: Replacing strings over multiple files
Group: Text tools
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kfilereplace = %version-%release
Obsoletes: kfilereplace < %version-%release
%description kfilereplace
KFileReplace is a terrific new addition to QuantaPlus. It allows one to
quickly replace strings over multiple files in only a few clicks of the
mouse.

%package kommander
Summary: Set of tools to create dynamic GUI
Group: Development/Other
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
%description kommander
Kommander is a set of tools that allow you to create dynamic GUI

%package kxsldbg
Summary: GUI front-end to xsldbg
Group: Development/Debuggers
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#Provides: libxsldbg = %version-%release
#Obsoletes: libxsldbg <= %version-%release
Conflicts: xsldbg
%description kxsldbg
%name-kxsldbg package provides a graphic user interface front-end to
xsldbg which supports debugging of XSLT scripts.

%package quanta
Summary: Web IDE
Group: Development/Other
Requires: %{get_dep kdelibs}
Requires: tidy
Requires: %name-common = %version-%release
Provides: quanta = %version-%release
Obsoletes: quanta <= %version-%release
%description quanta
QuantaPlus is a Web IDE that strives to be neutral and
transparent to all markup languages, while supporting popular
web-based scripting languages, CSS, and other emerging W3C
recommendations.

%prep
%setup -q
cp -ar altlinux/admin ./
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

mkdir quanta-doc
for f in altlinux/css altlinux/html altlinux/javascript altlinux/php altlinux/mysql altlinux/mysql5
do
    cp -ar "$f"/* quanta-doc/
    rm -rf quanta-doc/install.sh
done

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
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lkdeinit_kded -lDCOP \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done
make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%K3configure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-closure \
    --disable-gcc-hidden-visibility

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build


%install
%if %unstable
%set_strip_method none
%endif

%K3install

# install quanta docs
pushd quanta-doc
    cp -r * %buildroot/%_K3apps/quanta/doc
popd
rm -f %buildroot/%_K3apps/quanta/doc/install.sh



%files
%files common
%_K3cfg/*

%files klinkstatus
%_K3bindir/klinkstatus
%_K3lib/libklinkstatuspart.so*
%_K3apps/klinkstatus/
%_K3apps/klinkstatuspart/
%_K3srv/klinkstatus_part.desktop
%_kde3_iconsdir/*/*/apps/klinkstatus.*
%doc %_K3doc/en/klinkstatus/
%_K3xdg_apps/klinkstatus.desktop
%_K3iconsdir/crystalsvg/*/actions/bug.*

%files kimagemapeditor
%_K3bindir/kimagemapeditor
%_K3lib/libkimagemapeditor.so*
%_K3apps/kimagemapeditor
%_K3srv/kimagemapeditorpart.desktop
%_kde3_iconsdir/*/*/apps/kimagemapeditor.*
%_K3xdg_apps/kimagemapeditor.desktop

%files kommander
%doc %_K3doc/en/kommander/
%_K3bindir/kmdr-*
%_K3libdir/libkommanderplugin.so*
%_K3libdir/libkommanderwidget.so*
%_K3libdir/libkommanderwidgets.so*
%_K3lib/libkommander_part.so*
%_K3apps/kmdr-editor
%_K3apps/kommander/
%_K3apps/katepart/syntax/kommander.xml
%_K3mimelnk/application/x-kommander.desktop
%_K3applnk/.hidden/kmdr-executor.desktop
%_K3xdg_apps/kmdr-editor.desktop
%_K3apps/katepart/syntax/kommander-new.xml
%_K3apps/kdevappwizard/kommanderplugin.*
%_K3apps/kdevappwizard/templates/kommanderplugin.*
%_K3srv/kommander_part.desktop
%_K3iconsdir/crystalsvg/*/apps/kommander.*
#
%if %_keep_libtool_files
%_K3libdir/libkommanderplugin.la
%_K3libdir/libkommanderwidget.la
%_K3libdir/libkommanderwidgets.la
%endif
#
%_K3includedir/kommander*.h
%_K3includedir/specials.h

%files kxsldbg
%_K3bindir/kxsldbg
%_K3bindir/xsldbg
#usr/include/kde/kxsldbg_partif.h
#usr/include/kde/kxsldbgif.h
#%_K3libdir/libqtnotfier.so*
#%_K3libdir/libxsldbg.so*
%_K3lib/libkxsldbgpart.so*
%_K3apps/kxsldbg
%_K3apps/kxsldbgpart
%doc %_K3doc/en/kxsldbg
%_kde3_iconsdir/*/*/actions/xsldbg_*.png
%_kde3_iconsdir/*/*/actions/1downarrow.png
%_kde3_iconsdir/*/*/actions/configure.png
%_kde3_iconsdir/*/*/actions/exit.png
%_kde3_iconsdir/*/*/actions/hash.png
%_kde3_iconsdir/*/*/actions/mark.png
%_kde3_iconsdir/*/*/actions/next.png
%_kde3_iconsdir/*/*/actions/run.png
%_kde3_iconsdir/*/*/actions/step.png
%_K3srv/kxsldbg_part.desktop
%doc %_K3doc/en/xsldbg/
%_K3xdg_apps/kxsldbg.desktop

%files quanta
%_K3bindir/quanta
%_K3lib/quantadebugger*.so*
%_K3apps/kafkapart
%_K3apps/quanta
#%_K3apps/templates/text/scripts/demo.php
%_K3mimelnk/application/x-webprj.desktop
%_K3srv/quanta_preview_config.desktop
%_K3srv/quantadebugger*.desktop
%_K3srvtyp/quantadebugger.desktop
%_kde3_iconsdir/*/*/apps/quanta.png
%doc %_K3doc/en/quanta
%_K3xdg_apps/quanta.desktop

%files kfilereplace
%_K3bindir/kfilereplace
%_K3lib/libkfilereplacepart.so*
%_K3apps/kfilereplace
%_K3apps/kfilereplacepart
%_K3srv/kfilereplacepart.desktop
%_kde3_iconsdir/*/*/apps/kfilereplace.*
%doc %_K3doc/en/kfilereplace/
%_K3xdg_apps/kfilereplace.desktop

%changelog
* Fri Jun 15 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Automake version is fixed to 1.11.5 detect.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt2.2
- Removed bad RPATH

* Mon Apr 25 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- Remove xorg-x11-devel requirement

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Wed Dec 29 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt1.M51.1
- built for M51

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- update to lastest 3.5 branch
- remove deprecated macroses from specfile

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Thu Oct 19 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Mon Dec 12 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version
- update quanta docs

* Wed Jun 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt2
- add patch for kommander

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version
- add css,html,javascript,php,mysql docs for quanta

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Tue Oct 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- initial spec
