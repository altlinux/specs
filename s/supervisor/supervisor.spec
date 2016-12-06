Name: supervisor
Version: 3.3.1
Release: alt1

Summary: A System for Allowing the Control of Process State on UNIX

License: ZPLv2.1 and BSD and MIT
Group: System/Base
Url: http://supervisord.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.io/packages/source/s/%name/%name-%version%{?prever}.tar
Source1: supervisord.init
Source2: supervisord.conf
Source3: supervisor.logrotate

AutoProv:yes,nopython
%add_python_req_skip %name

BuildArch: noarch
BuildRequires: python-devel rpm-build-intro
BuildRequires: python-module-setuptools

Requires: python-module-meld3 >= 0.6.5
Requires: python-module-setuptools

%description
The supervisor is a client/server system that allows its users to control a
number of processes on UNIX-like operating systems.

%prep
%setup

%build
%python_build

%install
%python_install

mkdir -p %buildroot/%_sysconfdir
mkdir -p %buildroot/%_sysconfdir/supervisord.d
mkdir -p %buildroot/%_sysconfdir/logrotate.d/
mkdir -p %buildroot/%_initdir
mkdir -p %buildroot/%_localstatedir/log/%name
chmod 770 %buildroot/%_localstatedir/log/%name
install -p -m 755 %SOURCE1 %buildroot/%_initdir/supervisord
install -p -m 644 %SOURCE2 %buildroot/%_sysconfdir/supervisord.conf
install -p -m 644 %SOURCE3 %buildroot/%_sysconfdir/logrotate.d/supervisor
%__subst s'/^#!.*//' $( find %buildroot/%python_sitelibdir/supervisor/ -type f)
mkdir -p %buildroot%_sysconfigdir/
touch %buildroot%_sysconfigdir/supervisord

rm -rf %buildroot/%python_sitelibdir/supervisor/meld3/
rm -f %buildroot%prefix/doc/*.txt

%files
%doc CHANGES.txt COPYRIGHT.txt README.rst LICENSES.txt TODO.txt
%dir %_localstatedir/log/%name
%python_sitelibdir/*
%_initdir/supervisord
%_bindir/supervisor*
%_bindir/echo_supervisord_conf
%_bindir/pidproxy

%config(noreplace) %_sysconfdir/supervisord.conf
%dir %_sysconfdir/supervisord.d/
%config(noreplace) %_sysconfdir/logrotate.d/supervisor
%config(noreplace) %_sysconfigdir/supervisord

%changelog
* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 3.2.3-alt1
- new version 3.2.3 (with rpmrb script)

* Mon Aug 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.3-alt1
- new version 3.1.3 (with rpmrb script)

* Mon Aug 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- initial build for ALT Linux Sisyphus

