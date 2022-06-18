Name:    jose
Version: 11
Release: alt1
Summary: C-language implementation of Javascript Object Signing and Encryption

License: Apache-2.0
Group:   System/Libraries
URL:     https://github.com/latchset/jose
Source:  jose-%{version}.tar.gz

BuildRequires(pre): rpm-macros-meson rpm-macros-ninja-build
BuildRequires: meson
BuildRequires: asciidoc-a2x
BuildRequires: openssl-devel
BuildRequires: libjansson-devel
BuildRequires: zlib-devel

%description
Jose is a C-language implementation of the Javascript Object Signing and
Encryption standards. Specifically, Jose aims towards implementing the
following standards:

RFC 7515 - JSON Web Signature (JWS)
RFC 7516 - JSON Web Encryption (JWE)
RFC 7517 - JSON Web Key (JWK)
RFC 7518 - JSON Web Algorithms (JWA)
RFC 7519 - JSON Web Token (JWT)
RFC 7520 - Examples of ... JOSE
RFC 7638 - JSON Web Key (JWK) Thumbprint

Jose is extensively tested against the RFC test vectors.

%package -n lib%name
Summary: Libraries for %name
Group:   System/Libraries

%description -n lib%name
Libraries for %name

%package -n lib%name-devel
Summary: Devel files for lib%name
Group:   Development/Other

%description -n lib%name-devel
Devel files for lib%name

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
rm -rf %buildroot%_datadir/licenses/%name/COPYING

%check
%meson_test

%files
%_bindir/jose
%_man1dir/*.xz
%_man3dir/*.xz

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*

%changelog
* Sat Jun 18 2022 Andrey Limachko <liannnix@altlinux.org> 11-alt1
- Updated to 11 version

* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 10-alt1
- initial build

