Name:    tang
Version: 7
Release: alt1
Summary: Tang binding daemon

License: GPLv3
Group:   System/Libraries
URL:     https://github.com/latchset/tang
Source:  tang-%version.tar.gz

BuildRequires: openssl-devel
BuildRequires: libjose-devel
BuildRequires: libjansson-devel
BuildRequires: zlib-devel
BuildRequires: libhttp-parser-devel
BuildRequires: systemd systemd-devel

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

%prep
%setup

%build
%autoreconf
%configure --localstatedir=/var
%make_build

%install
%makeinstall_std

%files
%_bindir/tang-show-keys
%_libexecdir/tangd*
%_unitdir/tangd*

%changelog
* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt1
- initial build

