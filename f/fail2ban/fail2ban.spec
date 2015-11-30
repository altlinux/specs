Name: fail2ban
Version: 0.9.3
Release: alt1

Summary: Fail2Ban is an intrusion prevention framework

License: GPL v2
Group: Development/Python
Url: http://www.fail2ban.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://github.com/fail2ban/fail2ban/archive/%version.tar.gz
Source: %name-%version.tar
Source1: alt-initd
Source2: fail2ban.service
Source3: fail2ban-logrotate

BuildArch: noarch

BuildPreReq: help2man python-modules-json
%setup_python_module %name
%py_requires json
%add_python_req_skip systemd

%description
Fail2Ban is an intrusion prevention framework written in the Python
programming language. It is able to run on POSIX systems that have an
interface to a packet-control system or firewall installed locally
(for example, iptables or TCP Wrapper).

%prep
%setup

%build
%python_build
export PYTHONPATH=$PWD
cd man
./generate-man

%install
mkdir -p %buildroot%_man1dir/
cp man/*.1 %buildroot%_man1dir/
mkdir -p %buildroot%_man5dir/
cp man/*.5 %buildroot%_man5dir/
install -d %buildroot%_var/run/fail2ban
install -d %buildroot%_datadir
ln -s %python_sitelibdir/%name %buildroot%_datadir/

install -pD -m 744 %SOURCE1 %buildroot%_initdir/fail2ban
install -pD -m 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -pD -m 644 files/fail2ban-tmpfiles.conf %buildroot%_tmpfilesdir/%name.conf
install -pD -m 644 %SOURCE3 %buildroot%_logrotatedir/fail2ban

%python_install --optimize=2
rm -rf %buildroot/%_docdir/%name/

%pre
rm -fR %_datadir/%name

%files
%doc ChangeLog README.md THANKS TODO
%python_sitelibdir/*
%_datadir/%name
%_bindir/%name-*
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/*.d
%dir %_sysconfdir/%name/filter.d/ignorecommands
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/*.d/*.conf
%config(noreplace) %_sysconfdir/%name/*.d/*.py
%config(noreplace) %_sysconfdir/%name/filter.d/ignorecommands/*
%_var/run/fail2ban
%_initdir/fail2ban
%_unitdir/%name.service
%_man1dir/*
%_man5dir/*
%_tmpfilesdir/%name.conf
%_logrotatedir/%name

%changelog
* Tue Nov 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Tue Nov 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt5
- use pid file, fix start/stop logic (ALT bug #29756)
- add logrotate config (ALT bug #29756)

* Wed Jul 08 2015 Eugeny A. Rostovtsev <real at altlinux.org> 0.9.2-alt4
- Fixed for i586 (ALT #31119)

* Thu Jun 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3
- Fixed install (ALT #31047)

* Mon Jun 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2
- Avoid requirement on systemd (ALT #31041)

* Sat May 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Wed Jul 16 2014 Vitaly Lipatov <lav@altlinux.ru> 0.8.13-alt3
- cleanup spec, fix config file permissions

* Tue Jul 15 2014 Vitaly Lipatov <lav@altlinux.ru> 0.8.13-alt2
- add missed systemd server script, man jail.conf, tmpfiles file (ALT bug #29469)

* Fri May 30 2014 Anton Farygin <rider@altlinux.ru> 0.8.13-alt1
- new version

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.8.10-alt2
- implement reload method for service fail2ban

* Thu Jun 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt1
- Version 0.8.10

* Mon Nov 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7.1-alt1
- Version 0.8.7.1 (ALT #27951)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt4.1.1
- Rebuild with Python-2.7

* Tue Aug 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt4.1
- Fixed interaction with %name and iptables (ALT #25921)

* Wed Aug 25 2010 Denis Klimov <zver@altlinux.org> 0.8.4-alt4
- fix inherit with alt gear repo

* Wed Aug 25 2010 Denis Klimov <zver@altlinux.org> 0.8.4-alt3
- add man files to package (Closes: #23948)

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2.1
- Rebuilt with python 2.6

* Mon Nov 16 2009 Denis Klimov <zver@altlinux.org> 0.8.4-alt2
- add /var/run/fail2ban dir to package
- add initd script
- user rpm build python macros
- reduce Summary

* Fri Nov 13 2009 Denis Klimov <zver@altlinux.org> 0.8.4-alt1
- Initial build for ALT Linux

