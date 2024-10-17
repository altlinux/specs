%def_enable openssl
%define soname 30

Name: xml-security-c
Version: 3.0.0
Release: alt1

Summary: C++ Implementation of W3C security standards for XML

License: Apache-2.0
Group: System/Libraries
Url: https://shibboleth.atlassian.net/wiki/spaces/DEV/pages/3726671873/Santuario

Source: https://shibboleth.net/downloads/xml-security-c/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ libxerces-c-devel >= 3.2
%if_enabled openssl
BuildRequires: libssl-devel
%else
BuildRequires: LibreSSL-devel
%endif

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache Xerces-C XML Parser.

%package -n lib%name%soname
Summary: C++ Implementation of W3C security standards for XML
Group: System/Libraries

%description -n lib%name%soname
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache Xerces-C XML Parser.

This package provides C++ xml-security-c library.

%package -n lib%name-devel
Summary: Development files for xml-security-c
Group: Development/C++

%description -n lib%name-devel
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache Xerces-C XML Parser.

This package includes files needed for development with xml-security-c.

%package -n xsec-utils
Summary: Utilities for XML security C++ library
Group: Development/Other

%description -n xsec-utils
The xml-security-c library is a C++ implementation of the XML Digital Signature
and Encryption specifications. The library makes use of the Apache Xerces-C XML Parser.

This package contains the utility programs.

%prep
%setup

%build
%autoreconf
%configure \
  --disable-debug \
  --disable-static \
%if_enabled openssl
  --with-openssl \
%endif
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n lib%name%soname
%_libdir/libxml-security-c.so.%{soname}*

%files -n lib%name-devel
%doc LICENSE.txt NOTICE.txt README.txt
%_includedir/xsec
%_libdir/libxml-security-c.so
%_pkgconfigdir/xml-security-c.pc

%files -n xsec-utils
%_bindir/xsec-*

%changelog
* Thu Oct 17 2024 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt1
- New version 3.0.0.
- Changed url tag.

* Wed Apr 13 2022 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- Initial build for ALT Sisyphus.
