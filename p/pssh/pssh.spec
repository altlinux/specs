Name: pssh
Version: 2.3.1
Release: alt1

Summary: Parallel SSH tools

Url: http://www.theether.org/pssh/
Group: Shells
License: BSD like

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://parallel-ssh.googlecode.com/files/%name-%version.tar

BuildArch: noarch

# https://bugzilla.altlinux.org/show_bug.cgi?id=14907
Conflicts: putty

# Automatically added by buildreq on Thu Feb 21 2008
BuildRequires: python-module-setuptools

%description
This package provides various parallel tools based on ssh and scp.

%prep
%setup
%__subst "s|'man/man1'|'share/man/man1'|g" setup.py

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING ChangeLog
%_bindir/*
%python_sitelibdir/psshlib/
%python_sitelibdir/%{name}*.egg-info
%_man1dir/*

%changelog
* Sat Jun 02 2012 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt3.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3.1
- Rebuilt with python 2.6

* Sat Mar 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt3
- add conflicts to putty (fix bug #14907)

* Thu Feb 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- build as noarch (thanks to Grigory Batalov)
- add docs, change license to BSD like

* Tue Oct 09 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version 1.2.2 (with rpmrb script)

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.1
- initial build for ALT Linux Sisyphus
