%define soname 10
%define pkgdocdir %_docdir/%name-%version

Name: xmltooling
Version: 3.2.1
Release: alt1

Summary: OpenSAML XML Processing library

License: Apache-2.0
Group: System/Libraries
Url: https://wiki.shibboleth.net/confluence/display/OpenSAML/XMLTooling-C

Source: http://shibboleth.net/downloads/c++-opensaml/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ boost-devel-headers boost-devel liblog4shib-devel libxerces-c-devel >= 3.2 libxml-security-c-devel openssl-devel zlib-devel doxygen libcurl-devel

%description
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

%package -n libxmltooling%soname
Summary: OpenSAML XMLTooling library
Group: System/Libraries

%description -n libxmltooling%soname
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package contains just the shared library.

%package -n libxmltooling-lite%soname
Summary: OpenSAML XMLTooling library
Group: System/Libraries

%description -n libxmltooling-lite%soname
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package contains just the shared library.

%package -n libxmltooling-devel
Summary: XMLTooling development Headers
Group: Development/C++

%description -n libxmltooling-devel
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package includes files needed for development with XMLTooling.

%package -n xmltooling-schemas
Summary: XMLTooling schemas and catalog
Group: Development/Other
BuildArch: noarch

%description -n xmltooling-schemas
The XMLTooling library contains generic XML parsing and processing
classes based on the Xerces-C DOM. It adds more powerful facilities
for declaring element- and type-specific API and implementation
classes to add value around the DOM, as well as signing and encryption
support.

This package includes XML schemas and related files.

%prep
%setup

%build
# The default C++ standard used in GCC-11 is C++17,
# which does not support opensaml codebase.
CXXFLAGS="-std=c++11 %optflags"
export CXXFLAGS
%autoreconf
%configure
%make_build

%install
make DESTDIR=%buildroot pkgdocdir=%pkgdocdir install
# Don't package unit tester if present.
rm -f %buildroot/%_bindir/xmltoolingtest
rm -f %buildroot/%_libdir/libxmltooling.la
rm -f %buildroot/%_libdir/libxmltooling-lite.la

%files -n libxmltooling%soname
%_libdir/libxmltooling.so.%{soname}*

%files -n libxmltooling-lite%soname
%_libdir/libxmltooling-lite.so.%{soname}*

%files -n xmltooling-schemas
%dir %_datadir/xml/xmltooling
%_datadir/xml/xmltooling/*

%files -n libxmltooling-devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/xmltooling.pc
%_pkgconfigdir/xmltooling-lite.pc
%doc %pkgdocdir

%changelog
* Wed Apr 13 2022 Leontiy Volodin <lvol@altlinux.org> 3.2.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
