Name: BlockHosts
Version: 2.5.1
Release: alt1.1

Summary: Block IP Addresses based on information in system logs related to SSH/FTP failures

License: GPL
Group: Text tools
Url: http://www.aczoom.com/cms/blockhosts/

BuildArch: noarch
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.aczoom.com/tools/blockhosts/%name-%version.tar

# installs script checks /etc/logrotate dir
BuildPreReq: logrotate
# Automatically added by buildreq on Sat Jan 30 2010
BuildRequires: python-devel

%description
Block IP Addresses based on information in system logs
related to SSH/FTP or other such login attacks.

Updates hosts.allow file automatically, to block IP addresses.
Will also expire previously blocked addresses based on age of last failed
login attempt, this keeps the hosts.allow file size manageable.

%prep
%setup

%build
%python_build

%install
%python_install
rm -f %buildroot%python_sitelibdir/*.egg-info

%files
%doc CHANGES blockhosts.html bhrss.html
%_bindir/*
%config(noreplace) %_logrotatedir/blockhosts
%config(noreplace) %_sysconfdir/blockhosts.cfg

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt1.1
- Rebuild with Python-2.7

* Sun Mar 20 2011 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)

* Tue Aug 17 2010 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Sat Jan 30 2010 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version (2.4.0) import in git

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.1.1
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.3.1-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)

* Tue Dec 18 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sun Nov 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Sat Nov 10 2007 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Wed Sep 19 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.6-alt1
- new version 2.0.6 (with rpmrb script)

* Mon Jun 25 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Sat Jun 09 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)

* Thu May 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)
- this version fixed http://secunia.com/advisories/25352/

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)

* Sun Feb 19 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt0.1
- new version (1.0.4)

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt0.1
- new version
- remove broken buildreq to eric

* Mon Oct 31 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt0.1
- first build for ALT Linux Sisyphus

