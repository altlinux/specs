Name: ser2net
Version: 2.5
Release: alt1
Summary: The ser2net daemon allows telnet and tcp sessions to be established with a unit's serial ports.
License: GPL
Group: System/Servers
Url: http://ser2net.sourceforge.net/
Packager: Eugene Prokopiev <enp@altlinux.ru>

PreReq: chkconfig

Source0: %name-%version.tar
Source1: %name.init

Requires: service

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
%configure
%make_build

%install
%__mkdir_p %buildroot/%_sbindir
%__mkdir_p %buildroot/%_man8dir
%__mkdir_p %buildroot/%_sysconfdir
%__mkdir_p %buildroot/%_initdir

%__make DESTDIR=%buildroot install

%__install -m 0644 ser2net.conf %buildroot/%_sysconfdir
%__install -m 0755 %SOURCE1 %buildroot/%_initdir/ser2net

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/*
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/*
%_man8dir/*
%doc README NEWS ChangeLog COPYING INSTALL AUTHORS

%changelog
* Tue Apr 15 2008 Eugene Prokopiev <enp@altlinux.ru> 2.5-alt1
- first build for Sisyphus


