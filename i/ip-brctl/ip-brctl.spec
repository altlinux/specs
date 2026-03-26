Name: ip-brctl
Version: 0.3
Release: alt1

Summary: Drop-in replacement of the standalone brctl utility
License: GPLv2+
Group: System/Base

Url: https://patchwork.ozlabs.org/patch/1027627/
Source: %name-%version.tar

BuildArch: noarch

Requires: iproute2
Provides: bridge-utils = 1.6.0
Obsoletes: bridge-utils < 1.6.0
Provides: /sbin/brctl

%description
Introduce ip-brctl shell script.

This script wraps 'ip' and 'bridge' tools to provide a drop-in replacement
of the standalone 'brctl' utility.

It's bug-to-bug compatible with brctl as of bridge-utils version 1.6,
has no dependencies other than a POSIX shell, and it's less than half
the binary size of brctl on x86_64.

As many users  seem to find brctl usage vastly more
intuitive than ip-link, possibly due to habit, this might be a lightweight
approach to provide brctl syntax without the need to maintain bridge-utils
any longer.

%prep
%setup

%install
install -pD -m755 ip-brctl %buildroot%_sbindir/ip-brctl
install -pD -m644 ip-brctl.8 %buildroot%_man8dir/ip-brctl.8
ln -s ip-brctl %buildroot%_sbindir/brctl

%files
%_sbindir/*
%_man8dir/*

%changelog
* Fri Mar 27 2026 Alexey Shabalin <shaba@altlinux.org> 0.3-alt1
- Fix timer validation error texts.
- Fix delif error argument order.
- Tighten float input validation.
- Fix signed long range check.
- Fix hairpin slave option (ALT#58376).
- Fix boolean conversion in make_bool (ALT#58372).
- Fix setmaxage bridge attribute (ALT#58370).
- Align setgcint docs with implementation (ALT#58360).
- Fix addif validation (ALT#58359).
- Fix exec_iplink argument handling (ALT#58358).

* Wed Feb 25 2026 Alexey Shabalin <shaba@altlinux.org> 0.2-alt1
- Fix brctl show with no bridge (ALT#57898).

* Thu Nov 21 2024 Alexey Shabalin <shaba@altlinux.org> 0.1-alt1
- Initial build.
