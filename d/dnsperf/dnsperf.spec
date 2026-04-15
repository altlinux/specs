Name:    dnsperf
Version: 2.15.1
Release: alt1

Summary: DNS Performance Testing Tools
License: Apache-2.0
Group:   Other
URL:     https://www.dns-oarc.net/tools/dnsperf
VCS:     https://codeberg.org/DNS-OARC/dnsperf

Source: %name-%version.tar

BuildRequires: ck-devel
BuildRequires: libldns-devel
BuildRequires: libnghttp2-devel
BuildRequires: openssl-devel

Requires: gnuplot

%description
dnsperf and resperf are free tools developed by Nominum/Akamai (2006-2018) and
DNS-OARC (since 2019) that make it simple to gather accurate latency and
throughput metrics for Domain Name Service (DNS). These tools are easy-to-use
and simulate typical Internet, so network operators can benchmark their naming
and addressing infrastructure and plan for upgrades. The latest version of the
dnsperf and resperf can be used with test files that include IPv6 queries.

dnsperf "self-paces" the DNS query load to simulate network conditions. New
features in dnsperf improve the precision of latency measurements and allow for
per packet per-query latency reporting is possible. dnsperf is now
multithreaded, multiple dnsperf clients can be supported in multicore systems
(each client requires two cores). The output of dnsperf has also been improved
so it is more concise and useful. Latency data can be used to make detailed
graphs, so it is simple for network operators to take advantage of the data.

resperf systematically increases the query rate and monitors the response rate
to simulate caching DNS services.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_defaultdocdir/%name

%files
%doc README.md CHANGES
%_bindir/*
%_man1dir/*

%changelog
* Wed Apr 15 2026 Andrey Cherepanov <cas@altlinux.org> 2.15.1-alt1
- New version.

* Wed Jan 21 2026 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Wed Nov 12 2025 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt2
- Required gnuplot for resperf-report (ALT #56823).

* Thu Oct 30 2025 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- Initial build for Sisyphus.
