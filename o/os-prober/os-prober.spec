%define _unpackaged_files_terminate_build 1
%filter_from_requires s,python-module-zope\.app\.appsetup,,

Name: os-prober
Version: 1.82
Release: alt1

Summary: Operating systems detector
License: GPLv2+
Group: System/Configuration/Boot and Init
Url: https://salsa.debian.org/installer-team/os-prober
VCS: https://salsa.debian.org/installer-team/os-prober.git

Source0: %name-%version.tar

Patch: %name-1.42-UUID-rootdev-alt.patch
Patch1: %name-1.77-alt-grub2-detect-auto-reference.patch
Patch2: %name-1.77-alt-grub2-skip-30_os-prober-parsing.patch
Patch3: %name-1.77-alt-check-identical-uuid-of-root.patch
Patch4: %name-1.77-alt-dmdevfs-use-for-raid.patch

%description
This is a small package that may be depended on by any bootloader
installer package to detect other filesystems with operating systems on
them, and work out how to boot other linux installs.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build

%install
install -Dm755 os-prober -t %buildroot/%_bindir
install -Dm755 linux-boot-prober -t %buildroot/%_bindir
install -Dm755 newns -t %buildroot%_libexecdir/os-prober
install -Dm644 common.sh -t %buildroot%_datadir/os-prober

mkdir -p %buildroot%_libexecdir/os-probes/init
cp -a os-probes/init/common/* %buildroot%_libexecdir/os-probes/init/

mkdir -p %buildroot%_libexecdir/os-probes/mounted
cp -a os-probes/mounted/x86/* %buildroot%_libexecdir/os-probes/mounted/
cp -a os-probes/mounted/common/* %buildroot%_libexecdir/os-probes/mounted/
cp -a os-probes/common/* %buildroot%_libexecdir/os-probes/

mkdir -p %buildroot%_libexecdir/linux-boot-probes/mounted
cp -a linux-boot-probes/common/* %buildroot%_libexecdir/linux-boot-probes
cp -a linux-boot-probes/mounted/x86/* \
   %buildroot%_libexecdir/linux-boot-probes/mounted/
cp -a linux-boot-probes/mounted/common/* \
   %buildroot%_libexecdir/linux-boot-probes/mounted/

mkdir -p %buildroot%_localstatedir/os-prober

%files
%doc README
%_bindir/os-prober
%_bindir/linux-boot-prober
%_libexecdir/linux-boot-probes
%_libexecdir/os-probes
%_libexecdir/os-prober
%_datadir/os-prober
%_localstatedir/os-prober

%changelog
* Thu Jul 25 2024 Egor Ignatov <egori@altlinux.org> 1.82-alt1
- 1.82

* Fri Apr 19 2024 Anton Midyukov <antohami@altlinux.org> 1.77-alt5
- Find partitions involved in a RAID via /dev/mapper (evms)

* Wed Apr 17 2024 Anton Midyukov <antohami@altlinux.org> 1.77-alt4
- Skip partitions with UUID identical the UUID of '/'

* Fri Mar 20 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.77-alt3
- fix grub2-skip-30_os-prober-parsing patch

* Wed Mar 11 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.77-alt2
- add grub2-detect-auto-reference patch
- add grub2-skip-30_os-prober-parsing patch

* Tue Apr 30 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.77-alt1
- 1.77 (closes: #37224)
  + relies on grub-mount

* Fri Mar 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1.74-alt1
- 1.74

* Mon Nov 02 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.70-alt1
- 1.70
- Fix (ALT #31347)

* Thu May 23 2013 Mikhail Efremov <sem@altlinux.org> 1.61-alt1
- 1.61

* Thu May 23 2013 Michael Shigorin <mike@altlinux.org> 1.52-alt2
- dropped evms related hack that is long irrelevant (see #28181)

* Fri May 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.52-alt1
- 1.52

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.48-alt1
- 1.48

* Mon Jul 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.47-alt1
- 1.47

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.44-alt1
- 1.44

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.42-alt2
- add suport for UUID= root devices in lilo.conf (ALT #25168)

* Tue Feb 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.42-alt1
- 1.42

* Fri Nov 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.41-alt1
- 1.41

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.39-alt2
- hackaround evms

* Sun Jul 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.39-alt1
- 1.39

* Mon Jun 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.38-alt1
- 1.38

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.36-alt1
- initial
