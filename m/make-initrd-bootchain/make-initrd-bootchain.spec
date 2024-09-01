%define parent make-initrd
%define child  bootchain

%ifarch %e2k %mips riscv64
# shellcheck is not available on these architectures
%def_disable check
%endif

Name: %parent-%child
Version: 0.1.5
Release: alt24

Summary: %child modules set for %parent
License: GPL-3.0
Group: System/Base
BuildArch: noarch

Packager: Leonid Krivoshein <klark@altlinux.org>

%{!?_disable_check:BuildRequires: shellcheck}

Requires: %name-core        = %version-%release
Requires: %name-getimage    = %version-%release
Requires: %name-waitdev     = %version-%release
Requires: %name-interactive = %version-%release
Requires: %name-altboot     = %version-%release
Requires: %name-localdev    = %version-%release
Requires: %name-liverw      = %version-%release
Requires: %name-waitnet     = %version-%release
Requires: %name-nfs         = %version-%release
Requires: %name-cifs        = %version-%release

AutoReq: noshell, noshebang

Source0: %name-%version.tar

%description
Meta-package with the full set of the %child modules for %parent

%package core
Summary: %child-core module for %parent
Group: System/Base
BuildArch: noarch
Requires: %parent >= 2.9
AutoReq: noshell, noshebang

%description core
%child-core module for %parent

%package getimage
Summary: getimage sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-core = %version-%release
Requires: wget
AutoReq: noshell, noshebang

%description getimage
getimage sub-module for %name

%package waitdev
Summary: waitdev sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-core = %version-%release
AutoReq: noshell, noshebang

%description waitdev
waitdev sub-module for %name

%package interactive
Summary: interactive sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-core = %version-%release
Requires: console-vt-tools
Requires: dialog
Requires: less
Requires: pv
AutoReq: noshell, noshebang

%description interactive
interactive sub-module for %name

%package altboot
Summary: altboot sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-interactive = %version-%release
Requires: curl
Requires: losetup
AutoReq: noshell, noshebang

%description altboot
altboot sub-module for %name

%package localdev
Summary: localdev sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-altboot = %version-%release
AutoReq: noshell, noshebang

%description localdev
localdev sub-module for %name

%package liverw
Summary: liverw sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-localdev = %version-%release
Requires: e2fsprogs
Requires: fdisk
Requires: sfdisk
AutoReq: noshell, noshebang

%description liverw
liverw sub-module for %name

%package waitnet
Summary: waitnet sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-altboot = %version-%release
AutoReq: noshell, noshebang

%description waitnet
waitnet sub-module for %name

%package nfs
Summary: nfs sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-waitnet = %version-%release
Requires: nfs-utils
Requires: iproute2
AutoReq: noshell, noshebang

%description nfs
nfs sub-module for %name

%package cifs
Summary: cifs sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-waitnet = %version-%release
Requires: cifs-utils
Requires: hostinfo
AutoReq: noshell, noshebang

%description cifs
cifs sub-module for %name

%package doc
Summary: %parent-%child documentation
Group: Documentation
BuildArch: noarch
AutoReq: noshell, noshebang

%description doc
Documentation, testing and development files for %parent-%child

%prep
%setup -q

%install
./mix-altboot.sh
mkdir -p -- "%buildroot%_datadir/%parent"/features "%buildroot%_docdir"
cp -aRf -- %child-* "%buildroot%_datadir/%parent"/features/
mv -f -- "%buildroot%_datadir/%parent/features/%child-doc" "%buildroot%_docdir/%name"

%check
./check-scripts.sh --verbose

%files

%files core
%_datadir/%parent/features/%child-core

%files getimage
%_datadir/%parent/features/%child-getimage

%files waitdev
%_datadir/%parent/features/%child-waitdev

%files interactive
%_datadir/%parent/features/%child-interactive

%files altboot
%_datadir/%parent/features/%child-altboot

%files localdev
%_datadir/%parent/features/%child-localdev

%files liverw
%_datadir/%parent/features/%child-liverw

%files waitnet
%_datadir/%parent/features/%child-waitnet

%files nfs
%_datadir/%parent/features/%child-nfs

%files cifs
%_datadir/%parent/features/%child-cifs

%files doc
%_docdir/%name

%changelog
* Sun Sep 01 2024 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt24
- added asciidoc sources of the reference guide

* Thu Mar 07 2024 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt23
- cifs and nfs: change order to apply defaults

* Wed Mar 06 2024 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt22
- resolv.conf is now copied during the liveboot-post.d stage

* Thu Feb 15 2024 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt21
- use $BC_ROOT instead of $rootmnt, it fixes race conditions
- core+interactive: daemon stop has been reworked (ALT #49126)
- core+interactive: deallocate TTY's at finish (ALT #49125)
- core: add cmdline parameter to limit steps failure
- pipeline steps has been synced whith upstream v2.42.0

* Fri Nov 17 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt20
- introduced a common default for setting timeouts
- altboot: fixed localdev module (ALT #48448)

* Tue Jul 18 2023 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt19
- bootchain/copyfile: fix unbound variable

* Wed Jul 12 2023 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt18
- bootchain-altboot: do'nt unset STAGENAME
- Display distribution independent dialogs
- bootchain-core: Pack config 'bootchain' from $(BOOTCHAIN_PATH)

* Mon Jul 10 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt17
- altboot: use TMPFS when ramdisk_size not set (ALT #42966)
- altboot: introduce new 'type:iso' sub-argument (ALT #42967)
- doc: expand the test suite by cases without ramdisk_size=
- core: pack optional config file /etc/sysconfig/bootchain
- interactive: pack optional file /etc/dialogrc.error

* Mon May 08 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt16
- altboot: fixed timeout event on slow image loading (ALT #44107)

* Fri May 05 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt15
- interactive: introduce new IM_fatal() API call (ALT #44108)
- switch to localdev boot method in any case
- don't turn on lowmem mandatory for 'live' stage

* Tue May 02 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt14
- interactive: don't use console for VT TTY's (ALT #41521)

* Sun Apr 30 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt13
- rebuilt with shellcheck 0.9.0

* Sun Apr 09 2023 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt12
- bootchain-altboot: use altboot forever by check logic (ALT #45787)
- bootchain-core: delay switching to localdev boot method after loop
- download: don't set NFS method when loading via HTTP (ALT #43970)
- liveboot: add check for init= in propagator mode (ALT #44061)

* Wed Aug 31 2022 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt11
- cifs, nfs: revert back PREFIX, it repairs work with overlays

* Fri Jun 10 2022 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt10
- cifs, nfs: set PREFIX to '/' (Closes: 42965)

* Sat Jan 29 2022 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt9
- rebuilt with shellcheck 0.8.0

* Tue Nov 16 2021 Ivan A. Melnikov <iv@altlinux.org> 0.1.5-alt8
- disable check on %%mips and riscv64 (shellcheck is not there yet)

* Tue Nov 02 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt7
- bootchain-altboot: try to load module 'loop' (ALT #41263).

* Thu Oct 21 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt6
- bootchain-doc: introduce initial testing suite
- bootchain-cifs: fix unbound variable usage

* Fri Oct 15 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt5
- fix netboot problem on very slow hardware (ALT #41078).
- fix screen blinks in ponder widget (ALT #41096).
- bootchain-core: adds support for the early console.
- bootchain-waitnet: increase timeout and fix messages.
- bootchain: reworked interaction with TTY's (ALT #41097).
- bootchain-altboot: adds special actions to the main menu.
- concatinate bootchain-loop back with the bootchained.
- bootchain-core: daemon and log renamed to chaind.
- bootchain-waitnet: bring up interfaces only once.

* Tue Sep 28 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt4
- prepare to upstreaming started for core, getimage and waitdev.
- many fixes for synchronize code and style with the upstream.
- bootchain-core: fixed addressation in resolve_target().
- bootchain-core: resolve_devname() function added.
- bootchain-altboot: introduce new step 'copyfile'.

* Thu Sep 23 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt3
- hot plug "on the fly" new network settings, if not defined.
- fixed problem with the first handshake by ftp protocol.
- fixed typo: show ISO name when netstart download image.

* Tue Sep 21 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt2
- download: rewrited reaction to returned http/ftp status codes.
- don't count whole disk drive with the same first partition.
- don't connect to default router anymore, only suggests.
- checksum: reboot the computer if checksum mismatch.
- waitnet: back to the main menu if network not ready.

* Sun Sep 19 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.5-alt1
- introduce bootchain-waitnet sub-module and function bc_reboot().
- major fixes and improvements around networking boot methods.

* Sun Sep 12 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.4-alt1
- major fixes and improvements around using RAM-disks and tmpfs.
- package documentation reorganized and separated.
- old feature code and logs complete removed.

* Mon Sep 06 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.3-alt1
- localdev: no more choice dialog, if found single device.
- altboot/get_free_ramdisk(): added hack for RT kernels.

* Sun Sep 05 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.2-alt1
- major fixes, prepare to p10 netinstall, sample config updated.

* Sat Sep 04 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.1-alt1
- localdev: label globbing and 'fuid' option support added.

* Mon Aug 30 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.0-alt1
- Experimental build for Sisyphus: WiP!

