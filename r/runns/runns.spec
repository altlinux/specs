Name: runns
Version: 1.2
Release: alt1

Summary: This is a daemon and helper scripts to run program in network namespace.

License: MIT
Group: Networking/Other
Url: https://github.com/dalegr/runns

Packager: Nikita Ermakov <arei@altlinux.org>

Source: %name-%version.tar

BuildRequires: autoconf make iptables iproute2

%description
The RUNNS provides daemon (runns), client (runnsctl) and helper
scripts (build-net and clean-net) for GNU/Linux to easy create and
delete network namespaces, connect this network namespace to
default via veth pair and setup iptables NAT rules.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%doc LICENSE README.md

%changelog
* Fri Sep  6 2019 Nikita Ermakov <arei@altlinux.org> 1.2-alt1
- Initial build for ALT Linux Sisyphus.
