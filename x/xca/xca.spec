# vim: set ft=spec: -*- rpm-spec -*-

Name: xca
Version: 2.7.0
Release: alt1

Summary: A GUI for handling X509 certificates, RSA keys, PKCS#10 Requests
Group: Security/Networking
License: BSD
Url: https://hohnstaedt.de/xca/
# sources: https://github.com/chris2511/xca/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: qt6-sql-interbase qt6-sql-mysql qt6-sql-odbc qt6-sql-postgresql
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: ctest

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

%cmake
%cmake_build

%check
%cmake_build -t tests
LANG="C.UTF-8" TZ="GMT" \
    %ctest -L console

%install
%cmake_install

%files
%doc AUTHORS README.md
%_datadir/xca
%_datadir/doc/xca
%_datadir/metainfo/*.xml
%_desktopdir/xca*
%_datadir/bash-completion/completions/xca
%_datadir/mime/packages/xca.xml
%_man1dir/xca*.1*
%_pixmapsdir/xca*.xpm
%_iconsdir/hicolor/*/*/*
%_bindir/*

%changelog
* Sat Sep 07 2024 Pavel Nakonechnyi <zorg@altlinux.ru> 2.7.0-alt1
- update to 2.7.0 release
- enabling tests for packaging stage

* Wed Feb 28 2024 Pavel Nakonechnyi <zorg@altlinux.ru> 2.6.0-alt1
- update to 2.6.0 release

* Sat Sep 30 2023 Pavel Nakonechnyi <zorg@altlinux.ru> 2.5.0-alt1
- update to 2.5.0 release, Qt6-based build

* Sat Jul 22 2023 Pavel Nakonechnyi <zorg@altlinux.ru> 2.4.0-alt2
- add temporary OpenSSL3 support from xca-240-ossl3 branch

* Sun May 09 2021 Pavel Nakonechnyi <zorg@altlinux.ru> 2.4.0-alt1
- update to 2.4.0 release

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
