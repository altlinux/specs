%define _libexecdir /usr/libexec
%define vzdir /etc/vz
%define confdir %vzdir/conf
%define namesdir %vzdir/names
%define lockdir /var/lib/vz/lock
%define vzctl_lockdir /var/lock/vzctl
%define spooldir /var/lib/vz
%define netdir /etc/sysconfig/network-scripts
%define bashcompldir /etc/bash_completion.d

Name:     vzmigrate
Version:  7.0.149
Release:  alt2

Summary:  Virtuozzo migration tool
License:  GPLv2+
Group:    System/Servers
Url:      https://src.openvz.org/scm/ovz/vzmigrate.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

Requires: ploop >= 7.0.160
# Requires: network-config-subsystem
Requires: libvzctl >= 7.0.645
Requires: tar
Requires: rsync-ovz
Requires: phaul-ovz
Requires: vztt

Provides: pmigrate.c2c = %EVR

BuildRequires: gcc-c++
BuildRequires: glibc-devel libuuid-devel
BuildRequires: systemd-devel libudev-devel
BuildRequires: libvzctl-devel >= 7.0.535
BuildRequires: libvzsock-devel
BuildRequires: libssl-devel openssl libkrb5-devel
BuildRequires: libploop-devel >= 7.0.160
BuildRequires: libvztt-devel
BuildRequires: libzstd-devel
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0
BuildRequires: boost-asio-devel boost-devel boost-devel-headers

%description
%summary

%prep
%setup
%patch -p1

%build
%make_build

%install
make install \
        DESTDIR=%buildroot \
        SBINDIR=%_sbindir \
        MANDIR=%_mandir \
        SYSTEMDDIR=%_unitdir \
        NETSCRIPTDIR=%netdir \
        VZDIR=%vzdir \
        CONFDIR=%confdir \
        VZLOCKDIR=%lockdir \
        VZCTLLOCKDIR=%vzctl_lockdir \
        VZSPOOLDIR=%spooldir \
        BASHCOMPLDIR=%bashcompldir \
        LOGRDIR=%_logrotatedir

%files
%_sbindir/*
%_man8dir/*
%_datadir/%name/
%_datadir/pmigrate/
%config(noreplace) %_logrotatedir/%name
%doc *.md

%changelog
* Wed Nov 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.149-alt2
- use rsync-ovz with redirected descriptors
- several logging and build fixes

* Mon Jan 17 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.149-alt1
- 7.0.149

* Fri Aug 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.147-alt1
- 7.0.147

* Fri Jul 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.145-alt1
- 7.0.145

* Tue May 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.144-alt1
- 7.0.144

* Mon Mar 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.143-alt1
- 7.0.143

* Sat Dec 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.139-alt1
- 7.0.139

* Tue Nov 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.138-alt1
- 7.0.138

* Mon Oct 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.135-alt1
- 7.0.135

* Mon Aug 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.133-alt1
- 7.0.133

* Thu Jul 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.131-alt1
- 7.0.131

* Wed Jun 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.129-alt1
- 7.0.129

* Thu Apr 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.128-alt1
- 7.0.128

* Thu Apr 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.126-alt1
- 7.0.126

* Fri Jan 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.125-alt1
- 7.0.125

* Mon Nov 11 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt6
- fix FTB and C++11 warning

* Tue Oct 01 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt5
- fix branding

* Wed Sep 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt4
- fix double slashes in symlinks

* Tue Sep 17 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt3
- remove deprecated cipher and message

* Mon Aug 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt2
- fix build with static vzsock

* Fri Aug 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt1
- 7.0.124

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.123-alt2
- more specific requirements
- revert define macros patch

* Fri Aug 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.123-alt1
- Initial build for Sisyphus
