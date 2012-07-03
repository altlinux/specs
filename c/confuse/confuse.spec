Name: confuse
Version: 2.7
Release: alt1.1

Summary: A library for parsing configuration files
License: %bsdstyle
Group: System/Libraries
Url: http://www.nongnu.org/confuse

Source0: http://bzero.se/confuse/%name-%version.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildPreReq: rpm-build-licenses
BuildPreReq: check cvs flex gcc-c++

%description
libConfuse is a configuration file parser library, licensed under the
terms of the LGPL, and written in C. It supports sections and (lists of)
values (strings, integers, floats, booleans or other sections), as well
as some other features (such as single/double-quoted strings,
environment variable expansion, functions and nested include
statements). It makes it very easy to add configuration file capability
to a program using a simple API. 

The goal of libConfuse is not to be the configuration file parser
library with a gazillion of features. Instead, it aims to be easy to use
and quick to integrate with your code. libConfuse was called libcfg
before, but was changed to not confuse with other similar libraries.

%package -n lib%name
Summary: Dynamic libraries from %name
Group: System/Libraries

%description -n lib%name
Dynamic libraries from %name.

%package -n lib%name-devel
Summary: Files for developing applications that use %name
Requires: lib%name = %version
Group: Development/C

%description -n lib%name-devel
The header files and man pages for developing applications that use
%name.

%package -n lib%name-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch

%description -n lib%name-doc
Documentation for developing programs based on %name

%prep
%setup
%__subst '/^AM_CFLAGS/s/-Werror//' src/Makefile.am
%autoreconf

%build
%configure \
	--disable-static \
	--enable-shared
%make_build
%make_build -C tests check

%install
%makeinstall
%find_lang %name
mkdir -p %buildroot%_man3dir/
install doc/man/man3/* %buildroot%_man3dir/

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-doc
%doc doc/{tutorial-html,html}/
%_man3dir/*


%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.1
- Rebuilt for debuginfo

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 2.7-alt1
- 2.7

* Wed Jan 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6-alt2
- make -doc subpackage noarch
- remove obsolete macros

* Sat Feb 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6-alt1
- 2.6

* Sun Nov 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.5-alt2
- fix memory leak (php-coder@, #12411)

* Sat Sep 30 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.5-alt1
- initial build
