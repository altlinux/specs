%define _altdata_dir %_datadir/alterator

Name: cert-sh-functions
Version: 0.3
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

Summary: helper functions for ssl certificate generation
License: GPL
Group: System/Base
Requires: openssl

%description
helper functions for ssl certificate generation

%prep
%setup -q

%install
%__install -Dpm755 cert-sh %buildroot%_bindir/cert-sh
%__install -Dpm644 %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/*

%changelog
* Thu Apr 23 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3-alt1
- cert-sh: simple wrapper for cert-sh-functions

* Tue Mar 10 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Version bump
- Fix certificate sign request generation (ALT#19116)
- Add -batch option to openssl req invocation

* Wed Feb 25 2009 Sir Raorn <raorn@altlinux.ru> 0.1-alt5
- NMU:
     Create link from *.cert to *.pem and rehash SSL_CERTDIR
     ssl_make_req(): accept subject and openssl(1) options as arguments
     Renamed ssl_make_req2() to _ssl_make_req()

* Mon Feb 02 2009 Sir Raorn <raorn@altlinux.ru> 0.1-alt4
- NMU:
     Support for PEM certificates with included key (ALT#15480)
     Make /usr/bin/cert-sh-function non-executable

* Fri Feb 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- merge with ldv:
     Source /etc/init.d/functions (ALT#11813)
     ssl_exit_handler: Fix typo
- add README 

* Mon Jan 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add support for DH parameters generation

* Mon Apr 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
