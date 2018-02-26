Name: libXft
Version: 2.3.1
Release: alt1

Summary: X FreeType Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: fontconfig-devel libXrender-devel libfreetype-devel xorg-util-macros

%description
X FreeType Library

%package devel
Summary: X FreeType Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/X11/Xft
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Sun Jun 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Mar 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.2.0-alt3
- rebuild

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.2.0-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.1.14-alt1
- 2.1.14

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.13-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.13-alt1
- 2.1.13

* Mon May 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.12-alt5
- update lcd filter patch from ubuntu

* Wed Apr 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.12-alt4
- reapply subpixel rendering patch

* Sat Feb 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.12-alt3
- drop subpixel rendering patch

* Wed Oct 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.1.12-alt2
- merged SuSE patches

* Fri Dec 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.12-alt1
- 2.1.12:
  + XftNameUnparse: re-export to public API

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.11-alt1
- 2.1.11

* Sun Sep 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt1
- 2.1.10

* Mon Jul 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt3
- removed subpixel rendering patch

* Thu Jul 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt2
- added libXft-2.1.9-git-coverity.patch

* Sat Jun 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt1
- 2.1.9

* Thu May 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8.2-alt5
- added subpixel rendering patch

* Wed Apr 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8.2-alt4
- rebuild

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8.2-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8.2-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8-alt0.1
- initial build

