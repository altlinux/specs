%define  modulename mininet

Name:    python3-module-%modulename
Version: 2.3.1
Release: alt0.b4

Summary: Emulator for rapid prototyping of Software Defined Networks

License: MIT and GPLv2
Group:   Development/Python3
URL:     https://github.com/mininet/mininet

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%add_findreq_skiplist %python3_sitelibdir/%modulename/examples/*

%description
Mininet emulates a complete network of hosts, links, and switches on a single
machine. Mininet is useful for interactive development, testing, and demos,
especially those using OpenFlow and SDN. OpenFlow-based network controllers
prototyped in Mininet can usually be transferred to hardware with minimalchanges
for full line-rate execution.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/mn
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Tue Oct 24 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt0.b4
- Build new version.

* Mon Feb 27 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt0.b1
- Build new version.

* Mon Sep 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.0d6-alt1
- Initial build for Sisyphus.
