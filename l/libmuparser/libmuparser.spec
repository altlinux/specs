Name: libmuparser
Version: 1.32
Release: alt1.qa2

%define oname muparser
# 1.32 -> 132
%define oversion %(echo %version | sed -e "s|\\.||g")
%define tarname %{oname}_v%oversion

Summary: a fast math parser library

License: MIT
Group: System/Libraries
Url: http://muparser.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# It is new feature in etersoft-build-utils since 1.7.6: support commented real url (for rpmgs command)
# Source-url: http://prdownloads.sf.net/%oname/%oname/Version%%20%{version}/%tarname.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: gcc-c++

%description
The main objective of this project is to provide a fast and easy way
of doing this. muParser is an extensible high performance math parser
library. It is based on transforming an expression into a bytecode and
precalculating constant parts of it.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%prep
%setup
sed -i 's|^\(CXXFLAGS.*\)|\1 -g|' Makefile.in

%build
%configure --enable-shared=yes --disable-samples
%make_build

%install
%makeinstall_std

%files
%doc Changes.txt Credits.txt License.txt
%_libdir/%{name}*.so.*

%files devel
#doc examples
%_libdir/%name.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.32-alt1.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Mar 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.32-alt1
- new version 1.32
- moved to git, cleanup spec
- build without samples

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt2
- fix build with gcc 4.3
- remove post_ldconfig

* Mon Jun 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.30-alt1
- new version 1.30 (with rpmrb script)
- change license field to MIT

* Sun Feb 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.28-alt1
- new version

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
