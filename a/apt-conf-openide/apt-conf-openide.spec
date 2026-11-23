Name: apt-conf-openide
Version: 1.0
Release: alt1

Summary: Official repository of OpenIDE
License: Public-Domain
Group: System/Base

Url: https://openide.ru/

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

Requires: apt-https
Requires: apt-gpgkeys-pki

%description
%{summary}.

%prep
%setup

%install
sed "s/@arch@/%_arch/g" openide-sources.list.in > openide-sources.list
%__install -Dp -m0644 openide-sources.list %buildroot%_sysconfdir/apt/sources.list.d/openide.list
%__install -Dp -m0644 openide-vendors.list %buildroot%_sysconfdir/apt/vendors.list.d/openide.list
%__install -Dp -m0644 openide.asc %buildroot%_datadir/pki/apt-gpg/sources/openide.asc

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/openide.list
%_sysconfdir/apt/vendors.list.d/openide.list
%_datadir/pki/apt-gpg/sources/openide.asc

%changelog
* Mon Nov 23 2026 Nazarov Denis <nenderus@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
