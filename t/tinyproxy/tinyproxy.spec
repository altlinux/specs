Name: tinyproxy
Version: 1.11.1
Release: alt2

Summary: A small, efficient HTTP/SSL proxy daemon
License: GPLv2
Group: System/Servers

Url: http://tinyproxy.github.io/
# repacked https://github.com/tinyproxy/tinyproxy/archive/refs/tags/%version.tar.gz
Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: %name.conf
Source4: %name.logrotate
Source5: %name.tmpfiles
Source6: %name.sysconfig

BuildRequires: make gcc /usr/bin/pod2man

%description
tinyproxy is a small, efficient HTTP/SSL proxy daemon that is very useful in a
small network setting, where a larger proxy like Squid would either be too
resource intensive, or a security risk.

%define tinyproxy_rundir /run/tinyproxy
%define tinyproxy_logdir %_logdir/%name
%define tinyproxy_confdir %_sysconfdir/%name
%define tinyproxy_user tinyproxy
%define tinyproxy_group tinyproxy

%prep
%setup

%build
%autoreconf
%configure --enable-reverse \
	   --enable-transparent \
	   --enable-xtinyproxy \
	   --enable-filter

%make_build

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pDm755 %SOURCE2 %buildroot%_initdir/%name
install -pDm644 %SOURCE3 %buildroot%tinyproxy_confdir/%name.conf
install -pDm644 %SOURCE4 %buildroot%_logrotatedir/%name
install -pDm644	%SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -pDm640 %SOURCE6 %buildroot%_sysconfdir/sysconfig/%name
install -pdm755 %buildroot%tinyproxy_rundir
install -pdm755 %buildroot%tinyproxy_logdir

#delete duplicates doc files
rm -rf "%buildroot%_datadir/doc/%name"

%pre
if [ $1 == 1 ]; then
#Add the "tinyproxy" user
	%_sbindir/groupadd -r -f %tinyproxy_group 2>/dev/null ||:
	%_sbindir/useradd  -r -g %tinyproxy_group -c 'Tinyproxy daemon' \
		-s /dev/null -d /dev/null %tinyproxy_user 2>/dev/null ||:

fi

%post
%post_service %name

%preun
%preun_service %name
%files
%doc AUTHORS README NEWS README.md docs/*.txt
%_bindir/%name
%_man8dir/%name.8.xz
%_man5dir/%name.conf.5.xz
%_unitdir/%name.service
%_initdir/%name
%_sysconfdir/sysconfig/%name
%_tmpfilesdir/%name.conf
%_datadir/%name
%dir %tinyproxy_confdir
%ghost %dir %tinyproxy_rundir
%dir %tinyproxy_logdir
%config(noreplace) %tinyproxy_confdir/%name.conf
%config(noreplace) %_logrotatedir/%name
%attr(2770,root,%tinyproxy_group) %ghost %dir %tinyproxy_rundir
%attr(2770,root,%tinyproxy_group) %dir %tinyproxy_logdir

%changelog
* Tue May 07 2024 Nikolay Burykin <bne@altlinux.org> 1.11.1-alt2
- Fix (CVE-2023-49606)

* Wed Apr 05 2023 Nikolay Burykin <bne@altlinux.org> 1.11.1-alt1
- New version 1.11.1

* Fri Aug 20 2021 Nikolay Burykin <bne@altlinux.org> 1.11.0-alt1
- Initial build for ALT

