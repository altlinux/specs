# TODO https://bugzilla.altlinux.org/show_bug.cgi?id=20664
%define cfg %_builddir/%name-%version/

Name:       lazarus
Version:    1.0.4
Release:    alt2
Epoch:      1

Summary:    Lazarus Component Library and IDE
License:    GPL and modified LGPL
Group:      Development/Other
Url:        http://www.lazarus.freepascal.org/

Packager:   Andrey Cherepanov <cas@altlinux.org>

Source:     %name-%version.tar
Source2:    extra.tar
Source3:    environmentoptions.xml

Patch0:     %name-0.9.22-alt-relax-onwine.patch

BuildRequires: fpc >= 2.6.0 fpc-utils glibc-devel libgtk+2-devel libXi-devel desktop-file-utils 
BuildRequires: libXext-devel libXtst-devel libGL-devel libGLU-devel libode-devel

Requires:   fpc fpc-src fpc-utils gdb libGL-devel libXi-devel libXext-devel libgtk+2-devel
Requires:   glibc-devel glib-devel libGLU-devel libode-devel
Requires:   fonts-bitmap-terminus
Requires:   %name-docs = %version

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

%package docs
Summary:    Lazarus docs
Group:      Development/Other
#Requires: fpc-docs >= 2.2.4

%description docs
Lazarus docs

%description docs -l ru_RU.UTF8
Документация по Lazarus

%package examples
Summary:    Lazarus examples
Group:      Development/Other

%description examples
Lazarus examples

%description examples -l ru_RU.UTF8
Примеры программ, созданных с помощью Lazarus

%prep
%setup
%patch0 -p1
tar xf %SOURCE2
install -D -p -m 0644 %SOURCE3 tools/install/linux/environmentoptions.xml
#sed -i -e 's,@version@,%version,g' tools/install/linux/helpoptions.xml docs/index.ru.html

%build
MAKEOPTS="-Fl/opt/gnome/lib"
if [ -n "$FPCCfg" ]; then
  MAKEOPTS="$MAKEOPTS -n @$FPCCfg"
fi
#CHMHELP:MAKEOPTS="$MAKEOPTS -dUseCHMHelp"

# Make IDE
make bigide OPT="$MAKEOPTS" USESVN2REVISIONINC=0

# Make other program and utilites
sed -e "s#__LAZARUSDIR__#%{cfg}#" tools/install/linux/environmentoptions.xml > environmentoptions.xml

# Build apiwizz
make -C tools/apiwizz/

# Build explorateur_lrs
./lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg tools/explorateur_lrs/LRS_Explorer.lpr
mv tools/explorateur_lrs/release/* tools/explorateur_lrs
rm -rf tools/explorateur_lrs/release/

# Build lazdatadesktop
mkdir -p tools/lazdatadesktop/lib
./lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg tools/lazdatadesktop/lazdatadesktop.lpr

# Generate documentation
pushd docs/html
../../lazbuild --ws="$LCL_PLATFORM" --pcp=%cfg build_lcl_docs.lpi
sh build_html.sh
popd

export LCL_PLATFORM=
#export LCL_PLATFORM=gtk2
#export FPCDIR=%%_libdir/fpc
strip lazarus
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
mkdir -p %{buildroot}$LAZARUSDIR
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
# mkdir -p %%{buildroot}%%{_datadir}/gnome/apps/Development
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/lazarus
cp -a * %{buildroot}$LAZARUSDIR/
install -m 644 images/icons/lazarus128x128.png %{buildroot}%{_datadir}/pixmaps/lazarus.png
install -m 644 install/lazarus.desktop %{buildroot}%{_datadir}/applications/lazarus.desktop
install -m 644 install/lazarus-mime.xml $LazBuildDir%{buildroot}%{_datadir}/mime/packages/lazarus.xml
ln -sf $LAZARUSDIR/lazarus %{buildroot}%{_bindir}/lazarus-ide
ln -sf $LAZARUSDIR/startlazarus %{buildroot}%{_bindir}/startlazarus
ln -sf $LAZARUSDIR/lazbuild %{buildroot}%{_bindir}/lazbuild
ln -sf $LAZARUSDIR/tools/explorateur_lrs/LRS_Explorer %buildroot%_bindir/LRS_Explorer
ln -sf $LAZARUSDIR/tools/explorateur_lrs/LRS_Explorer %buildroot%_bindir/lrsexplorer
ln -sf $LAZARUSDIR/tools/apiwizz/apiwizz %buildroot%_bindir/apiwizz
ln -sf $LAZARUSDIR/tools/lazres %buildroot%_bindir/lazres
ln -sf $LAZARUSDIR/tools/lrstolfm %buildroot%_bindir/lrstolfm
ln -sf $LAZARUSDIR/tools/svn2revisioninc %buildroot%_bindir/svn2revisioninc
ln -sf $LAZARUSDIR/tools/updatepofiles %buildroot%_bindir/updatepofiles
ln -sf $LAZARUSDIR/tools/lazdatadesktop/lazdatadesktop %buildroot%_bindir/lazdatadesktop
cat install/man/man1/lazbuild.1 | gzip > %{buildroot}%{_mandir}/man1/lazbuild.1.gz
cat install/man/man1/lazarus-ide.1 | gzip > %{buildroot}%{_mandir}/man1/lazarus-ide.1.gz
cat install/man/man1/startlazarus.1 | gzip > %{buildroot}%{_mandir}/man1/startlazarus.1.gz
install tools/install/linux/editoroptions.xml %{buildroot}%{_sysconfdir}/lazarus/editoroptions.xml
cat tools/install/linux/environmentoptions.xml | sed -e "s#__LAZARUSDIR__#$LAZARUSDIR/#" -e "s#__FPCSRCDIR__#%{_datadir}/fpcsrc/#" > %{buildroot}%{_sysconfdir}/lazarus/environmentoptions.xml

# fix bug 13256
mkdir -p %buildroot%_datadir/fpcsrc/packages/fcl-base
mkdir -p %buildroot%_datadir/fpcsrc/rtl/inc

#Docs
mv docs/index.html docs/index.en.html
#mv docs/index.ru.html docs/index.html

%files
%_libdir/%name
%_bindir/*
%_sysconfdir/%name/*
%_mandir/*/*
%_pixmapsdir/lazarus.png
%_desktopdir/lazarus.desktop
%_datadir/mime/packages/lazarus.xml
#_man1dir/*
%exclude %_libdir/%name/docs
%exclude %_libdir/%name/examples
%exclude %_libdir/%name/debian
%exclude %_libdir/%name/tools/install
# fix bug 13256
%dir %_datadir/fpcsrc/rtl/inc
%dir %_datadir/fpcsrc/packages/fcl-base

%files docs
%doc %_libdir/%name/docs

%files examples
%_libdir/%name/examples

%changelog
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
