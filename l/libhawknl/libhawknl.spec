Name: libhawknl
Version: 1.68
Release: alt4

Summary: Game oriented network library
License: LGPLv2+
Group: System/Libraries

URL: http://www.hawksoft.com/hawknl/
%define srcversion %(echo %version | tr -d .)
Source: http://www.sonic.net/~philf/download/HawkNL%{srcversion}src.tar.gz
Patch: libhawknl-64bit.patch

%description
HawkNL is a free, open source, game oriented network API released under
the GNU LGPL.  HawkNL (NL) is a fairly low level API, a wrapper over
Berkeley/Unix Sockets and Winsock.  But NL also provides other features.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for developing
applications that use %name.

%prep
%setup -n hawknl%version
%patch -p1

%build
%add_optflags -fno-strict-aliasing
# fixups
subst 's/-soname,NL.so/-soname,libNL.so/; s|ln -s $(LIBDIR)/$(OUTPUT)|ln -s $(OUTPUT)|g' src/makefile.linux
subst 's/-O./%optflags/' src/makefile.linux
%make_build -f makefile.linux

%install
install -d %buildroot{%_libdir,%_includedir/hawknl}
%make -f makefile.linux install LIBDIR=%buildroot%_libdir INCDIR=%buildroot%_includedir/hawknl

# cleanups
rm -f %buildroot%_libdir/{libNL.a,NL*}

%files
%_libdir/libNL.so.*

%files devel
%_includedir/*
%_libdir/libNL.so

%changelog
* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.68-alt4
- Disabled optimizations based on strict aliasing rules.
- Rebuilt for debuginfo.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.68-alt3
- Rebuilt for soname set-versions.

* Fri Nov 13 2009 Victor Forsyuk <force@altlinux.org> 1.68-alt2
- Remove deprecated ldconfig calls.

* Fri Aug 08 2008 Victor Forsyuk <force@altlinux.org> 1.68-alt1
- Initial build.
