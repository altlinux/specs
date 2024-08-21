# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_without check

Name:     earlyoom
Version:  1.6.2
Release:  alt1.1

Summary:  Early OOM Daemon for Linux
License:  MIT
Group:    Other
Url:      http://github.com/rfjakob/earlyoom

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar
Source1:  %name.init

Patch: fix-config-path.patch

BuildRequires: /proc
%ifnarch %e2k
BuildRequires: pandoc
%endif
%if_with check
BuildRequires: golang
%endif

%description
The oom-killer generally has a bad reputation among Linux users.
This may be part of the reason Linux invokes it only when it has
absolutely no other choice. It will swap out the desktop
environment, drop the whole page cache and empty every buffer
before it will ultimately kill a process. At least that's what
I think what it will do. I have yet to be patient enough to wait
for it, sitting in front of an unresponsive system.

%prep
%setup
%patch0 -p1

sed -e '/systemctl/d' -i Makefile
sed -e 's/VERSION ?= \$(shell git describe --tags --dirty 2> \/dev\/null)/VERSION = %version/' -i Makefile

%build
%make_build \
    PREFIX=%_prefix \
    SYSCONFDIR=%_sysconfdir \
    SYSTEMDUNITDIR=%_unitdir

%install
%makeinstall_std \
    PREFIX=%_prefix \
    SYSCONFDIR=%_sysconfdir \
    SYSTEMDUNITDIR=%_unitdir

mkdir -p %buildroot%_initdir
install -pm755 %SOURCE1 %buildroot%_initdir/%name

%check
%make_build test

%post
[ -f %_sysconfdir/default/%name ] &&
  cp -f %_sysconfdir/default/%name %_sysconfdir/sysconfig/%name
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/%name
%_unitdir/%name.service
%_initdir/%name
%ifnarch %e2k
%_man1dir/%name.*
%endif
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Tue Aug 20 2024 Michael Shigorin <mike@altlinux.org> 1.6.2-alt1.1
- E2K: skip docs (no pandoc available so far)

* Mon Nov 16 2020 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Wed Aug 19 2020 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt2
- Replace config to /etc/sysconfig/earlyoom (Closes: 38825)

* Thu Jul 16 2020 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt1
- new version 1.6.1

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 1.6-alt1
- new version 1.6

* Tue Mar 03 2020 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- new version 1.4

* Mon Nov 18 2019 Anton Midyukov <antohami@altlinux.org> 1.3-alt2.1
- Disable check

* Fri Jun 07 2019 Anton Midyukov <antohami@altlinux.org> 1.3-alt2
- add condrestart, condstop in init script

* Wed Jun 05 2019 Anton Midyukov <antohami@altlinux.org> 1.3-alt1
- new version 1.3

* Sat Jan 26 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt2
- Added init script (Thanks Specyfighter)

* Sun Jan 20 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt1
- Initial build (Closes: 35924)
