Name: librcc
Version: 0.2.13
Release: alt1

Summary: RusXMMS Charset Conversion Library
License: GPLv2+
Group: System/Libraries
Url: http://rusxmms.sourceforge.net
Packager: Nick S. Grechukh <gns@altlinux.org>

Source: %name-%version.tar
Patch: librcc-0.2.12-alt-gtk3_build.patch

BuildRequires: gcc-c++ libenca-devel libgtk+2-devel libgtk+3-devel
BuildRequires: librcd-devel libxml2-devel libtranslate-devel libguess-devel
BuildRequires: libaspell-devel libdb4-devel

%description
RusXMMS Charset Conversion Library.

%package gtk2
Group: Development/Other
Summary: RusXMMS Encoding Conversion Library GTK2 bindings

%description gtk2
This package contains %name GTK2 bindings.

%package gtk3
Group: Development/Other
Summary: RusXMMS Encoding Conversion Library GTK3 bindings

%description gtk3
This package contains %name GTK3 bindings.

%package devel
Group: Development/Other
Summary: RusXMMS Encoding Conversion Library header files
Requires: %name = %version-%release

%description devel
This package contains %name header files.

%prep
%setup
%patch

%build
%autoreconf
%configure \
	--enable-bdb \
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

%files gtk2
%_libdir/librccgtk2.so.*
%_bindir/rcc-gtk2-config

%files gtk3
%_libdir/librccgtk3.so.*
%_bindir/rcc-gtk3-config

%files devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/lib*.so

%changelog
* Tue Apr 18 2023 L.A. Kostis <lakostis@altlinux.ru> 0.2.13-alt1
- 0.2.13.
- Update License tag.

* Wed Mar 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.12-alt3
- Rebuilt without gtk+.

* Mon Jan 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt2
- enabled multilanguage support with DB4
- enabled language autodetection using aspell
- new gtk3 subpackage
- built with libguess.so.1

* Fri Dec 06 2013 Michael Shigorin <mike@altlinux.org> 0.2.12-alt1
- 0.2.12
- dropped patches
  + patch0 and patch1 merged upstream
  + patch2 fails to apply now
- added pkgconfig file
- avoid needless compression

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
