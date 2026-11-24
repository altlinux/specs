Name: ser2net
Version: 4.6.8
Release: alt1

Summary: The ser2net daemon allows telnet and tcp sessions to be established with a unit's serial ports.
License: GPLv2
Group: System/Servers
URL: https://github.com/cminyard/ser2net
VCS: https://github.com/cminyard/ser2net

Source: %name-%version.tar

Buildrequires: libgensio-devel libyaml-devel

%description
The ser2net daemon allows telnet and tcp sessions to be established
with a unit's serial ports.

The program comes up normally as a daemon, opens the TCP ports
specified in the configuration file, and waits for connections.  Once
a connection occurs, the program attempts to set up the connection and
open the serial port.  If another user is already using the connection
or serial port, the connection is refused with an error message.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pm0644 -D ser2net.yaml %buildroot%_sysconfdir/ser2net/ser2net.yaml
install -pm0644 -D ser2net.sysusers %buildroot%_sysusersdir/ser2net.conf
install -pm0644 -D ser2net.service %buildroot%_unitdir/ser2net.service
mkdir -p %buildroot%_sysconfdir/ser2net/auth

%files
%doc AUTHORS COPYING README.rst
%dir %_sysconfdir/ser2net
%dir %_sysconfdir/ser2net/auth
%config(noreplace) %_sysconfdir/ser2net/ser2net.yaml
%_sysusersdir/ser2net.conf
%_unitdir/ser2net.service
%_bindir/ser2net
%_man5dir/ser2net.yaml.5*
%_man8dir/ser2net.8*

%changelog
* Tue Nov 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.6.8-alt1
- 4.6.8 released

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Apr 15 2008 Eugene Prokopiev <enp@altlinux.ru> 2.5-alt1
- first build for Sisyphus
