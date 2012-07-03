
Summary: Exploring Euclidean geometry 
Name:    kseg	
Version: 0.403
Release: alt2.qa2

License: GPL
Url:     http://www.mit.edu/~ibaran/%name.html	
Source:  http://www.mit.edu/~ibaran/%name-%version.tar.gz
Group:   Education
Packager: Fr. Br. George <george@altlinux.ru>

Source1: %name.desktop
Source2: %name.png

Patch1: %name-setFilePath.patch
Patch2: %name-KSEG_HOME.patch

%define _appdir %_datadir/%name

# Automatically added by buildreq on Fri Jun 08 2007
BuildRequires: gcc-c++ libXext-devel libqt3-devel

BuildRequires: libqt3-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils

Requires: libgtk+2-common

%description
KSEG is a Linux program for exploring Euclidean geometry. 
KSEG was inspired by the Geometer's Sketchpad, but plans 
are to go beyond the functionality that it provides. 


%prep
%setup -q -n %name
%patch1 -p1
%patch2 -p1

%build
qmake-qt3

%make KSEG_HOME="%_appdir"


%install
mkdir -p %buildroot%_appdir/{examples,pics,lang} %buildroot%_bindir
install -p -m755 %name %buildroot%_bindir/
install -p -m644 *.qm *.html %buildroot%_appdir/lang/
install -p -m644 examples/* %buildroot%_appdir/examples/ 	
install -p -m644 pics/*	 %buildroot%_appdir/pics/

install -p -D -m644 %SOURCE2 %buildroot%_datadir/icons/hicolor/32x32/apps/%name.png

desktop-file-install \
   --dir %buildroot%_datadir/applications \
   --vendor="ALT Linux" \
   %SOURCE1


%files
%doc AUTHORS COPYING README*
%_bindir/*
%_appdir/
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*


%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.403-alt2.qa2
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for kseg
  * update_menus for kseg
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.403-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for kseg

* Sun Sep 23 2007 Fr. Br. George <george@altlinux.ru> 0.403-alt2
- Desktop file fixed

* Fri Jun 08 2007 Fr. Br. George <george@altlinux.ru> 0.403-alt1
- Initial build from FC

* Fri Apr 14 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.403-1
- 0.403

* Mon Nov 07 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.402-1
- 0.402

* Thu Jul 15 2004 Rex Dieter <rexdieter at sf.net> 0:0.401-0.fdr.1
- 0.401

* Fri Mar 26 2004 Rex Dieter <rexdieter at sf.net> 0:0.4-0.fdr.2
- autodetect qt version
- cleanup desktop-file handling

* Mon Jan 12 2004 Rex Dieter <rexdieter at sf.net> 0:0.4-0.fdr.1
- patch for gcc33(FC1)
- (BuildRequires) qt-3.2

* Fri May 16 2003 Rex Dieter <rexdieter at sf.net> 0:0.4-0.fdr.0
- first try at 0.4 

