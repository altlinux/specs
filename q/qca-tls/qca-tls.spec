Name: qca-tls
Version: 1.0
Release: alt7.1

License: GPLv2+
Group: Networking/Instant messaging
Summary: QCA TLS Plugin
URL: http://delta.affinix.com/qca/
Packager: Konstantin Baev <kipruss@altlinux.org>
# http://delta.affinix.com/download/qca/%name-%version.tar.bz2
Source: %name-%version.tar
Patch: qca-tls-1.0-alt-openssl.patch
Obsoletes: qssl

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: gcc-c++ libcom_err-devel libqt3-devel libssl-devel

%description
This is a plugin to provide SSL/TLS capability to programs that
utilize the Qt Cryptographic Architecture (QCA).

It's used by Psi Jabber client to support SSL connections.

%description -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SSL/TLS для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

Он используется Jabber-клиентом Psi для поддержки соединений SSL.

%prep
%setup
%patch -p1

%build
QTDIR=%_libdir/qt3
QMAKESPEC="linux-g++"
export QTDIR QMAKESPEC
./configure
%make

%install
mkdir -p %buildroot%_libdir/qt3/plugins/crypto/
cp libqca-tls.so %buildroot%_libdir/qt3/plugins/crypto/

%files
%_libdir/qt3/plugins/crypto/libqca-tls.so
%doc README

%changelog
* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt7.1
- Fixed build with openssl-1.0.

* Tue Jan 27 2009 Konstantin Baev <kipruss@altlinux.org> 1.0-alt7
- Add URL

* Mon Sep 29 2008 Konstantin Baev <kipruss@altlinux.org> 1.0-alt6
- Cleanup BuildRequires

* Mon Sep 29 2008 Konstantin Baev <kipruss@altlinux.org> 1.0-alt5
- Fixed BuildRequires and add "QMAKE_PROJECT_DEPTH=0" in qca-tls.pro

* Sun Jan 14 2007 Mikhail Yakshin <greycat@altlinux.ru> 1.0-alt4
- Fixed build with OpenSSL 0.9.8

* Tue Feb 21 2006 Anton Farygin <rider@altlinux.ru> 1.0-alt3.2
- NMU: rebuild for x86_64

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt3.1
- Rebuilt with libstdc++.so.6.

* Sun May 16 2004 Mikhail Yakshin <greycat@altlinux.ru> 1.0-alt3
- Build fixes to compile with OpenSSL 0.9.7
- Removed patch due to fixes to build process

* Tue Jan 20 2004 Mikhail Yakshin <greycat@altlinux.ru> 1.0-alt2
- Added a patch from Vadim Gorodisky to make SSL work

* Sun Jan  4 2004 Mikhail Yakshin <greycat@altlinux.ru> 1.0-alt1
- Initial release
- It's a plugin mostly for Psi jabber client, designed to replace
  older qssl plugin and provide uniform QCA support
