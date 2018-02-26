Name: atsar_linux
Version: 1.7
Release: alt1
License: GPL
Summary: AT Computing System Activity Report is a sar clone for Linux
Group: System/Base
Packager: Mikhail Pokidko <pma@altlinux.org>
URL: ftp://ftp.atcomputing.nl/pub/tools/linux/
Source0: atsar_linux-1.7.tar.gz
Patch0: atsar-full.patch

%description
Atsar can be used to measure the load on the most relevant system resources,
such as CPU, disk, memory and network.  Long-term analysis can be done via
cron, by maintaining log files with statistical information.  Short-term
analysis can be done by starting the command atsar with an interval and
a number of samples.
The current version of atsar gathers statistics about the utilization
of CPU's, disks, memory and swap, serial lines and network (TCP/IP v4 and v6).

%prep
%setup -q
%patch0 -p1
%build
%make

%install
mkdir -p  %buildroot%_bindir
install -m 0755 atsar/atsar atsadc/atsadc scripts/atsa1	\
                scripts/atsaftp scripts/atsahttp %buildroot%_bindir
mkdir -p  %buildroot%_man1dir
install -m 0644 man/* %buildroot%_man1dir
install -m 0755 -d %buildroot%_logdir/%name
mkdir -p  %buildroot%_initdir
install -m 0755 atsar_linux.init %buildroot%_initdir/%name
mkdir -p  %buildroot/etc/cron.d
install -m 0644 atsar_linux.cron %buildroot%_sysconfdir/cron.d/%name
install -m 0644 atsar_linux.conf %buildroot%_sysconfdir/%name.conf
mkdir -p %buildroot%_logdir/atsar

%post
/sbin/chkconfig --add %name

mkdir -d -m 0755 %_logdir/atsar     2> /dev/null
rm    /var/log/atsar/atsa`date +%d` 2> /dev/null
rm    /var/log/atsar/ftpstat        2> /dev/null
rm    /var/log/atsar/httpstat       2> /dev/null
touch /var/lock/subsys/atsar
%_bindir/atsa1
echo "Configure the names of FTP- and HTTP-logfiles in /etc/atsar.conf ...."

%preun
if [ $1 = 0 ]; then
	/sbin/chkconfig --del atsar
fi

%postun
rm -f /var/lock/subsys/atsar 2> /dev/null

%files
%doc README
%_bindir/*
#_bindir/atsadc
#_bindir/atsa1
#_bindir/atsaftp
#_bindir/atsahttp
%_man1dir/atsa*.1*
%config %_initdir/%name
%config %_sysconfdir/cron.d/%name
%config %_sysconfdir/%name.conf
%_logdir/atsar

%changelog
* Wed Sep 13 2006 Mikhail Pokidko <pma@altlinux.ru> 1.7-alt1
- Initial build

