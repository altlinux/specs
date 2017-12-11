Name: supervisor
Version: 3.3.3
Release: alt1

Summary: A System for Allowing the Control of Process State on UNIX

License: ZPLv2.1 and BSD and MIT
Group: System/Base
Url: http://supervisord.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.io/packages/source/s/%name/%name-%version%{?prever}.tar
Source1: supervisord.service
Source2: supervisord.conf
Source3: supervisor.logrotate
Source4: supervisor.tmpfiles
Source5: supervisord.init

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
mkdir -p %buildroot/%_logrotatedir/
mkdir -p %buildroot/%_unitdir
mkdir -p %buildroot/%_logdir/%name
mkdir -p %buildroot/%_runtimedir/supervisor
chmod 770 %buildroot/%_logdir/%name
chmod 770 %buildroot/%_runtimedir/supervisor
install -p -m 644 %SOURCE1 %buildroot/%_unitdir/supervisord.service
install -p -m 644 %SOURCE2 %buildroot/%_sysconfdir/supervisord.conf
install -p -m 644 %SOURCE3 %buildroot/%_logrotatedir/supervisor
install -D -p -m 0644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
%__subst s'/^#!.*//' $( find %buildroot/%python_sitelibdir/supervisor/ -type f)
mkdir -p %buildroot%_sysconfigdir/
touch %buildroot%_sysconfigdir/supervisord
mkdir -p %buildroot/%_initdir
install -p -m 755 %SOURCE5 %buildroot/%_initdir/supervisord

rm -rf %buildroot/%python_sitelibdir/supervisor/meld3/
rm -f %buildroot%prefix/doc/*.txt

%files
%doc CHANGES.txt COPYRIGHT.txt README.rst LICENSES.txt
%dir %_logdir/%name
%_unitdir/supervisord.service
%python_sitelibdir/*
%_initdir/supervisord
%_bindir/supervisor*
%_bindir/echo_supervisord_conf
%_bindir/pidproxy
%_runtimedir/supervisor
%_tmpfilesdir/%name.conf

%config(noreplace) %_sysconfdir/supervisord.conf
%dir %_sysconfdir/supervisord.d/
%config(noreplace) %_logrotatedir/supervisor
%config(noreplace) %_sysconfigdir/supervisord

%changelog
* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 3.3.3-alt1
- new version 3.3.3 (with rpmrb script)

* Tue Mar 21 2017 Lenar Shakirov <snejok@altlinux.ru> 3.3.1-alt2
- systemd ready now
- Move socket to /var/run/supervisor. Fedora bug #1247877
- use %%_logdir instead %%_localstatedir/log

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 3.2.3-alt1
- new version 3.2.3 (with rpmrb script)

* Mon Aug 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.3-alt1
- new version 3.1.3 (with rpmrb script)

* Mon Aug 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- initial build for ALT Linux Sisyphus

