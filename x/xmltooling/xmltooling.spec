%define soname 11
%define pkgdocdir %_docdir/%name-%version

Name: xmltooling
Version: 3.3.0
Release: alt1

Summary: OpenSAML XML Processing library

License: Apache-2.0
Group: System/Libraries
Url: https://wiki.shibboleth.net/confluence/display/OpenSAML/XMLTooling-C

Source: https://shibboleth.net/downloads/c++-opensaml/%version/%name-%version.tar.gz

# Automatically added by buildreq on Thu Oct 17 2024
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libgpg-error libssl-devel libstdc++-devel libxerces-c libxerces-c-devel libxml-security-c30 perl pkg-config sh5
BuildRequires: gcc-c++ boost-devel-headers doxygen libcurl-devel liblog4shib-devel libxml-security-c-devel zlib-devel

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
%ifarch %e2k
# lcc's cpp adds an extra space breaking this regex
sed -r -i 's,\^boost(.)lib(.)version,boost\1lib\2version,' configure m4/boost.m4
%endif

%build
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
%doc %pkgdocdir
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/xmltooling.pc
%_pkgconfigdir/xmltooling-lite.pc

%changelog
* Thu Oct 17 2024 Leontiy Volodin <lvol@altlinux.org> 3.3.0-alt1
- New version 3.3.0.

* Wed Jun 28 2023 Leontiy Volodin <lvol@altlinux.org> 3.2.4-alt1
- New version 3.2.4.

* Tue Jun 06 2023 Leontiy Volodin <lvol@altlinux.org> 3.2.3-alt1
- New version 3.2.3.

* Fri May 20 2022 Michael Shigorin <mike@altlinux.org> 3.2.1-alt1.1
- E2K: lcc cpp related ftbfs workaround

* Wed Apr 13 2022 Leontiy Volodin <lvol@altlinux.org> 3.2.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
