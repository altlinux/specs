Name: libgadu
Version: 1.11.0
Release: alt1

Summary: Library for Handling of Gadu-Gadu Instant Messaging
License: LGPLv2.1
Group: System/Libraries
Url: http://toxygen.net/libgadu/

Source: %name-%version.tar.gz

BuildRequires: doxygen libgnutls-devel libxml2-devel zlib-devel

%description
libgadu is a library for handling of protocol of a popular Polish
instant messenger Gadu-Gadu.

%package devel
Group: Development/C
Summary: Library for Handling of Gadu-Gadu Instant Messaging
License: LGPLv2.1
Requires: %name = %version-%release

%description devel
libgadu is a library for handling of protocol of a popular Polish
instant messenger Gadu-Gadu.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--without-bind \
	--without-openssl \
	--with-pthread

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog README
%_libdir/lib*.so.*

%files devel
%doc docs/protocol.html docs/html
%_includedir/*.h
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Jun 08 2011 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- 1.10.1
- build with gnutls

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.1
- Rebuilt for soname set-versions

* Sat May 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.8.2-alt1
- 1.8.1 -> 1.8.2

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.8.1-alt2
- apply patch from repocop

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 1.8.1-alt1
- 1.8.0 -> 1.8.1

* Wed Apr 23 2008 Igor Zubkov <icesik@altlinux.org> 1.8.0-alt1
- build for Sisyphus

* Sat Mar 08 2008 crrodriguez@suse.de
- update to version 1.8.0
  * for details see  http://toxygen.net/libgadu/releases/1.8.0.html
  (in polish, no english changelog available)
- disable static libraries
* Fri May 11 2007 aj@suse.de
- Remove duplicate post/postun sections.
* Thu May 10 2007 sbrabec@suse.cz
- New SuSE package, version 1.7.1.
