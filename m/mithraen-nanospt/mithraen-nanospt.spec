Name: mithraen-nanospt

%add_findreq_skiplist %_datadir/%name/*

Summary: Simple script, that I used before spt was wrote
Version: 0.1
Release: alt2
License: GPL
Group: Development/Other

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# System
Requires: hasher >= 1.1.0-alt1
Requires: squashfsprogs
Requires: mithraen-spt-utils
Requires: syslinux
Requires: csed

%description
%summary

%prep
%setup
%build
%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/%name
install -m755 gen_repo nanospt compile.partitions %buildroot%_bindir/
install -m755 scripts/kernel %buildroot%_datadir/%name
%files
%_bindir/*
%_datadir/%name/*
%changelog
* Wed Sep 16 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- fix requires

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

