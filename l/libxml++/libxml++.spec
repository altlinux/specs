%def_disable static

Name: libxml++
Version: 1.0.5
Release: alt3.1

Summary: libxml++ is a C++ wrapper for the libxml XML parser library.
License: LGPL
Group: System/Libraries
Url: http://libxmlplusplus.sourceforge.net/

Source0: http://ftp.gnome.org/pub/GNOME/sources/libxml++/1.0/%name-%version.tar.bz2

Packager: Pavlov Konstantin <thresh@altlinux.ru>

BuildRequires: gcc-c++ libstdc++-devel libxml2-devel pkg-config zlib-devel

%description
libxml++ is a C++ wrapper for the libxml XML parser library.
It's original author is Ari Johnson and it is currently maintained
by Christophe de Vienne and Murray Cumming.

%package devel
Summary: Development files for libxml++
Group: Development/C
Requires: %name = %version-%release

%description devel
libxml++ is a C++ wrapper for the libxml XML parser library.
It's original author is Ari Johnson and it is currently maintained
by Christophe de Vienne and Murray Cumming.

This package contains the libraries, include and other files.

%package devel-static
Summary: Static library for building static applications with libxml++
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libxml++ is a C++ wrapper for the libxml XML parser library.
It's original author is Ari Johnson and it is currently maintained
by Christophe de Vienne and Murray Cumming.

This package contains the static library you can use to develop
statically linked applications.

%prep
%setup -q

%build
%__autoreconf
%configure \
	--disable-rpath \
	%{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog README
%_libdir/*.so.*

%files devel
%_includedir/%name-1.0
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt3.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxml++
  * postun_ldconfig for libxml++

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5-alt3
- Fix build with gcc 4.3.

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5-alt2
- spec cleanup.

* Sat Dec 31 2005 Igor Zubkov <icesik@altlinux.ru> 1.0.5-alt1
- 1.0.5
- spec clean and update buildrequires
- #5599

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.4-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Oct 18 2004 Dmitriy Porollo <spider@altlinux.ru> 1.0.4-alt1
- 1.0.4-alt1 release
