
Name: blacklist-nouveau
Version: 1.0.0
Release: alt1

Group: System/Configuration/Other
Summary: Disable nouveau kernel module
Url: https://altlinux.org/
License: GPL-3.0-or-later

BuildArch: noarch

Provides: nouveau-blacklist = %EVR
Obsoletes: nouveau-blacklist < %EVR

%description
Disable automatic nouveau kernel module load.

%install
mkdir -p %buildroot/%_sysconfdir/modprobe.d/
cat >%buildroot/%_sysconfdir/modprobe.d/blacklist-nouveau.conf <<__EOF__
blacklist nouveau
__EOF__
chmod 0644 %buildroot/%_sysconfdir/modprobe.d/blacklist-nouveau.conf

%files
%config(noreplace) %_sysconfdir/modprobe.d/blacklist-nouveau.conf

%changelog
* Fri Jul 11 2025 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial build
