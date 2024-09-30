%define kernel_base_version	6.10
%define kernel_sublevel        .12

Name: kernel-image-mp
Version: %kernel_base_version%kernel_sublevel
Release: alt1

%define krelease	%release
%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )

## Don't edit below this line ##################################
%define kversion	%kernel_base_version%kernel_sublevel
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/

Patch0: %name-%version-%release.patch

ExclusiveArch: aarch64 %{?_enable_extra:armh %ix86 x86_64}

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc flex kmod lzma-utils
BuildRequires: libdb4-devel
BuildRequires: kernel-source-%kernel_base_version
BuildRequires: libelf-devel libssl-devel zlib-devel
BuildRequires: openssl python3 rsync

Requires: bootloader-utils >= 0.5.2-alt3
Provides: kernel = %kversion

%ifarch %arm
%define Image zImage
%endif
%ifarch aarch64
%define Image Image
%endif
%ifarch %ix86 x86_64
%define Image bzImage
%endif
%ifarch %arm aarch64
%define dtb dtbs
%else
%define dtb %nil
%endif

%description
This package contains the Linux kernel that is used to boot and run
your system and supports most recent arm machines.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

Since Linux 2.6.18 the kernel build system supports creation of
sanitized kernel headers for use in userspace (by deleting headers
which are not usable in userspace and removing #ifdef __KERNEL__
blocks from installed headers).  This package contains sanitized
headers instead of raw kernel headers which were present in some
previous versions of similar packages.

If possible, try to use glibc-kernheaders instead of this package.

%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source
directory.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = -%flavour-%krelease/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%build
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

cp -vf config-%_target_cpu .config
for f in arch/arm/boot/dts/Makefile arch/arm64/boot/dts/*/Makefile; do
	echo -e '\nDTC_FLAGS += -@' >> $f
done

%make_build oldconfig
%make_build %Image modules %dtb

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/%Image %buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer
make modules_install INSTALL_MOD_PATH=%buildroot
%ifarch armh aarch64
make dtbs_install INSTALL_DTBS_PATH=%buildroot/lib/devicetree/$KernelVer
%endif

mkdir -p %buildroot%kbuild_dir/arch/%base_arch
cp -a include %buildroot%kbuild_dir/include
%ifarch %arm aarch64
cp -a arch/%base_arch/include %buildroot%kbuild_dir/arch/%base_arch
%endif

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/md/dm*.h \
	%buildroot%kbuild_dir/drivers/md/
cp -a drivers/usb/core/*.h \
	%buildroot%kbuild_dir/drivers/usb/core/
cp -a drivers/net/wireless/Kconfig \
	%buildroot%kbuild_dir/drivers/net/wireless/
cp -a lib/hexdump.c %buildroot%kbuild_dir/lib/
cp -a kernel/workqueue.c %buildroot%kbuild_dir/kernel/
cp -a net/mac80211/ieee80211_i.h \
	%buildroot%kbuild_dir/net/mac80211/
cp -a net/mac80211/sta_info.h \
	%buildroot%kbuild_dir/net/mac80211/

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Module.symvers
	arch/%base_arch/Makefile
	arch/%base_arch/kernel/module.lds
	scripts/Kbuild.include
	scripts/Makefile
	scripts/Makefile.*
	scripts/basic/fixdep
	scripts/basic/hash
	scripts/bin2c
	scripts/checkconfig.pl
	scripts/checkincludes.pl
	scripts/checkversion.pl
	scripts/conmakehash
	scripts/depmod.sh
	scripts/extract-ikconfig
	scripts/gcc-goto.sh
	scripts/gcc-plugins/*.so
	scripts/gcc-version.sh
	scripts/genksyms/genksyms
	scripts/kallsyms
	scripts/kconfig/conf
	scripts/ld-version.sh
	scripts/link-vmlinux.sh
	scripts/makelst
	scripts/mkcompile_h
	scripts/mkmakefile
	scripts/mkversion
	scripts/mod/mk_elfconfig
	scripts/mod/modpost
	scripts/module.lds
	scripts/modules-check.sh
	scripts/pahole-flags.sh
	scripts/pnmtologo
	scripts/recordmcount
	scripts/recordmcount.c
	scripts/recordmcount.h
	scripts/recordmcount.pl
	scripts/subarch.include
	tools/objtool/objtool
	.config
	.kernelrelease
	System.map
"
for f in $KbuildFiles; do
	[ -e "$f" ] || continue
	[ -x "$f" ] && mode=755 || mode=644
	install -Dp -m$mode "$f" %buildroot%kbuild_dir/"$f"
done

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin

%set_verify_elf_method none
%add_debuginfo_skiplist /boot %modules_dir

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%ifarch %arm aarch64
/lib/devicetree/%kversion-%flavour-%krelease
%endif
%modules_dir
%exclude %modules_dir/build
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build

%changelog
* Mon Sep 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.10.12-alt1
- 6.10.12

* Mon Sep 09 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.10.8-alt1
- 6.10.8

* Mon Sep 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.10.4-alt1
- 6.10.4

* Mon Sep 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.10.0-alt1
- 6.10

* Mon Jul 29 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.9.12-alt1
- 6.9.12

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.9.8-alt1
- 6.9.8

* Thu Jun 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.9.4-alt1
- 6.9.4

* Mon Jun 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.9.0-alt1
- 6.9

* Thu May 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.8.12-alt1
- 6.8.12

* Wed May 01 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.8.8-alt1
- 6.8.8

* Fri Apr 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.8.4-alt1
- 6.8.4

* Thu Apr 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.8.0-alt1
- 6.8

* Wed Apr 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.7.12-alt1
- 6.7.12

* Mon Mar 04 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.7.8-alt1
- 6.7.8

* Tue Feb 06 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.7.4-alt1
- 6.7.4

* Tue Feb 06 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.7.0-alt1
- 6.7

* Tue Feb 06 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.6.16-alt1
- 6.6.16

* Tue Jan 16 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.6.12-alt1
- 6.6.12

* Thu Dec 21 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.6.8-alt1
- 6.6.8

* Wed Dec 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.6.4-alt1
- 6.6.4

* Tue Dec 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.6.0-alt1
- 6.6

* Mon Nov 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.5.12-alt1
- 6.5.12

* Fri Oct 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.5.8-alt1
- 6.5.8

* Tue Sep 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.5.4-alt1
- 6.5.4

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.5.0-alt1
- 6.5

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.4.16-alt1
- 6.4.16

* Sat Aug 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.4.12-alt1
- 6.4.12

* Mon Aug 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.4.8-alt1
- 6.4.8

* Thu Jul 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.4.4-alt1
- 6.4.4

* Thu Jul 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.4.0-alt1
- 6.4

* Thu Jul 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.3.12-alt1
- 6.3.12

* Wed Jun 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.3.8-alt1
- 6.3.8

* Thu May 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.3.4-alt1
- 6.3.4

* Thu May 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.3.0-alt1
- 6.3

* Wed May 17 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.16-alt1
- 6.2.16

* Thu Apr 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.12-alt1
- 6.2.12

* Wed Mar 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.8-alt1
- 6.2.8

* Tue Mar 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.4-alt1
- 6.2.4

* Mon Mar 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.0-alt1
- 6.2

* Mon Mar 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.19-alt1
- 6.1.19

* Fri Mar 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.16-alt1
- 6.1.16

* Wed Feb 15 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.12-alt1
- 6.1.12

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.8-alt1
- 6.1.8

* Mon Jan 09 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.4-alt1
- 6.1.4

* Mon Jan 09 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.0-alt1
- 6.1

* Fri Jan 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.16-alt1
- 6.0.16

* Thu Dec 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.12-alt1
- 6.0.12

* Fri Nov 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.8-alt1
- 6.0.8

* Wed Oct 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.4-alt1
- 6.0.4

* Mon Oct 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.0-alt1
- 6.0

* Mon Oct 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.19.16-alt1
- 5.19.16

* Wed Sep 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.19.12-alt1
- 5.19.12

* Mon Sep 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.19.8-alt1
- 5.19.8

* Thu Aug 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.19.4-alt1
- 5.19.4

* Thu Aug 04 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.19.0-alt1
- 5.19

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.18.16-alt1
- 5.18.16

* Fri Jul 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.18.12-alt1
- 5.18.12

* Wed Jun 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.18.8-alt1
- 5.18.8

* Wed Jun 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.18.4-alt1
- 5.18.4

* Tue Jun 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.18.0-alt1
- 5.18

* Mon May 30 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.17.12-alt1
- 5.17.12

* Mon May 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.17.8-alt1
- 5.17.8

* Wed Apr 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.17.4-alt1
- 5.17.4

* Tue Mar 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.17.0-alt1
- 5.17

* Mon Mar 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.16.16-alt1
- 5.16.16

* Sat Mar 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.16.12-alt1
- 5.16.12

* Fri Feb 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.16.8-alt1
- 5.16.8

* Mon Jan 31 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.16.4-alt1
- 5.16.4

* Fri Jan 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.16.0-alt1
- 5.16

* Fri Jan 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.15.16-alt1
- 5.15.16

* Wed Dec 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.15.12-alt1
- 5.15.12

* Tue Dec 14 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.15.8-alt1
- 5.15.8

* Mon Nov 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.15.4-alt1
- 5.15.4

* Mon Nov 15 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.15.0-alt1
- 5.15

* Wed Nov 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.14.16-alt1
- 5.14.16

* Wed Oct 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.14.12-alt1
- 5.14.12

* Mon Sep 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.14.8-alt1
- 5.14.8

* Wed Sep 15 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.14.4-alt1
- 5.14.4

* Tue Sep 14 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.14.0-alt1
- 5.14

* Mon Sep 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.13.16-alt1
- 5.13.16

* Wed Aug 18 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.13.12-alt1
- 5.13.12

* Wed Aug 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.13.8-alt1
- 5.13.8

* Tue Jul 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.13.4-alt1
- 5.13.4

* Mon Jul 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.13.0-alt1
- 5.13

* Mon Jul 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.12.16-alt1
- 5.12.16

* Fri Jun 18 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.12.12-alt1
- 5.12.12

* Fri May 28 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.12.8-alt1
- 5.12.8

* Fri May 14 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.12.4-alt1
- 5.12.4

* Mon Apr 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.12.0-alt1
- 5.12

* Wed Apr 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.11.16-alt1
- 5.11.16

* Wed Apr 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.11.12-alt1
- 5.11.12

* Mon Mar 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.11.8-alt1
- 5.11.8

* Mon Mar 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.11.4-alt1
- 5.11.4

* Mon Feb 15 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.11.0-alt1
- 5.11

* Mon Feb 15 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.10.16-alt1
- 5.10.16

* Mon Feb 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.10.12-alt1
- 5.10.12

* Sun Jan 17 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.10.8-alt1
- 5.10.8

* Wed Dec 30 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.10.4-alt1
- 5.10.4

* Thu Dec 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.10.0-alt1
- 5.10

* Thu Dec 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.9.16-alt1
- 5.9.16

* Wed Dec 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.9.12-alt1
- 5.9.12

* Wed Nov 11 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.9.8-alt1
- 5.9.8

* Thu Nov 05 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.9.4-alt1
- 5.9.4

* Mon Oct 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.9.0-alt1
- 5.9

* Sat Oct 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.16-alt1
- 5.8.16

* Mon Sep 28 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.12-alt1
- 5.8.12

* Thu Sep 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.8-alt1
- 5.8.8

* Wed Aug 26 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.4-alt1
- 5.8.4

* Wed Aug 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.0-alt1
- 5.8

* Wed Aug 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.16-alt1
- 5.7.16

* Mon Aug 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.12-alt1
- 5.7.12

* Mon Jul 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.8-alt1
- 5.7.8

* Thu Jun 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.4-alt1
- 5.7.4

* Sun Jun 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.0-alt1
- 5.7.0

* Wed Jun 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.6.16-alt1
- 5.6.16

* Tue May 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.6.12-alt1
- 5.6.12

* Wed May 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.6.8-alt1
- 5.6.8

* Mon Apr 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.6.4-alt1
- 5.6.4

* Mon Apr 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.6.0-alt1
- 5.6.0

* Mon Apr 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.5.16-alt1
- 5.5.16

* Wed Mar 25 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.5.12-alt1
- 5.5.12

* Fri Mar 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.5.8-alt1
- 5.5.8

* Tue Feb 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.5.4-alt1
- 5.5.4

* Thu Feb 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.5.0-alt1
- 5.5.0

* Thu Jan 30 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.4.16-alt1
- 5.4.16

* Wed Jan 15 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.4.12-alt1
- 5.4.12

* Sun Jan 05 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.4.8-alt1
- 5.4.8

* Thu Dec 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.4.4-alt1
- 5.4.4

* Mon Dec 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.16-alt1
- 5.3.16

* Fri Nov 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.12-alt1
- 5.3.12

* Tue Oct 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.8-alt1
- 5.3.8

* Mon Oct 07 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.4-alt1
- 5.3.4

* Thu Sep 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.0-alt1
- 5.3

* Thu Sep 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.16-alt1
- 5.2.16

* Fri Sep 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.12-alt1
- 5.2.12

* Mon Aug 12 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.8-alt1
- 5.2.8

* Mon Jul 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.4-alt1
- 5.2.4

* Mon Jul 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.0-alt1
- 5.2

* Wed Jul 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.16-alt1
- 5.1.16

* Wed Jun 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.12-alt1
- 5.1.12

* Mon Jun 10 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.8-alt1
- 5.1.8

* Wed May 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.4-alt1
- 5.1.4

* Mon May 20 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.0-alt1
- 5.1

* Wed May 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.16-alt1
- 5.0.16

* Sat May 04 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.12-alt1
- 5.0.12

* Wed Apr 17 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.8-alt1
- 5.0.8

* Mon Mar 25 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.4-alt1
- 5.0.4

* Mon Mar 04 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0.0-alt1
- 5.0

* Sun Feb 24 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.20.12-alt1
- 4.20.12

* Wed Feb 13 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.20.8-alt1
- 4.20.8

* Mon Jan 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.20.4-alt1
- 4.20.4

* Wed Jan 23 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.20.0-alt1
- 4.20

* Wed Jan 23 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.19.16-alt1
- 4.19.16

* Mon Dec 24 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.19.12-alt1
- 4.19.12

* Mon Dec 10 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.19.8-alt1
- 4.19.8

* Fri Nov 23 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.19.4-alt1
- 4.19.4

* Thu Oct 25 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.19.0-alt1
- 4.19

* Mon Oct 22 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.18.16-alt1
- 4.18.16

* Fri Oct 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.18.12-alt1
- 4.18.12

* Mon Sep 17 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.18.8-alt1
- 4.18.8

* Thu Aug 23 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.18.4-alt1
- 4.18.4

* Tue Aug 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.18.0-alt1
- 4.18

* Sat Aug 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.17.16-alt1
- 4.17.16

* Fri Aug 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.17.12-alt1
- 4.17.12

* Wed Jul 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.17.8-alt1
- 4.17.8

* Wed Jul 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.17.4-alt1
- 4.17.4

* Mon Jul 02 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.17.0-alt1
- 4.17

* Mon Jun 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.16.16-alt1
- 4.16.16

* Mon May 28 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.16.12-alt1
- 4.16.12

* Sat May 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.16.8-alt1
- 4.16.8

* Tue Apr 24 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.16.4-alt1
- 4.16.4

* Wed Apr 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.16.0-alt1
- 4.16

* Mon Apr 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15.16-alt1
- 4.15.16

* Wed Mar 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15.12-alt1
- 4.15.12

* Sun Mar 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15.8-alt1
- 4.15.8

* Mon Feb 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15.4-alt1
- 4.15.4

* Thu Feb 01 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15.0-alt1
- 4.15

* Wed Jan 31 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.16-alt1
- 4.14.16

* Sat Jan 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.12-alt1
- 4.14.12

* Mon Dec 25 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.8-alt1
- 4.14.8

* Mon Dec 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.5-alt1
- 4.14.5

* Wed Dec 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.4-alt1
- 4.14.4

* Wed Nov 15 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.14.0-alt1
- 4.14.0

* Wed Nov 08 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.13.12-alt1
- 4.13.12

* Wed Oct 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.13.8-alt1
- 4.13.8

* Fri Sep 29 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.13.4-alt1
- 4.13.4

* Mon Sep 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.12.12-alt1
- 4.12.12

* Fri Aug 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.12.8-alt1
- 4.12.8

* Fri Jul 28 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.12.4-alt1
- 4.12.4

* Mon Jul 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.12.2-alt1
- 4.12.2

* Thu Jul 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.12.0-alt1
- 4.12

* Thu Jun 29 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.11.8-alt1
- 4.11.8

* Wed May 31 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.11.3-alt1
- 4.11.3

* Sun May 14 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.10.16-alt1
- 4.10.16

* Mon Mar 13 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.10.2-alt1
- 4.10.2

* Mon Feb 20 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.10.0-alt1
- 4.10

* Thu Feb 16 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.10-alt1
- 4.9.10

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.8-alt1
- 4.9.8

* Thu Jan 26 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.6-alt1
- 4.9.6

* Mon Jan 16 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.4-alt1
- 4.9.4

* Tue Jan 10 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.2-alt1
- 4.9.2

* Mon Jan 09 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.0-alt1
- 4.9

* Mon Dec 12 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.14-alt1
- 4.8.14

* Mon Nov 21 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.10-alt1
- 4.8.10

* Tue Nov 15 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.8-alt1
- 4.8.8

* Mon Oct 31 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.6-alt1
- 4.8.6

* Mon Oct 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.4-alt1
- 4.8.4

* Mon Oct 17 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.2-alt1
- 4.8.2

* Tue Oct 04 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.8.0-alt1
- 4.8

* Fri Sep 30 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.6-alt1
- 4.7.6

* Sat Sep 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.5-alt1
- 4.7.5

* Thu Sep 15 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.4-alt1
- 4.7.4

* Wed Sep 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.3-alt1
- 4.7.3

* Sun Aug 28 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.2-alt1
- 4.7.2

* Tue Aug 23 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.7.0-alt1
- 4.7

* Thu Aug 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.6-alt1
- 4.6.6

* Tue Jul 12 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6.4-alt1
- 4.6.4

* Sat May 14 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.5.4-alt1
- 4.5.4

* Thu May 05 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.5.3-alt1
- 4.5.3

* Wed Apr 20 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.5.0-alt1
- 4.5

* Fri Mar 04 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.4-alt1
- 4.4.4

* Mon Feb 22 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Tue Feb 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Mon Jan 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.0-alt1
- 4.4

* Mon Nov 09 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3.0-alt1
- 4.3

* Wed Sep 23 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.8-alt1
- 4.1.8

* Tue Aug 18 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.6-alt1
- 4.1.6

* Wed Aug 05 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.4-alt1
- 4.1.4

* Sun Jul 12 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.2-alt1
- 4.1.2

* Thu Jul 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.0-alt1
- 4.1

* Sat May 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt1
- 4.0

* Mon Apr 13 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.19.4-alt1
- 3.19.4

* Thu Mar 19 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.19.2-alt1
- 3.19.2

* Mon Mar 16 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.19.0-alt1
- 3.19.0

* Fri Feb 27 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.18.8-alt1
- 3.18.8

* Mon Feb 09 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.18.6-alt1
- 3.18.6

* Wed Jan 28 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.18.4-alt1
- 3.18.4

* Tue Jan 20 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.18.2-alt1
- 3.18.2

* Thu Jan 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.18.0-alt1
- 3.18

* Mon Jan 12 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.8-alt1
- 3.17.8

* Tue Dec 16 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.6-alt1
- 3.14.6

* Mon Nov 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.4-alt1
- 3.17.4

* Wed Nov 19 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.3-alt1
- 3.17.3

* Fri Oct 31 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.2-alt1
- 3.17.2

* Mon Oct 20 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.0-alt1
- 3.17

* Tue Aug 05 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.15.8-alt1
- 3.15.8

* Mon Jul 07 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.15.4-alt1
- 3.15.4

* Tue May 13 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.14.4-alt1
- 3.14.4

* Mon Mar 31 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.14.0-alt1
- 3.14

* Fri Feb 21 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.12-alt1
- 3.12.12

* Fri Feb 14 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.11-alt1
- 3.12.11

* Fri Feb 07 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.10-alt1
- 3.12.10

* Tue Jan 28 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.9-alt1
- 3.12.9

* Thu Jan 16 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.8-alt1
- 3.12.8

* Tue Jan 07 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.6-alt1
- 3.12.6

* Mon Dec 16 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.5-alt1
- 3.12.5

* Mon Dec 09 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.4-alt1
- 3.12.4

* Wed Dec 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.3-alt1
- 3.12.3

* Mon Nov 25 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.0-alt2
- fixes from stable queue:
  + mvebu: re-enable PCIe on Armada 370 DB
  + mvebu: use the virtual CPU registers to access coherency registers
  + irqchip: armada-370-xp: fix IPI race condition

* Tue Nov 05 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.0-alt1
- 3.12

* Thu Sep 26 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.11.0-alt1
- 3.11

* Wed Jul 03 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- 3.10

* Wed Jun 26 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.0-alt1
- initial
