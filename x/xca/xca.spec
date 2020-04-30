# vim: set ft=spec: -*- rpm-spec -*-

Name: xca
Version: 2.3.0
Release: alt1

Summary: A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Group: Security/Networking
License: BSD
Url: https://hohnstaedt.de/xca/
# sources: https://github.com/chris2511/xca/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: qt5-base-devel qt5-tools
BuildRequires: libltdl-devel openssl-devel linuxdoc-tools rpm-build-xdg OpenSP groff-base

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
./bootstrap
CFLAGS="%optflags" \
CXXFLAGS="%optflags" \
./configure --prefix="%_prefix" \
      docdir=%_docdir/%name-%version
%make_build

%install
mkdir -p %buildroot{%_bindir,%_datadir/xca,%_desktopdir,%_man1dir}

%make_install install \
    DESTDIR=%buildroot prefix=/usr STRIP=: \
    mandir=%_mandir docdir=%_docdir/%name-%version datarootdir=%_datadir

%files
%doc AUTHORS doc/*.html
%_bindir/*
%_datadir/xca
%_desktopdir/xca*
%_man1dir/xca*.1*
%_xdgmimedir/packages/xca.xml
%_pixmapsdir/xca*.xpm

%changelog
* Thu Apr 30 2020 Pavel Nakonechnyi <zorg@altlinux.ru> 2.3.0-alt1
- update to 2.3.0 release

* Sun Feb 09 2020 Pavel Nakonechnyi <zorg@altlinux.ru> 2.2.1-alt1
- update to 2.2.1 release

* Sat Sep 15 2018 Pavel Nakonechnyi <zorg@altlinux.ru> 2.1.1-alt1
- update to 2.1.1 release

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Aug 02 2018 Pavel Nakonechnyi <zorg@altlinux.ru> 2.1.0-alt1
- update to 2.1.0 release
- databases are incompatible with 1.x versions!
- switched to Github upstream: https://github.com/chris2511/xca/
- upstream switched to Qt5

* Thu Dec 29 2016 Pavel Nakonechnyi <zorg@altlinux.ru> 1.3.2-alt2.git1584579
- fix data lookup path

* Sun Oct 09 2016 Pavel Nakonechnyi <zorg@altlinux.ru> 1.3.2-alt1.git1584579
- updated to revision 1584579 from http://gitweb.hohnstaedt.de/?p=xca.git
- closes: #32305
- closes: #32301

* Thu Feb 16 2012 Mykola Grechukh <gns@altlinux.ru> 0.9.1-alt1
- new version

* Tue Mar 29 2011 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt1
- Initial build
