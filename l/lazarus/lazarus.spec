%define _unpackaged_files_terminate_build 1
%define cfg %_builddir/%name-%version/

Name:    lazarus
Version: 3.6
Release: alt1
Epoch:   1

Summary: Lazarus Component Library and IDE
License: GPL-2.0 and LGPL-2.0 and MPL-1.1
# For additional components and tools: LGPL-2.0 and LGPL-2.1 and MPL-1.1 and MPL-2.0 and GPL-2.0 and BSD-3-Clause
Group:   Development/Other
Url:     http://www.lazarus-ide.org/
# Git: https://gitlab.com/freepascal.org/lazarus/lazarus.git

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: %ix86 x86_64 aarch64

Source:  %name-%version.tar
Source2: extra.tar
Source3: environmentoptions.xml
Source4: projectoptions.xml

Patch0: %name-0.9.22-alt-relax-onwine.patch
Patch1: %name-without-tests.patch
Patch2: %name-fix-desktop-file.patch
Patch3: %name-fix-install-path-in-Makefile.patch
Patch4: %name-2.0.2-fix-fpc-search.patch
Patch6:	%name-set-user-TestBuildDirectory.patch

# Patches from Debian
Patch11: lazarus-default-config.patch
Patch12: lazarus-lcl-with-multple-widget-sets.patch

# Other patches
Patch13: lazarus-customform-sigsegv-fix.patch

BuildRequires(pre): qt5-base-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: fpc >= 3.2.2 fpc-utils glibc-devel libgtk+2-devel libXi-devel desktop-file-utils
BuildRequires: libXext-devel libXtst-devel libGL-devel libGLU-devel libode-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5pas-devel
# .xct files for documentation build
BuildRequires: fpc-docs

Requires:   fpc >= 3.2.2 fpc-src fpc-utils gdb libGL-devel libXi-devel libXext-devel libgtk+2-devel
Requires:   glibc-devel
Requires:   libdbus-devel
Requires:   xterm
Requires:   lazarus-lcl
# Default LCL
Requires:   lazarus-gtk
Requires:   gcc

Provides:   %name-docs = %version
Obsoletes:  %name-docs < %version
Provides:   %name-examples = %version
Obsoletes:  %name-examples < %version

%add_findreq_skiplist %_libdir/%name/examples/* %_libdir/%name/components/*

%description
Lazarus is a free and open source Rapid Application Development tool
for the FreePascal compiler using the Lazarus component library - LCL.
The LCL is included in this package.

%description -l ru_RU.UTF8
Lazarus - свободно-распространяемая, с открытым исходным кодом,
среда для быстрой разработки прикладных программ (Rapid Application
Development tool) на FreePascal, использующая библиотеки компонет LCL
(Lazarus component library).  LCL входят в состав данного пакета.

%package additional
Summary: Additional components and tools for Lazarus
License: LGPL-2.0 and LGPL-2.1 and MPL-1.1 and MPL-2.0 and GPL-2.0 and BSD-3-Clause
Group:   Development/Other
Requires: lazarus = %EVR

%description additional
Additional components and tools for Lazarus:
* fortes4lazarus
* fpspreadsheet
* GLScene
* Indy
* jvcl
* lnet
* Orca_Ext
* powerpdf
* rxnew
* Virtual-TreeView
* zeoslib
* explorateur_lrs

%package qt5
Summary: Interface for Lazarus based on Qt5
Group: Development/Other
Provides: lazarus-lcl
Requires: qt5pas-devel
Requires: %name = %EVR

%description qt5
Interface for Lazarus based on Qt5.

%package gtk
Summary: Interface for Lazarus based on GTK+
Group: Development/Other
Provides: lazarus-lcl
Requires: %name = %EVR

%description gtk
Interface for Lazarus based on GTK+.

%package -n qt5pas
Summary: Qt5 bindings for Pascal
Group:   Development/Other

%description -n qt5pas
Qt5 bindings for Pascal from Lazarus.

%package -n qt5pas-devel
Summary: Development files for qt5pas
Group:   Development/Other
Requires: qt5pas = %EVR

%description -n qt5pas-devel
The qt5pas-devel package contains libraries and header files for
developing applications that use qt5pas.

%prep
%setup
%patch0 -p1

tar xf %SOURCE2
%patch1 -p2
%patch2 -p2
%patch3 -p2
subst 's|/usr/lib/|%{_libdir}/|' %PATCH4
%patch4 -p2
%patch6 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p2

install -D -p -m 0644 %SOURCE3 tools/install/linux/environmentoptions.xml
#sed -i -e 's,@version@,%version,g' tools/install/linux/helpoptions.xml docs/index.ru.html

# Replace xterm call with real path
find . -name *.lpi -print0 -o -name *.kof -print0 | xargs -0 -L 1 subst 's,[\\/]usr[\\/]\(X11R6[\\/]\)\?bin[\\/]\(xterm\|gnome-terminal\),/usr/bin/xterm,'

# Install to %%_libdir instead of %%_datadir because lasarus dir contains binaries
subst 's|share/lazarus|%_lib/lazarus|' Makefile

# Generate revision.inc
echo "const RevisionStr = '${SVNVERSION}';" > ide/revision.inc

# Fix path to fpdoc
subst 's|fpdocpath=.*|fpdocpath="%_bindir"|' docs/html/build_*.sh

%build
MAKEOPTS="-Fl/opt/gnome/lib"
if [ -n "$FPCCfg" ]; then
  MAKEOPTS="$MAKEOPTS -n @$FPCCfg"
fi
#CHMHELP:MAKEOPTS="$MAKEOPTS -dUseCHMHelp"

# Make IDE
# Build IDE based on Qt5
make bigide OPT="$MAKEOPTS" USESVN2REVISIONINC=0 LCL_PLATFORM=qt5
mv lazarus lazarus-qt5

# Build IDE based on GTK+
make bigide OPT="$MAKEOPTS" USESVN2REVISIONINC=0 LCL_PLATFORM=gtk2
cp lazarus lazarus-gtk

# Make other program and utilites
sed -e "s#__LAZARUSDIR__#%{cfg}#" tools/install/linux/environmentoptions.xml > environmentoptions.xml

%ifnarch aarch64
# Build apiwizz
make -C tools/apiwizz/
%endif

# Build additional components
# TODO: GLScene fortes4lazarus fpspreadsheet(FileNameIsAbsolute is unknown) jvcl rxnew(rx)
for lpk in \
    Indy/Lib/indylaz.lpk \
    Orca_Ext/pl_OpenGL/pl_opengl.lpk \
    VirtualTreeView-Lazarus/Source/virtualtreeview_package.lpk \
    lnet/lazaruspackage/lnetbase.lpk \
    lnet/lazaruspackage/lnetvisual.lpk \
    powerpdf/pack_powerpdf.lpk \
    zeoslib/packages/lazarus/zcomponent.lpk \
    zeoslib/packages/lazarus/zcomponentdesign.lpk \
    zeoslib/packages/lazarus/zcore.lpk \
    zeoslib/packages/lazarus/zdbc.lpk \
    zeoslib/packages/lazarus/zparsesql.lpk \
    zeoslib/packages/lazarus/zplain.lpk
do
	echo "Building components/$lpk..."
	./lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg components/$lpk
done

# Build explorateur_lrs
./lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg tools/explorateur_lrs/LRS_Explorer.lpr
mv tools/explorateur_lrs/release/* tools/explorateur_lrs
rm -rf tools/explorateur_lrs/release/

# Build lazdatadesktop
mkdir -p tools/lazdatadesktop/lib
./lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg tools/lazdatadesktop/lazdatadesktop.lpr

# Generate documentation
export LCL_PLATFORM=nogui
./lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg docs/html/build_lcl_docs.lpi
pushd docs/html
for i in rtl.xct fcl.xct fclres.chm fcl.chm rtl.chm; do
    ln -s %_defaultdocdir/fpc/$i ../chm/$i
done
./build_lcl_docs
./build_html.sh
./build_chm.sh
popd

# Build Qt5 bindings
pushd lcl/interfaces/qt5/cbindings/
    %qmake_qt5
    %make_build
popd

export LCL_PLATFORM=
#export LCL_PLATFORM=gtk2
#export FPCDIR=%%_libdir/fpc
strip lazarus-qt5
strip lazarus-gtk
strip startlazarus
strip lazbuild
strip tools/lazres
strip tools/updatepofiles
strip tools/lrstolfm
strip tools/svn2revisioninc
if [ -f components/chmhelp/lhelp/lhelp ]; then
  strip components/chmhelp/lhelp/lhelp
fi

rm -f environmentoptions.xml

%install
LAZARUSDIR=%_libdir/%name
mkdir -p %buildroot$LAZARUSDIR \
         %buildroot%_sysconfdir/%name
%makeinstall_std INSTALL_PREFIX=%buildroot%_prefix _LIB=%_lib
install -m 644 install/lazarus.desktop %buildroot%_desktopdir/%name.desktop

install -Dm0755 lazarus-qt5 %buildroot%_bindir/lazarus-qt5
install -Dm0755 lazarus-gtk %buildroot%_bindir/lazarus-gtk
rm -f %buildroot%_bindir/lazarus-ide
mkdir -p %buildroot%_altdir
echo "%_bindir/lazarus	%_bindir/lazarus-qt5	50" > %buildroot%_altdir/lazarus-qt5
echo "%_bindir/lazarus	%_bindir/lazarus-gtk	100" > %buildroot%_altdir/lazarus-gtk

ln -sf $LAZARUSDIR/tools/explorateur_lrs/LRS_Explorer %buildroot%_bindir/LRS_Explorer
ln -sf $LAZARUSDIR/tools/explorateur_lrs/LRS_Explorer %buildroot%_bindir/lrsexplorer
%ifnarch aarch64
ln -sf $LAZARUSDIR/tools/apiwizz/apiwizz %buildroot%_bindir/apiwizz
%endif
ln -sf $LAZARUSDIR/tools/lazdatadesktop/lazdatadesktop %buildroot%_bindir/lazdatadesktop

cat tools/install/linux/environmentoptions.xml | sed -e "s#__LAZARUSDIR__#$LAZARUSDIR/#" -e "s#__FPCSRCDIR__#%{_datadir}/fpcsrc/#" > %buildroot%_sysconfdir/%name/environmentoptions.xml

# fix bug 13256
mkdir -p %buildroot%_datadir/fpcsrc/packages/fcl-base
mkdir -p %buildroot%_datadir/fpcsrc/rtl/inc

# fix navigate to line with error (see https://bugs.altlinux.org/25991#c20)
install -D -p -m 0644 %SOURCE4 %buildroot%_sysconfdir/lazarus/projectoptions.xml
subst 's|/usr/lib/|%{_libdir}/|' %buildroot%_sysconfdir/lazarus/projectoptions.xml

# Docs
test -e docs/index.en.html || mv docs/index.html docs/index.en.html

# Install CHM files to doc dir
cp -a docs/chm/* %buildroot$LAZARUSDIR/docs/html/

# cleanup installation
rm -rf %buildroot$LAZARUSDIR/tools/install
rm -rf %buildroot$LAZARUSDIR/tools/find_merged_revisions.pas

# generate correct compilertest.pas
echo -e "begin\nend." > %buildroot$LAZARUSDIR/compilertest.pas

pushd lcl/interfaces/qt5/cbindings/
    %makeinstall_std INSTALL_ROOT=%buildroot
popd
rm -rf %buildroot$LAZARUSDIR/lcl/interfaces/qt5/cbindings
rm -rf %buildroot$LAZARUSDIR/lazarus.app

# Make executable symlink to selected program
rm -f %buildroot$LAZARUSDIR/lazarus
ln -s ../../bin/lazarus %buildroot$LAZARUSDIR/lazarus

# Fix python3 shebang
subst 's|#!.*python$|#!%__python3|' %buildroot%_libdir/lazarus/components/GLScene/external/Tetgen/tetgentogls.py

%files
%_libdir/%name
%_bindir/*
%exclude %_bindir/lazarus-qt5
%exclude %_bindir/lazarus-gtk
%exclude %_bindir/LRS_Explorer
%exclude %_bindir/lrsexplorer
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/environmentoptions.xml
%config(noreplace) %_sysconfdir/%name/projectoptions.xml
%_pixmapsdir/lazarus.png
%_desktopdir/lazarus.desktop
%_datadir/mime/packages/lazarus.xml
%_man1dir/*
# fix bug 13256
%dir %_datadir/fpcsrc/rtl/inc
%dir %_datadir/fpcsrc/packages/fcl-base
%exclude %_libdir/libQt5Pas.so*
%_iconsdir/hicolor/48x48/mimetypes/*.png
%exclude %_libdir/lazarus/components/fortes4lazarus
%exclude %_libdir/lazarus/components/fpspreadsheet
%exclude %_libdir/lazarus/components/GLScene
%exclude %_libdir/lazarus/components/Indy
%exclude %_libdir/lazarus/components/jvcl
%exclude %_libdir/lazarus/components/lnet
%exclude %_libdir/lazarus/components/Orca_Ext
%exclude %_libdir/lazarus/components/powerpdf
%exclude %_libdir/lazarus/components/rxnew
%exclude %_libdir/lazarus/components/VirtualTreeView-Lazarus
%exclude %_libdir/lazarus/components/zeoslib
%exclude %_libdir/lazarus/tools/explorateur_lrs

%files additional
%_bindir/LRS_Explorer
%_bindir/lrsexplorer
%_libdir/lazarus/components/fortes4lazarus
%_libdir/lazarus/components/fpspreadsheet
%_libdir/lazarus/components/GLScene
%_libdir/lazarus/components/Indy
%_libdir/lazarus/components/jvcl
%_libdir/lazarus/components/lnet
%_libdir/lazarus/components/Orca_Ext
%_libdir/lazarus/components/powerpdf
%_libdir/lazarus/components/rxnew
%_libdir/lazarus/components/VirtualTreeView-Lazarus
%_libdir/lazarus/components/zeoslib
%_libdir/lazarus/tools/explorateur_lrs

%files qt5
%_bindir/lazarus-qt5
%_altdir/lazarus-qt5

%files gtk
%_bindir/lazarus-gtk
%_altdir/lazarus-gtk

%files -n qt5pas
%doc lcl/interfaces/qt5/cbindings/COPYING.TXT
%doc lcl/interfaces/qt5/cbindings/README.TXT
%_libdir/libQt5Pas.so.*

%files -n qt5pas-devel
%_libdir/libQt5Pas.so

%changelog
* Sat Sep 28 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.6-alt1
- New version.

* Sat May 25 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.4-alt1
- New version.

* Mon Mar 18 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.2-alt2
- Required gcc.

* Wed Mar 06 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.2-alt1
- New version.

* Mon Dec 18 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.0-alt2
- End of bootstrap qtpas.

* Sun Dec 17 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.0-alt1
- New version.
- Bootstraped qtpas with version of lazarus.

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.2.6-alt3
- Updated additional components, add Orca_Ext, Virtual-TreeView, jvcl.
- Built additional components.
- Package additional components and tools to lazarus-additional.

* Mon Sep 04 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.2.6-alt2
- Use upstream sources from tag lazarus_2_2_6 (ALT #47097).

* Sun Mar 05 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.2.6-alt1
- New version.

* Mon Sep 26 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.2.4-alt1
- New version.

* Thu Jun 09 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.2.2.0-alt2
- Use FPC documentation in CHM format from fpc-docs.

* Sun May 15 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.2.2.0-alt1
- New version.
- Build help (ALT #42054).

* Tue Mar 08 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.2.0.4-alt2
- Frontend subpackages require lazarus (ALT #42077).

* Mon Jan 10 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.2.0.4-alt1
- New version.
- Build from upstream Git: https://gitlab.com/freepascal.org/lazarus/lazarus.git

* Wed Jun 16 2021 Andrey Cherepanov <cas@altlinux.org> 1:2.0.12-alt1
- New version.

* Thu Dec 17 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.0.10-alt4
- Translate comment in desktop file into Russian (ALT #36852).
- Make different weights if alternatives.
- Remove tests to prevent sendmail autoreq.

* Thu Oct 22 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.0.10-alt3
- Fix run startlazarus.

* Thu Oct 15 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.0.10-alt2
- Packages lcl packages lazarus-qt5 and lazarus-gtk.

* Wed Sep 30 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.0.10-alt1
- New version.
- Build on aarch64 (except apiwizz).

* Mon Apr 20 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.0.8-alt1
- New version.
- Fix License tag according to SPDX.

* Tue Nov 05 2019 Andrey Cherepanov <cas@altlinux.org> 1:2.0.6-alt1
- New version.

* Fri Aug 09 2019 Andrey Cherepanov <cas@altlinux.org> 1:2.0.4-alt1
- New version.

* Thu Jul 04 2019 Andrey Cherepanov <cas@altlinux.org> 1:2.0.2-alt1
- New version.
- Add Qt5 bindings for Pascal from Lazarus (qt5pas).

* Mon Feb 18 2019 Andrey Cherepanov <cas@altlinux.org> 1:2.0.1-alt1.r60436
- New version.
- Remove requirements only needed for old version.

* Wed Jan 23 2019 Andrey Cherepanov <cas@altlinux.org> 1:1.8.4-alt2
- Remove requirement of fpc-src.

* Fri Jun 29 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.8.4-alt1
- New version.
- Build only for i586 and x86_64.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.8.2-alt1
- New version.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.8.0-alt1
- New version.

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.4-alt3
- Add Russian localization for desktop file

* Mon Mar 06 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.4-alt2
- Revert regression made in 1.6.4 in customform.inc (ALT #33204)

* Thu Mar 02 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.4-alt1
- New version (http://wiki.lazarus.freepascal.org/Lazarus_1.6.0_release_notes)
- Fix TCustomEdit behaviour in new upstream version (ALT #33189)

* Mon Nov 28 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.6.2-alt1
- New version

* Fri Feb 19 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.6.0-alt1
- New version (http://wiki.lazarus.freepascal.org/Lazarus_1.6.0_release_notes)
- Change project URL

* Mon Dec 14 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.4.4-alt2
- Rebuild with fpc-3.0.0

* Thu Oct 08 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.4.4-alt1
- New version (http://forum.lazarus.freepascal.org/index.php/topic,29886.0.html)

* Wed Jul 15 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.4.2-alt1
- New version

* Tue May 05 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.4.0-alt2
- Upstream fix for http://bugs.freepascal.org/view.php?id=27991

* Thu Apr 23 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.4.0-alt1
- New version (http://wiki.lazarus.freepascal.org/Lazarus_1.4.0_release_notes)

* Thu Nov 06 2014 Andrey Cherepanov <cas@altlinux.org> 1:1.2.6-alt1
- New version

* Tue Oct 14 2014 Andrey Cherepanov <cas@altlinux.org> 1:1.2.4-alt3
- Place TestBuildDirectory in ~/.lazarus/tmp by default and if /tmp/ is
  used from previous configuration

* Thu Oct 09 2014 Andrey Cherepanov <cas@altlinux.org> 1:1.2.4-alt2
- Apply patches from Debian
- Replace xterm path fix patch by regular expression in command line
- Use user personal temporary directory to prevent temporary files clash

* Wed Aug 13 2014 Andrey Cherepanov <cas@altlinux.org> 1:1.2.4-alt1
- New version

* Wed Aug 13 2014 Andrey Cherepanov <cas@altlinux.org> 1:1.2.2-alt1
- New version

* Fri Mar 07 2014 Andrey Cherepanov <cas@altlinux.org> 1:1.2.0-alt1
- New version

* Wed Nov 20 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.0.14-alt1
- New version

* Wed Sep 25 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.0.12-alt1
- New version 1.0.12

* Mon Jun 24 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.0.10-alt1
- New version 1.0.10

* Fri May 24 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.0.8-alt1
- New version 1.0.8
- Fix search FPC compiler with localized output from fpc (ALT #25991)
- Set correct path to xterm for all existing modules (ALT #24803)
- Update PowerPDF to 0.9.10 (ALT #24804)
- Add libdbus-devel and xterm to requires
- Pack man pages
- Add patches from Fedora
- Make symlink /usr/bin/lazarus for lazarus-ide
- Add docs and examples in main package

* Fri Mar 15 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.0.6-alt1
- New version 1.0.6

* Wed Dec 26 2012 Andrey Cherepanov <cas@altlinux.org> 1:1.0.4-alt2
- Build LRS_Explorer

* Fri Dec 14 2012 Andrey Cherepanov <cas@altlinux.org> 1:1.0.4-alt1
- New version 1.0.4 (ALT #27695)
- Do not build LRS_Explorer

* Wed Jun 06 2012 Andrey Cherepanov <cas@altlinux.org> 1:0.9.30.4-alt0.M60P.4
- Set correct pathes to default configuration
- Enable LRS_Explorer
- Clean spec

* Mon Jun 04 2012 Andrey Cherepanov <cas@altlinux.org> 1:0.9.30.4-alt0.M60P.3
- Add all available components

* Sun Jun 03 2012 Andrey Cherepanov <cas@altlinux.org> 1:0.9.30.4-alt0.M60P.2
- Add rxnew compoent

* Sat Jun 02 2012 Andrey Cherepanov <cas@altlinux.org> 1:0.9.30.4-alt0.M60P.1
- Pack stable version to p6 branch

* Fri Jun 01 2012 Andrey Cherepanov <cas@altlinux.org> 1:0.9.30.4-alt1
- New version 0.9.30.4

* Wed Dec 22 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt9
- Update PowerPDF, restore build pdfexport.
- Fix bu #24804

* Wed Dec 22 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt8
- Fix bug #24803

* Fri Dec 10 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt7
- Added GLScene.

* Mon Sep 27 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt6
- Disable ruqires fpc-docs

* Mon Sep 06 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt5
- Added requires libGL-devel. Fix bug #23895

* Wed Jun 02 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt4
- Added requieres fpc-utils
- Fix bug #23578

* Tue Jun 01 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt3
- restructure default options.

* Mon May 31 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt2
- Restore build lazdatadesktop

* Fri May 28 2010 Alexey Shentzev <ashen@altlinux.ru> 0.9.29-alt1
- New version build
- Update ZeosDBO, RxNew
- Disable build lazdatadesktop, lnet, indy, pdfexport

* Mon Dec 07 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt10
- fix error build on x86_64 for lazarus/components/indy/fpc/IdCoderBinHex4.pas

* Mon Nov 23 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt9
- Added indy from http://www.indyproject.org/sockets/fpc/index.html.

* Sun Nov 22 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt8
- Added zeoslib documenation.

* Sun Nov 22 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt7
- Added lNet LCL from http://lnet.wordpress.com/.

* Fri Nov 20 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt6
- Added ZeosLib from http://sourceforge.net/projects/zeoslib/

* Mon Nov 16 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt5
- ln -sf ../%_lib/%name/tools/lrstolfm %buildroot%_bindir/lrstolfm

* Fri Oct 30 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt4
- added helpoptions.xml for default configurations.

* Fri Oct 30 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt3
- Build lazarus-docs in html. Including subpackage lazarus-tools in package lazarus.

* Wed Oct 28 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt2
- added LRS_Explorer http://lrsexplorer.sourceforge.net/.
- added PowerPDF LCL https://lazarus-ccr.svn.Urlforge.net/svnroot/lazarus-ccr/components/powerpdf/.
- patching RxNew backport from https://lazarus-ccr.svn.Urlforge.net/svnroot/lazarus-ccr/components/rx/.
- patching lazdatadesktop.

* Tue Oct 20 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.28-alt1
- New version build.

* Wed Sep 30 2009 Grigory Batalov <bga@altlinux.ru> 0.9.26.2-alt4
- Don't strip precompiled objects (ALT #20428).

* Fri Sep 11 2009 Grigory Batalov <bga@altlinux.ru> 0.9.26.2-alt3
- Require libXext-devel as well (ALT #19592).
- Build lazdatadesktop (ALT #20664, ashen@).
- Replace DejaVu fonts requirement with Terminus one (ALT #21139).
- Add RxNew and PowerPDF components (ashen@).
- Add default configs (ALT #21291, ashen@).
- Add man pages.

* Wed Aug 05 2009 Grigory Batalov <bga@altlinux.ru> 0.9.26.2-alt2
- Fix build on x86_64.

* Thu Jul 02 2009 Alexey Shentzev <ashen@altlinux.ru> 0.9.26.2-alt1.1
- update spec

* Sun Apr 19 2009 Afanasov Dmitry <ender@altlinux.org> 0.9.26.2-alt1
- 0.9.26.2
- require fpc >= 2.2.2.
- patch:
  + merge fix-desktop and alt-font patches to alt-changes patch
- spec changes:
  + force english messages when compiling
  + pack sources as tar
- don't install absent manpages

* Sun Apr 05 2009 Alexey Rusakov <ktirf@altlinux.org> 0.9.24-alt3.4
- finally closing ALT Bug 17531
- fixed ALT Bug 16207
- fixed Repocop-reported bugs in the .desktop file.
- catch-up to alt3.3 changelog:
  + rx components are not built since their build fails on x86_64

* Tue Mar 31 2009 Alexey Rusakov <ktirf@altlinux.org> 0.9.24-alt3.3
- NMU (thanks to mike@):
  + fixed #19350 (suppressed extra requirements of examples subpackage)
  + spec cleanup

* Sat Oct 11 2008 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt3.2
- fix bug 17531

* Wed Sep 10 2008 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt3.1
- add BuildRequires libXext-devel

* Tue Apr 08 2008 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt3
- build with bigide

* Thu Apr 03 2008 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt2.3.2
- add russian descriptions
- fix bugs #14516, #14390

* Fri Dec 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.9.24-alt2.3.1
- fix optimization flags (s,OG,O1, s,Og,Os,)

* Fri Dec 07 2007 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt2.3
- add call fpcmake -r
- Thanks Slava Dubrovskiy <dubrsl@altlinux.org> for help

* Mon Dec 03 2007 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt2.2
- really added requirement on fpc-src

* Mon Dec 03 2007 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt2.1
- restore require for fpc-src

* Wed Nov 28 2007 Alexey Shentzev <ashen@altlinux.ru> 0.9.24-alt1
- New version build
- fixed bugs 13256
- Thanks Sergey Bolshakov <sbolshakov@altlinux.ru> for help and patching

* Mon Oct 15 2007 Alexey Shentzev <ashen@altlinux.ru> 0.9.22-alt1.1
- fixed bug #13052

* Wed Aug 08 2007 Alexey Shentzev <ashen@altlinux.ru> 0.9.22-alt1
- first buid for sisyphus
- Thanks Slava Dubrovskiy <dubrsl@altlinux.org> for help
