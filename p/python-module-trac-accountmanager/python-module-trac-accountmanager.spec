%define tarname accountmanagerplugin
Name: python-module-trac-accountmanager
%define r_minor r9425
Version: 0.12
Release: alt1.%r_minor.1

Summary: User account management plugin for Trac

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/AccountManagerPlugin

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %{tarname}_%version-%r_minor.zip

BuildArch: noarch

# manually removed: python-module-Pyrex python-module-Rabbyt python-module-lxml
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: python-module-MySQLdb python-module-ruledispatch python-module-setuptools unzip

%description
The AccountManager offers several features for managing user accounts: 
 * allow users to register new accounts 
 * login via an HTML form instead of using HTTP authentication 
 * allow existing users to change their passwords or delete their accounts 
 * send a new password to users who've forgotten their password 
 * administration of user accounts

%prep
%setup -q -n %tarname/trunk

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

#Fix rights for template
chmod -R a+r %buildroot%python_sitelibdir/acct_mgr/templates/*

%files
%doc README
%python_sitelibdir/*

%changelog
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
