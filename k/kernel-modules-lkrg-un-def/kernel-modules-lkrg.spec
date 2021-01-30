%define module_name	lkrg
%define module_version	0.8.1+git20210130
%define module_release	alt1

%define flavour		un-def
%define karch		%ix86 x86_64 aarch64 armh
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def
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

Source1: lkrg.init

BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

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
cp -a %SOURCE1 .

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour modules M=$(pwd)
echo "enable lkrg.service" > lkrg.preset

%install
install -D -p -m0644 p_lkrg.ko %buildroot%module_dir/p_lkrg.ko
install -D -p -m0755 lkrg.init %buildroot%_initdir/lkrg
install -D -p -m0644 scripts/bootup/systemd/lkrg.service %buildroot%_unitdir/lkrg.service
install -D -p -m0644 lkrg.preset %buildroot%_presetdir/30-lkrg.preset

%post
%post_service lkrg

%preun
%preun_service lkrg

%files
%module_dir/p_lkrg.ko
%_initdir/lkrg
%_unitdir/lkrg.service
%_presetdir/30-lkrg.preset

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kepoch%kversion-%krelease.

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

