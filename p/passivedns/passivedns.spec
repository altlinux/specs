%define _unpackaged_files_terminate_build 1

Name: passivedns
Version: 1.2.1
Release: alt1
Summary: A network sniffer that logs all DNS server replies for use in a passive DNS setup
License: GPLv2
Group: Monitoring
URL: https://github.com/gamelinux/passivedns

Source: %name-%version.tar
Source2: %name.init
Source3: %{name}@.service

Patch1: %name-%version-alt.patch

BuildRequires: libpcap-devel libldns-devel
BuildRequires: libjansson-devel
BuildRequires: perl(DBI.pm) perl(Date/Simple.pm) perl(DateTime.pm) perl(Time/Local.pm)

%description
A tool to collect DNS records passively to aid Incident handling, Network
Security Monitoring (NSM) and general digital forensics.

PassiveDNS sniffes traffic from an interface or reads a pcap-file and outputs
the DNS-server answers to a log file. PassiveDNS can cache/aggregate duplicate
DNS answers in-memory, limiting the amount of data in the logfile without
loosing the essens in the DNS answer.

%package daemon
Summary: Daemon for passive DNS 
Group: Monitoring
Requires: %name = %EVR

%description daemon
Daemon for %name

%package tools
Summary: Tools for passive DNS 
Group: Monitoring

%description tools
A tools for work with %name data

%prep
%setup
%patch1 -p1

find . -type f | xargs sed -i \
	-e "s|%_logdir/passivedns.log|%_logdir/%name/passivedns.log|g" \
	-e "s|%_logdir/passivedns.stats|%_logdir/%name/passivedns.stats|g" \
	-e "s|%_logdir/passivedns-run.log|%_logdir/%name/passivedns-run.log|g" \
	-e "s|%_logdir/passivedns-alert.log|%_logdir/%name/passivedns-alert.log|g" \
	%nil

%build
%autoreconf
%configure \
	--enable-json \
	%nil

%make_build

%install
install -pD -m755 src/%name %buildroot%_sbindir/%name
install -pD -m755 tools/pdns2db.pl %buildroot%_bindir/pdns2db.pl
install -pD -m755 tools/search-pdns.pl %buildroot%_bindir/search-pdns.pl
install -pD -m755 %SOURCE2 %buildroot%_initdir/%name

mkdir -p %buildroot%_unitdir
install -pD -m755 %SOURCE3 %buildroot%_unitdir/%{name}@.service

mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_logrotatedir

cat > %buildroot%_sysconfdir/sysconfig/%name  <<EOF
#OPTIONS:
# -i <iface>      Network device <iface> (default: eth0).
# -l <file>       Name of the logfile (default: %_logdir/%name/passivedns.log).
# -b 'BPF'        Berkley Packet Filter (default: 'port 53').
# -S <mem>        Soft memory limit in MB (default: 256).
# -C <sec>        Seconds to cache DNS objects in memory (default 43200).
# -P <sec>        Seconds between printing duplicate DNS info (default 86400).
# -X <flags>      Manually set DNS RR Types to care about(Default -X 46CDNPRS).

OPTIONS='-i lo'

EOF

cat << EOF > %buildroot%_logrotatedir/%name
%_logdir/%name/%name.log {
    create 644 root _%name
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
}

EOF


%pre
/usr/sbin/groupadd -r -f _%name
/usr/sbin/useradd -r -g _%name -d %_sharedstatedir/%name -s /dev/null -n -c "DNS network sniffer" _%name >/dev/null 2>&1 ||:

%post daemon
%post_service %name

%preun daemon
%preun_service %name

%files
%doc README doc tools/README.skip_white_black-list.txt www
%_sbindir/*
%dir %attr(3770,root,_%name) %_logdir/%name
%_logrotatedir/%name

%files daemon
%dir %_sharedstatedir/%name
%_sysconfdir/sysconfig/%name
%_initdir/*
%_unitdir/%{name}@.service

%files tools 
%_bindir/*.pl

%changelog
* Wed Feb 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt1
- Updated to upstream version 1.2.1.
- Removed %%ubt macro from release.

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt2
- Rebuilt with ldns-1.7.0.
- Added %%ubt macro to release.
- Added systemd service.

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- NMU: new version (fixes build)

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1.git20140826.1
- bugfixes for perl 5.22

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20140826
- New snapshot

* Tue Dec 31 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.3-alt1
- New version

* Tue Mar 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.3-alt1
- built for ALT Linux
