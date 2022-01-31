Name:           mpdecimal
Version:        2.5.1
Release:        alt1

Summary:        Library for general decimal arithmetic
License:        BSD
Group:          System/Libraries

URL:            http://www.bytereef.org/mpdecimal/index.html
Source0:        %name-%version.tar
Source1:        http://speleotrove.com/decimal/dectest.zip

BuildRequires:  make gcc-c++ unzip

%description
The package contains a library limpdec implementing General Decimal Arithmetic
Specification. The specification, written by Mike Cowlishaw from IBM, defines
a general purpose arbitrary precision data type together with rigorously
specified functions and rounding behavior.

%package        devel
Summary:        Development headers for mpdecimal library
Group:          System/Libraries
Requires:       %name = %EVR

%description devel
The package contains development headers for the mpdecimal library.

%package        doc
Summary:        Documentation for mpdecimal library
Group:          Documentation

%description doc
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

%files
%doc LICENSE.txt
%_libdir/libmpdec.so.%version
%_libdir/libmpdec.so.3
%_libdir/libmpdec++.so.%version
%_libdir/libmpdec++.so.3

%files devel
%doc LICENSE.txt
%_libdir/libmpdec.so
%_libdir/libmpdec++.so
%_includedir/mpdecimal.h
%_includedir/decimal.hh

%files doc
%doc LICENSE.txt
%_docdir/%name

%changelog
* Fri Dec 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus.
