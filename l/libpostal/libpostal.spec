%define _unpackaged_files_terminate_build 1
%define soname 1

Name: libpostal
Version: 1.1.4
Release: alt1

Summary: A C library for parsing/normalizing street addresses
License: MIT
Group: Sciences/Geosciences
Url: https://github.com/openvenues/libpostal
Vcs: https://github.com/openvenues/libpostal.git

Source0: %name-%version.tar
Source1: %name-%version-data.tar

BuildRequires: libblas-devel

%description
libpostal is a C library for parsing/normalizing street addresses around the
world using statistical NLP and open data. The goal of this project is to
understand location-based strings in every language, everywhere.

%package -n libpostal%soname
Summary: Dynamic libraries for libpostal
Group: Sciences/Geosciences

%description -n libpostal%soname
The runtime shared library for libpostal, a fast statistical address parser and
normalizer.  This package contains the core library (`libpostal.so`) needed to
run applications that  parse and standardize street addresses worldwide. It
includes prebuilt language models  for address normalization across multiple
countries and languages.

%package tools
Summary: Command line utils for libpostal
Group: Sciences/Geosciences

%description tools
Command-line utilities for libpostal providing address parsing and
normalization functions.  Includes tools for batch processing street addresses,
expanding abbreviations, and standardizing address formats across different
countries and languages. Essential for geocoding systems, data cleaning
pipelines, and geographic information processing.

%package devel
Summary: Development files for libpostal
Group: Development/C

%description devel
Development files for building applications that use libpostal's address
parsing capabilities. Provides everything needed to integrate international
address normalization into C/C++ projects, including API references and build
configuration files.

%prep
%setup -a1
%autopatch -p1
./bootstrap.sh

%build
export CFLAGS="-Wno-incompatible-pointer-types"
%configure \
    datadir="$PWD/data" \
    --disable-data-download \
%ifnarch ix86 x86_64
    --disable-sse2 \
%endif

%make_build

%install
%makeinstall
rm -f %buildroot%_libdir/libpostal.a

%check
%make check

%files -n libpostal%soname
%doc LICENSE
%_libdir/libpostal.so.%soname
%_libdir/libpostal.so.%soname.*

%files tools
%_bindir/libpostal_data

%files devel
%_libdir/libpostal.so
%_includedir/libpostal/
%_pkgconfigdir/libpostal.pc

%changelog
* Wed May 13 2026 Ivan Khanas <xeno@altlinux.org> 1.1.4-alt1
- New version.

* Fri Jun 06 2025 Ivan Khanas <xeno@altlinux.org> 1.1-alt1
- First build for ALT.
