%global import_path github.com/dmachard/dns-collector
Name:    dns-collector
Version: 2.4.0
Release: alt1

Summary: Ingesting, pipelining, and enhancing your DNS logs with usage indicators, security analysis, and additional metadata
License: MIT
Group:   Other
Url:     https://github.com/dmachard/DNS-collector

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar
Source2: dnscollector.service
Source3: config.yml

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
DNS-collector acts as a passive high speed ingestor with pipelining support for
your DNS logs, written in Golang. It allows enhancing your DNS logs by adding
metadata, extracting usage patterns, and facilitating security analysis.

Additionally, DNS-collector also supports:
- Extended DNStap with TLS encryption, compression, and more metadata
  capabilities DNS protocol conversions to Plain text, Key/Value JSON, Jinja
  and more
- DNS parser with Extension Mechanisms for DNS (EDNS) support
- Live capture on a network interface
- IPv4/v6 defragmentation and TCP reassembly
- Nanoseconds in timestamps

%prep
%setup
tar xf %SOURCE1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version"
cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -Dpm0644 %SOURCE2 %buildroot%_unitdir/dnscollector.service
install -Dpm0644 %SOURCE3 %buildroot%_sysconfdir/dnscollector/config.yml
mkdir -p %buildroot%_runtimedir/dnscollector
mkdir -p %buildroot%_logdir/dnscollector
mkdir -p %buildroot%_localstatedir/dnscollector

%pre
%_sbindir/useradd -c 'Go DnsCollector' -d %_runtimedir/dnscollector \
    -s /sbin/nologin -r dnscollector 2>/dev/null ||:
# Create SSL key
test -x /var/lib/ssl/certs/dnscollector.cert || /usr/bin/cert-sh generate "dnscollector" &>/dev/null

%preun
%preun_service dnscollector

%post
if [ ! -x %_localstatedir/dnscollector/dnscollector.key ]; then
	cp -a /var/lib/ssl/private/dnscollector.key %_localstatedir/dnscollector/dnscollector.key &>/dev/null
	chown dnscollector %_localstatedir/dnscollector/dnscollector.key &>/dev/null
fi
%post_service dnscollector

%files
%doc *.md
%_bindir/*
%config(noreplace) %_sysconfdir/dnscollector/config.yml
%_unitdir/dnscollector.service
%attr(0700,dnscollector,dnscollector) %_runtimedir/dnscollector
%attr(0700,dnscollector,dnscollector) %_logdir/dnscollector
%attr(0700,dnscollector,dnscollector) %_localstatedir/dnscollector

%changelog
* Wed Jul 01 2026 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Wed Jun 03 2026 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Sat May 02 2026 Andrey Cherepanov <cas@altlinux.org> 2.2.3-alt1
- New version.

* Sun Apr 26 2026 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version.

* Mon Mar 30 2026 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- New version.

* Wed Mar 18 2026 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Fri Feb 20 2026 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Sat Jan 10 2026 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Sun Dec 07 2025 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt1
- New version.

* Thu Nov 13 2025 Andrey Cherepanov <cas@altlinux.org> 1.13.0-alt1
- New version.

* Mon Oct 27 2025 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt2
- Fixed version show (ALT #52747).
- Added service file.

* Sun Oct 19 2025 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version.

* Sat Aug 30 2025 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt1
- New version.

* Wed Aug 27 2025 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- New version.

* Mon Jul 14 2025 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- New version.

* Tue Jun 17 2025 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version.

* Fri May 02 2025 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Fri Apr 11 2025 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.

* Wed Mar 05 2025 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- New version.

* Mon Feb 10 2025 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Thu Jan 16 2025 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
