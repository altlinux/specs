Name: ip-brctl
Version: 0.1
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
* Thu Nov 21 2024 Alexey Shabalin <shaba@altlinux.org> 0.1-alt1
- Initial build.
