#define svndate 20100621

Name: epdfview
Version: 0.1.8
Release: alt1.2

Summary: ePDFView is a simple and lightweight PDF viewer
Group: Office
Source: %name-%version.tar.bz2

License: GPL
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.emma-soft.com/projects/epdfview/
Patch1: alt-epdfview-fixbuild.patch
Patch2: alt-fix-ru-translation.patch
Patch3: alt-fix-desktop-file.patch
#Patches from Mandriva
Patch11: mdk-epdfview-0.1.6-fix-compile.patch
Patch12: mdk-epdfview-0.1.6-fix-printing.patch

Patch10: epdfview-poppler-0.15.patch
Patch20: epdfview-0.1.7-poppler-changeset_r357.patch
Patch21: epdfview-0.1.8-alt-glib2-2.32.0.patch

BuildRequires: desktop-file-utils libgtk+2-devel

# Automatically added by buildreq on Mon May 19 2008
BuildRequires: doxygen gcc-c++ libcups-devel libpoppler-glib-devel

%description
ePDFView is a free lightweight PDF document viewer using Poppler and GTK+ libraries.

The aim of ePDFView is to make a simple PDF document viewer, in the lines of Evince but without using the Gnome libraries.

%prep
%setup -q
%patch1 -p1
#patch10 -p0
#patch20 -p0
#patch2 -p1
#patch3 -p1

#patch11 -p1
#patch12 -p1
%patch21 -p2

%build
#/autogen.sh
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_man1dir/%{name}*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.2
- Fixed build with new glib2

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.1
- Fixed build

* Sat Jun 11 2011 Ilya Mashkin <oddity@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Mon May 10 2011 Ilya Mashkin <oddity@altlinux.ru> 0.1.7-alt4.20100621
- try to fix SIGSEGV (#25590)

* Fri May 06 2011 Ilya Mashkin <oddity@altlinux.ru> 0.1.7-alt3.20100621
- build from svn with FC patch

* Sun Oct 17 2010 Ilya Mashkin <oddity@altlinux.ru> 0.1.7-alt2
- rebuild with poppler7

* Fri Jul 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.6-alt2
- fix build
- remove post scripts
- fix desktop file

* Mon May 19 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.6-alt1
- fix build fix new libpoppler

* Sat Oct 13 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.6-alt0.1.1
- Rebuilt due to libpoppler-glib.so.1 -> libpoppler-glib.so.2 soname change.

* Mon Apr 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.1.6-alt0.1
- first build

