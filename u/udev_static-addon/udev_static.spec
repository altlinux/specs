Name: udev_static-addon
Version: 0.2
Release: alt6
Summary: Set of static device nodes suitable for virtual /dev filesystem
License: GPL
Group: System/Configuration/Hardware
Url: https://bugzilla.altlinux.org/show_bug.cgi?id=6296

Provides: udev_static = %version-%release
Conflicts: udev_static-complete
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: propagator

%description
udev_static is a package complement to udev. While udev itself deals mostly with dynamically created
devices nodes, its approach is not always suitable for real-life usage. In particular, pure udev
system is not able to load an appropriate module when a program accesses corresponding device node,
because this device node simply doesn't exist if the module hasn't been loaded yet. 

modules_lookup tries to make up for this deficiency by intercepting attempts to access yet
amissing device nodes and load associated modules before. Unfortunately it requires a patched
version of tmpfs and still doesn't cover all possible cases

recent udev packages (>= 0.50-alt3) support /etc/udev/devices/ subdirectory where system
administrators can create "preconfigured" device nodes which will be copied to /dev upon
udev daemon startup. But this approach when applied thoughtlessly can use a lot of space right
in root partition.

udev_static provides a compressed cpio archive which contains devices inodes to create
upon udevd startup similar to /etc/udev/devices. But because of the form chosen (compressed
cpio archive) even entire contents of old static dev package takes about 90Kb of disk space.

This package contains an almost complete snapshot of /dev system excluding devices which
_exactly_ are handled by hotplug or other standard subsystems

%prep
%setup -q
%patch -p1

%build
cat udev_static | gencpio - | bzip2 -c > static_devices.cpio.bz2

%install
install -pD -m0644 static_devices.cpio.bz2 %buildroot%_sysconfdir/udev/static_devices.cpio.bz2

%files
%config(noreplace, missingok) %_sysconfdir/udev/static_devices.cpio.bz2

%changelog
* Wed Mar 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt6
- added null and kmsg nods (closes: #23212)

* Mon Nov 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt5
- fixed fuse permission

* Tue Nov 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt4
- added cuse nod

* Mon Jun 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt3
- removed slamr (closes: #9665)

* Sun Nov 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt2
- fixed permission for fuse nod

* Thu Jun 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt1
- added fuse nod (close #8629)

* Sun Jul 17 2005 Anton Farygin <rider@altlinux.ru> 0.1-alt1
- specfile based on udev_static-complete
- use gencpio for building static_devices.cpio.bz2

* Sat Mar 26 2005 Alexey Morozov <morozov@altlinux.org> 0.0.1-alt1
- Initial build.
