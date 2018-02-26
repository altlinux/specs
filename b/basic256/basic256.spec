Name: basic256
Version: 0.9.6
Release: alt6
URL: http://kidbasic.sourceforge.net
Source: http://ovh.dl.sourceforge.net/sourceforge/kidbasic/%name-%version.tar.gz
Source1: basic256.desktop
Source2: basic256_32.png
Patch0: basic256-0.9.6-alt-fix-say-function.patch

License: GPL
Group: Development/Other
Packager: Sergey Irupin <lamp@altlinux.org>

BuildRequires: libqt4-devel libSDL-devel libSDL_mixer-devel libsqlite3-devel gcc-c++ flex bison

Summary: Simple BASIC IDE that allows young children to learn to programming

%description
BASIC-256 is a simple BASIC IDE that allows young children to learn to program. 
It was written in response to David Brin's article, "Why Johnny Can't Code," 
in which he bemoans the lack of a simple, line-oriented programming language 
for children that runs on modern computers. It features a byte-code compiler 
and interpreter, a debugger, easy to use graphical and text output, and an editor.

%prep
%setup
cd trunk
%patch0 -p1

%build
cd trunk
%add_optflags -D_REENTRANT
%_libdir/qt4/bin/qmake
%make_build CXXFLAGS="%optflags \$(DEFINES)"
%_libdir/qt4/bin/lrelease Translations/*.ts

%install
mkdir -p %buildroot%_datadir/%name/Examples
mkdir -p %buildroot%_datadir/%name/help
cd trunk
install -D BASIC256 %buildroot%_bindir/BASIC256
install Translations/*.qm %buildroot%_datadir/%name/
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D %SOURCE2 %buildroot%_niconsdir/%name.png
cp -r Examples %buildroot%_datadir/%name/
cp -r ./../doc/en/ %buildroot%_datadir/%name/help/
cp -r ./../doc/ru/ %buildroot%_datadir/%name/help/

%files
%doc trunk/CONTRIBUTORS trunk/license.txt trunk/ChangeLog
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_niconsdir/%name.png

%changelog
* Mon Jan 10 2011 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt6
- Updated to 0.9.6.58.

* Mon Dec 20 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt5
- Check and correct the syntax highlighting keywords
- Added buttons back, forward, home, exit - in the help window

* Wed Dec 15 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt4
- Updated to 0.9.6.53.
- Fixed Group and CXXFLAGS.
- Make new patch for say function.

* Sun Dec 12 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt3
- Updated to 0.9.6.51 - add sqr() and exp() functions.
- Help files (ru|en) updated.

* Fri Dec 03 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt2
- Updated to 0.9.6.49.
- Russian translation and help files (ru|en) updated.

* Thu Nov 04 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt1
- Updated to 0.9.6w.
- Russian translation updated.
- Fixed locale problem and seek, lower, upper statements.
- Change help system and add russian help.
- Change some icons toolbar.

* Wed Apr 10 2010 Sergey Irupin <lamp@altlinux.org> 0.9.5-alt1
- Updated to 0.9.5.
- Russian translation updated.

* Tue Sep 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt4
- Fixed build.

* Sat Mar 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt3
- Packaged examples.

* Sat Mar 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt2
- Enable non-ASCII strings.
- Added .desktop file.

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt1
- Initial build for ALT Linux.
- Russian translation added.
- Search for translation in %%_datadir/%%name.
