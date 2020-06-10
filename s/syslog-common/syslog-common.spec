Name: syslog-common
Version: 2.1
Release: alt1

Summary: Common files for syslog servers
License: GPLv2+
Group: System/Servers
BuildArch: noarch
Url: http://git.altlinux.org/gears/s/syslog-common.git

Source0: syslog.log
Source1: reload-syslog.sh

%description
This package contains log directories structure and logrotate scripts
for different syslog server implementations.

%prep
%setup -cT

%install
install -pD -m640 %_sourcedir/syslog.log \
	%buildroot%_sysconfdir/logrotate.d/syslog

install -pD -m700 %_sourcedir/reload-syslog.sh \
	%buildroot/sbin/reload-syslog

d=$(pwd)
mkdir -p %buildroot%_logdir
cd %buildroot%_logdir

mkdir -p kernel user mail daemons auth lpr news uucp cron ftp syslog
%define syslog_files {{kernel,user,mail,daemons,lpr,news,uucp,cron,ftp}/{info,warnings,errors} auth/{all,messages,secure} mail/all syslog/{messages,alert,spooler,boot,sudo}}
touch %syslog_files
ln -s syslog/alert alert
ln -s syslog/boot boot.log
ln -s mail/all maillog
ln -s syslog/messages messages
ln -s auth/secure secure
ln -s syslog/spooler spooler

{
	find . -mindepth 1 -type d |
		sed 's|^\.|%%dir %%attr(750,root,adm) %_logdir|'
	find . -mindepth 1 -type l |
		sed 's|^\.|%%attr(-,root,root) %_logdir|'
	find . -mindepth 1 -type f |
		sed 's|^\.|%%ghost %%attr(640,root,adm) %%verify(not md5 mtime size) %_logdir|'
} > $d/%name.files

%post
umask 077
cd %_logdir
# create each log directory with log files
for f in %syslog_files; do
	[ -f "$f" ] || {
		>>"$f"
		chgrp -h adm "$f"
		chmod 640 "$f"
	}
done ||:

%files -f %name.files
/sbin/reload-syslog
%config(noreplace) %_sysconfdir/logrotate.d/*

%changelog
* Wed Jun 10 2020 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt1
- reload-syslog: added systemd support (closes: #38594).

* Tue Aug 28 2018 Dmitry V. Levin <ldv@altlinux.org> 2-alt1
- Split syslog-common out of sysklogd package.
- Moved /etc/syslog.d to filesystem package.
- Fixed %_logdir/uucp permissions (closes: #31636).
