Name: codeblocks
%define revision 7966
Version: 10.05.%revision
Release: alt1

Summary: Code::Blocks is open source, cross platform free C++ IDE
Summary(ru_RU.UTF-8): Code::Blocks это кросс-платформенная свободная среда разработки для C++ с открытым исходным кодом

License: %gpl3only
Group: Development/C++
Url: http://www.codeblocks.org
Packager: Denis Kirienko <dk@altlinux.ru>

# http://svn.berlios.de/svnroot/repos/codeblocks/trunk 
Source0: %name-svn%revision-src.tar.bz2
Source1: %name-8.02-alt-icons.tar.bz2
Source3: %name.desktop
Source4: %name.po

Patch0: codeblocks-scriptedwizard-localization.patch
Patch1: codeblocks-ebuild.conf.patch

BuildPreReq: wxGTK-devel >= 2.8.10-alt2 gcc-c++ libgtk+2-devel zip sed grep coreutils bzip2 gettext-tools boost-devel libgamin-devel rpm-build-licenses libhunspell-devel wxGTK-contrib-gizmos-devel
Requires: automake >= 1.7 wxGTK >= 2.8.10-alt2 gcc gcc-c++ gdb xterm

%set_verify_elf_skiplist %_datadir/%name/*

%description
Code::Blocks is a free C++ IDE built specifically to meet the most
demanding needs of its users. It was designed, right from the start,
to be extensible and configurable. Built around a plugin framework,
Code::Blocks can be extended with plugin DLLs.
It includes a plugin wizard so you can compile your own plugins!

%description -l ru_RU.UTF-8
Code::Blocks это свободная IDE для C++, которая создана для
удовлетворения множества требований её пользователей.
Она разрабатывалась с самого начала, как расширяемая
и легко настраиваемая. Собранная с поддержкой плагинов
Code::Blocks может быть расширена с помощью подключаемых библиотек.

%package contrib
Summary: Code::Blocks contrib plugins
Summary(ru_RU.UTF-8): Дополнительные плагины для Code::Blocks
Group: Development/C++
Requires: codeblocks = %{version}-%{release}

%description contrib
Additional Code::Blocks plugins.

%description contrib -l ru_RU.UTF-8
Набор дополнительных плагинов для среды разработки Code::Blocks.

%package devel
Summary: Code::Blocks SDK
Group: Development/C++
Requires: codeblocks = %{version}-%{release}

%description devel
Code::Blocks SDK to develop your own plugins.

%description devel -l ru_RU.UTF-8
SDK для создания собственных плагинов к среде разработки Code::Blocks.

%define pkgdata %_datadir/%name

%prep
%setup -q -n %name -a 1
cp %SOURCE3 src/mime/
cp %SOURCE4 .

%patch0 -p1
%patch1 -p1

# Script update_revision.sh generates file revision.m4 that contains info about svn revision.
# It takes data from .svn directory. Since we haven't this directory in %SOURCE0, we should remove
# this script and create correct file revision.m4 instead.
rm update_revision.sh
echo "m4_define([SVN_REV], %{revision})" > revision.m4
echo "m4_define([SVN_REVISION], %{version})" >> revision.m4
echo "m4_define([SVN_DATE], `date +'%%F %%T'`)" >> revision.m4

%build
msgfmt %name.po -o %name.mo
./bootstrap
%configure --with-contrib-plugins=all
%make_build

%install
%make_install DESTDIR=%buildroot install
install -m 644 -D alt-icons/16x16/%name.png %buildroot%_miconsdir/%name.png
install -m 644 -D alt-icons/32x32/%name.png %buildroot%_niconsdir/%name.png
install -m 644 -D alt-icons/48x48/%name.png %buildroot%_liconsdir/%name.png
install -m 644 -D alt-icons/64x64/%name.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -m 644 -D %name.mo %buildroot%pkgdata/locale/ru_RU/%name.mo

%files
%doc README COPYING AUTHORS BUGS COMPILERS TODO NEWS
%_bindir/%name
%_bindir/cb_console_runner
%_libdir/libcodeblocks.so.*
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml
%_mandir/man?/*
%dir %pkgdata
%{pkgdata}/abbreviations.zip
%{pkgdata}/astyle.zip
%{pkgdata}/autosave.zip
%{pkgdata}/classwizard.zip
%{pkgdata}/codecompletion.zip
%{pkgdata}/compiler.zip
%{pkgdata}/debugger.zip
%{pkgdata}/defaultmimehandler.zip
%{pkgdata}/IncrementalSearch.zip
%{pkgdata}/manager_resources.zip
%{pkgdata}/resources.zip
%{pkgdata}/scriptedwizard.zip
%{pkgdata}/start_here.zip
%{pkgdata}/todo.zip
%{pkgdata}/Valgrind.zip
%{pkgdata}/tips.txt
%{pkgdata}/icons
%dir %{pkgdata}/images
%{pkgdata}/images/*.png
%{pkgdata}/images/16x16
%{pkgdata}/images/codecompletion
%{pkgdata}/images/settings
%{pkgdata}/lexers
%{pkgdata}/locale
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libabbreviations.*
%{_libdir}/%{name}/plugins/libastyle.*
%{_libdir}/%{name}/plugins/libautosave.*
%{_libdir}/%{name}/plugins/libclasswizard.*
%{_libdir}/%{name}/plugins/libcodecompletion.*
%{_libdir}/%{name}/plugins/libcompiler.*
%{_libdir}/%{name}/plugins/libdebugger.*
%{_libdir}/%{name}/plugins/libdefaultmimehandler.*
%{_libdir}/%{name}/plugins/libIncrementalSearch.*
%{_libdir}/%{name}/plugins/libscriptedwizard.*
%{_libdir}/%{name}/plugins/libtodo.*
%{_libdir}/%{name}/plugins/libValgrind.*
%{pkgdata}/scripts
%{pkgdata}/templates
%_iconsdir/*/*/*/*
%_pixmapsdir/*

%files contrib
%_bindir/cb_share_config
%_bindir/codesnippets
%_libdir/libwxsmithlib.so.*
%_libdir/%{name}/wxContribItems
%{pkgdata}/AutoVersioning.zip
%{pkgdata}/BrowseTracker.zip
%{pkgdata}/byogames.zip
%{pkgdata}/cb_koders.zip
%{pkgdata}/Cccc.zip
%{pkgdata}/codesnippets.zip
%{pkgdata}/CppCheck.zip
%{pkgdata}/codestat.zip
%{pkgdata}/copystrings.zip
%{pkgdata}/Cscope.zip
%{pkgdata}/DoxyBlocks.zip
%{pkgdata}/dragscroll.zip
%{pkgdata}/EditorTweaks.zip
%{pkgdata}/envvars.zip
%{pkgdata}/exporter.zip
%{pkgdata}/FileManager.zip
%{pkgdata}/help_plugin.zip
%{pkgdata}/HexEditor.zip
%{pkgdata}/headerfixup.zip
%{pkgdata}/keybinder.zip
%{pkgdata}/lib_finder.zip
%{pkgdata}/MouseSap.zip
%{pkgdata}/NassiShneiderman.zip
%{pkgdata}/openfileslist.zip
%{pkgdata}/projectsimporter.zip
%{pkgdata}/Profiler.zip
%{pkgdata}/RegExTestbed.zip
%{pkgdata}/ReopenEditor.zip
%{pkgdata}/SpellChecker.zip
%{pkgdata}/SymTab.zip
%{pkgdata}/ThreadSearch.zip
%{pkgdata}/ToolsPlus.zip
%{pkgdata}/wxsmith.zip
%{pkgdata}/wxSmithAui.zip
%{pkgdata}/wxsmithcontribitems.zip
%{pkgdata}/images/codesnippets
%{pkgdata}/images/DoxyBlocks
%{pkgdata}/images/ThreadSearch
%{pkgdata}/images/wxsmith
%{pkgdata}/lib_finder
%{pkgdata}/SpellChecker
%{_libdir}/%{name}/plugins/libAutoVersioning.*
%{_libdir}/%{name}/plugins/libBrowseTracker.*
%{_libdir}/%{name}/plugins/libbyogames.*
%{_libdir}/%{name}/plugins/libcb_koders.*
%{_libdir}/%{name}/plugins/libCccc.*
%{_libdir}/%{name}/plugins/libcodesnippets.*
%{_libdir}/%{name}/plugins/libcodestat.*
%{_libdir}/%{name}/plugins/libcopystrings.*
%{_libdir}/%{name}/plugins/libCppCheck.*
%{_libdir}/%{name}/plugins/libCscope.*
%{_libdir}/%{name}/plugins/libDoxyBlocks.*
%{_libdir}/%{name}/plugins/libdragscroll.*
%{_libdir}/%{name}/plugins/libEditorTweaks.*
%{_libdir}/%{name}/plugins/libenvvars.*
%{_libdir}/%{name}/plugins/libexporter.*
%{_libdir}/%{name}/plugins/libFileManager.*
%{_libdir}/%{name}/plugins/libhelp_plugin.*
%{_libdir}/%{name}/plugins/libHexEditor.*
%{_libdir}/%{name}/plugins/libheaderfixup.*
%{_libdir}/%{name}/plugins/libkeybinder.*
%{_libdir}/%{name}/plugins/liblib_finder.*
%{_libdir}/%{name}/plugins/libMouseSap.*
%{_libdir}/%{name}/plugins/libNassiShneiderman.*
%{_libdir}/%{name}/plugins/libopenfileslist.*
%{_libdir}/%{name}/plugins/libprojectsimporter.*
%{_libdir}/%{name}/plugins/libProfiler.*
%{_libdir}/%{name}/plugins/libRegExTestbed.*
%{_libdir}/%{name}/plugins/libReopenEditor.*
%{_libdir}/%{name}/plugins/libSpellChecker.*
%{_libdir}/%{name}/plugins/libSymTab.*
%{_libdir}/%{name}/plugins/libThreadSearch.*
%{_libdir}/%{name}/plugins/libToolsPlus.*
%{_libdir}/%{name}/plugins/libwxsmith.*
%{_libdir}/%{name}/plugins/libwxSmithAui.*
%{_libdir}/%{name}/plugins/libwxsmithcontribitems.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Thu May 17 2012 Denis Kirienko <dk@altlinux.org> 10.05.7966-alt1
- SVN snapshot 7966

* Tue Apr 17 2012 Denis Kirienko <dk@altlinux.org> 10.05.7932-alt1
- SVN snapshot 7932

* Sat Apr 07 2012 Denis Kirienko <dk@altlinux.org> 10.05.7917-alt1
- SVN snapshot 7917

* Sat Jan 07 2012 Denis Kirienko <dk@altlinux.org> 10.05.7678-alt1
- SVN snapshot 7678

* Sat Aug 27 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7385-alt1
- SVN snapshot 7385
- Added SpellChecker plugin

* Fri Jul 22 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7289-alt1
- SVN snapshot 7289

* Thu Jun 30 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7259-alt1
- SVN snapshot 7259

* Sun May 15 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7143-alt1
- SVN snapshot 7143

* Sun Apr 03 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7075-alt1
- SVN snapshot 7075

* Fri Mar 11 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7040-alt1
- SVN snapshot 7040

* Wed Feb 23 2011 Denis Kirienko <dk@altlinux.ru> 10.05.7017-alt1
- SVN snapshot 7017
- Added FileManager and ToolsPlus plugins

* Wed Jan 26 2011 Denis Kirienko <dk@altlinux.ru> 10.05.6931-alt1
- SVN snapshot 6931
- Added ReopenEditor plugin

* Fri Dec 24 2010 Denis Kirienko <dk@altlinux.ru> 10.05.6900-alt2
- Fixed bug in the CodeComplition plugin
- Added EditorTweaks plugin

* Sun Dec 19 2010 Denis Kirienko <dk@altlinux.ru> 10.05.6900-alt1
- SVN snapshot 6900
- Fixed license (closes: 23731)

* Sun Nov 14 2010 Denis Kirienko <dk@altlinux.ru> 10.05.6846-alt1
- SVN snapshot 6846
- Added new plugins: abbreviations, Cscope, DoxyBlocks, NassiShneiderman
- Updated russian translation

* Mon Jun 21 2010 Denis Kirienko <dk@altlinux.ru> 10.05-alt1
- New version 10.05
- Updated russian translation

* Sun May 23 2010 Denis Kirienko <dk@altlinux.ru> 8.02.6271-alt1
- SVN snapshot 6271

* Sun Feb 28 2010 Denis Kirienko <dk@altlinux.ru> 8.02.6181-alt1
- SVN snapshot 6181
- Updated russian translation

* Sat Feb 13 2010 Denis Kirienko <dk@altlinux.ru> 8.02-alt24
- SVN snapshot 6155
- Updated russian translation

* Wed Jan 13 2010 Denis Kirienko <dk@altlinux.ru> 8.02-alt23
- SVN snapshot 6080
- Added Cccc and CppCheck plugins
- Updated russian translation

* Wed Nov 11 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt22
- SVN snapshot 5911
- Updated russian translation

* Sun Oct 18 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt21
- Updated russian translation

* Sat Oct 10 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt20
- SVN snapshot 5859
- Updated russian translation
- Added MouseSap plugin

* Sun Sep 27 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt19
- Updated russian translation

* Sun Sep 06 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt18
- Updated russian translation

* Mon Aug 24 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt17
- Rebuid with wxGTK-2.8.10-alt2 (see #20451)

* Sun Aug 23 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt16
- Updated russian translation
- Added dependencies to gcc, gcc-c++, gdb, xterm

* Sat Aug 22 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt15
- Added russian translation (yet unfinished)

* Tue Aug 18 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt14
- SVN snapshot 5731

* Thu Jul 30 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt13
- SVN snapshot 5716
- Added wxSmithAui plugin to codeblocks-contrib package

* Sun Jun 21 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt12
- SVN snapshot 5678

* Mon Jun 15 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt11
- Rebuild with wxGTK-2.8.9-alt2 (fix #20450)

* Sat Jun 06 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt10
- SVN snapshot 5616

* Tue May 19 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt9
- SVN snapshot 5602

* Sat May 02 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt8
- SVN snapshot 5535
- Added copystrings plugin to codeblocks-contrib package

* Sun Apr 12 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt7
- SVN snapshot 5489

* Sun Feb 15 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt6
- SVN snapshot 5456
- Removed QtWorkbench plugin (see http://code.google.com/p/qtworkbench/issues/detail?id=20)

* Sat Feb 07 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt5
- SVN snapshot 5432
- Compressed ChangeLog

* Fri Jan 09 2009 Denis Kirienko <dk@altlinux.ru> 8.02-alt4
- SVN snapshot 5382
- Added IncrementalSearch and Valgrind plugins to codeblocks package
- Added HexEditor and headerfixup plugins to codeblocks-contrib package
- QtWorkbench plugin updated to version 0.6.0-alpha (SVN 146)

* Sat Nov 29 2008 Denis Kirienko <dk@altlinux.ru> 8.02-alt3
- Really updated codeblocks.desktop

* Mon Nov 24 2008 Denis Kirienko <dk@altlinux.ru> 8.02-alt2
- Spec cleanup
- Updated codeblocks.desktop

* Sun Mar 02 2008 Denis Kirienko <dk@altlinux.ru> 8.02-alt1
- Stable release 8.02
- Added BrowseTracker plugin

* Sun Jan 13 2008 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4807
- New SVN snapshot
- Added ThreadSearch plugin

* Sat Dec 22 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4742
- New SVN snapshot
- Added openfilelist plugin
- Added AutoVersioning plugin

* Sat Sep 08 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4439
- New SVN snapshot
- Added QtWorkbench plugin

* Sun Aug 26 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4405
- New SVN snapshot

* Sat Aug 04 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4346
- New SVN snapshot
- Added projectsimporter plugin

* Sat Jun 30 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4193
- New SVN snapshot

* Sun Jun 17 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn4101
- New SVN snapshot
- Removed wxRE_ADVANCED patch (no more needed)

* Tue May 01 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3910
- New SVN snapshot
- Updated patches
- Added patch that fixes undefined symbol wxRE_ADVANCED error during build
- Added libwxsmith as a contrib package

* Wed Jan 10 2007 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3450
- New SVN snapshot
- Automatical creation of revision.m4 file before configure
- Added --enable-contrib option to the configure
- Splitted into three separate packages: codeblocks, codeblocks-contrib, codeblocks-devel
- Added set of icons according to requirements of new iconpaths policy

* Fri Nov 24 2006 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3258
- New SVN snapshot

* Fri Oct 06 2006 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn3025
- New SVN snapshot

* Sat Sep 14 2006 Denis Kirienko <dk@altlinux.ru> 1.0-alt0.svn2975
- New maintainer
- New SVN snapshot
- Fixed Icon parameter in the desktop file
- Fixed Qt4 application wizard

* Wed Jan 04 2006 php-coder <php-coder@altlinux.ru> 1.0-alt0.svn1652
- Initial build for ALT Linux Sisyphus
- Added patch which fixes some warnings from compiler
