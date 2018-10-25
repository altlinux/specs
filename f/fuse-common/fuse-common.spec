Name: fuse-common
Version: 1.0.0
Release: alt2

BuildArch: noarch

Summary: a tool for creating virtual filesystems
License: GPL
Group: System/Kernel and hardware

Url: https://github.com/libfuse/

Source: %name-%version.tar

Packager: Denis Smirnov <mithraen@altlinux.ru>

Conflicts: fuse <= 2.9.7-alt1

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
install -pD fuserumount        %buildroot%_bindir/fuserumount

%pre
%_sbindir/groupadd -r -f fuse
%_sbindir/groupadd -r -f cuse

%files
%_sysconfdir/control.d/facilities/fusermount
%_udevrulesdir/*
%attr(0755,root,root) %_bindir/fuserumount

%changelog
* Thu Oct 25 2018 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt2
- remove unneeded %%post (ALT #33754)

* Tue Jul 25 2017 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt1
- moved from fuse package
