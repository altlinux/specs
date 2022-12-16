%define module_name	lkrg
%define module_version	0.9.6
%define module_release	alt1

%define flavour		std-debug
%define karch		aarch64 %arm %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-debug
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Linux Kernel Runtime Guard module
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-2.0
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://www.openwall.com/lkrg/

%define qemu_pkg %_arch
%ifarch %ix86 x86_64
%define qemu_pkg x86
%endif
%ifarch %arm
%define qemu_pkg arm
%endif

BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
%{?!_without_check:%{?!_disable_check:BuildRequires(pre): rpm-build-kernel-perms}}
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static kernel-image-%flavour}}

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires: lkrg-common >= %module_version

ExclusiveArch: %karch

%description
Linux Kernel Runtime Guard (LKRG) is a loadable kernel module that performs
runtime integrity checking of the Linux kernel and detection of security
vulnerability exploits against the kernel. As controversial as this concept is,
LKRG attempts to post-detect and hopefully promptly respond to unauthorized
modifications to the running Linux kernel (integrity checking) or to
credentials (such as user IDs) of the running processes (exploit
detection). For process credentials, LKRG attempts to detect the exploit and
take action before the kernel would grant the process access (such as open a
file) based on the unauthorized credentials.

%prep
rm -rf %module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n %module_name-%module_version

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules M=$(pwd)

%install
install -D -p -m0644 lkrg.ko %buildroot%module_dir/lkrg.ko

%check
# based on %%check of kernel-image-%%flavour.spec
KernelVer=%kversion-%flavour-%krelease
mkdir -p test
cd test
lkrg_trigger=/proc/sys/lkrg/trigger
failmsg="LKRG test failed"
%__cc %optflags -s -static -xc -o init - <<__EOF__
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <linux/module.h>
#include <sys/mount.h>
#include <sys/reboot.h>
#include <sys/syscall.h>
#define finit_module(fd, param_values, flags) syscall(__NR_finit_module, fd, param_values, flags)
#define delete_module(name, flags) syscall(__NR_delete_module, name, flags)
int main()
{
	int fd = open("lkrg.ko", O_RDONLY);

	if (fd == -1) {
		perror("$failmsg lkrg.ko");
		goto exit;
	}

	/* always returns -1 caused module verification */
	finit_module(fd, "log_level=3", MODULE_INIT_IGNORE_MODVERSIONS|MODULE_INIT_IGNORE_VERMAGIC);
	close(fd);

	sleep(2);

	if (mount("proc", "/proc", "proc", 0, NULL) == -1) {
		perror("$failmsg mount");
		goto exit;
	}

	fd = open("$lkrg_trigger", O_WRONLY);
	if (fd == -1) {
		perror("$failmsg $lkrg_trigger");
		goto exit;
	}

	int r = write(fd, "1\n", sizeof("1\n"));
	close(fd);

	if (r == -1) {
		perror("$failmsg write");
		goto exit;
	}

	fd = open("fuse.ko", O_RDONLY);
	if (fd == -1) {
		perror("$failmsg fuse.ko");
		goto exit;
	}

	finit_module(fd, NULL, MODULE_INIT_IGNORE_MODVERSIONS|MODULE_INIT_IGNORE_VERMAGIC);
	close(fd);

	sleep(2);

exit:
	delete_module("fuse", 0);
	delete_module("lkrg", 0);

	reboot(RB_POWER_OFF);
	pause();
}
__EOF__
mkdir -p proc
cp -a %buildroot%module_dir/lkrg.ko lkrg.ko
cp -a /lib/modules/%kversion-%flavour-%krelease/kernel/fs/fuse/fuse.ko fuse.ko
find init fuse.ko lkrg.ko proc -print | cpio -H newc -o | gzip -8n > initrd.img.gz
qemu_arch=%_arch
qemu_opts=""
console=ttyS0
timeout=600
%ifarch %ix86
qemu_arch=i386
%endif
%ifarch aarch64
qemu_opts="-machine accel=tcg,type=virt -cpu cortex-a57"
console=ttyAMA0
%endif
%ifarch %arm
qemu_arch=arm
qemu_opts="-machine accel=tcg,type=virt"
console=ttyAMA0
timeout=1800
%endif
timeout --foreground "$timeout" qemu-system-"$qemu_arch" -m 512 $qemu_opts -kernel /boot/vmlinuz-$KernelVer -nographic -append console="$console no_timer_check" -initrd initrd.img.gz > boot.log &&
grep -qF "LKRG initialized successfully" boot.log &&
grep -qF "LKRG unloaded" boot.log &&
grep -qE '^.*Power down' boot.log &&
! grep -qF "$failmsg" &&
! grep -qF 'Kernel panic' || {
	cat >&2 boot.log
	exit 1
}

%post
if [ $1 -eq 2 ]; then
	service lkrg condrestart
fi

%preun
# do not stop service if module was not build for currently running kernel
# do not unregister service: the other kernel flavour module still can be installed
if [ $1 -eq 0 ] && [ "$(uname -r)" = "%kversion-%flavour-%krelease" ]; then
	service lkrg stop
fi

# {{{
# hacks to keep LKRG running to prevent it stopping during remove-old-kernel
%triggerun -- kernel-modules-lkrg-std-def < 0.9.1-alt1
if [ "$2" -gt 0 ]; then
	/sbin/service lkrg-%kversion-%flavour-%krelease condrestart
fi

%triggerun -- kernel-modules-lkrg-un-def < 0.9.1-alt1
if [ "$2" -gt 0 ]; then
	/sbin/service lkrg-%kversion-%flavour-%krelease condrestart
fi

%triggerun -- kernel-modules-lkrg-std-debug < 0.9.1-alt1
if [ "$2" -gt 0 ]; then
	/sbin/service lkrg-%kversion-%flavour-%krelease condrestart
fi

%triggerun -- kernel-modules-lkrg-std-pae < 0.9.1-alt1
if [ "$2" -gt 0 ]; then
	/sbin/service lkrg-%kversion-%flavour-%krelease condrestart
fi
# }}}

%files
%doc README
%dir %module_dir
%module_dir/lkrg.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kepoch%kversion-%krelease.

* Fri Dec 16 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.6-alt1
- Updated to v0.9.6.
- un-def: built for aarch64 again.
- std-debug: restored build.

* Mon Oct 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.5.0.7.gitf32f627-alt1
- Updated to v0.9.5-7-gf32f627.
- ud-def: temporary do not build for aarch64.

* Wed Jul 20 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.3.0.41.gitcbd4198-alt1
- Updated to v0.9.3-41-gcbd4198 (closes: 43005).
- %%check: Fixed for centos and ovz-el7 flavours.

* Thu Apr 21 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.3-alt1
- Updated to v0.9.3.

* Fri Apr 08 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.23.git43db5f1-alt1
- Updated to v0.9.2-23-g43db5f1.

* Sun Jan 30 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.10.git17752c8-alt1
- Updated to v0.9.2-10-g17752c8.
- Built for centos kernel flavour.
- Removed some non-actual conflicts to older versions of the module.

* Sat Jan 08 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.0.1.git10ba314-alt1
- Updated to v0.9.2-1-g10ba314.

* Fri Dec 31 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2-alt1
- Updated to v0.9.2.

* Thu Dec 23 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.34.git0270c95-alt2
- Added %%module_dir directory to %%files.

* Thu Nov 25 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.34.git0270c95-alt1
- Updated to v0.9.1-34-g0270c95.

* Sat Nov 13 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.27.gitabd8719-alt1
- Updated to 0.9.1.0.27.gitabd8719.
- Moved init and service files to lkrg-common.

* Thu Oct 21 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.25.gita9906a6-alt1
- Updated to v0.9.1-25-ga9906a6.

* Wed Oct 06 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.19.git51ea889-alt2
- Built for ovz-el7 kernel flavour.

* Fri Sep 03 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.19.git51ea889-alt1
- Updated to v0.9.1-19-g51ea889.

* Sat May 29 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.8.git0fba5fe-alt1
- Updated to v0.9.1-8-g0fba5fe.
- Added explicit conflicts with LKRG module version 0.9.1.

* Thu May 27 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.6.gita516ef4-alt2
- Moved %%_sysconfdir/sysctl.d/lkrg.conf to lkrg-config package.
- Added dependency to lkrg-config package.

* Tue May 25 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.6.gita516ef4-alt1
- Updated to v0.9.1-6-ga516ef4.
- Added support for nolkrg kernel parameter.

* Thu Apr 29 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1-alt2
- Fixed %%post and %%preun.
- Added more workarounds to handle the previous module version incorrect
  behavior during removing.

* Tue Apr 27 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1-alt1
- Updated to v0.9.1.
- Introduced %_sysconfdir/sysctl.d/lkrg.conf.
- Versionified service files to avoid conflicts with other module versions.
- Added workaround to handle the previous module version incorrect behavior
  during removing.
- Fixed tests.
- Packed README.

* Fri Apr 16 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.0-alt1
- Updated to v0.9.0.

* Tue Mar 02 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210222.abaca2f-alt1
- Updated to commit abaca2fc7218fb992a2836d005db5c035851b4a6.
- Fixed FTBFS with kernel 5.11 on aarch64.

* Fri Feb 19 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210219.8a3aaa6-alt1
- Updated to commit 8a3aaa65c0fb97064139d2f361ad82ab6e28a377 (fixes work on
  IA-32).
- Enabled tests for all architectures on all flavours.
- std-debug: built for aarch64 and %%arm.

* Fri Feb 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210207.da571d3-alt1
- Updated to da571d3e8a35b2d6ea45e760d2da27aaada5eafb.
- Enabled armh build (was lack of kernel-source-lkrg armh build).
- Enable tests for all flavours but %%ix86 arch on std-debug and un-def.
- Adjusted tests.

* Mon Feb 08 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210207.993be4b-alt1
- Updated to 993be4b6249849abdc33e18d959c29cc6a8aba9e.
- Added tests (enabled only for std-def for now).

* Fri Jan 30 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210130-alt1
- Updated to commit e43d2dd525f014388c1f8cc0eb8a23f2ef07f415 (fixes #39626).

* Wed Dec 16 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20201210-alt1
- Updated to 47d6aca4d424f21044f2b890c245fccfad3a40f3.
- Fixed build against kernel 5.10.

* Tue Nov 24 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20201116-alt2
- Added SysVini script.

* Wed Nov 18 2020 Vitaly Chikunov <vt@altlinux.org> 0.8.1+git20201116-alt1
- Update to 3f76f5148b184e02b0b5b24bb1e8bac0e96a3376 (2020-11-16).

* Mon Oct 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20201016.c7d427d-alt1
- Updated to c7d427de476920f0585532ad57ee4280f083bf7f (fixed build with kernel
  5.9).

* Wed Sep 09 2020 Vitaly Chikunov <vt@altlinux.org>  0.8.1+git20200827.6f700b5-alt2
- Add aarch64, armh arches to build.
- Change module install dir to a generic misc/ dir.
- Add systemd unit (enabled by default).

* Tue Sep 01 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20200827.6f700b5-alt1
- Updated to 6f700b5b08b5a0fbc5fa41e1ba1908923a29eca9.

* Thu Aug 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1-alt2
- Rebuilt with new key.

* Thu Jul 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1-alt1
- Update to 0.8.1 (bugfix preventing Oops).

* Sun Jun 28 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8-alt1
- Updated to 0.8.

* Thu Jun 04 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt6.gitd57b4c0
- Updated to git commit d57b4c0f0e63d4d88761e098c53280967f2d1aec (fixed
  build with kernel 5.7).

* Fri Apr 17 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt5.git0f7c635
- Updated to git commit 0f7c6350a844c4a65a6860bff1172035e3cccae3 (fixed
  build with kernel 5.6).
- Disabled aarch64 build.

* Thu Aug 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt2
- Built with gear km-karch scheme.
- std-def flavour: built for aarch64.
- spec: replaced 'SUBDIRS' with 'M='.

* Mon Jul 22 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1
- Initial build for ALT Sisyphus.

