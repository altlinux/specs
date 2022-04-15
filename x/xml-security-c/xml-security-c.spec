%define soname 20

Name: xml-security-c
Version: 2.0.4
Release: alt1

Summary: C++ Implementation of W3C security standards for XML

License: Apache-2.0
Group: System/Libraries
Url: https://santuario.apache.org

Source: https://www.apache.org/dist/santuario/c-library/%name-%version.tar.gz

BuildRequires: gcc-c++ libssl-devel xalan-c-devel libxerces-c-devel

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

%package -n lib%name%soname
Summary: C++ Implementation of W3C security standards for XML
Group: System/Libraries

%description -n lib%name%soname
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

This package provides C++ xml-security-c library.

%package -n lib%name-devel
Summary: Development files for xml-security-c
Group: Development/C++

%description -n lib%name-devel
This package provides development files for xml-security-c, a C++ library for
XML Digital Signatures.

%package -n xsec-utils
Summary: Tools for xml-security-c
Group: Development/Other

%description -n xsec-utils
This package provides tools for xml-security-c.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-debug \
	--disable-static \
	--without-nss \
	--with-openssl \
	--with-xalan \
	%nil
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%check
./xsec/xsec-xtest

%files -n lib%name%soname
%_libdir/libxml-security-c.so.%{soname}*

%files -n lib%name-devel
%doc LICENSE.txt CHANGELOG.txt NOTICE.txt
%_includedir/xsec
%_libdir/libxml-security-c.so
%_pkgconfigdir/xml-security-c.pc

%files -n xsec-utils
%_bindir/xsec-*

%changelog
* Wed Apr 13 2022 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- Initial build for ALT Sisyphus.
