%define abiversion 3

Name:           mpdecimal
Version:        2.5.1
Release:        alt3

Summary:        Library for general decimal arithmetic
License:        BSD
Group:          System/Libraries

URL:            http://www.bytereef.org/mpdecimal/index.html
Source0:        %name-%version.tar
Source1:        http://speleotrove.com/decimal/dectest.zip

BuildRequires:  make gcc-c++ unzip

Requires:       libmpdec%abiversion libmpdecxx%abiversion

%description
The package contains a library limpdec implementing General Decimal Arithmetic
Specification. The specification, written by Mike Cowlishaw from IBM, defines
a general purpose arbitrary precision data type together with rigorously
specified functions and rounding behavior.

%package        -n libmpdec%abiversion
Summary:        Library for general decimal arithmetic
Group:          System/Libraries
%description    -n libmpdec%abiversion
The package contains a library limpdec implementing General Decimal Arithmetic
Specification. The specification, written by Mike Cowlishaw from IBM, defines
a general purpose arbitrary precision data type together with rigorously
specified functions and rounding behavior.

%package        -n libmpdecxx%abiversion
Summary:        Library for general decimal arithmetic
Group:          System/Libraries
%description    -n libmpdecxx%abiversion
The package contains libmpdec++ is a complete implementation of the General
Decimal Arithmetic Specification. libmpdec++ is mostly a header library
around libmpdec C functions.

%package        -n libmpdec-devel
Summary:        Development headers for mpdecimal library
Group:          System/Libraries
Requires:       libmpdec%abiversion = %EVR
Requires:       libmpdecxx%abiversion = %EVR
Provides:       mpdecimal-devel = %EVR
Obsoletes:      mpdecimal-devel < %EVR

%description    -n libmpdec-devel
The package contains development headers for the mpdecimal library.

%package        -n libmpdec-doc
Summary:        Documentation for mpdecimal library
Group:          Documentation
BuildArch:      noarch

%description    -n libmpdec-doc
The package contains documentation for the mpdecimal library.

%prep
%setup
unzip -d tests/testdata %SOURCE1

%build
# NOTE: without -ffat-lto-objects the inline assembly tests in ./configure
# have false positives on a variety of architectures.
export CFLAGS="%optflags -ffat-lto-objects"
export CXXFLAGS="$CFLAGS"
%configure
%make_build

%install
%makeinstall_std

rm -v %buildroot%_libdir/*.a

%check
make check

# for dummy package
%files

%files -n libmpdec%abiversion
%doc LICENSE.txt
%_libdir/libmpdec.so.%abiversion
%_libdir/libmpdec.so.%version

%files -n libmpdecxx%abiversion
%doc LICENSE.txt
%_libdir/libmpdec++.so.%abiversion
%_libdir/libmpdec++.so.%version

%files -n libmpdec-devel
%doc LICENSE.txt
%_libdir/libmpdec.so
%_libdir/libmpdec++.so
%_includedir/mpdecimal.h
%_includedir/decimal.hh

%files -n libmpdec-doc
%doc LICENSE.txt
%_docdir/%name

%changelog
* Wed Feb 01 2023 Anton Vyatkin <toni@altlinux.org> 2.5.1-alt3
- NMU: Spec refactoring.

* Tue Jan 31 2023 Anton Vyatkin <toni@altlinux.org> 2.5.1-alt2
- NMU: (ALT 42388) Split into libmpdec3 and libmpdecxx3 packages.

* Fri Dec 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus.
