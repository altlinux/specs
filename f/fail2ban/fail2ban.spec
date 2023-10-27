Name: fail2ban
Version: 0.11.2
Release: alt3

Summary: Fail2Ban is an intrusion prevention framework

License: GPL v2
Group: Development/Python
Url: http://www.fail2ban.org

# Source-git: https://github.com/fail2ban/fail2ban.git
Source: %name-%version.tar
Source1: alt-initd
Source2: fail2ban.service
Source3: fail2ban-logrotate
Source4: paths-altlinux.conf
Source5: paths-altlinux-systemd.conf

# CVE-2021-32749
Patch1: 410a6ce5c80dd981c22752da034f2529b5eee844.patch
Patch2: 747d4683221b5584f9663695fb48145689b42ceb.patch
# python 3.10 fix
Patch3: ea26509594a3220b012071604d73bb42d0ecae2c.patch
# python 3.12 fix
Patch4: drop-distutils.patch

BuildArch: noarch

BuildRequires: help2man
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: python3-module-urllib3
BuildRequires: python3-tools

AutoProv: no

# due to /etc/fail2ban/action.d/badips.py
%add_python3_lib_path /etc/fail2ban

# obsoleted
%add_python3_req_skip gamin

# https://bugzilla.altlinux.org/show_bug.cgi?id=31041
%add_python3_req_skip systemd

%description
Fail2Ban is an intrusion prevention framework written in the Python
programming language. It is able to run on POSIX systems that have an
interface to a packet-control system or firewall installed locally
(for example, iptables or TCP Wrapper).

Recommends: python3-module-systemd

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%__subst "s|paths-debian.conf|paths-altlinux.conf|g" config/jail.conf
# setuptools>=58 breaks support for use_2to3
%__subst "s|.*use_2to3.*||" setup.py
python3-2to3 -w --no-diffs bin/* fail2ban
%__subst "s|/usr/bin/env python|%__python3|" bin/*

%build
%python3_build
export PYTHONPATH=$PWD
cd man
./generate-man

%install
%python3_install
%python3_prune

mkdir -p %buildroot%_man1dir/
cp man/*.1 %buildroot%_man1dir/
mkdir -p %buildroot%_man5dir/
cp man/*.5 %buildroot%_man5dir/
install -d %buildroot%_var/run/fail2ban

install -pD -m 744 %SOURCE1 %buildroot%_initdir/fail2ban
install -pD -m 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -pD -m 644 %SOURCE3 %buildroot%_logrotatedir/fail2ban
install -pD -m 644 %SOURCE4 %buildroot%_sysconfdir/%name/paths-altlinux.conf
install -pD -m 644 %SOURCE5 %buildroot%_sysconfdir/%name/paths-altlinux-systemd.conf

mkdir -p %buildroot%_tmpfilesdir/
echo "d /var/run/fail2ban 0755 root root -" >%buildroot%_tmpfilesdir/%name.conf

rm -rv %buildroot/%_docdir/%name/
rm -v %buildroot%_sysconfdir/%name/paths-{arch,debian,fedora,freebsd,osx,opensuse}.conf
rm -v %buildroot/usr/bin/fail2ban-testcases

mkdir -p %buildroot%_var/lib/fail2ban/

%post
%post_service %name

%preun
%preun_service %name

%files
%doc ChangeLog README.md THANKS TODO
%python3_sitelibdir/%name/
%python3_sitelibdir/%{name}*.egg-info/
#%_datadir/%name/
%_bindir/%name-python
%_bindir/%name-client
%_bindir/%name-server
%_bindir/%name-regex
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/*.d
%dir %_sysconfdir/%name/filter.d/ignorecommands
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/*.d/*.conf
%config(noreplace) %_sysconfdir/%name/*.d/*.py
%config(noreplace) %_sysconfdir/%name/filter.d/ignorecommands/*
%exclude %_sysconfdir/fail2ban/action.d/__pycache__/
%_var/run/fail2ban/
%_var/lib/fail2ban/
%_initdir/fail2ban
%_unitdir/%name.service
%_man1dir/*
%_man5dir/*
%_tmpfilesdir/%name.conf
%_logrotatedir/%name

%changelog
* Fri Oct 27 2023 Anton Vyatkin <toni@altlinux.org> 0.11.2-alt3
- Dropped dependency on distutils.

* Sat Sep 18 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.2-alt2
- fix build, apply patches from upstream
- .service: use /run instead of /var/run
- CVE-2021-32749

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.2-alt1
- new version 0.11.2 (with rpmrb script) (ALT bug 40859)
- don't pack tests, disable AutoProv

* Thu Mar 12 2020 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt1
- new major version 0.11.1 (with rpmrb script)
- switch to python3
- add paths-altlinux-systemd.conf
- see ChangeLog for upgrade instructions

* Wed Oct 03 2018 Anton Farygin <rider@altlinux.ru> 0.10.3.1-alt1
- 0.10.3.1

* Wed Apr 12 2017 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- new version

* Mon Dec 05 2016 Anton Farygin <rider@altlinux.ru> 0.9.5-alt2
- removed iptables requires
- added requires to python-module-systemd (closes: #32592)

* Sat Oct 22 2016 Anton Farygin <rider@altlinux.ru> 0.9.5-alt1
- new version

* Thu Dec 03 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt3
- add post/preun_service
- add condreload/condrestart
- drop /usr/share/fail2ban link

* Wed Dec 02 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt2
- fix paths, drop rm -rf from pre script
- create directory for persistent database

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

