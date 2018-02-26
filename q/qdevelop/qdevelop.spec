Name:		qdevelop
Version:	0.28
Release:	alt3
Summary:	IDE dedicated to QT4
License:	GPLv2
Group:		Development/KDE and QT
Url:		http://qdevelop.org
Source0:	http://qdevelop.free.fr/download/%name-%version.tar.gz
Source1:	%{name}16.png
Source2:	%{name}32.png
Source3:	%{name}48.png
Source4:	%{name}64.png
Source5:	%name.desktop
Patch0:		%name-0.28-alt_translations-dir.diff
Patch1:		qdevelop_fix_ftbfs_qt47.patch

BuildPreReq:	cmake >= 2.4.3 cpack
BuildPreReq:	fontconfig gcc-c++ libqt4-devel libXext-devel
Requires:	gdb ctags libqt4-devel make qt4-designer libqt4-sql-sqlite
Requires:	%{get_dep libqt4-core}

%description
QDevelop is a development environment entirely dedicated to Qt4.
QDevelop requires Qt4, gcc under Linux or MinGW under Windows,
possibly gdb for programs debugging and ctags for code completion.
QDevelop is available in English, French, German, Dutch, Polish,
Spanish, Chinese and Russian. If you want to translate in your
language, please contact to author.
QDevelop is not a Kdevelop like or reduced. It's an independent
IDE dedicated to Qt and is totally independent of KDevelop.
Less complete, but faster, light and especially multi-platforms.
QDevelop and KDevelop have different code sources.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
subst 's|lib/qdevelop|%_lib/qdevelop|g' \
					CMakeLists.txt \
					plugins/formatting-astyle/astyleplugin.cpp \
					plugins/tools-regexp-planner/replugin.cpp \
					src/main.cpp \
					src/mainimpl.cpp
export PATH=$PATH:%_qt4dir/bin
cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_SKIP_RPATH=YES \
	-DAUTOPLUGINS=1 \
	-DCMAKE_CXX_FLAGS:STRING="%optflags"

%make_build

%install
%make DESTDIR=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
install -pD -m644 %SOURCE2 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -pD -m644 %SOURCE3 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -pD -m644 %SOURCE4 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -pD -m644 %SOURCE5 %buildroot%_desktopdir/%name.desktop
install -pD -m644 resources/images/logo.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%files
%doc {ChangeLog.txt,copying,README*}
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_datadir/%name
%dir %_datadir/%name/translations
%dir %_datadir/%name/translations/formatting-astyle
%dir %_datadir/%name/translations/tools-regexp-planner
%_bindir/*
%_libdir/%name/plugins/*.so
%_datadir/%name/translations/*/*.qm
%_datadir/%name/translations/*.qm
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%changelog
* Thu Jul 29 2010 Motsyo Gennadi <drool@altlinux.ru> 0.28-alt3
- added patch for qt4.7

* Sun May 30 2010 Motsyo Gennadi <drool@altlinux.ru> 0.28-alt2
- fix translation path

* Tue Mar 30 2010 Motsyo Gennadi <drool@altlinux.ru> 0.28-alt1
- 0.28

* Fri Mar 27 2009 Motsyo Gennadi <drool@altlinux.ru> 0.27.4-alt1
- 0.27.4

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.26.1-alt2
- delete post/postun scripts (new rpm)

* Tue Nov 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.26.1-alt1
- 0.26.1:
  + Fix many issues
  + The Replace widget is now embeded in editors as the Find widget.
  + Mac OS enhancements
  + Update the gui, now all dock windows are QDockWidget, and not widgets
  + Assistant can be started and controled with the version 4.4.0 of Qt. Works also with previous versions.

* Mon Oct 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.26-alt0.1.svn339
- new svn version (#17514 closed)

* Wed Dec 19 2007 Motsyo Gennadi <drool@altlinux.ru> 0.25-alt1
- new version released

* Wed Sep 05 2007 Motsyo Gennadi <drool@altlinux.ru> 0.24-alt1
- new version released

* Fri Jun 15 2007 Motsyo Gennadi <drool@altlinux.ru> 0.23-alt2.1
- add desktop-file

* Thu Jun 14 2007 Motsyo Gennadi <drool@altlinux.ru> 0.23-alt1.1 
- NMU
- build for Sisyphus

* Tue Jun 12 2007 Motsyo Gennadi <drool@altlinux.ru> 0.23-alt0.M40.2.1 
- build new version for M40

* Thu Dec 28 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.22-alt2.rev96
- fix buildreqs

* Wed Dec 27 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.22-alt1.rev96
- Sisyphus build
- 0.22-rev96
- spec cleanup
- remove qt4-assistant qt4-doc from Requires
- build using cmake

* Sat Dec 02 2006 Motsyo Gennadi <drool@altlinux.ru> 0.21-alt0.rev77.M24.3
- add qt4-assistant qt4-doc to Requires

* Thu Nov 30 2006 Motsyo Gennadi <drool@altlinux.ru> 0.21-alt0.rev77.M24.2
- add libqt4-sql-sqlite to Requires
- modify menu

* Wed Nov 29 2006 Motsyo Gennadi <drool@altlinux.ru> 0.21-alt0.rev77.M24.1
- initial build for ALT Linux 2.4 Master
