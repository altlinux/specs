Name: mcelog
Version: 0.8
Release: alt0.1

Summary: Tool to translate x86-64 CPU Machine Check Exception data
Group: System/Base
License: GPL
Url: ftp://ftp.x86-64.org/pub/linux/tools/mcelog
Packager: Dmitry V. Levin <ldv@altlinux.org>
ExclusiveArch: x86_64

# ftp://ftp.x86-64.org/pub/linux/tools/mcelog/mcelog-0.8pre.tar.gz
Source: mcelog-0.8pre.tar

Source1: mcelog.cron
Source2: mcelog.logrotate

Patch: mcelog-0.8pre-alt-fmt_tsc.patch

%description
mcelog is a tool that collects and decodes Machine Check Exception data
on x86-64 machines.

%prep
%setup -n mcelog-0.8pre
%patch -p1

%build
%make_build mcelog CFLAGS='%optflags -fpie' LDFLAGS=-pie

%install
install -pD -m755 mcelog \
	%buildroot%_sbindir/mcelog
install -pD -m644 mcelog.8 \
	%buildroot%_man8dir/mcelog.8
install -pD -m700 %_sourcedir/mcelog.cron \
	%buildroot/etc/cron.hourly/mcelog
install -pD -m600 %_sourcedir/mcelog.logrotate \
        %buildroot/etc/logrotate.d/mcelog
install -pD -m600 /dev/null \
        %buildroot/var/log/mcelog
	
%files
%config(noreplace) /etc/cron.hourly/*
%config(noreplace) /etc/logrotate.d/*
%ghost /var/log/mcelog
%_sbindir/*
%_man8dir/*
%doc CHANGES README mce.pdf

%changelog
* Thu Jun 28 2007 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt0.1
- Initial revision.
