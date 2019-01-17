
Name: libgadu
Version: 1.12.2
Release: alt1

Summary: Library for Handling of Gadu-Gadu Instant Messaging
License: LGPLv2.1
Group: System/Libraries
Url: http://toxygen.net/libgadu/

Source: %name-%version.tar

BuildRequires: doxygen
BuildRequires: libgnutls-devel >= 2.10.0
BuildRequires: libxml2-devel  >= 2.2.3
BuildRequires: zlib-devel
BuildRequires: libprotobuf-c-devel >= 1.0.0 protobuf-c-compiler

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
%autoreconf
%configure \
	--disable-static \
	--with-gnutls-system-trust-store=/usr/share/ca-certificates/ca-bundle.crt \
	--without-bind \
	--without-openssl


%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog README
%_libdir/lib*.so.*

%files devel
%doc docs/protocol.html docs/html
%_includedir/*.h
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.2-alt1
- 1.12.2

* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt2
- rebuild with new gnutls

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Tue May 06 2014 Alexey Shabalin <shaba@altlinux.ru> 1.11.3-alt1
- 1.11.3

* Fri Sep 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1.11.2-alt1
- 1.11.2

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
