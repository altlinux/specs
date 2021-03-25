Name: metrohash
Version: 1.1.3
Release: alt1
Summary: Hash functions for non-cryptographic use cases
Group: Development/C++
# https://github.com/jandrewrogers/MetroHash
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
License: ASL 2.0
Url: https://github.com/jandrewrogers/MetroHash
BuildRequires: gcc-c++

%description
Set of state-of-the-art hash functions for non-cryptographic use cases.
They  are notable for being algorithmically generated in addition to their
exceptional performance. The set of published hash functions may be expanded
in the future, having been selected from a very large set of hash functions
that have been constructed this way.

%package devel
Group: Development/C++
Summary: Developmen environment for %name
Requires: %name = %version
%description devel
Development environment for %name, %summary

%prep
%setup
%patch0 -p1

%build
%make

%install
mkdir -p %buildroot%_includedir/metrohash
mkdir -p %buildroot%_libdir
install -m0644 src/metrohash*.h src/platform.h %buildroot%_includedir/metrohash/
install -m0755 libmetrohash.so.1.0 %buildroot%_libdir/ 
ln -sf libmetrohash.so.1.0 %buildroot%_libdir/libmetrohash.so.1
ln -sf libmetrohash.so.1.0 %buildroot%_libdir/libmetrohash.so

%files
%doc README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Thu Mar 25 2021 Anton Farygin <rider@altlinux.org> 1.1.3-alt1
- sync version with upstream
- split source to tarball from upstream tag and alt patch

* Mon Jun 24 2019 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT
