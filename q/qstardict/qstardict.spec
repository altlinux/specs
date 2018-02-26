Name: qstardict
Version: 1.0.1
Release: alt1

Summary: QStarDict Qt4 clone of StarDict
License: GPLv2
Group: System/Internationalization
Url: http://qstardict.ylsoftware.com
Source: %name-%version.tar
Patch0: %name-1.0-alt-glib2-2.32.0.patch
Packager: Evgenii Terechkov <evg@altlinux.ru>

# Automatically added by buildreq on Fri Jun 13 2008
BuildRequires: gcc-c++ glib2-devel libqt4-devel

BuildRequires: desktop-file-utils

Provides: stardict = 2.4.5

%description
QStarDict Qt4 clone of StarDict.

%prep
%setup
%patch0 -p2
find . -type f -name '*.pro' |while read f; do
echo 'QMAKE_CXXFLAGS += %optflags' >> $f
done

%build
qmake-qt4 PLUGINS_DIR=%_libdir/%name/plugins
make

%install
make install INSTALL_ROOT=%buildroot
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=TextTools \
	--add-category=Office \
	%buildroot%_desktopdir/qstardict.desktop

%files
%_bindir/%name
%_datadir/%name
%_libdir/%name
%_desktopdir/*.desktop
%_pixmapsdir/%name.png

%doc AUTHORS ChangeLog README THANKS 

%changelog
* Mon May 28 2012 Terechkov Evgenii <evg@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1.2
- rebuilt with rpm optflags

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build with new glib2

* Thu Jul  7 2011 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- 1.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.13.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qstardict

* Fri May  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt2
- Build with gcc4.4 fixed

* Wed Feb 25 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt1.1
- Provide: stardict added (closes #18960)

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Sun Feb  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13-alt1
- 0.13

* Sat Jun 14 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12.9-alt1.1
- Build for x86_64 fixed (brain-deat upstream defaults)

* Fri Jun 13 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12.9-alt1
- 0.12.9

* Sat Mar 29 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12-alt1
- 0.12

* Wed Mar 26 2008 Terechkov Evgenii <evg@altlinux.ru> 0.10-alt1
- 0.10

* Sun Mar 23 2008 Terechkov Evgenii <evg@altlinux.ru> 0.09-alt1
- 0.09

* Sat Sep 22 2007 Terechkov Evgenii <evg@altlinux.ru> 0.07-alt1
- 0.07
- License changed to GPLv2 (package relicensed)

* Tue Aug 14 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1.2
- Wrong Provides: tag removed (Shame on me!)

* Fri Aug 10 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1.1
- gpl3 changed to gpl3plus (due change to rpm-build-licenses)

* Sat Jul 28 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1
- 0.04

* Sun Jul  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.03-alt2
- "Fix" conflict with stardict-gtk (see #12267,#12268) by providing stardict=2.4.2

* Sun Jul  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.03-alt1
- Initial build for Sisyphus
