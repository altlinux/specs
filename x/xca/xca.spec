# vim: set ft=spec: -*- rpm-spec -*-

Name: xca
Version: 0.9.1
Release: alt1

Summary: A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Group: Security/Networking
License: BSD
Url: http://www.hohnstaedt.de/xca.html

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libqt4-devel libltdl-devel openssl-devel linuxdoc-tools rpm-build-xdg OpenSP groff-base

%description
Graphical certification authority is an interface for managing RSA
keys and certificates, and the creation and signing of PKCS#10
requests. It uses the OpenSSL library and a Berkeley DB for key and
certificate storage. It supports importing and exporting keys and PEM
DER PKCS8 certificates, signing and revoking of PEM DER PKCS12, and
the selection of x509v3 extensions. A tree view of certificates is
presented.

%prep
%setup
%patch -p1

%build
prefix="%_prefix" \
CFLAGS="%optflags" \
CXXFLAGS="%optflags" \
./configure
%make_build

%install
mkdir -p %buildroot{%_bindir,%_datadir/xca,%_desktopdir,%_man1dir}

%make_install install destdir=%buildroot STRIP=: mandir=..%_mandir

%files
%doc AUTHORS doc/*.html
%_bindir/*
%_datadir/xca
%_desktopdir/xca*
%_man1dir/xca.1*
%_xdgmimedir/packages/xca.xml

%changelog
* Thu Feb 16 2012 Mykola Grechukh <gns@altlinux.ru> 0.9.1-alt1
- new version

* Tue Mar 29 2011 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt1
- Initial build

