%define module_name fail2ban
Name: %module_name
Version: 0.8.13
Release: alt2

Summary: Fail2Ban is an intrusion prevention framework

License: GPL v2
Group: Development/Python
Url: http://www.fail2ban.org

Source: %name-%version.tar
Source1: alt-initd
Source2: fail2ban.service

BuildArch: noarch

%setup_python_module %module_name


%description
Fail2Ban is an intrusion prevention framework written in the Python
programming language. It is able to run on POSIX systems that have an
interface to a packet-control system or firewall installed locally
(for example, iptables or TCP Wrapper).

%prep
%setup

%build
%python_build
cd man
./generate-man

%install
mkdir -p %buildroot%_man1dir
cp man/*.1 %buildroot%_man1dir
mkdir -p %buildroot%_man5dir
cp man/*.5 %buildroot%_man5dir

install -pD -m 744 %SOURCE1 %buildroot%_initdir/fail2ban
install -pD -m 744 %SOURCE2 %buildroot%_unitdir/%name.service
install -pD -m 744 files/fail2ban-tmpfiles.conf %buildroot%_tmpfilesdir/%name.conf
%python_install
rm -rf %buildroot/%_docdir/%name/

%files
%doc ChangeLog README.md THANKS TODO
%_datadir/%module_name
%_bindir/%module_name-*
%dir %_sysconfdir/%module_name
%dir %_sysconfdir/%module_name/*.d
%config(noreplace) %_sysconfdir/%module_name/*.conf
%config(noreplace) %_sysconfdir/%module_name/*.d/*.conf
%_var/run/fail2ban
%_initdir/fail2ban
%_unitdir/%name.service
%_man1dir/*
%_man5dir/*
%_tmpfilesdir/%name.conf

%changelog
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

