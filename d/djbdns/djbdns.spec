Name: djbdns
Version: 1.05
Release: alt1

Summary: A bind replacement
License: Public domain
Group: Networking/DNS
URL: http://cr.yp.to/djbdns.html

Source: http://cr.yp.to/djbdns/%name-%version.tar
Source1: alt-stuff.tar
Packager: Boris Gulay <boresexpress@altlinux.org>

BuildPreReq: rpm-macros-daemontools >= 0.76-alt12

Patch: %name-%version.errno.patch
Patch1: %name-%version.srv.patch
Patch2: %name.check.setgroup.patch
Patch3: %name.HOME.patch

%description 
dnscache maintains a limited-size cache of DNS information, 1 megabyte
by default. When the cache fills up, dnscache smoothly discards old
cache entries.

You can easily configure dnscache to send queries for a particular
domain to a particular set of servers, such as ``split DNS'' internal
servers behind a firewall. All you have to do is put the server IP
addresses into a file named after the domain.

The djbdns package includes three servers that publish local host
information: tinydns, walldns, and rbldns. Every aspect of
configuration was rethought from the perspective of an overworked
administrator who has better things to do than play with DNS.

tinydns handles basic DNS service. The tinydns-data file format
combines the flexibility of zone files with the convenience of modern
zone-building tools. Host information is stored in one file. PTR
records are handled automatically. Changes can be scheduled in
advance, with TTLs handled automatically.

tinydns has several load-balancing features. It automatically
selects a random set of 8 servers from a cluster of any size. It
allows easy removal of dead servers by external monitoring
tools. It also supports client differentiation, checking the
client's IP address and choosing one of several clusters
accordingly.  walldns is a reverse DNS wall. It lets firewalled
sites access name-checking servers without revealing true host
information.

rbldns publishes lists of IP addresses, such as RBL or DUL, through
DNS. This could be done with a general-purpose server, but rbldns uses
much less memory and much less disk space.

Databases for tinydns, pickdns, and rbldns are compiled into cdb
format. The servers start up instantly, even if the database is a
gigabyte or more. While a new database is being compiled, the servers
continue to answer queries from the old database. There is no gap in
DNS service when the new database is finished. The old database is
left in place if anything goes wrong.

%prep
%setup
%setup -T -D -a 1
%patch -p1
%patch1 -p1
%patch2 -p0
%patch3 -p2

%build
%make_build prog

# Folders
%define djbdns_cd_nr	%_sysconfdir/djbdns
%define djbdns_cd		%buildroot%djbdns_cd_nr
%define djbdns_ld_nr	%_var/log/djbdns
%define djbdns_ld		%buildroot%djbdns_ld_nr

%package common
Summary: Common files
Group: System/Base
BuildArch: noarch

%description common
Common files for DJBDNS package

%package dnscache
Summary: DNS cache
Group: Networking/DNS
Requires: %name-common = %version-%release daemontools >= 0.76-alt7

%description dnscache
dnscache is a DNS cache. It accepts recursive DNS queries from local
clients such as web browsers and mail transfer agents. It collects
responses from remote DNS servers. It caches the responses to save time
later.

%pre dnscache
adduser -r -M -c "DJBDNS logging account" -s /dev/null -d %_var/log/djbdns djbdns_log > /dev/null 2>&1 ||:
adduser -r -M -c "DJBDNS account" -s /dev/null -d %djbdns_cd_nr djbdns > /dev/null 2>&1 ||:

%postun dnscache
svc -d %daemontools_conf/dnscache
svc -d %daemontools_conf/dnscache/log

%package tinydns
Summary: DNS server
Group: Networking/DNS
Requires: %name-common = %version-%release daemontools >= 0.76-alt7

%description tinydns
tinydns is a DNS server. It accepts iterative DNS queries from hosts
around the Internet, and responds with locally configured information.

%pre tinydns
adduser -r -M -c "DJBDNS logging account" -s /dev/null -d %_var/log/djbdns djbdns_log > /dev/null 2>&1 ||:
adduser -r -M -c "DJBDNS account" -s /dev/null -d %djbdns_cd_nr djbdns > /dev/null 2>&1 ||:

%postun tinydns
svc -d %daemontools_conf/tinydns
svc -d %daemontools_conf/tinydns/log

%package axfrdns
Summary: DNS zone transfer server and client
Group: Networking/DNS
Requires: ucspi-tcp >= 0.88-alt1
Requires(pre): %name-tinydns = %version-%release

%description axfrdns
axfrdns is a DNS zone-transfer server. It reads a zone-transfer request
in DNS-over-TCP format from its standard input, and responds with
locally configured information.
axfr-get is a DNS zone-transfer client. It sends a zone-transfer request
in DNS-over-TCP format to descriptor 7, reads the results from
descriptor 6, and saves the results in a file.
Normally axfr-get is run under tcpclient, which sets up descriptors 6
and 7 as a TCP connection to a remote host.

%postun axfrdns
svc -d %daemontools_conf/axfrdns
svc -d %daemontools_conf/axfrdns/log

%package walldns
Summary: Reverse DNS wall
Group: Networking/DNS
Requires: %name-common = %version-%release daemontools >= 0.76-alt7

%description walldns
walldns is a reverse DNS wall. It accepts iterative DNS queries for
in-addr.arpa domains from hosts around the Internet, and supplies
generic responses that avoid revealing local host information.
For example, walldns provides a PTR record for 4.3.2.1.in-addr.arpa
showing 4.3.2.1.in-addr.arpa as the name of IP address 1.2.3.4, and a
matching A record showing 1.2.3.4 as the IP address
of 4.3.2.1.in-addr.arpa.

%pre walldns
adduser -r -M -c "DJBDNS logging account" -s /dev/null -d %_var/log/djbdns djbdns_log > /dev/null 2>&1 ||:
adduser -r -M -c "DJBDNS account" -s /dev/null -d %djbdns_cd_nr djbdns > /dev/null 2>&1 ||:

%postun walldns
svc -d %daemontools_conf/walldns
svc -d %daemontools_conf/walldns/log

%package rbldns
Summary: IP-address-listing DNS server
Group: Networking/DNS
Requires: %name-common = %version-%release daemontools >= 0.76-alt7

%description rbldns
rbldns is an IP-address-listing DNS server. It accepts iterative DNS
queries from hosts around the Internet asking about various IP
addresses. It provides responses showing whether the addresses are on a
locally configured list, such as RBL or DUL.

%pre rbldns
adduser -r -M -c "DJBDNS logging account" -s /dev/null -d %_var/log/djbdns djbdns_log > /dev/null 2>&1 ||:
adduser -r -M -c "DJBDNS account" -s /dev/null -d %djbdns_cd_nr djbdns > /dev/null 2>&1 ||:

%postun rbldns
svc -d %daemontools_conf/rbldns
svc -d %daemontools_conf/rbldns/log

%package pickdns
Summary: Load-balancing DNS server
Group: Networking/DNS
Requires: %name-common = %version-%release daemontools >= 0.76-alt7

%description pickdns
pickdns accepts iterative DNS queries from hosts around the Internet,
and responds with a dynamic selection of locally configured IP addresses
with 5-second TTLs. In versions 1.04 and above, the features of pickdns
have been integrated into tinydns.

%pre pickdns
adduser -r -M -c "DJBDNS logging account" -s /dev/null -d %_var/log/djbdns djbdns_log > /dev/null 2>&1 ||:
adduser -r -M -c "DJBDNS account" -s /dev/null -d %djbdns_cd_nr djbdns > /dev/null 2>&1 ||:

%postun pickdns
svc -d %daemontools_conf/pickdns
svc -d %daemontools_conf/pickdns/log

%package utils
Summary: Testing and debug utilities
Group: Networking/DNS
Requires: %name-common = %version-%release

%description utils
Command-line tools to look up DNS information  and debug DNS
configuration.

%install

## common ##
mkdir -p %djbdns_cd
mkdir -p %djbdns_ld

## dnscache ##
for F in dnscache dnscache-conf
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done
%daemontools_install alt-stuff/run_dnscache dnscache
%daemontools_logger_install alt-stuff/run_dnscache_log dnscache
for F in CACHESIZE DATALIMIT IP IPSEND
do
	install -Dp -m 644 alt-stuff/$F %djbdns_cd/dnscache/env/$F
done
install -Dp -m 644 alt-stuff/ROOT_dnscache %djbdns_cd/dnscache/env/ROOT
install -Dp -m 644 /dev/null %djbdns_cd/dnscache/root/ip/127.0.0.1
install -Dp -m 644 alt-stuff/dnsroots %djbdns_cd/dnscache/root/servers/\@
touch %djbdns_cd/dnscache/seed
mkdir -p %djbdns_ld/dnscache

## tinydns ##
for F in tinydns-conf tinydns tinydns-get tinydns-data tinydns-edit
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done
%daemontools_install alt-stuff/run_tinydns tinydns
%daemontools_logger_install alt-stuff/run_tinydns_log tinydns
install -Dp -m 644 alt-stuff/IP %djbdns_cd/tinydns/env/IP
install -Dp -m 644 alt-stuff/ROOT_tinydns %djbdns_cd/tinydns/env/ROOT
install -Dp -m 644 alt-stuff/Makefile_tinydns %djbdns_cd/tinydns/root/Makefile
touch %djbdns_cd/tinydns/root/data
install -p -m 755 alt-stuff/add-* %djbdns_cd/tinydns/root/
mkdir -p %djbdns_ld/tinydns

## afxrdns ##
for F in axfrdns-conf axfrdns axfr-get
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done
%daemontools_install alt-stuff/run_axfrdns axfrdns
%daemontools_logger_install alt-stuff/run_axfrdns_log axfrdns
install -Dp -m 644 alt-stuff/Makefile_axfrdns %djbdns_cd/axfrdns/Makefile
cp alt-stuff/tcp %djbdns_cd/axfrdns/
install -Dp -m 644 alt-stuff/IP %djbdns_cd/axfrdns/env/IP
install -Dp -m 644 alt-stuff/ROOT_tinydns %djbdns_cd/axfrdns/env/ROOT
mkdir -p %djbdns_ld/axfrdns

## walldns ##
for F in walldns-conf walldns
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done
%daemontools_install alt-stuff/run_walldns walldns
%daemontools_logger_install alt-stuff/run_walldns_log walldns
install -Dp -m 644 alt-stuff/IP %djbdns_cd/walldns/env/IP
install -Dp -m 644 alt-stuff/ROOT_walldns %djbdns_cd/walldns/env/ROOT
mkdir -p %djbdns_cd/walldns/root
mkdir -p %djbdns_ld/walldns

## rbldns ##
for F in rbldns-conf rbldns rbldns-data
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done
%daemontools_install alt-stuff/run_rbldns rbldns
%daemontools_logger_install alt-stuff/run_rbldns_log rbldns
install -Dp -m 644 alt-stuff/IP %djbdns_cd/rbldns/env/IP
install -Dp -m 644 alt-stuff/ROOT_rbldns %djbdns_cd/rbldns/env/ROOT
install -Dp -m 644 alt-stuff/BASE %djbdns_cd/rbldns/env/BASE
install -Dp -m 644 alt-stuff/Makefile_rbldns %djbdns_cd/rbldns/root/Makefile
touch %djbdns_cd/rbldns/root/data
mkdir -p %djbdns_ld/rbldns

## pickdns ##
for F in pickdns-conf pickdns pickdns-data
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done
%daemontools_install alt-stuff/run_pickdns pickdns
%daemontools_logger_install alt-stuff/run_pickdns_log pickdns
install -Dp -m 644 alt-stuff/IP %djbdns_cd/pickdns/env/IP
install -Dp -m 644 alt-stuff/ROOT_pickdns %djbdns_cd/pickdns/env/ROOT
install -Dp -m 644 alt-stuff/Makefile_pickdns %djbdns_cd/pickdns/root/Makefile
touch %djbdns_cd/pickdns/root/data
mkdir -p %djbdns_ld/pickdns


## utils ##
for F in dnsip dnsipq dnsname dnstxt dnsmx dnsfilter random-ip dnsqr dnsq dnstrace dnstracesort
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done

%files common
%doc CHANGES
%doc README*
%doc TODO
%doc VERSION
%dir %djbdns_cd_nr
%dir %djbdns_ld_nr

%files dnscache
%_bindir/dnscache
%_bindir/dnscache-conf
%dir %daemontools_conf/dnscache/
%config(noreplace) %daemontools_conf/dnscache/run
%dir %daemontools_conf/dnscache/log
%config(noreplace) %daemontools_conf/dnscache/log/run
%dir %djbdns_cd_nr/dnscache/
%config(noreplace) %djbdns_cd_nr/dnscache/seed
%dir %djbdns_cd_nr/dnscache/env
%config(noreplace) %djbdns_cd_nr/dnscache/env/*
%dir %djbdns_cd_nr/dnscache/root
%dir %djbdns_cd_nr/dnscache/root/ip
%config(noreplace) %djbdns_cd_nr/dnscache/root/ip/*
%dir %djbdns_cd_nr/dnscache/root/servers
%config(noreplace) %djbdns_cd_nr/dnscache/root/servers/@
%attr(750, djbdns_log, djbdns_log) %dir %djbdns_ld_nr/dnscache

%files tinydns
%_bindir/tinydns-conf
%_bindir/tinydns
%_bindir/tinydns-get
%_bindir/tinydns-data
%_bindir/tinydns-edit
%dir %daemontools_conf/tinydns/
%config(noreplace) %daemontools_conf/tinydns/run
%dir %daemontools_conf/tinydns/log
%config(noreplace) %daemontools_conf/tinydns/log/run
%dir %djbdns_cd_nr/tinydns/
%dir %djbdns_cd_nr/tinydns/env
%config(noreplace) %djbdns_cd_nr/tinydns/env/*
%dir %djbdns_cd_nr/tinydns/root
%djbdns_cd_nr/tinydns/root/add-*
%djbdns_cd_nr/tinydns/root/Makefile
%config(noreplace) %djbdns_cd_nr/tinydns/root/data
%attr(750, djbdns_log, djbdns_log) %dir %djbdns_ld_nr/tinydns

%files axfrdns
%_bindir/axfrdns-conf
%_bindir/axfrdns
%_bindir/axfr-get
%dir %daemontools_conf/axfrdns/
%config(noreplace) %daemontools_conf/axfrdns/run
%dir %daemontools_conf/axfrdns/log
%config(noreplace) %daemontools_conf/axfrdns/log/run
%dir %djbdns_cd_nr/axfrdns/
%djbdns_cd_nr/axfrdns/Makefile
%djbdns_cd_nr/axfrdns/tcp
%dir %djbdns_cd_nr/axfrdns/env
%config(noreplace) %djbdns_cd_nr/tinydns/env/*
%attr(750, djbdns_log, djbdns_log) %dir %djbdns_ld_nr/axfrdns

%files walldns
%_bindir/walldns-conf
%_bindir/walldns
%dir %daemontools_conf/walldns/
%config(noreplace) %daemontools_conf/walldns/run
%dir %daemontools_conf/walldns/log
%config(noreplace) %daemontools_conf/walldns/log/run
%dir %djbdns_cd_nr/walldns/
%dir %djbdns_cd_nr/walldns/env
%config(noreplace) %djbdns_cd_nr/walldns/env/*
%dir %djbdns_cd_nr/walldns/root
%attr(750, djbdns_log, djbdns_log) %dir %djbdns_ld_nr/walldns

%files rbldns
%_bindir/rbldns-conf
%_bindir/rbldns
%_bindir/rbldns-data
%dir %daemontools_conf/rbldns/
%config(noreplace) %daemontools_conf/rbldns/run
%dir %daemontools_conf/rbldns/log
%config(noreplace) %daemontools_conf/rbldns/log/run
%dir %djbdns_cd_nr/rbldns/
%dir %djbdns_cd_nr/rbldns/env
%config(noreplace) %djbdns_cd_nr/rbldns/env/*
%dir %djbdns_cd_nr/rbldns/root
%djbdns_cd_nr/rbldns/root/Makefile
%config(noreplace) %djbdns_cd_nr/rbldns/root/data
%attr(750, djbdns_log, djbdns_log) %dir %djbdns_ld_nr/rbldns

%files pickdns
%_bindir/pickdns-conf
%_bindir/pickdns
%_bindir/pickdns-data
%dir %daemontools_conf/pickdns/
%config(noreplace) %daemontools_conf/pickdns/run
%dir %daemontools_conf/pickdns/log
%config(noreplace) %daemontools_conf/pickdns/log/run
%dir %djbdns_cd_nr/pickdns/
%dir %djbdns_cd_nr/pickdns/env
%config(noreplace) %djbdns_cd_nr/pickdns/env/*
%dir %djbdns_cd_nr/pickdns/root
%djbdns_cd_nr/pickdns/root/Makefile
%config(noreplace) %djbdns_cd_nr/pickdns/root/data
%attr(750, djbdns_log, djbdns_log) %dir %djbdns_ld_nr/pickdns

%files utils
%_bindir/dnsip
%_bindir/dnsipq
%_bindir/dnsname
%_bindir/dnstxt
%_bindir/dnsmx
%_bindir/dnsfilter
%_bindir/random-ip
%_bindir/dnsqr
%_bindir/dnsq
%_bindir/dnstrace
%_bindir/dnstracesort

%changelog
* Sun Jan 24 2010 Boris Gulay <boresexpress@altlinux.org> 1.05-alt1
- first build for ALT Linux
