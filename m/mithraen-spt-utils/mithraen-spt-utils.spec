Name: mithraen-spt-utils
Summary: Simple utilites that simplify distro building to me
Version: 0.1
Release: alt1
License: GPL
Group: Development/Other

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

%add_findreq_skiplist %_datadir/%name/* %_bindir/*

# System
Requires: hasher >= 1.1.0-alt1
Requires: squashfsprogs
Requires: cpio

%description
%summary

%prep
%setup
%build
%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/%name
install -m755 scripts/* %buildroot%_bindir/
install -m755 hscripts/* %buildroot%_datadir/%name/
%files
%_bindir/*
%_datadir/%name/*
%changelog
* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

