%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libcityhash
Version: 1.1.1
Release: alt2
Summary: A family of hash functions for strings
Group: Development/C++
License: MIT
Url: http://code.google.com/p/cityhash/

Source: cityhash-%version.tar

# Automatically added by buildreq on Sat Jul 23 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++

%description
CityHash provides hash functions for strings. The functions mix the
input bits thoroughly but are not suitable for cryptography.

The README contains a good explanation of the various CityHash functions.

%package devel
Group: Development/C++
Summary: Developmen environment for %name
Requires: %name = %EVR
%description devel
Development environment for %name, %summary

%package devel-static
Group: Development/C++
Summary: Static developmen environment for %name
Requires: %name-devel = %EVR
%description devel-static
Static development environment for %name, %summary

%prep
%setup -n cityhash-%version

%build
%autoreconf
%configure
%make

%install
%makeinstall

%check
%make check

%files
%doc README NEWS
%_libdir/*.so.*
%exclude %_defaultdocdir/cityhash

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Tue Oct 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Fixed build with LTO

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Mon Nov 12 2012 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

