%define module_name lkrg
%define module_version 0.9.6

Name: kernel-source-lkrg
Version: %module_version
Release: alt2

Summary:  Linux Kernel Runtime Guard module sources

License: GPL-2.0
Group: Development/Kernel
Url:  https://lkrg.org/

VCS: https://github.com/lkrg-org/lkrg.git
Source: %module_name-%version.tar
Source1: %module_name.init
Patch: %name-%version-%release.patch

ExclusiveArch: aarch64 armh %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
%{?!_without_check:%{?!_disable_check:BuildRequires: kernel-headers-modules-un-def}}
BuildArch: noarch

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

This package contains the LKRG sources.

%package -n lkrg-common
Summary: Common files for Linux Kernel Runtime Guard module
BuildArch: noarch
Group: System/Configuration/Other
Provides: lkrg-config = %version
Obsoletes: lkrg-config < %version

%description -n lkrg-common
Linux Kernel Runtime Guard (LKRG) is a loadable kernel module that performs
runtime integrity checking of the Linux kernel and detection of security
vulnerability exploits against the kernel. As controversial as this concept is,
LKRG attempts to post-detect and hopefully promptly respond to unauthorized
modifications to the running Linux kernel (integrity checking) or to
credentials (such as user IDs) of the running processes (exploit
detection). For process credentials, LKRG attempts to detect the exploit and
take action before the kernel would grant the process access (such as open a
file) based on the unauthorized credentials.

This package contains common files fo Linux Kernel Runtime Guard.

%prep
%setup -q -c
pushd %module_name-%version
%patch -p1
popd
cp -a %SOURCE1 .

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %module_name-%version
mkdir -p %buildroot%_sysconfdir
cp -a %module_name-%version/scripts/bootup/lkrg.conf %buildroot%_sysconfdir/lkrg.conf

mkdir -p %buildroot%_initdir
install -pm755 lkrg.init %buildroot%_initdir/lkrg

mkdir -p %buildroot%_unitdir
cat <<EOF >%buildroot%_unitdir/lkrg.service
[Unit]
Description=Linux Kernel Runtime Guard
DefaultDependencies=no
After=systemd-modules-load.service
Before=systemd-sysctl.service
Before=sysinit.target shutdown.target
Conflicts=shutdown.target
ConditionKernelCommandLine=!nolkrg

[Service]
Type=oneshot
ExecStart=/etc/rc.d/init.d/lkrg start
ExecStop=/etc/rc.d/init.d/lkrg stop
RemainAfterExit=yes

[Install]
WantedBy=sysinit.target
EOF

mkdir -p %buildroot%_presetdir
cat <<EOF >%buildroot%_presetdir/30-lkrg.preset
enable lkrg.service
EOF

%check
# Just a test build on un-def kernel.
cd %module_name-%version
for V in $(ls /lib/modules); do
	make -s %_smp_mflags KERNELRELEASE=$V
done

%triggerun -n lkrg-common -- lkrg-config < 0.9.2.0.1.git10ba314-alt2 lkrg-common < 0.9.2.0.1.git10ba314-alt2
if [ -e %_sysconfdir/sysctl.d/lkrg.conf ]; then
	echo "Migrating an LKRG config to the new place"
	if ! diff -q %_sysconfdir/{,sysctl.d/}lkrg.conf >/dev/null; then
		mv %_sysconfdir/lkrg.conf{,.rpmnew}
	fi
	mv %_sysconfdir/sysctl.d/lkrg.conf %_sysconfdir/lkrg.conf
fi

%preun -n lkrg-common
%preun_service lkrg

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n lkrg-common
%config(noreplace) %_sysconfdir/lkrg.conf
%_initdir/lkrg
%_unitdir/lkrg.service
%_presetdir/30-lkrg.preset

%changelog
* Fri Feb 10 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.6-alt2
- Add support for RHEL9.2 5.14.0-248.el9.

* Fri Dec 16 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.6-alt1
- Updated to v0.9.6.

* Thu Oct 27 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.5.0.7.gitf32f627-alt2
- Fixed build for centos kernel.

* Mon Oct 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.5.0.7.gitf32f627-alt1
- Updated to v0.9.5-7-gf32f627.
- Temporally disable %%check for aarch64.

* Wed Jul 20 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.3.0.41.gitcbd4198-alt1
- Updated to v0.9.3-41-gcbd4198 (closes: 43005).

* Thu Apr 21 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.3-alt1
- Updated to v0.9.3.

* Fri Apr 08 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.23.git43db5f1-alt1
- Updated to v0.9.2-23-g43db5f1.
- Enhanced lkrg.init.

* Sun Jan 30 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.10.git17752c8-alt1
- Updated to v0.9.2-10-g17752c8.

* Fri Jan 14 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.0.1.git10ba314-alt2
- Updated upstream URL and VCS.
- lkrg-common:
  + Moved lkrg.conf to %%_sysconfdir;
  + Enhanced init script.

* Sat Jan 08 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2.0.1.git10ba314-alt1
- Updated to v0.9.2-1-g10ba314.

* Fri Dec 31 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.2-alt1
- Updated to v0.9.2.

* Thu Nov 25 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.34.git0270c95-alt1
- Updated to v0.9.1-34-g0270c95.

* Fri Nov 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.27.gitabd8719-alt1
- Updated to v0.9.1-27-gabd8719.
- Fixed FTBFS with kernel 5.15 on armh.
- lkrg-common: renamed from lkrg-config, added init and service files.

* Thu Oct 21 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.25.gita9906a6-alt1
- Updated to v0.9.1-25-ga9906a6.

* Fri Sep 03 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.19.git51ea889-alt1
- Updated to v0.9.1-19-g51ea889.

* Sat May 29 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.8.git0fba5fe-alt1
- Updated to v0.9.1-8-g0fba5fe.

* Thu May 27 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.6.gita516ef4-alt2
- Added lkrg-config subpackage.

* Tue May 25 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1.0.6.gita516ef4-alt1
- Updated to v0.9.1-6-ga516ef4.

* Tue Apr 27 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1-alt1
- Updated to v0.9.1.

* Fri Apr 16 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.0-alt1
- Updated to v0.9.0.

* Tue Mar 02 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210222.abaca2f-alt1
- Updated to commit abaca2fc7218fb992a2836d005db5c035851b4a6.
- Fixed FTBFS with kernel 5.11 on aarch64.

* Fri Feb 19 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210219.8a3aaa6-alt1
- Updated to commit 8a3aaa65c0fb97064139d2f361ad82ab6e28a377 (fixes work on
  IA-32).

* Fri Feb 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210211.da571d3-alt1
- Updated to commit da571d3e8a35b2d6ea45e760d2da27aaada5eafb.
- Built for armh.

* Mon Feb 08 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210207.993be4b-alt1
- Updated to commit 993be4b6249849abdc33e18d959c29cc6a8aba9e.

* Sat Jan 30 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20210130-alt1
- Updated to commit e43d2dd525f014388c1f8cc0eb8a23f2ef07f415 (closes #39626).

* Sat Dec 26 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20201210-alt2
- Fixed BR: kernel-build-tools -> rpm-build-kernel.

* Wed Dec 16 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20201210-alt1
- Updated to 47d6aca4d424f21044f2b890c245fccfad3a40f3 (2020-12-10).
- Fixed build against kernel 5.10.

* Wed Nov 18 2020 Vitaly Chikunov <vt@altlinux.org> 0.8.1+git20201116-alt1
- Update to 3f76f5148b184e02b0b5b24bb1e8bac0e96a3376 (2020-11-16).

* Mon Oct 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20201016.c7d427d-alt1
- Updated to c7d427de476920f0585532ad57ee4280f083bf7f.

* Tue Sep 01 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20200827.6f700b5-alt1
- Updated to 6f700b5b08b5a0fbc5fa41e1ba1908923a29eca9.

* Thu Jul 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1-alt1
- Update to 0.8.1 (bugfix release preventing Oops).

* Sun Jun 28 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8-alt1
- Updated to 0.8.

* Thu Jun 04 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt6.gitd57b4c0
- Updated to git commit d57b4c0f0e63d4d88761e098c53280967f2d1aec (fixed
  build with kernel 5.7).

* Fri Apr 17 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt5.git0f7c635
- Updated to git commit 0f7c6350a844c4a65a6860bff1172035e3cccae3 (fixed
  build with kernel 5.6).

* Sat Mar 21 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt4.gitd379e93
- Updated to git commit d379e93c29b4933753a7e769d147c08ea03df63e.

* Thu Feb 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt3
- Fixed FTBFS for kernel 5.3+ on aarch64.

* Thu Aug 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt2
- Built for aarch64.

* Mon Jul 22 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1
- Initial build for ALT Sisyphus.

