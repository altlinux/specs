Name: libgoogle-sparsehash
Summary: hash_map and hash_set classes with minimal space overhead
Version: 1.5.2
Release: alt1
Group: Development/C++
URL: http://code.google.com/p/google-sparsehash
License: BSD
Packager: Maxim Ivanov <redbaron@altlinux.org>
Source: %name-%version.tar
Buildarch: noarch
BuildRequires: gcc-c++

%description
The %name package contains several hash-map implementations, similar
in API to the SGI hash_map class, but with different performance
characteristics. sparse_hash_map uses very little space overhead: 1-2
bits per entry. dense_hash_map is typically faster than the default
SGI STL implementation. This package also includes hash-set analogues
of these classes.

%prep
%setup

%build
%configure
%make

%install
%makeinstall

%files
%doc %_docdir/sparsehash-%version
%_includedir/google

%changelog
* Wed Nov 11 2009 Maxim Ivanov <redbaron at altlinux.org> 1.5.2-alt1
- Initial build for ALT Linux

