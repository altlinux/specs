%define _unpackaged_files_terminate_build 1

Name: nohang
Version: 0.3.0
Release: alt1

Summary: Sophisticated low memory handler for Linux
License: MIT
Group: System/Configuration/Other
URL: https://github.com/hakavlad/nohang

BuildRequires(pre): rpm-macros-systemd

BuildRequires: rpm-build-python3

Requires: logrotate
Requires: /usr/bin/notify-send

BuildArch: noarch

Source: %name-%version.tar

%description
nohang is a highly configurable daemon for Linux which is able to correctly
prevent out of memory (OOM) and keep system responsiveness in low memory
conditions.

%prep
%setup

%build
%make_build

%install
%makeinstall_std \
                 BINDIR=%_bindir \
                 MANDIR=%_mandir \
                 PREFIX=%_prefix \
                 SYSCONFDIR=%_sysconfdir \
                 SYSTEMDUNITDIR=%_unitdir

echo "v%{version}-%{release}" > %buildroot%_datadir/%name/version

%files
%doc LICENSE README.md
%config(noreplace) %_sysconfdir/logrotate.d/nohang
%dir %_sysconfdir/nohang
%config(noreplace) %_sysconfdir/nohang/nohang-desktop.conf
%config(noreplace) %_sysconfdir/nohang/nohang.conf
%_bindir/oom-sort
%_bindir/psi-top
%_bindir/psi2log
%_unitdir/nohang-desktop.service
%_unitdir/nohang.service
%_sbindir/nohang
%exclude %_datadir/doc/nohang/CHANGELOG.md
%exclude %_datadir/doc/nohang/README.md
%_man1dir/oom-sort.1.*
%_man1dir/psi-top.1.*
%_man1dir/psi2log.1.*
%_man8dir/nohang.8.*
%dir %_datadir/nohang
%_datadir/nohang/nohang-desktop.conf
%_datadir/nohang/nohang.conf
%_datadir/nohang/version

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
