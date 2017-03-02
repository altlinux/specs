Name: 	  nagwad
Version:  0.6
Release:  alt1

Summary:  Nagios watch daemon
License:  MIT
Group:    System/Servers
Url: 	  http://git.altlinux.org/people/nbr/packages/nagwad.git


Source:   %name-%version.tar

BuildArch: noarch

Requires:  systemd

%description
Daemon that listens to journald and generates alerts based on journal messages
Example configuration works with alterator-ports-access. It provides Nagios
alerts when unauthorized USB devices are inserted.

%prep
%setup

%package server

Summary: Server for nagwad example data and docs
Group:   System/Servers

%description server
These are examples of configuration of Nagios for the controlling machine.


%install
install -Dm 0755 usr/sbin/nagwad %buildroot%_sbindir/nagwad
mkdir -p  %buildroot%_libexecdir/nagwad/device
mkdir -p  %buildroot%_libexecdir/nagwad/audit
mkdir -p  %buildroot%_libexecdir/nagwad/authdata
mkdir -p  %buildroot%_libexecdir/nagwad/osec
install -Dm 0755 usr/lib/nagwad/nagwad.sh  %buildroot%_libexecdir/nagwad/
install -Dm 0755 usr/lib/nagwad/device/*  %buildroot%_libexecdir/nagwad/device/
install -Dm 0755 usr/lib/nagwad/audit/*  %buildroot%_libexecdir/nagwad/audit/
install -Dm 0755 usr/lib/nagwad/authdata/*  %buildroot%_libexecdir/nagwad/authdata/
install -Dm 0755 usr/lib/nagwad/osec/*  %buildroot%_libexecdir/nagwad/osec/
install -Dm 0755 unit/nagwad.service %buildroot/lib/systemd/nagwad.service
mkdir -p  %buildroot%_libexecdir/nagios/plugins/
install -Dm 0755 nagios/plugins/* %buildroot/%_libexecdir/nagios/plugins/
mkdir -p %buildroot/%_docdir
install -Dm 0755 README.md  %buildroot/%_docdir
mkdir -p %buildroot/%_docdir/examples/nrpe
install -Dm 0755 examples/nrpe/*  %buildroot/%_docdir/examples/nrpe/
mkdir -p %buildroot/%_docdir/examples/nagios/server/objects
mkdir -p %buildroot/%_docdir/examples/nagios/server/templates
cp -ar examples/nagios/*  %buildroot/%_docdir/examples/nagios/
install -Dm 0755 signal.odt %buildroot/%_docdir
mkdir -p %buildroot/%_localstatedir/nagwad/audit
mkdir -p %buildroot/%_localstatedir/nagwad/audit_archived
mkdir -p %buildroot/%_localstatedir/nagwad/authdata
mkdir -p %buildroot/%_localstatedir/nagwad/authdata_archived
mkdir -p %buildroot/%_localstatedir/nagwad/osec
mkdir -p %buildroot/%_localstatedir/nagwad/osec_archived
mkdir -p %buildroot/%_localstatedir/nagwad/device
mkdir -p %buildroot/%_localstatedir/nagwad/device_archived

%files
%_sbindir/*
%_libexecdir/nagwad/*
/lib/systemd/nagwad.service
%_libexecdir/nagios/plugins/*
%_localstatedir/nagwad/*
%_localstatedir/nagwad/*/
%_docdir/README.md
%_docdir/examples/nrpe/*


%files server
%_docdir/examples/nagios/*
%_docdir/signal.odt


%changelog
* Thu Mar 02 2017 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
- More mature version that checks 3 additional signals.

* Mon Feb 27 2017 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
 Initial release

