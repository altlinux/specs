
Name: libdotconf
Version: 1.0.13
Release: alt2.qa2
Summary: configuration file parser
License: %lgpl2only
Group: System/Libraries
URL: http://www.azzit.de/dotconf/

# Automatically added by buildreq on Sun Sep 07 2008
BuildRequires: glibc-devel-static

BuildRequires: rpm-build-licenses

Source: dotconf-%version.tar.gz

Patch1: dotconf-1.0.13-alt-aclocal.patch

Packager: Michael Pozhidaev <msp@altlinux.ru>

%description
dotconf is a configuration file parser.

%package devel
Summary: Development files for dotconf library
Group: Development/C

%description devel
dotconf is a configuration file parser.
This package contains development files

%package devel-static
Summary: Development files for dotconf library with static library
Group: Development/C
Requires: %name-devel

%description devel-static
dotconf is a configuration file parser.
This package contains static library

%package -n libpool-devel-static
Summary: Development static library files for libpool
Group: Development/C

%description -n libpool-devel-static
libpool is an auxiliary library, comes with libdotconf.

%prep
%setup -q -n dotconf-%version
%patch1 -p1
%build
%configure
make

%install
%make_install DESTDIR='%buildroot' install

%files
#%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING doc/dotconf-api.txt doc/dotconf-features.txt NEWS README 
%_libdir/libdotconf*.so.*

%files devel
%_libdir/libdotconf.so
%_includedir/dotconf.h
%_bindir/*
%_datadir/aclocal/dotconf.m4
%_libdir/pkgconfig/*

%files devel-static
%_libdir/libdotconf.a

%files -n libpool-devel-static
%_includedir/libpool.h
%_libdir/libpool.a

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.13-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdotconf
  * postun_ldconfig for libdotconf
  * postclean-05-filetriggers for spec file

* Sun Sep 14 2008 Michael Pozhidaev <msp@altlinux.ru> 1.0.13-alt2
- Fixed bug in m4 script

* Sun Sep 07 2008 Michael Pozhidaev <msp@altlinux.ru> 1.0.13-alt1
- ALT Linux package

* Fri Apr 05 2002 Mike Javorski <mike_javorski@bigfoot.com>
- Fixed inclusion of .so files

* Mon Dec 24 2001 Benjamin Lee <benjamin.lee@dotwap.com>
- initial release of dotconf rpm package.
