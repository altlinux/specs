%define _unpackaged_files_terminate_build 12.7.1
%global import_path github.com/pouriyajamshidi/tcping

Name: tcping
Version: 2.7.1
Release: alt1
Summary: Ping TCP ports using tcping. Inspired by Linux's ping utility. Written in Go
License: MIT
Group: Networking/Other
Url: https://github.com/pouriyajamshidi/tcping

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
TCPing will send TCP probes to an IP address or a hostname specified
by you and prints the result.
It works with both IPv4 and IPv6.

TCPING uses different TCP sequence numbering for successful and
unsuccessful probes, so that when you look at the results and spot
a failed probe, understanding the total packet drops to that point
would be illustrative enough.

 * Monitor your network connection.
 * Determine packet loss.
 * Analyze the network's latency.
 * Show min/avg/max probes latency.
 * Use the -r flag to retry hostname resolution after a predetermined
   number of ping failures. If you want to test your DNS load
   balancing or Global Server Load Balancer (GSLB), you should
   utilize this option..
 * Print connection statistics on Enter key press.
 * Display the longest encountered downtime and uptime duration and
   time.
 * Monitor and audit your peers network.
 * Calculate the total uptime/downtime when conducting a maintenance.
 * An alternative to ping in environments that ICMP is blocked.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot%_datadir/%name
%golang_install

%check
%make test

%files
%doc README.md SECURITY.md README.cn.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%_bindir/%name

%changelog
* Tue May 06 2025 Pavel Shilov <zerospirit@altlinux.org> 2.7.1-alt1
- Initial build for Sisyphus.

