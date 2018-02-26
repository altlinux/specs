# Upstream doesn't use a SONAME and nobody knows how stable the interface is
# Please take extra care when updating this package -- bump the following
# and rebuild dependencies (shouldn't be many) if you suspect an ABI change:
%define abi_major 0
%define abi_minor 1

Name: libpnglite
Version: 0.1.17
Release: alt3

Summary: Lightweight PNG C library
License: zlib/libpng
Group: System/Libraries

Url: http://sourceforge.net/projects/pnglite/
Source: http://download.sourceforge.net/pnglite/pnglite-%version.zip

Patch1: pnglite-0.1.17-teeworldsfixes.patch

# Automatically added by buildreq on Wed Sep 02 2009
BuildRequires: unzip zlib-devel

%description
pnglite is a C library for loading PNG images. It was created as a substitute
for libpng in situations when libpng is more than enough. It currently requires
zlib for inflate and crc checking and it can read the most common types of PNG
images. The library has a small and simple to use interface.

%package devel
Summary: Files needed to build and link programs with pnglite
Group: Development/C
Requires: %name = %version-%release

%description devel
This contains a header file and a link to library for the linker to link against
pnglite.

%prep
%setup -c -n pnglite-%version

subst 's#"../zlib/zlib.h"#<zlib.h>#' pnglite.c
subst 's/\r//' pnglite.h

%patch1 -p1

%build
gcc %optflags -shared -fPIC -Wl,--soname,libpnglite.so.%abi_major -o libpnglite.so.%abi_major.%abi_minor pnglite.c -lz

%install
install -Dpm 644 pnglite.h %buildroot%_includedir/pnglite.h
install -Dpm 644 libpnglite.so.%abi_major.%abi_minor %buildroot%_libdir/libpnglite.so.%abi_major.%abi_minor
pushd %buildroot%_libdir
ln -s libpnglite.so.%abi_major.%abi_minor libpnglite.so.%abi_major
ln -s libpnglite.so.%abi_major.%abi_minor libpnglite.so
popd

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Aug 11 2011 Victor Forsiuk <force@altlinux.org> 0.1.17-alt3
- Fixes for pnglite from teeworlds.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 0.1.17-alt2
- Rebuilt for soname set-versions.

* Wed Sep 02 2009 Victor Forsyuk <force@altlinux.org> 0.1.17-alt1
- Initial build.
