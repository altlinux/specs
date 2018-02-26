Name: libfontenc
Version: 1.1.1
Release: alt1
Summary: The fontenc Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-font-utils xorg-util-macros xorg-xproto-devel zlib-devel

%description
The fontenc Library

%package devel
Summary: The fontenc Library and Header Files
Group: Development/C
Requires: %name = %version-%release
Conflicts: XFree86-devel < 4.4 xorg-x11-devel <= 6.9.0

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-encodingsdir=%_datadir/X11/fonts/encodings \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/X11/fonts
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Mar 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Apr 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2
- rebuild for debuginfo

* Thu Oct 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Aug 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Apr 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt5
- CVS snapshot 2006-04-10

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- fixed requires for %name-devel

* Mon Jan 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- added cp1251 patch

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

