Name: packagekit-background
Version: 0.1.1
Release: alt3

Summary: Script to update the system with PackageKit
Group: System/Configuration/Packaging
License: GPL-2.0
Url: https://build.opensuse.org/package/show/openSUSE:Factory/PackageKit

BuildArch: noarch
Conflicts: packagekit-cron
Requires: /usr/bin/pkcon

Source0: PackageKit-systemd-timers.patch
Source1: packagekit-background.conf
Patch1: alt-timer.patch
Patch2: alt-config.patch

#BuildRequires: 

%description
%{summary}.

%prep
%setup -T -c -n %name-%version
rm -rf %_builddir/%name-%version/*
cd %_builddir/%name-%version
ls -al `dirname %SOURCE0`
patch --force <%SOURCE0 ||:
%patch1 -p1
%patch2 -p1

%install
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%_unitdir/timers.target.wants/
mkdir -p %buildroot/%_sysconfdir/sysconfig/
# install script
install -m 0755  packagekit-background.sh %buildroot/%_bindir/
# install timer
install -m 0644 packagekit-background.timer %buildroot/%_unitdir/
ln -sr %buildroot/%_unitdir/packagekit-background.timer %buildroot/%_unitdir/timers.target.wants/
# install service
install -m 0644 packagekit-background.service.in %buildroot/%_unitdir/packagekit-background.service
sed -i "s|^ExecStart=.*|ExecStart=%_bindir/packagekit-background.sh|" %buildroot/%_unitdir/packagekit-background.service
# install config
install -m 0644 %SOURCE1  %buildroot/%_sysconfdir/sysconfig/packagekit-background

%files
%config(noreplace) %_sysconfdir/sysconfig/packagekit-background
%_bindir/*
%_unitdir/packagekit-background.service
%_unitdir/timers.target.wants/packagekit-background.timer
%_unitdir/packagekit-background.timer


%changelog
* Fri Apr 10 2026 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt3
- fix requries

* Mon Oct 27 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt2
- add conflict with packagekit-cron

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- don't use --background option because pkcon freeze

* Tue Oct 07 2025 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
