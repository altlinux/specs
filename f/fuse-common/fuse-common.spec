Name: fuse-common
Version: 1.1.2
Release: alt1

BuildArch: noarch

Summary: a tool for creating virtual filesystems
License: GPL-2.0
Group: System/Kernel and hardware

Url: https://github.com/libfuse/

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Conflicts: fuse < 2.9.9-alt1 fuse3 < 3.4.1-alt2

%description
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort
as well as for using them.

%prep
%setup
%build
%install
install -pD fusermount-control %buildroot%_sysconfdir/control.d/facilities/fusermount
install -D -m644 udev.rules    %buildroot%_udevrulesdir/60-fuse.rules
install -D fuse.conf %buildroot%_sysconfdir/fuse.conf

%pre
%_sbindir/groupadd -r -f fuse
%_sbindir/groupadd -r -f cuse
if [ $1 -ge 2 ]; then
    %_sbindir/control-dump fusermount
fi

%post
if [ $1 -ge 2 ]; then
    %_sbindir/control-restore fusermount
fi

%files
%config(noreplace) %_sysconfdir/fuse.conf
%_sysconfdir/control.d/facilities/fusermount
%_udevrulesdir/*

%changelog
* Sun Jul 18 2021 Vitaly Chikunov <vt@altlinux.org> 1.1.2-alt1
- Fix fusermount control logic of calling udevadm trigger.
- Update License tag.

* Sun Mar 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.1.1-alt1
- fix fusermount control with common use of builtin mode
- add fuse.conf generated by fuse-3.10.2

* Mon Aug 31 2020 Rustem Bapin <rbapin@altlinux.org> 1.1.0-alt2
- fix double help

* Sun Feb 03 2019 Rustem Bapin <rbapin@altlinux.org> 1.1.0-alt1
- fuserumount moved back to fuse package
- add support control both fuse and fuse3

* Thu Oct 25 2018 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt2
- remove unneeded %%post (ALT #33754)

* Tue Jul 25 2017 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt1
- moved from fuse package
