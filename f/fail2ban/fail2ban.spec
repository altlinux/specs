%define module_name fail2ban
Name: %module_name
Version: 0.8.4
Release: alt4.1.1

Summary: Fail2Ban is an intrusion prevention framework

License: GPL v2
Group: Development/Python
Url: http://www.fail2ban.org

Source: %name-%version.tar
Source1: alt-initd
Packager: Denis Klimov <zver@altlinux.org>

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

install -pD -m 744 %SOURCE1 %buildroot%_initdir/fail2ban
%python_install

%files
%doc README
%_datadir/%module_name
%_bindir/%module_name-*
%_sysconfdir/%module_name
%_var/run/fail2ban
%_initdir/fail2ban
%_man1dir/fail2ban-*

%changelog
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

