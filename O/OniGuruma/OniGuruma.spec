Name: OniGuruma
Version: 5.9.5
Release: alt1
Summary: Regular expressions library
License: BSD
Group: Development/Tools
Url: http://www.geocities.jp/kosako3/oniguruma/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)

%package -n lib%name
Summary: Regular expressions library
Group: System/Libraries

%description -n lib%name
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)

%package -n lib%name-devel
Summary: Development files of Oniguruma, regular expressions library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)

This package contains development files of Oniguruma.

%prep
%setup

touch NEWS ChangeLog

%build
%autoreconf
%configure --enable-static=no
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc AUTHORS HISTORY README
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/API doc/FAQ doc/RE
%_includedir/*
%_libdir/*.so
%_bindir/*
%_pkgconfigdir/*

%changelog
* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.5-alt1
- Initial build for Sisyphus

