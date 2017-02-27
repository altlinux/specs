Name: 	  nagwad
Version:  0.5
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

%install
install -Dm 0755 usr/sbin/nagwad %buildroot%_sbindir/nagwad
mkdir -p  %buildroot%_libexecdir/nagwad/devid
install -Dm 0755 usr/lib/nagwad/nagwad.sh  %buildroot%_libexecdir/nagwad/
install -Dm 0755 usr/lib/nagwad/devid/*  %buildroot%_libexecdir/nagwad/devid/
install -Dm 0755 unit/nagwad.service %buildroot/lib/systemd/nagwad.service
mkdir -p  %buildroot%_libexecdir/nagios/plugins/
install -Dm 0755 nagios/plugins/* %buildroot/%_libexecdir/nagios/plugins/
mkdir -p %buildroot/%_docdir
install -Dm 0755 README.md  %buildroot/%_docdir
mkdir -p %buildroot/%_docdir/examples/nrpe
install -Dm 0755 examples/nrpe/*  %buildroot/%_docdir/examples/nrpe/

%files
%_sbindir/*
%_libexecdir/nagwad/*
%_libexecdir/nagwad/devid/*
/lib/systemd/nagwad.service
%_libexecdir/nagios/plugins/*
%_docdir/README.md
%_docdir/examples/nrpe/*


%changelog
* Mon Feb 27 2017 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
 Initial release

