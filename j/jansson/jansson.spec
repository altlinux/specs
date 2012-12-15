Name: jansson
Version: 2.4
Release: alt1
License: MIT
Url: http://www.digip.org/jansson/
Source: %name-%version.tar
Group: System/Libraries
Summary: C library for encoding, decoding and manipulating JSON data
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: python-module-sphinx
#gcc-c++ 

%description
Jansson is a C library for encoding, decoding and manipulating JSON data. It features:
 - Simple and intuitive API and data model
 - Comprehensive documentation
 - No dependencies on other libraries
 - Full Unicode support (UTF-8)
 - Extensive test suite

%package -n lib%name
Summary: C library for encoding, decoding and manipulating JSON data
Group: System/Libraries
Provides: %name = %version-%release

%description -n lib%name
Jansson is a C library for encoding, decoding and manipulating JSON data. It features:
 - Simple and intuitive API and data model
 - Comprehensive documentation
 - No dependencies on other libraries
 - Full Unicode support (UTF-8)
 - Extensive test suite

%package -n lib%name-devel
Summary: C library for encoding, decoding and manipulating JSON data
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Jansson is a C library for encoding, decoding and manipulating JSON data. It features:
 - Simple and intuitive API and data model
 - Comprehensive documentation
 - No dependencies on other libraries
 - Full Unicode support (UTF-8)
 - Extensive test suite

%prep
%setup

%build
%autoreconf
%configure
%make_build
%make html

%install
%makeinstall_std

%check
%make check


%files -n lib%name
%_libdir/*.so.*
%doc README* LICENSE CHANGES

%files -n lib%name-devel
%doc doc/_build/html/*
%_includedir/*.h
%_pkgconfigdir/*
%_libdir/*so


%changelog
* Sat Dec 15 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4-alt1
- Buld for ALT

