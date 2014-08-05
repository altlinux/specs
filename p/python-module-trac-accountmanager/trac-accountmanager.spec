Summary: User account management plugin for Trac
Name: python-module-trac-accountmanager
Version: 0.5
Release: alt2.r12976
Url: http://trac-hacks.org/wiki/AccountManagerPlugin
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: BSD
Group: Development/Python
Epoch: 1

BuildArch: noarch
BuildRequires: python-module-MySQLdb python-module-ruledispatch python-module-setuptools unzip

%description
The AccountManager offers several features for managing user accounts: 
 * allow users to register new accounts 
 * login via an HTML form instead of using HTTP authentication 
 * allow existing users to change their passwords or delete their accounts 
 * send a new password to users who've forgotten their password 
 * administration of user accounts

%prep
%setup -q

%build
%python_build

%install
%python_build_install

%files
%doc README README.hashes README.update COPYING
%python_sitelibdir/acct_mgr/
%python_sitelibdir/TracAccountManager-0.5dev_r0-py2.7.egg-info/

%changelog
* Tue Aug 05 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1:0.5-alt2.r12976
- Fixed build

* Thu Apr 18 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 1:0.5-alt1.r12976
- New version

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.r9425.1
- Rebuild with Python-2.7

* Fri Nov 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12-alt1.r9425
- New version

* Wed Apr 28 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt2.r7902
- New version

* Fri Jan 29 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt2.r7485
- Fix file mode for %python_sitelibdir/acct_mgr/templates/*

* Fri Jan 29 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt1.r7485
- New version
- Rname to python-module-trac-accountmanager

* Mon Dec 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt3
- fix README packing

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.10-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.10-alt2
- Use __python_version macro while packaging.

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for ALT Linux Sisyphus
