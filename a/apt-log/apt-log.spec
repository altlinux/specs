Name: apt-log
Version: 0.1
Release: alt2

Summary: Log support for APT
License: GPL
Group: System/Configuration/Packaging
Packager: Evgenii Terechkov <evg@altlinux.ru>

Source0: %name-%version.tar.gz

Requires: apt-scripts
BuildRequires: apt
BuildArch: noarch

%description
This package add support for package transaction logging to APT.
Default log file is /var/log/apt.log

%prep
%setup -q

%install
for i in *.lua; do install -pD -m644 $i %buildroot%_datadir/apt/scripts/$i; done
for i in *.conf; do install -pD -m644 $i %buildroot%_sysconfdir/apt/apt.conf.d/$i; done

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
ls *.conf |sed 's:^:^%_sysconfdir/apt/apt.conf.d/:;s:[.]:[.]:g' >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name

mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/apt.log
chmod 644 %buildroot%_logdir/apt.log
install -pD -m644 %name.logrotate %buildroot%_sysconfdir/logrotate.d/apt-log

%files
%ghost %_logdir/apt.log
%_datadir/apt/scripts/*.lua
%config %_sysconfdir/apt/apt.conf.d/*.conf
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name

%changelog
* Thu Mar 20 2008 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt2
- Logrotate file added (#14922)
- Packager tag added to spec

* Sun Jun 24 2007 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt1
- Initial build for Sisypus
 
