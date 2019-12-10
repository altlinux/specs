%define _unpackaged_files_terminate_build 1

Name: supervisor
Version: 4.1.0
Release: alt1

Summary: A System for Allowing the Control of Process State on UNIX
License: ZPLv2.1 and BSD and MIT
Group: System/Base
Url: http://supervisord.org/
BuildArch: noarch

Source: http://pypi.io/packages/source/s/%name/%name-%version%{?prever}.tar
Source1: supervisord.service
Source2: supervisord.conf
Source3: supervisor.logrotate
Source4: supervisor.tmpfiles
Source5: supervisord.init

BuildRequires(pre): rpm-build-python3 rpm-build-intro
Requires: python3-module-%name


%description
The supervisor is a client/server system that allows its users to control a
number of processes on UNIX-like operating systems.

%package -n python3-module-%name
Summary: Python3 module for %name
Group: Development/Python3
Requires: python3-module-meld3 >= 0.6.5

%description -n python3-module-%name
The supervisor is a client/server system that allows its users to control a
number of processes on UNIX-like operating systems.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

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

%__subst s'/^#!.*//' $( find %buildroot/%python3_sitelibdir/supervisor/ -type f)

mkdir -p %buildroot%_sysconfigdir/
touch %buildroot%_sysconfigdir/supervisord
mkdir -p %buildroot/%_initdir
install -p -m 755 %SOURCE5 %buildroot/%_initdir/supervisord

rm -rf %buildroot/%python3_sitelibdir/supervisor/meld3/
rm -f %buildroot%prefix/doc/*.txt

%files
%doc *.txt *.rst
%dir %_logdir/%name
%_bindir/supervisor*
%_bindir/echo_supervisord_conf
%_bindir/pidproxy
%_unitdir/supervisord.service
%_initdir/supervisord
%_runtimedir/supervisor
%_tmpfilesdir/%name.conf

%config(noreplace) %_sysconfdir/supervisord.conf
%dir %_sysconfdir/supervisord.d/
%config(noreplace) %_logrotatedir/supervisor
%config(noreplace) %_sysconfigdir/supervisord

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt1
- version updated to 4.1.0

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 3.3.5-alt1
- new version 3.3.5 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3.4-alt1
- new version 3.3.4 (with rpmrb script)

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

