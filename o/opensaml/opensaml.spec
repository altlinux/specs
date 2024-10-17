%define soname 13
%define pkgdocdir %_docdir/%name-%version

Name: opensaml
Version: 3.3.0
Release: alt1

Summary: Security Assertion Markup Language library

License: Apache-2.0
Group: System/Libraries
Url: https://wiki.shibboleth.net/confluence/display/OpenSAML/

Source: https://shibboleth.net/downloads/c++-opensaml/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ doxygen boost-devel-headers liblog4shib-devel libxerces-c-devel >= 3.2 libxml-security-c-devel libxmltooling-devel

%description
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

%package -n opensaml-utils
Summary: Utilities for OpenSAML library
Group: Development/Tools

%description -n opensaml-utils
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package contains the utility programs.

%package -n libsaml%soname
Summary: Security Assertion Markup Language library
Group: System/Libraries

%description -n libsaml%soname
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package contains just the shared library.

%package -n libsaml-devel
Summary: OpenSAML development Headers
Group: Development/C++

%description -n libsaml-devel
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package includes files needed for development with OpenSAML.

%package -n opensaml-schemas
Summary: OpenSAML schemas and catalog
Group: Development/C++
BuildArch: noarch

%description -n opensaml-schemas
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

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
%makeinstall_std pkgdocdir=%pkgdocdir
# Don't package unit tester if present.
rm -f %buildroot/%_bindir/samltest
rm -f %buildroot/%_libdir/libsaml.la

%files -n opensaml-utils
%_bindir/samlsign

%files -n libsaml%soname
%_libdir/libsaml.so.%{soname}*

%files -n opensaml-schemas
%dir %_datadir/xml/opensaml
%_datadir/xml/opensaml/*

%files -n libsaml-devel
%doc %pkgdocdir
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/opensaml.pc

%changelog
* Thu Oct 17 2024 Leontiy Volodin <lvol@altlinux.org> 3.3.0-alt1
- New version 3.3.0.

* Mon May 23 2022 Michael Shigorin <mike@altlinux.org> 3.2.1-alt2
- E2K: lcc ftbfs workaround for lousy boost test

* Thu Apr 14 2022 Leontiy Volodin <lvol@altlinux.org> 3.2.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
