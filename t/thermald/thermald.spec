# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _localstatedir /var

Name: thermald
Version: 2.5.12
Release: alt1

Summary: Thermal daemon for IA

License: GPL-3.0-or-later
Group: System/Kernel and hardware

URL: https://github.com/intel/thermal_daemon
VCS: https://github.com/intel/thermal_daemon.git

Source: %name-%version.tar
Source1: thermald.init
Source2: %name-monitor.svg
Patch: %name-%version-%release.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: gcc-c++ libgomp-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: systemd-devel
BuildRequires: gtk-doc
BuildRequires: liblzma-devel
BuildRequires: libupower-devel
BuildRequires: libevdev-devel
BuildRequires: autoconf-archive
Requires: dbus

%filter_from_requires s;/usr/lib/lsb/init-functions;/lib/lsb/init-functions;

%description
Thermal issues are important to handle proactively to reduce performance impact.

The project provides a Linux user mode daemon to system developers, reducing
time to market with controlled thermal management using P-states, T-states, and
the Intel power clamp driver. The Thermal Daemon uses the existing Linux kernel
infrastructure and can be easily enhanced.

%description -l ru_RU.UTF-8
thermald представляет собой службу, которая управляет питанием с помощью
Р-состояний, Т-состояния и Intel power clamp driver. thermald использует
существующую инфраструктуру ядра Linux, и его возможности могут быть легко
расширены.

%prep
%setup
%autopatch -p1

%build
./autogen.sh
%configure \
    --disable-option-checking \
    --disable-silent-rules
%make_build

%install
%makeinstall_std
install -pD -m644 data/%name.service \
    %buildroot%_unitdir/%name.service
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name

# Install management-script
install -Dpm 0755 tools/thermald_set_pref.sh \
    %buildroot%_bindir/%name-set-pref

# Install tmpfiles.d
mkdir -p alt_addons
cat << EOF > alt_addons/%name.conf
d /run/%name 0755 root root -
EOF

install -Dpm 0644 alt_addons/%name.conf \
    %buildroot%_tmpfilesdir/%name.conf

# Install sysusers.conf
cat >thermald.sysusers.conf <<EOF
g power -
EOF

install -m0644 -D thermald.sysusers.conf \
	%buildroot%_sysusersdir/thermald.conf

# Install config
install -Dpm 0644 data/thermal-conf.xml \
    %buildroot%_sysconfdir/%name/thermal-conf.xml

%pre
%_bindir/getent group power >/dev/null || %_sbindir/groupadd -r power
exit 0

%post
%post_service thermald

%preun
%preun_service thermald

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/thermal-conf.xml
%config(noreplace) %_sysconfdir/%name/thermal-cpu-cdev-order.xml
%config(noreplace) %_sysconfdir/%name/thermald-features.xml
%doc README.txt thermal_daemon_usage.txt COPYING
%_tmpfilesdir/%name.conf
%_sbindir/%name
%_bindir/%name-set-pref
%_datadir/dbus-1/system-services/org.freedesktop.%name.service
%_datadir/dbus-1/system.d/org.freedesktop.%name.conf
%_unitdir/%name.service
%_sysusersdir/thermald.conf
%_initdir/%name
%_man5dir/*.5.*
%_man8dir/*.8.*

%changelog
* Thu Sep 10 2026 Anton Midyukov <antohami@altlinux.org> 2.5.12-alt1
- New version 2.5.12.
- Add upstream fixes:
  + Allow desktop platform with ignore-cpuid-check
  + Remove fatal error for non mobile platform
  + thermald: platform: intel: Re-add Wildcat Lake support
- Add sysusers config.
- Build on aarch64 too.
- Remove subpackage thermald-monitor (remove in upstream).

* Tue Nov 11 2025 Anton Midyukov <antohami@altlinux.org> 2.5.10-alt1
- New version 2.5.10.

* Mon Aug 19 2024 Anton Midyukov <antohami@altlinux.org> 2.5.8-alt1
- new version 2.5.8

* Sun Mar 31 2024 Anton Midyukov <antohami@altlinux.org> 2.5.7-alt1
- new version 2.5.7

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 2.5.6-alt1
- new version 2.5.6

* Sat Oct 07 2023 Anton Midyukov <antohami@altlinux.org> 2.5.4-alt1
- new version 2.5.4
- cleaup spec

* Mon Jul 10 2023 Anton Midyukov <antohami@altlinux.org> 2.5.3-alt1
- new version 2.5.3
- Update License tag (GPLv2+ -> GPL-3.0-or-later)

* Mon Apr 25 2022 Anton Midyukov <antohami@altlinux.org> 2.4.9-alt1
- new version 2.4.9

* Mon Jan 10 2022 Nikolai Kostrigin <nickel@altlinux.org> 2.4.7-alt1
- new version 2.4.7
  + Alder Lake and Jasper Lake support introduced by upstream

* Wed Oct 06 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.4.6-alt2
- add alt-ui-cosmetic-fixes-to-avoid-label-cut-in-dialogs patch
  (closes: #41065)

* Mon Sep 20 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.4.6-alt1
- new version 2.4.6

* Mon Dec 21 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.4.1-alt1
- new version 2.4.1
- turn TermalMonitor build on
- spec: remove obsolete Packager tag
  + update upstream URL

* Mon Nov 09 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.2-alt1
- new version 2.2
  + change packaging scheme to git subtree

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 1.8-alt2
- Update buildrequires (Fix FTBFS)

* Sun Oct 21 2018 Anton Midyukov <antohami@altlinux.org> 1.8-alt1
- new version 1.8
- exclusive arch x86_64

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 1.7.2-alt1
- new version 1.7.2
- exclusive arch ix86 and x86_64

* Sat Oct 28 2017 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt1
- new version (1.7.1) with rpmgs script

* Fri Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 1.6-alt1
- new version (1.6) with rpmgs script

* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- new version (1.5.4) with rpmgs script

* Wed Oct 05 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.3-alt2
- Fixed the adaption of the Debian-style .init for ALT:
  + .init: condrestart/condstop implemented in a simple way;
  + .init: status cmd added;
  + .init: do not print DONE when printing the usage.
- (.spec) Do not own dbus and systemd dirs.

* Fri May 27 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- New version.

* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt2
- Remove init-condrestart.

* Tue Feb 16 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- Initial build for Altlinux Sisyphus.
