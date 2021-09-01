
Name: ovztransfer
Version: 1.2.0
Release: alt1

Summary: OpenVZ 6 to 7 transfer tool
License: GPLv2
Group: System/Configuration/Other
Url: http://openvz.org/
Vcs: https://src.openvz.org/scm/ovzl/ovztransfer.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source: %name-%version.tar

ExclusiveArch: x86_64

Requires: openssh-common

%description
OpenVZ is an Operating System-level server virtualization solution, built
on Linux.  OpenVZ creates isolated, secure virtual private servers on a
single physical server enabling better server utilization and ensuring
that applications do not conflict.  Each VE performs and executes exactly
like a stand-alone server; VEs can be rebooted independently and have
root access, users, IP addresses, memory, processes, files, applications,
system libraries and configuration files.

This package contains the transfer tool to migrate Virtual Environments
from OpenVZ 6 to OpenVZ 7.

%prep
%setup

%build

%install
mkdir -p %buildroot%_sbindir
install -pm 755 %name.sh %buildroot%_sbindir

%files
%_sbindir/*

%changelog
* Wed Sep 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Jan 28 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1.1-alt1
- 1.1.1

* Thu Nov 26 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.0.6-alt1
- initial import for ALT

