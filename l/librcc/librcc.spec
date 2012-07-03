Summary: RusXMMS Charset Conversion Library
Name: librcc
Version: 0.2.9
Release: alt1.3
License: GPL
Group: System/Libraries
URL: http://rusxmms.sourceforge.net
Source: %name-%version.tar.bz2
Patch: librcc-0.2.9-alt-fixes.patch
Patch1: librcc-0.2.9-alt-glib2-2.32.0.patch
Patch2: librcc-0.2.9-alt-DSO.patch
Packager: Nick S. Grechukh <gns@altlinux.org>

BuildRequires: gcc-c++ gtk+-devel libenca-devel libgtk+2-devel librcd-devel libxml2-devel
BuildRequires: libtranslate-devel libguess-devel

%description
RusXMMS Charset Conversion Library.

%package gtk
Group: Development/Other
Summary: RusXMMS Encoding Conversion Library GTK1 bindings

%description gtk
This package contains %name GTK1 bindings.

%package gtk2
Group: Development/Other
Summary: RusXMMS Encoding Conversion Library GTK2 bindings

%description gtk2
This package contains %name GTK2 bindings.

%package devel
Group: Development/Other
Summary: RusXMMS Encoding Conversion Library header files
Requires: %name = %version-%release

%description devel
This package contains %name header files.

%prep
%setup
%patch -p1
%patch1 -p2
%patch2 -p2

%build
%autoreconf
%configure \
	--disable-bdb \
	--disable-static

%make_build
%make -C examples

%install
%makeinstall_std
%makeinstall_std -C examples

install -pD -m644 examples/rcc.xml %buildroot%_sysconfdir/rcc.xml

rm -f %buildroot%_bindir/example*
find %buildroot%_libdir/rcc/engines -depth -name \*.la -delete

%files
%doc AUTHORS NEWS README examples/rcc-example.xml
%_sysconfdir/rcc.xml
%_libdir/librcc.so.*
%_libdir/librccui.so.*
%_libdir/rcc

%files gtk
%_libdir/librccgtk.so.*
%_bindir/rcc-gtk-config

%files gtk2
%_libdir/librccgtk2.so.*
%_bindir/rcc-gtk2-config

%files devel
%_includedir/*
%_libdir/lib*.so

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.3
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.2
- Fixed build with new glib2

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.1
- Rebuilt for debuginfo

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.2.9-alt1
- Updated to 0.2.9.

* Mon Jul 13 2009 Nick S. Grechukh <gns@altlinux.org> 0.2.6-alt4
- build fixed (incorrect strnlen redefinition)
- recoding cache disabled (#20753)

* Fri Apr 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt3
- disable aspell

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Aug 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt4
- rebuild with libdb4-4.7

* Sat May 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt3
- rebuild with libdb4-4.6

* Mon Oct 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt2
- build with libtranslate and libguess

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Fri May 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Sun Dec 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt3
- added librcc-0.2.3-libdb4-perms-bug8752.patch

* Thu Jun 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt2
- fixed #9674

* Sun May 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt1
- cleanup spec
- fixed libdir
- disabled static
- fixed system config

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.3-alt0.5.1
- Rebuilt with libdb4.4.

* Thu Jan 12 2006 Nick S. Grechukh <gns@altlinux.org> 0.2.3-alt0.5
- new version

* Sat Aug 13 2005 Nick S. Grechukh <gns@altlinux.ru> 0.2.0-alt0.5
- initial build for Sisyphus
