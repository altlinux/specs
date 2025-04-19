%global optflags_lto %nil

Name: libtranslate
Version: 0.99
Release: alt4

Summary: library for translating text

License: See COPYING
Group: Development/C
Url: http://www.nongnu.org/libtranslate/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: %name-services.xml

Patch1: libtranslate-0.99-charsetparse.diff
Patch2: libtranslate-0.99-condfix.diff
Patch3: libtranslate-ds-memory.patch
Patch4: libtranslate-ds-empty.patch
Patch5: libtranslate-ds-promt.patch
Patch6: libtranslate-ds-fixcharset.patch
Patch7: libtranslate-ds-timed.patch
Patch8: libtranslate-talkfilter-stdlib.patch
Patch9: libtranslate-cli-unresolved.patch

BuildRequires: gcc-c++ glib2-devel libgcrypt-devel libgnutls-devel libgpg-error-devel libsoup22-devel
BuildRequires: libtalkfilters-devel libtasn1-devel libxml2-devel perl-XML-Parser zlib-devel
BuildRequires: intltool gtk-doc

%description
libtranslate is a library for translating text and web pages
between natural languages. Its modular infrastructure allows
to implement new translation services separately from the core
library.

%package devel
Summary: Header files for libtranslate
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for libtranslate.

%prep
%setup -q

%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1

%build
%autoreconf -I m4
%configure \
	--disable-static \
	--enable-generic \
	--enable-talkfilters
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make DESTDIR=%buildroot install

install -m 644 %SOURCE1 %buildroot%_datadir/%name/services.xml
 
%find_lang %name

%files -f %name.lang
%doc COPYING README
%_bindir/*
%_libdir/*.so.*
%_libdir/%name
%_datadir/%name
%_man1dir/*
%_man5dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/*

%changelog
* Sat Apr 19 2025 L.A. Kostis <lakostis@altlinux.ru> 0.99-alt4
- Fix FTBFS:
  + disable LTO
  + update BR
  + talkfilter: fix detection.
  + cli: fix unresolved symbols.

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99-alt3.qa2
- Removed bad RPATH

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99-alt3.qa1.1
- Rebuilt for debuginfo

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.99-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Mar 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt2
- rebuild with libsoup-2.4.0

* Mon Oct 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt1
- added patches on Suren A. Chilingaryan

* Tue Feb 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt0.1
- first build for ALT Linux Sisyphus
