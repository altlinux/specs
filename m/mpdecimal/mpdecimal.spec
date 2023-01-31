Name:           mpdecimal
Version:        2.5.1
Release:        alt2

Summary:        Library for general decimal arithmetic
License:        BSD
Group:          System/Libraries

URL:            http://www.bytereef.org/mpdecimal/index.html
Source0:        %name-%version.tar
Source1:        http://speleotrove.com/decimal/dectest.zip

BuildRequires:  make gcc-c++ unzip

Requires:       libmpdec3 libmpdecxx3

%description
The package contains a library limpdec implementing General Decimal Arithmetic
Specification. The specification, written by Mike Cowlishaw from IBM, defines
a general purpose arbitrary precision data type together with rigorously
specified functions and rounding behavior.

%package        -n libmpdec3
Summary:        Library for general decimal arithmetic
Group:          System/Libraries
%description    -n libmpdec3
The package contains mpdecimal %version libs.

%package        -n libmpdecxx3
Summary:        Library for general decimal arithmetic
Group:          System/Libraries
%description    -n libmpdecxx3
The package contains mpdecimal %version libs.

%package        -n libmpdec-devel
Summary:        Development headers for mpdecimal library
Group:          System/Libraries
Requires:       libmpdec3 = %EVR
Requires:       libmpdecxx3 = %EVR
Provides:       mpdecimal-devel

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

%files -n libmpdec3
%doc LICENSE.txt
%_libdir/libmpdec.so.3
%_libdir/libmpdec.so.%version

%files -n libmpdecxx3
%doc LICENSE.txt
%_libdir/libmpdec++.so.3
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
* Tue Jan 31 2023 Anton Vyatkin <toni@altlinux.org> 2.5.1-alt2
- NMU: (ALT 42388) Split into libmpdec3 and libmpdecxx3 packages.

* Fri Dec 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus.
