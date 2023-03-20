Name: mkimage-profiles
Version: 1.5.3
Release: alt1

Summary: ALT based distribution metaprofile
License: GPLv2+
Group: Development/Other

Url: http://altlinux.org/m-p
Source: %name-%version.tar
Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch
BuildRequires: rsync

Requires: rsync git-core
Requires: time schedutils sfdisk
Requires: mkimage >= 0.2.5
Requires: mkimage-preinstall

# Recommends: graphviz qemu-img
# Recommends: isomd5sum

%define mpdir %_datadir/%name
%add_findreq_skiplist %mpdir/*.in/*

%def_with doc
%define docs $HOME/docs

Summary(ru_RU.UTF-8): метапрофиль дистрибутивов на базе Альт

%description
mkimage-profiles is a collection of bits and pieces useful for
distributions construction: it contains package lists, features,
and whole subprofiles (like "rescue" building block) for you
to choose from, and some ready-made image recipes as well.

Make no mistake: constructing distributions isn't just fun, it takes
a lot of passion and knowledge to produce a non-trivial one.  So m-p
(the short alias for mkimage-profiles) is complex too.  If you need
-- or want -- to make a few tweaks to an existing recipe, it might
be easier to comprehend the generated profile (aka builddir) which
contains only the needed subprofiles, script hooks and package lists
and is way more compact.

The main deliverable form for x86 is a (hybrid) ISO; virtual environment
template caches (OpenVZ/LXC) can be made either as well as VM disk images.

In short, setup hasher (http://en.altlinux.org/hasher) and here we go:
  cd %mpdir
  head README
  make syslinux.iso

But if you're into regular distro hacking and are not afraid of make
and modest metaprogramming (some code generation and introspection),
welcome to the metaprofile itself; read the docs and get the git:
%url (NB: these are mostly in Russian with translation on demand).

%description -l ru_RU.UTF-8
mkimage-profiles является собранием всего необходимого для
построения дистрибутивов и содержит списки пакетов, особенности
и целые субпрофили (вроде "кирпичика" rescue), из которых можно
выбирать требуемое; также включены и описания готовых образов.

Поймите правильно: создание дистрибутивов является занятием
не только интересным, но и требующим вдохновения и знаний
для получения нетривиального результата.  Если хочется или же
необходимо чуток поправить уже существующий "рецепт", может
быть проще разобраться в сгенерированном профиле (builddir),
который содержит только необходимые субпрофили, скрипты
и списки пакетов, являясь намного более компактным.

Основной формой результата на x86 является (гибридный) ISO-образ;
также возможно создавать шаблоны контейнеров OpenVZ/LXC и образы
дисков виртуальных машин.

Короче говоря, настройте hasher (http://altlinux.org/hasher) и:
  cd %mpdir
  head README
  make syslinux.iso

Но если разработка дистрибутивов становится обыденным делом
и не страшитесь make и чуточки метапрограммирования (немного
генерирования кода и интроспекции), добро пожаловать в сам
метапрофиль; гляньте документацию и забирайте git:
%url

%package doc
Summary: %name documentation
Group: Development/Documentation
%{?_with_doc:BuildRequires: java /proc}
%{?_with_doc:BuildRequires: asciidoc-a2x fop fonts-ttf-dejavu}
Summary(ru_RU.UTF-8): документация %name

%description doc
This package holds developer docs for %name
as a book in HTML and PDF formats.

%description -l ru_RU.UTF-8 doc
Этот пакет содержит документацию разработчика
для %name в форме книжки (HTML, PDF).

%prep
%setup

%build
%if_with doc
make BUILDDIR=%docs docs
%endif

%install
mkdir -p %buildroot{%mpdir,%_man7dir}
cp -a * %buildroot%mpdir
%if_with doc
mv %buildroot%mpdir/doc/mkimage-profiles.7 %buildroot%_man7dir/
%endif

%files
%mpdir/
%if_with doc
%_man7dir/*
%endif

%if_with doc
%files doc
%doc README
%doc QUICKSTART
%doc %docs/*
%endif

%changelog
* Mon Mar 20 2023 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- services: fix DEFAULT_SYSTEMD_USER_SERVICES_{DISABLE,ENABLE} support
- Initial feature live-install
- regular.mk: installation from live image by classic installer
- grub: add submenu for install live over network
- stage2: add option '--no-hardliks' to mksquashfs (Closes: 45329)
- initrd-{bootchain,propagator}: save initrd.mk, make-initrd to .disk/
- stage2,initrd-*: fix adding udev rules for named network interfaces
- mediacheck: check available implantisomd5 command
- install2: add mdadm to altinst
- features.in: drop armh-skit
- Include README of features to documentation; fix syntax & links in them

* Wed Feb 22 2023 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- wireless: removed crda, added firmware-wireless-regdb for all arch
  (thanks iv@)
- update package lists for riscv64 support (thanks iv@)
- init: drop stage2/image-scripts.d/91-systemd
- features.in: replace 50-bootargs script from bootloader to build-vm
- plymouth: drop use/plymouth/vm, cleanup
- stage2: drop 90-cleanup-drm script
- stage2: drop 50-udev script
- desktop+live: drop installer-feature-runlevel5-stage3
- live: do'nt mkdir /live.hooks
- x11-autologin: do nothing, if user altlinux does not exist
- init: drop live/image-scripts.d/50-var-run-fix (fix clash with rootfs script)
- init: not fix tmpfiles.d/*.conf
- efi: don't add refind, $$(EFI_SHELL), $$(EFI_BOOTLOADER) to rescue
- deflogin: create live user on first run
- dev: do not configure altlinux user in live (51-hasher)
- rescue: do'nt enable online repo
- grub, l10n: available only languages from $LOCALES in grub and installer
  (Closes: 45290)
- workstation, server, server-v: add latest commits

* Thu Jan 05 2023 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- efi: fix condition for use/efi/dtb
- mixin.mk: exclude gnome3-regular metapackage from regular-gnome3 target
- syslinux: try SYSLINUX_UI to none
- initrd-bootchain: use method disk for local boot
- net-ssh: Use two-pass method to install an authorized key for root (thanks
  manowar@)
- net: Allow to configure hostname via TARGET_HOSTNAME (thanks manowar@)

* Fri Dec 30 2022 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Updating lists for riscv64 (thanks iv@)
- check conditions of make for equality of variables with an empty value
- Set variable BRANCH, if not defined or empty; show $BRANCH
- Add STDOUT option to output log to stdout
- reports.mk: archive report with REPORT=2
- profile.mk: do not cleanup BUILDDIR, which is a symlink
- use/dev: Fix: Enable hasher-privd by default (thanks manowar@)
- regular.mk: set KFLAVOUR un-def for jeos in Sisyphus
- regular.mk: add drm kernel moules + firmware to initrd for all
- regular.mk: net-install is available for alles BRANCH
- grub: drop $linux_suffix in *.cfg
- grub: add ip=dhcp to bootargs in 88netinstall.cfg
- sound: use wireplumber instead pipewire-media-session for pipewire in
  Sisyphus (request by aris@)
- uboot: add u-boot-rpi3 to list
- image.in/functions.mk: protect the code from spontaneous execution
  (Closes: 44561)
- regular.mk: add use/efi/dtb
- education: add latest commits (from cas@)
- workstation: add latest commits (from sem@)
- alt-server: add latest commits (from jqt4)
- slinux: Add pam_gnome-keyring (from jqt4)

* Fri Dec 02 2022 Anton Midyukov <antohami@altlinux.org> 1.4.35-alt1
- alt-workstation-cloud: Use NetworkManager (from obirvalger@)
- install2: Don't cleanup /lib/modules/*/kernel/arch (from jqt4@)
- alt-server: add commits from jqt4@
- kworkstation: add commitd from zerg@
- grub: drop kazakh language support
- efi: add workaround for p10 branch to fix booting from a flash drive
- grub: do not copy locale, if not used gfxterm

* Mon Oct 10 2022 Anton Midyukov <antohami@altlinux.org> 1.4.34-alt1
- regular.mk: add to jeos 'xdriver=vesa' for Legacy, 'xdriver=fbdev' for EFI
- live: add use/live/runapp; live.mk: initial distro/live-blender with runapp
  (thanks mike@)
- build-ve: fix /run and /run/lock for ve images (thanks obirvalger@)
- rescue: add gostsum, use alt repo
- regular: use alt repo
- services: add logind services, add defaults for SYSTEMD services
- sound: add pipewire support
- x11: replace pulseaudio with pipewire for gnome3
- regular.mk: add gnome3-install
- alt-server: add commits from jqt4@
- server-v: add commits from andy@
- education: add commits from cas@
- workstation: add commits from sem@
- slinux: change light-locker to xfce4-screensaver (from jqt4@)

* Fri Sep 02 2022 Anton Midyukov <antohami@altlinux.org> 1.4.33-alt1
- grub: add nosplash for vnc install items
- base+rescue: add the required minimum applications for rescue
- firmware: add firmware-ast_dp501 to use/firmware/server
- Save rpm and srpm lists for chroots of subprofiles and main repo
- realtime.mk: add kernel-headers and devel packages for linuxcnc
- regular.mk: remove drm from jeos, enable nomodeset for jeos
- kworkstation: add commits from zerg@

* Mon Jul 25 2022 Anton Midyukov <antohami@altlinux.org> 1.4.32-alt1
- Add commits from zerg@ for kworkstation
- arm-rpi4: use/arm-rpi4/kernel available for aarch64 only
- regular-vm.mk: *-rpi targets available for aarch64 only
- Drop aarch64-tegra feature
- server (starterkit): drop php7, add php8.0, php8.1
- alt-server: drop un-def kernel from jqt4@
- alt-server, server-v: enable multipathd by default (from jqt4@, andy@)
- workstation: Use grubpcboot on i586 and x86_64 from sem@
- live.mk: update live-privacy.iso
- distributivs: update lists for support wine 7.13.1-alt1
- mixin-alt-server.mk: Add all kernel modules through MAIN_KMODULES
  instead list
- browser: replace seamonkey with firefox-esr for not x86 platforms

* Mon Jul 11 2022 Anton Midyukov <antohami@altlinux.org> 1.4.31-alt1
- arm-rpi4: add disabled option 'max_framebuffers=2' to config.txt
- init: add startup to use/init
- grub: add lowmem for nfs, samba methods to 88netinstall.cfg
- kernel: add the same modules to initrd for riscv64 as for aarch64
- regular-builder: add qemu support for non-ix86 platforms
- dev: add systemd-settings-disable-kill-user-processes to
  builder/live/systemd
- stage2: add copy devicetree in 95-copy-kernel, if $GLOBAL_COPY_DTB
  is set
- efi: add use/efi/dtb for copy devicetree for default kernel to ESP
  partition
- efi: not require EFI_FB kernel config support
- office: fix for riscv64, add abiword, gnumeric
- browser: made chromium available for x86_64, aarch64 only
- slinux 10.1 (thanks sem@)
- slinux: builded iso on riscv64
- slinux: enhancement for e2k (thanks mike@)
- fix lists for wine >= 7.6
- education: switch to use/browser/chromium
- alt-server: add latests commits (thanks jqt4@)
- alt-workstation: add latests commits (thanks sem@)

* Fri Jun 03 2022 Anton Midyukov <antohami@altlinux.org> 1.4.30-alt1
- create initrd.img with propagator instead full.cz
- base+network, base+nm: add missing iputils
- uboot: use relative pathes in extlinux.conf
- replace 'egrep' to 'grep -E', replace 'fgrep' to 'grep -F'
- install2: drop STAGE1_KMODULES virtualbox-additions, vmguest
- slinux, workstation: add latest commits from sem@
- education: add latest commits from cas@
- alt-server: add latest commits from jqt4@
- fix build slinux, workstation, education, alt-server on e2k

* Mon Apr 18 2022 Anton Midyukov <antohami@altlinux.org> 1.4.29-alt1
- stage2: fix 50-stage2-fs
- desktop+mate: replace package list to metapackages

* Mon Apr 11 2022 Anton Midyukov <antohami@altlinux.org> 1.4.28-alt1
- lib/profile.mk: install branding-$$(BRANDING)-release always after basesystem
- stage2: use propagator for c% BRANCH also
- install2, live: don't add priority base packages for these stage
- regular-vm.mk: replace blueberry to blueman for desktop regulars
- tar2fs: avoid losetup race (thanks mike@ and glebfm)
- kernel: drop std-pae kernel flavour
- stage2: add more modules to 50-stage2-net
- output errors Step 3 to BUILDLOG and on screen
- pkg.in/lists/Makefile: sort lists before copying
- regular.mk: drop feature robotics
- education: add latest commits from cas@
- education: mark task-edu-* as metapackages
- slinux, workstation: add latest commits from sem@
- education, slinux, workstation: add fixes for e2k from mike@

* Tue Mar 01 2022 Anton Midyukov <antohami@altlinux.org> 1.4.27-alt1
- regular.mk: add regular-xfce-install target
- regular.mk: add use/firmware to regular-builder
- regular.mk: set KFLAVOUR to un-def for regular-builder on x86_64, aarch64
- dev: fix links to repositories for ports Sisyphus in generated source lists
- vmguest: exclude xorg-dri-virtio for armh
- plymouth: require branding-@BRANDING@-graphics
- cleanup: add CLEANUP_LIVE_PACKAGES
- mixin.mk: add polkit-rule-admin-root to mixin/regular-desktop
- .gitignore: exclude .image.in/files/.empty
- initrd-propagator: not add empty layer
- build-vm: fix PATH to tar2fs with future mkimage
- lib/profile.mk, build-distro: save current commit
- vmguest: update stage1 modules list
- stage2: stage1 modules list update
- live.mk: add language submenu to grub-net-install
- mixin.mk: control libnss-role is disabled for regular-desktops
- kernel: exclude bcmwl kernel module, see ALT bug 41620
- kworkstation: add latest commits from zerg@
- kworkstation: add stage2 lists
- all distro: add use/stage2/ata

* Sun Feb 13 2022 Anton Midyukov <antohami@altlinux.org> 1.4.26-alt1
- vmguest: fix stage1/modules.d/50-vmguest
- sub.in/stage1: remove empty lines from kernel modules list
- drm: exclude ancient from full drm
- init: clear machine id (reported by obirvalger@)
- basealt.mk: specify network backend for netplan in alt-workstation-cloud
  (thanks obirvalger@)
- regular-lxqt, regular-xfce: replace light-locker to xscreensaver
- initrd-bootchain: simplify the procedure for adding modules to initrd

* Mon Feb 07 2022 Anton Midyukov <antohami@altlinux.org> 1.4.25-alt1
- stage2: add Baikal M support to 50-stage2-usb list
- server-v: use crio instead of docker with k8s (thanks 
  obirvalger@altlinux.org)
- dev: fix owner:group for /home/altlinux/*
- dev: add apt.conf's and source.list's for supported BRANCHES
  and ARCHES
- regular.mk: switch regular-builder on systemd, add regular-builder-sysv
- disable gpm.service for regular-builder
- add NetworkManager-tui to regular-builder
- grub: Add ability to override terminal from external grub.cfg on ESP
- init: do not add systemd-utils-standalone to use/init/sysv
  (fix build target with sysvinit on p9)
- uboot: update list for riscv64
- alt-server.mk: switch to grub-efi for bootloading iso on x86_64 UEFI
- init: not copy os-release in live, rescue (more not needed)
- reports.mk: do not abort, if not available rpm cache
- regular.mk: add use/tty for all regulars
- repo: add the ability to select a repository mirror (default http/alt)
- repo: setup mirror in install script 99-online-repo.sh
- e2k: fix bootloading iso from CD/DVD

* Thu Dec 30 2021 Anton Midyukov <antohami@altlinux.org> 1.4.24-alt1
- regular-server-sysv: add use/power/acpi/button
- fix META_VOL_ID for Starterkits
- drop kernel-modules-igb, kernel-modules-e1000e (report by boyarsh@)
- drop opensc, pccs-lite-openct package from base+smartcard,
  workstation/smartcard lists (report by klark@)
- made feature volumes available only for distro targets
- slinux 10.0 (thanks sem@, jqt4@, iv@)
- education.mk: drop targets rootfs for not supported platforms
- add +vmguest feature for vm/alt-education, vm/alt-workstation,
  vm/slinux and vm desktop regulars
- apt-conf: replace IMAGE_INIT_LIST to PINNED_PACKAGES
- vmguest: update vmguest modules list for support Hyper-v gen2

* Mon Dec 20 2021 Anton Midyukov <antohami@altlinux.org> 1.4.23-alt1
- lib/profile.mk: add branding-<BRANDING>-release to
  PACKAGES_REQUIRES_INITROOT (Closes: 41570)
- profile.mk: quote variables properly (thanks mike@)
- mixin.mk, regular.mk: do not +power for regulars with systemd
- syslinux: cleanup syslinux/.in/ always
- oem: fix BASE_BRANDING to THE_BRANDING
- pkg.in/lists: exclude varible NO_SORT_PACKAGES from package lists
- install2, vmguest: add xorg-dri-vmwgfx to vmware drivers (thanks
  zerg@)
- x11: update use/x11/xorg
- kernel: add kernel modules to initrd for framebuffer support
  on SBC (RPi3, RPi4, Sunxi, Rockchip, Tegra)
- basealt.mk: change firefox-esr to chromium for
  vm/alt-workstation-rpi (thanks jqt4@)

* Sat Dec 11 2021 Anton Midyukov <antohami@altlinux.org> 1.4.22-alt1
- Revert "arm-rpi4: change firefox-esr to chromium"
- Revert "regular-vm.mk, regular.mk: add wireless support"

* Fri Dec 10 2021 Anton Midyukov <antohami@altlinux.org> 1.4.21-alt1
- tar2fs: start partitions from 34 MiB for riscv64
- add support build iso for riscv64
- oem: not use/x11vnc for use/oem/vnc
- oem: not use/net-eth/dhcp for use/oem/vnc
- build.mk, params.txt: add parameter USE_QEMU
- bin/archdep-filter: implement multi-matching (thanks mike@)
- init: Set priority for systemd-utils-standalone package (use/init/sysv)
- init: add apt-conf-ignore-systemd for sysvinit
- install2: Set piority for installer-distro-common-stage2 package
- live: Set piority for livecd-installer-features package
- oem: Set piority for rootfs-installer-features package
- regular.mk, regular-vm.mk: add NetworkManager to regular-builder
- build-vm: add 20-grub-terminal script for setup terminal_output
- use/net-eth: add dhcp ipv4 only support for networkd (thanks lakostis@)
- features: add gitlab-runner (thanks lakostis@)
- arm-rpi4: copy actualy dtb for last kernel
- net: fix setup NetworkManager controlled with etcnet (fix typo in 50-net-nm)
- alt-server: add latest commits (thanks boyarsh@)
- alt-workstation: add latest commits (thanks sem@)
- slinux: add latest commits (thanks sem@)
- alt-education: add latest commits (thanks cas@)
- server-v: add latest commits (thanks shaba@)

* Mon Nov 15 2021 Anton Midyukov <antohami@altlinux.org> 1.4.20-alt1
- ve.mk: refactor those ve/lxc-* dups (thanks mike@)
- ve.mk: initial ve/lxc-builder (thanks mike@)
- ve.mk: refactor those ve/systemd-* dups
- x11: Add graphics card support for HiFive Unmatched (thanks jqt4@)
- x11: use/x11/amdgpu too when use/x11/3d (thanks mike@)
- e2k: more patches by mike@
- x11, lists/tagged: initial use/x11/xscreensaver
- net: fix build without etcnet
- l10n: add base+l10n tagged list
- Revert "regular.mk: add grub submenu 'Network installation'"
- grub: add submenu for stagename to netinstall.cfg
- alt-server: add latest commits (thanks boyarsh@)
- alt-workstation: add latest commits (thanks sem@)
- slinux: add latest commits (thanks sem@)
- alt-education: add latest commits (thanks cas@)
- server-v: add latest commits (thanks shaba@)
- virt/base.pkgs: drop libnss-resolve

* Mon Oct 18 2021 Anton Midyukov <antohami@altlinux.org> 1.4.19-alt1
- syslinux: fix broken 01-syslinux script in previous version 1.4.18
- regular-vm.mk, regular.mk: drop udev-rule-generator
- kernel: add rtw89 wifi kernel module for support Realtek RTL8852AE
  (thanks zerg@)
- install2: don't remove mmc kernel modules to allow USB 0bda:0129 cardreader
  (thanks zerg@)
- install2: do not cleanup cec and rc kernel modules (needed for amdgpu)
  (thanks zerg@)
- kernel/stage1: prevent to include nvidia to stage1 (thanks zerg@)
- drm: drop use/drm/stage2/nvidia target
- kworkstation: add latest commits from zerg@
- initrd-bootchain: add etwork interface naming udev rules
- initrd-bootchain: allow BOOTCHAIN_LOGFILE, BOOTCHAIN_LOG_VT to be reassigned
- build-vm: create initrd from a special config (/etc/initrd.mk.oem)
- kernel: add use/kernel/disable-usb-autosuspend
- mixin.mk: disable usb autosuspend for regular-x11
- kernel: add drivers/mfd drivers/clk to initrd for aarch64, armh
- grub: remove 'ip=dhcp' from netinstall.cfg
- isomd5sum: drop obsoletes feature
- build.mk: Do nothing with IMAGEDIR if $(DIRECT_TARGETS) is running
- init: Fix install /etc/os-release (thanks sem@)
- workstation: add latest commits from sem@
- slinux: add latest commits from sem@
- education: add latest commits from cas@

* Mon Sep 20 2021 Anton Midyukov <antohami@altlinux.org> 1.4.18-alt1
- If the BRANCH variable is not empty, and the BRANDING variable on
  the contrary is empty, then BRANDING is assigned to alt-starterkit.
- Revert commit "base+rescue: add eepm"
- Fixed conditions with variable BRANCH
- Drop STARTERKIT variable
- grub: add submenu "Network installation"
- Do not use udev-rule-generator-net in regulars/starterkits
- initrd-bootchain: Initial feature
- stage1: allow creating stage1 without stage2
- ntp: fix add fallbck THE_NTPD_SERVICE
- Makefile: check *_PACKAGES* variables as lists
- vmguest: fix build with use/vmguest/kvm/x11 for BRANCH=p9
- grub, syslinux: replace 'splash=0' to 'nosplash' in rescue
- drop features: aarch64-dbm, armh-cubox, armh-dovefb, nexus7,
  armh-tegra, armh
- build-vm: add FEATURES and MODULES_TRY_ADD from /etc/initrd.mk
- syslinux: Generate isolinux.cfg for any BOOTLOADER
- build-vm, stage2: set GLOBAL_HSH_PROC=1
- vm.mk: Add sr_mod to initrd modules for vm/cloud-system
  (thanks obirvalger@)

* Tue Aug 31 2021 Anton Midyukov <antohami@altlinux.org> 1.4.17-alt1
- Add COMMON_LISTS variable support by analogy COMMON_PACKAGES.
  Fix use/efi (the list 'base+efi' was not added to rescue, base,
  live)
- kernel: add drivers/soc to VM_INITRDMODULES (needed for rk3399
  support)
- uboot: Added HiFive Unmatched support (thanks jqt4@)
- lib/profile.mk: do not abort build with CHECK=0, if unavailable ARCH
- base+rescue: add eepm (request by lav@)
- stage2: update 50-stage2-sbc-aarch64. Use directories instead of
  specifying modules 

* Mon Aug 23 2021 Anton Midyukov <antohami@altlinux.org> 1.4.16-alt1
- efi: add mokutil, pesign to COMMON_PACKAGES (for Secure Boot,
  requset by nikel@)
- build.mk: fix build without APTCONF parameter
- image.in/Makefile: fix save-profile (exclude .work)
- bin/metadep-expander: fix output redirection to /dev/null
- bin/metadep-expander: do not abort build, if metapackage not available
- adapt bin/check-pkg-list for mkimage-profiles. Use for build without
  parameter CHECK=0
- reports.mk: fix build with REPORT=1, CHECK=1 and undefined DEBUG
- test.mk: add package availability test in all package lists.
  Usage: make CHECK=1 DEBUG=1 check-all-pkglists.iso
- add missing README for features: mipsel-bfk3, mipsel-mitx, lxc
- ve.mk, vm.mk: replace systemd to use/init/systemd (request by obirvalger@)
- net: Add networkd/resolved and networkd/resolved-stub subfeatures
  (thanks obirvalger@)
- education, slinux, workstation: fix build for non e2k ARCH.
  See also commit 'e2k: add a stub for non e2k%'
- education, slinux, workstation: add use/arm-rpi4 to vm/ targets
  on aarch64, armh
- fix build vm/alt-workstation-cloud
- fix build vm/regular-cnc-rt-efi
- drop armh.conf, target use/slinux/arm and linux-arm list
- cleanup unavailable packages for p10 from package lists

* Tue Aug 10 2021 Anton Midyukov <antohami@altlinux.org> 1.4.15-alt1
- reports.mk: convert targets.svgz to pdf, if rsvg-convert is available
- reports.mk: save distcfg.mk to report directory, when check build (CHECK=1)
- vmguest: add xorg-drv-spiceqxl, xorg-dri-virtio to kvm/x11
- grub: add missing '--id' for items menu grub.cfg
- grub: not set GRUB_UI for unsupported ARCHES
- grub: fix selection by default install2, if GRUB_DEFAULT is not set
- live.mk: add new target grub-ui.iso
- build.mk: initial .work/aptbox immediately after configuring the profile
- pkg.in: Add @META suffix support for pkglist items
- tar2fs: Add offset 16 MiB for singleboard PC support
- tar2fs: Mark root partition as bootable if extlinux.conf is present
- arm-rpi4: use mode nouboot for rpi kernel only
- regular-vm.mk: build universal images for aarch64/armh
- net: use/net/nm/native not require use/net/nm
- net: enable udevd-final for etcnet
- regular.mk: not use grupcboot and multiple kernels for boot ISO for
  starterkit's
- firmware: add firmware-alsa-sof to use/firmware/laptop (thanks cas@)
- x11: drop primus
- init: enable udevd-final for sysvinit
- pack: add squash to the list of ve archive formats (thanks glebfm@)
- add lxc-guest feature (thanks glebfm@)
- arm-rpi4: not use specyphic features for RPi4 in use/arm-rpi4
- regular-vm.mk: set VM_SIZE to 7 GiB
- realtime.mk: disable plymouth
- e2k fixes for alt-workstation, slinux
- add latest commits for alt-server (thanks boyarsh@)
- add latest commits for alt-workstation (thanks sem@)

* Mon Jul 05 2021 Anton Midyukov <antohami@altlinux.org> 1.4.14-alt1
- reports.mk: fix launch together with the CHECK option
- Makefile: Create a report directory at each iteration
- Makefile, profile.mk: not create temp directories with DIRECT_TARGETS
- log.mk:  Don't write anything to build.log when DIRECT_TARGETS
- Do not rsync .gitignore to build directories
- regular-vm.mk: add deepin rootfs targets
- engineering: use metapackage instead list
- dev, kernel: not set BIGRAM to std-def
- regulars: require the entire metapackage chain
- grub: Updating 95fwsetup_efi.cfg. Replace "System setup" to
  "UEFI Firmware Settings"
- build-vm: overwrite existing output file
- workstation: 9.2 rc1
- server-v: 9.2 rc1

* Mon Jun 07 2021 Anton Midyukov <antohami@altlinux.org> 1.4.13-alt1
- add parametr's BRANCH, NO_SYMLINK
- fix usage AUTOCLEAN parameter with DEBUG
- use variable REPORT from ~/.mkimage/profiles.mk
- move logs to reports directory, if enable REPORT
- fix build pdf documentation after clean
- update documetation
- build starterkits from regular.mk profile
- cnc-rt: uses lxqt DE instead of lxde
- cnc-rt: Not add efi=runtime to EFI_BOOTARGS
- kernel: add missing virtio kernel modules to VM_INITRDMODULES
- server-v: 9.2 beta
- workstation: 9.2 beta
- education: added last commits

* Fri May 21 2021 Anton Midyukov <antohami@altlinux.org> 1.4.12-alt1
- fix VM_SAVE_TARBALL parameter support
- grub: save ang read default menu item (thanks jqt4@, sin@)

* Mon May 17 2021 Anton Midyukov <antohami@altlinux.org> 1.4.11-alt1
- build-vm: Add ability to build .img.xz (thanks sem@)
- reports.mk: optimiztion for generate rpm and srpms lists (thanks mike@)
- reports.mk: generate targets.svgz instead targets.png
- add VM_SAVE_TARBALL parameter
- add MKIMAGE_PREFIX parameter
- kernel: optimization use/kernel/initrd-setup
- set STAGE1_INITRD_BOOTARGS in initrd-propagator
- slinux 9.1
- education 9.2

* Mon Apr 26 2021 Anton Midyukov <antohami@altlinux.org> 1.4.10-alt1
- build propagator and copy kernel in mkimage-profiles
- copy kernel to boot/ directory on iso image
- multiple kernels support for iso with grub
- add support initrd.img instead full.cz in stage1 with grub, syslinux
- use method:cdrom,fuid instead method:disk,uuid in uuid-iso feature
  (thanks jqt4@)
- vmguest: Drop virtualbox-addition kernel modules
- fix make distclean
- reports.mk: Generate rpm and srpms lists
- add hdt for grub-pc (floppy disk image)
- add items boot with local drive for grub-pc (iso)
- oem: use/deflogin/root
- add switch sddm|lightdm for kde5
- education 9.2 beta

* Mon Apr 05 2021 Anton Midyukov <antohami@altlinux.org> 1.4.9-alt1
- build-distro: BOOT_TYPE = BOOTLOADER
- Add the ability to override BOOTLOADER
- grub: restrict graphics mode to architectures i586, x86_64, aarch64
- Add grub-efi support for riscv64 (thanks arei@)
- New feature uuid-iso for create UUID for ISO image (thanks jqt4@)
- Disable sort subprofiles (build stage1 first)
- fonts: Set SYSTEM_FONTS for use/fonts/install2 again
- stage2: Add cmac.ko for use SMB2 and newer
- live.mk: Add distro/grub, fix allowed targets for architectures
- init: Add mount-efivars for sysvinit
- alt-server: fix missing packages in p9
- education: pull new commits

* Mon Mar 15 2021 Anton Midyukov <antohami@altlinux.org> 1.4.8-alt1
- Set BOOT_TYPE, BOOTLOADER to efiboot for aarch64
- 'Simply Linux 9.1 (beta)' commits contained (Thanks sem@)
- mipsel-bfk3: Switch to 5.4 kernel, other changes (Thanks iv@)
- oem: Add use/oem/distro
- uboot: Drop BOOTARGS cma=192M
- net: Added switch between NetworkManager (etcnet) and NetworkManager (native)
  Assigned by default NetworkManager (etcnet)
- x11: Not add use/drm to use/x11
- efi: Add check EFIVAR_FS option
- sound/base: Add test-audio
- armh-mcom02: set screen resolution 1366x768
- realtime.mk: Refactoring, drop live with session support
- engineering.mk: Switch to MATE
- x11: Reduce size of kde5
- regular-vm.mk: Set as default un-def kernel flavour, drop lts kernel flavour

* Mon Feb 15 2021 Anton Midyukov <antohami@altlinux.org> 1.4.7-alt1
- Add kernel modules for support Raspberry Pi 4 (mainline kernel)
- grub: Markup configuration files for translation (thanks Ivan Razzhivin)
- grub: Use META_VOL_ID for @distro@ instead RELNAME if available
  (ALT bug 39611, 39612)
- tar2fs: Enable secure-boot support for x86_64, add riscv64 support
- Add initrd features for rootfs: kbd rdshell rootfs
- desktop+mate: list is fixed,  as removed metapackage mate-default
- grub: use single boot/grub/grub.cfg in ISO
- Add support grub-pc for bootloading ISO (experimentall)
- Removed kernel modules that haven't been built for a long time

* Mon Jan 25 2021 Anton Midyukov <antohami@altlinux.org> 1.4.6-alt1
- deepin: add Network Manager applet
- engineering: initial as distributiv
- efi: fixed check modules for kernel-image >= 5.10
- oem: fixed calculation of required free space for installing additional
  packages
- oem: not use git in 60-oem-install.mk
- regular: do not default to mounting anything found (thanks mike@)
- rescue: added save session mode support for efi
- tar2fs: Disable os-probe at the time of grub installation
- xfce-sysv: add gnome-disks (suggested by Speccyfighter)

* Mon Dec 07 2020 Anton Midyukov <antohami@altlinux.org> 1.4.5-alt1
- Initial feature drm, added Nvidia proprietary driver support
- Adapted use/repo/main for vm/ targets
- oem: Added ability to set alterator-setup steps
- oem: Added use/oem/install target
- wireless: Update kernel modules for wi-fi
- armh-skit: Initial feature
- grub: Drop multiple kernel support
- stage1: Also add STAGE1_KMODULES
- bootloader, plymouth: Add splash to BASE_BOOTARGS only when using
  the plymouth feature
- tar2fs: Not add EFI partition for all aarch64, armh, but only for
  those with grub-efi bootloader or VM_BOOTTYPE variable set
- regular.mk, x11: Initial regular-deepin.iso
- arm-rpi4: Cleanup
- grub: Added EFI_BOOTARGS into BOOT/EFI/grub.cfg

* Mon Oct 26 2020 Anton Midyukov <antohami@altlinux.org> 1.4.4-alt1
- apply server-v 9.1 release patches (thanks shaba@)
- apply e2k patches (mike@)
- mipsel-bfk3: Fix /etc/fstab generation (thanks iv@)
- Rename all RPMs to canonical names before genbasedir (thanks boyars@)
- gnustep: Fix build
- oem: Add use/oem/no-cleanup
- deflogin: Now you can add a user with specific uid, gid and so on

* Fri Sep 25 2020 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- education: added commits skipped when rebase was done
- wireless: added rtl8812au driver
- partially added commits from the kworkstation
- added e2k patches (mike@)
- tar2fs: set UUID in extlinux.conf, if exist
- vm.mk: simplified conditions for choosing a bootloader depending on arch
- added a couple of commits (obirvalger@)
- added commits for mipsel support (iv@)
- added the ability to override fonts (needed kworkstation)
- added target use/live/no-cleanup which is needed to disable cleanup
  documentation and rpmdb; is needed for live kworkstation without
  livecd-install
- fixed adding empty variable in "use/efi"
- don't cleanup dri modules from install2 (needed for support glamore)
- metadata/lib/50-metadata.mk: space-prefixed strings handling fixed (boyarsh@)

* Tue Sep 01 2020 Anton Midyukov <antohami@altlinux.org> 1.4.2-alt1
- x11: Added missing xorg-dri-armsoc for armh
- oem: Added rootfs-installer-features
- server-v: Added more commits by andy@, shaba@
- Set default timeout 60 seconds for syslinux and grub
- Set default item to install2 for syslinux and grub
- main.mk: Added vm/, ve/ targets into everything target
- Extended e2k support in distributions (thanks mike@)
- education: fix build and install

* Mon Aug 17 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- Revert commit for support multiple kernel in iso image.

* Mon Aug 17 2020 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New official maintainer antohami@ (blessed by mike@)
- Added grub config file generator for iso images
  (thanks shaba@)
- Expanded support for USB controllers and SD card readers
- Added support for booting on single-board Raspberry Pi 3 and 4
  in EFI mode (u-boot or edk2)
- Added grub-efi bootloader support for rootfs images
- Merged with branches for Workstation, Education,
  Simply Linux, Server, Server-V distributions
- Added a starterkit build profile with a real-time kernel (live)
- Added riscv64 platform support (thanks arei@)
- rootfs: support headless boot via alterator-setup-vnc (thanks arei@)

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1.3.15-alt1
- autoinstall fix (sin@)
- Baikal-M support, @ARM, elogind removal, other tweaks (antohami@)
- factored out archdep-filter, pulled in check-pkg-list (me)

* Mon Oct 21 2019 Michael Shigorin <mike@altlinux.org> 1.3.14-alt1
- make bails out on single image build error, see also make -k (iv@)
- mipsel support (iv@, antohami@)
- regular-vm.mk, refactoring, cleanups (antohami@)

* Mon Sep 16 2019 Michael Shigorin <mike@altlinux.org> 1.3.13-alt1
- recovery.tar support (iv@)
- mixin/mixin deps, aarch64 EFI, mcom02 & jetson nano support,
  multikernel & portability fixes, refactoring & cleanups (antohami@)
- document STAGE1_MODLISTS (me)

* Mon Aug 19 2019 Michael Shigorin <mike@altlinux.org> 1.3.12-alt1
- ppc64le support (glebfm@)
- build-vm hacked to build tarballs too (iv@ et al)
- p8.mk: dropped; along with other cleanups/fixups (antohami@)

* Tue Jul 09 2019 Michael Shigorin <mike@altlinux.org> 1.3.11.1-alt1
- x11: reverted vulkan changes (need more testing)

* Mon Jul 08 2019 Michael Shigorin <mike@altlinux.org> 1.3.11-alt1
- pkg.in/profiles subdirs support (shaba@)
- repo fixup regarding target arch (obirvalger@)
- switch back to yandex mirror by default,
  portability fixes, refactoring, cleanups (antohami@)
- x11 amdgpu/radeon and dm fixups, vmguest refactoring (me)

* Mon Jun 17 2019 Michael Shigorin <mike@altlinux.org> 1.3.10-alt1
- add server-v profile, drop groups/openstack (shaba@)

* Mon Jun 10 2019 Michael Shigorin <mike@altlinux.org> 1.3.9-alt1
- uboot feature, bootloader refactoring, etc (antohami@)
- cleanlog factored out from reports.mk (me)

* Mon Jun 03 2019 Michael Shigorin <mike@altlinux.org> 1.3.8-alt1
- p9.mk, office feature and other enhancements/fixes (antohami@)
- education (cas@)
- simply (sem@)
- minor tidbits and major merge-up (me)

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 1.3.7-alt1
- docker, vm, browser fixups (obirvalger@)
- elogind support, refactoring, cleanups (antohami@)
- a couple more improvements (me)

* Mon Apr 01 2019 Michael Shigorin <mike@altlinux.org> 1.3.6-alt1
- no joke!

* Mon Mar 04 2019 Michael Shigorin <mike@altlinux.org> 1.3.5-alt1
- Spring 2019 patch queue cleanup
  + antohami@, jqt4@, iv@, obirvalger@, zerg@, me
  + tar2fs fixes for mipsel, qemu etc
  + lots of pkglist updates

* Mon Jan 14 2019 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- new 2019 year release ;-)
- tar2fs related security fix (iv@) iff sudo's been configured
- use/x11/dm rework (antohami@)
- archfixes (antohami@, iv@)
- pre-p8 bits cleanup (me)

* Mon Dec 24 2018 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- aarch64/armh portability fixups (antohami@)
- grub-based vm images (shaba@)
- even smaller images (glebfm@)
- lxc/lxd lists/feature/image (dans@)
- updated robotics lists/image (dd@)
- e2k: 801/101/jeos tweaks (me)

* Mon Dec 10 2018 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- sisyphus drops

* Mon Nov 05 2018 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- current fixes and tweaks

* Mon Oct 15 2018 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1
- pre-p9 sisyphus: fixes, drops and just two kludges

* Mon Aug 13 2018 Michael Shigorin <mike@altlinux.org> 1.2.21-alt1
- volumes feature; fixups

* Mon Aug 06 2018 Michael Shigorin <mike@altlinux.org> 1.2.20-alt1
- isoboot/isodata; apt-conf feature; dual-seat e801

* Mon Jul 23 2018 Michael Shigorin <mike@altlinux.org> 1.2.19-alt1
- alt-workstation: x86 (sem@), e2k (me)

* Mon Jul 16 2018 Michael Shigorin <mike@altlinux.org> 1.2.18-alt1
- ldm feature (lakostis@)

* Mon Jun 25 2018 Michael Shigorin <mike@altlinux.org> 1.2.17-alt1
- e2k & profiles

* Mon Jun 11 2018 Michael Shigorin <mike@altlinux.org> 1.2.16-alt1
- starterkits-20180612

* Mon May 28 2018 Michael Shigorin <mike@altlinux.org> 1.2.15-alt1
- fixup release

* Mon May 21 2018 Michael Shigorin <mike@altlinux.org> 1.2.14-alt1
- pkgpriorities feature (manowar@)
- extended e2k support

* Mon Apr 23 2018 Michael Shigorin <mike@altlinux.org> 1.2.13-alt1
- antohami@'s improvements

* Mon Mar 19 2018 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- @IA32, @X86

* Mon Mar 12 2018 Michael Shigorin <mike@altlinux.org> 1.2.11-alt1
- starterkits-20180312

* Mon Feb 19 2018 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- antohami@'s fixups

* Mon Feb 12 2018 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- antohami@'s release

* Mon Feb 05 2018 Michael Shigorin <mike@altlinux.org> 1.2.8-alt1
- regular fixes

* Mon Jan 22 2018 Michael Shigorin <mike@altlinux.org> 1.2.7-alt1
- 2018: better sound feature (antohami@)

* Mon Dec 11 2017 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- starterkits-20171212

* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 1.2.5-alt1
- qcow2c

* Mon Nov 20 2017 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- opennebula-systemd

* Mon Sep 25 2017 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- p8+

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- regular-engineering

* Mon Aug 21 2017 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- seven years ago...

* Mon Aug 07 2017 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- e2k

* Mon Jul 31 2017 Michael Shigorin <mike@altlinux.org> 1.1.110-alt1
- lxde-sysv

* Mon Jun 12 2017 Michael Shigorin <mike@altlinux.org> 1.1.109-alt1
- starterkits-20170612

* Mon Apr 24 2017 Michael Shigorin <mike@altlinux.org> 1.1.108-alt1
- yandex.mirror

* Mon Apr 03 2017 Michael Shigorin <mike@altlinux.org> 1.1.107-alt1
- serial improvements

* Mon Mar 13 2017 Michael Shigorin <mike@altlinux.org> 1.1.106-alt1
- starterkits-20170312

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 1.1.105-alt1
- disable git hooks (glebfm@)

* Mon Feb 06 2017 Michael Shigorin <mike@altlinux.org> 1.1.104-alt1
- [[vncinst]] fixed

* Mon Jan 30 2017 Michael Shigorin <mike@altlinux.org> 1.1.103-alt1
- rescue -= bootsplash

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 1.1.102-alt1
- 2017

* Mon Dec 12 2016 Michael Shigorin <mike@altlinux.org> 1.1.101-alt1
- starterkits-20161212

* Mon Dec 05 2016 Michael Shigorin <mike@altlinux.org> 1.1.100-alt1
- preparing for starterkits

* Mon Nov 14 2016 Michael Shigorin <mike@altlinux.org> 1.1.99-alt1
- xfce-sysv
- preparing...

* Mon Oct 31 2016 Michael Shigorin <mike@altlinux.org> 1.1.98-alt1
- preparing for workstation 8.1

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 1.1.97-alt1
- regular tweaks

* Mon Sep 12 2016 Michael Shigorin <mike@altlinux.org> 1.1.96-alt1
- starterkits-20160912

* Mon Aug 15 2016 Michael Shigorin <mike@altlinux.org> 1.1.95-alt1
- s/basealt/alt/g

* Mon Jun 27 2016 Michael Shigorin <mike@altlinux.org> 1.1.94-alt1
- workstation

* Mon Jun 13 2016 Michael Shigorin <mike@altlinux.org> 1.1.93-alt1
- starterkits-20160612

* Mon May 30 2016 Michael Shigorin <mike@altlinux.org> 1.1.92-alt1
- server-openstack

* Mon May 23 2016 Michael Shigorin <mike@altlinux.org> 1.1.91-alt1
- nvidia/nouveau rehash
- overlayfs support (lakostis@)

* Tue May 03 2016 Michael Shigorin <mike@altlinux.org> 1.1.90-alt1
- starterkits-20160429

* Mon Apr 25 2016 Michael Shigorin <mike@altlinux.org> 1.1.89-alt1
- preparing for p8 starterkits

* Mon Apr 11 2016 Michael Shigorin <mike@altlinux.org> 1.1.88-alt1
- pkg.in/profiles

* Mon Mar 14 2016 Michael Shigorin <mike@altlinux.org> 1.1.87-alt1
- starterkits-20160312

* Mon Feb 29 2016 Michael Shigorin <mike@altlinux.org> 1.1.86-alt1
- junior

* Mon Feb 15 2016 Michael Shigorin <mike@altlinux.org> 1.1.85-alt1
- regular-jeos-ovz

* Mon Feb 08 2016 Michael Shigorin <mike@altlinux.org> 1.1.84-alt1
- %name(7) :)

* Mon Jan 25 2016 Michael Shigorin <mike@altlinux.org> 1.1.83-alt1
- openssh 7.x (see also #31716)

* Mon Jan 11 2016 Michael Shigorin <mike@altlinux.org> 1.1.82-alt1
- firmwarez

* Mon Dec 07 2015 Michael Shigorin <mike@altlinux.org> 1.1.81-alt1
- regular fixes

* Mon Nov 30 2015 Michael Shigorin <mike@altlinux.org> 1.1.80-alt1
- pre-starterkit cleanups

* Mon Nov 16 2015 Michael Shigorin <mike@altlinux.org> 1.1.79-alt1
- faked workaround

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.78-alt1
- regular-enlightenment

* Mon Oct 19 2015 Michael Shigorin <mike@altlinux.org> 1.1.77-alt1
- webkiosk improvements

* Mon Oct 12 2015 Michael Shigorin <mike@altlinux.org> 1.1.76-alt1
- no more GREP_OPTIONS

* Mon Sep 28 2015 Michael Shigorin <mike@altlinux.org> 1.1.75-alt1
- systemd-specific hook for installer (solo@)

* Mon Sep 14 2015 Michael Shigorin <mike@altlinux.org> 1.1.74-alt1
- starterkits-20150912

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 1.1.73-alt1
- im feature

* Mon Aug 31 2015 Michael Shigorin <mike@altlinux.org> 1.1.72-alt1
- starterkits alpha

* Mon Aug 10 2015 Michael Shigorin <mike@altlinux.org> 1.1.71-alt1
- docs feature

* Mon Jul 20 2015 Michael Shigorin <mike@altlinux.org> 1.1.70-alt1
- check KFLAVOURS

* Mon Jun 29 2015 Michael Shigorin <mike@altlinux.org> 1.1.69-alt1
- yet another systemd- tweak

* Mon Jun 22 2015 Michael Shigorin <mike@altlinux.org> 1.1.68-alt1
- LIVE_CLEANUP_KDRIVERS actually works

* Mon Jun 08 2015 Michael Shigorin <mike@altlinux.org> 1.1.67-alt1
- minor post-tweaks

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 1.1.66-alt1
- remote rescue

* Mon May 04 2015 Michael Shigorin <mike@altlinux.org> 1.1.65-alt1
- archdep pkglists

* Mon Apr 20 2015 Michael Shigorin <mike@altlinux.org> 1.1.64-alt1
- modularized stage1 modules list

* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 1.1.63-alt1
- support USB3, ACPI suspend

* Mon Mar 16 2015 Michael Shigorin <mike@altlinux.org> 1.1.62-alt1
- starterkits-20150312

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.61-alt1
- EFI_BOOTARGS

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 1.1.60-alt1
- vmguest, install2: refactoring

* Mon Feb 23 2015 Michael Shigorin <mike@altlinux.org> 1.1.59-alt1
- regular rebase

* Mon Feb 16 2015 Michael Shigorin <mike@altlinux.org> 1.1.58-alt1
- vagrant feature (closes: #28553)

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.57-alt1
- fix the lists copying fix

* Mon Feb 02 2015 Michael Shigorin <mike@altlinux.org> 1.1.56-alt1
- fix lilo check for vm images

* Mon Jan 26 2015 Michael Shigorin <mike@altlinux.org> 1.1.55-alt1
- lists copying fixed

* Mon Jan 05 2015 Michael Shigorin <mike@altlinux.org> 1.1.54-alt1
- live: don't force localboot

* Mon Dec 15 2014 Michael Shigorin <mike@altlinux.org> 1.1.53-alt1
- starterkits-20141212

* Mon Nov 17 2014 Michael Shigorin <mike@altlinux.org> 1.1.52-alt1
- docs: "7.0+" (closes: #30474)
- l10n feature

* Mon Nov 10 2014 Michael Shigorin <mike@altlinux.org> 1.1.51-alt1
- current updates

* Mon Oct 27 2014 Michael Shigorin <mike@altlinux.org> 1.1.50-alt1
- minor tweaks

* Mon Oct 13 2014 Michael Shigorin <mike@altlinux.org> 1.1.49-alt1
- pkglist updates

* Mon Sep 29 2014 Michael Shigorin <mike@altlinux.org> 1.1.48-alt1
- (sysv)init: exclude systemd explicitly

* Mon Sep 22 2014 Michael Shigorin <mike@altlinux.org> 1.1.47-alt1
- kpackages() argswap

* Mon Sep 15 2014 Michael Shigorin <mike@altlinux.org> 1.1.46-alt1
- regular fixes

* Mon Sep 01 2014 Michael Shigorin <mike@altlinux.org> 1.1.45-alt1
- starterkits alpha

* Mon Aug 18 2014 Michael Shigorin <mike@altlinux.org> 1.1.44-alt1
- connman fixup

* Mon Aug 04 2014 Michael Shigorin <mike@altlinux.org> 1.1.43-alt1
- fixed package build

* Mon Jul 28 2014 Michael Shigorin <mike@altlinux.org> 1.1.42-alt1
- current bits

* Mon Jul 07 2014 Michael Shigorin <mike@altlinux.org> 1.1.41-alt1
- post-214 fixups

* Mon Jun 30 2014 Michael Shigorin <mike@altlinux.org> 1.1.40-alt1
- systemd-214

* Mon Jun 16 2014 Michael Shigorin <mike@altlinux.org> 1.1.39-alt1
- starterkits-20140612

* Mon Jun 02 2014 Michael Shigorin <mike@altlinux.org> 1.1.38-alt1
- mksquashfs 4.3 support

* Mon May 26 2014 Michael Shigorin <mike@altlinux.org> 1.1.37-alt1
- use/browser

* Mon May 19 2014 Michael Shigorin <mike@altlinux.org> 1.1.36-alt1
- regular-lxqt

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 1.1.35-alt1
- yet another rescue week

* Mon May 05 2014 Michael Shigorin <mike@altlinux.org> 1.1.34-alt1
- remember Odessa

* Mon Apr 28 2014 Michael Shigorin <mike@altlinux.org> 1.1.33-alt1
- net-eth tweaks

* Mon Apr 21 2014 Michael Shigorin <mike@altlinux.org> 1.1.32-alt1
- regular-rescue week

* Mon Apr 14 2014 Michael Shigorin <mike@altlinux.org> 1.1.31-alt1
- live: refactoring
- forensics mode

* Mon Apr 07 2014 Michael Shigorin <mike@altlinux.org> 1.1.30-alt1
- robotics support

* Mon Mar 31 2014 Michael Shigorin <mike@altlinux.org> 1.1.29-alt1
- mediacheck feature

* Mon Mar 24 2014 Michael Shigorin <mike@altlinux.org> 1.1.28-alt1
- install2: more cleanups

* Mon Mar 17 2014 Michael Shigorin <mike@altlinux.org> 1.1.27-alt1
- don't insist on k-m-r8168
- codebase deduplication

* Mon Mar 10 2014 Michael Shigorin <mike@altlinux.org> 1.1.26-alt1
- docs week
- deflogin: empty ROOTPW explicitly ignored (potential security fix)

* Mon Mar 03 2014 Michael Shigorin <mike@altlinux.org> 1.1.25-alt1
- regular updates

* Mon Feb 10 2014 Michael Shigorin <mike@altlinux.org> 1.1.24-alt1
- service bridge

* Mon Feb 03 2014 Michael Shigorin <mike@altlinux.org> 1.1.23-alt1
- live, net*, syslinux fixes (see also #26608)

* Mon Jan 27 2014 Michael Shigorin <mike@altlinux.org> 1.1.22-alt1
- ahci kludge (see #29705) :(

* Mon Jan 20 2014 Michael Shigorin <mike@altlinux.org> 1.1.21-alt1
- rescue tweaks

* Mon Jan 13 2014 Michael Shigorin <mike@altlinux.org> 1.1.20-alt1
- support for CIFS installation method (sin@)
- glibc-locales for regular images (closes: #29693)

* Mon Dec 30 2013 Michael Shigorin <mike@altlinux.org> 1.1.19-alt1
- regular fixes

* Mon Dec 23 2013 Michael Shigorin <mike@altlinux.org> 1.1.18-alt1
- efi updates

* Mon Dec 16 2013 Michael Shigorin <mike@altlinux.org> 1.1.17-alt1
- refind branding

* Mon Dec 09 2013 Michael Shigorin <mike@altlinux.org> 1.1.16-alt1
- e18

* Mon Dec 02 2013 Michael Shigorin <mike@altlinux.org> 1.1.15-alt1
- regular fixups

* Mon Nov 25 2013 Michael Shigorin <mike@altlinux.org> 1.1.14-alt1
- important bugfix: THE_PACKAGES weren't getting through to .base
- regular-sysv-tde related churn

* Mon Nov 04 2013 Michael Shigorin <mike@altlinux.org> 1.1.13-alt1
- rescue friday

* Mon Oct 21 2013 Michael Shigorin <mike@altlinux.org> 1.1.12-alt1
- live-builder update

* Mon Oct 14 2013 Michael Shigorin <mike@altlinux.org> 1.1.11-alt1
- luks better

* Mon Sep 30 2013 Michael Shigorin <mike@altlinux.org> 1.1.10-alt1
- regular tweaks

* Mon Sep 23 2013 Michael Shigorin <mike@altlinux.org> 1.1.9-alt1
- regular fixes

* Mon Sep 16 2013 Michael Shigorin <mike@altlinux.org> 1.1.8-alt1
- armh/p7/ve fixes

* Mon Aug 26 2013 Michael Shigorin <mike@altlinux.org> 1.1.7-alt1
- minor fixes

* Mon Aug 12 2013 Michael Shigorin <mike@altlinux.org> 1.1.6-alt1
- vm-net retired

* Mon Aug 05 2013 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- armh related fixes

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 1.1.4-alt1
- assorted fixups

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- armh fixes and tweaks

* Mon Jul 15 2013 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- control and sound features

* Mon Jul 01 2013 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- cuboxism

* Mon Jun 17 2013 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.x branch: public alpha development status
  + new subprofile: rootfs
  + new features: armh*, deflogin, init, services
  + refactored features: build-*, efi, fonts, live, x11*
  + tar2vm got rewritten as tar2fs, gained ARM support
- minor spec metadata update

* Mon Jun 17 2013 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0

* Mon Jun 10 2013 Michael Shigorin <mike@altlinux.org> 0.9.16-alt1
- 1.0pre

* Mon May 27 2013 Michael Shigorin <mike@altlinux.org> 0.9.15-alt1
- +installer

* Mon May 20 2013 Michael Shigorin <mike@altlinux.org> 0.9.14-alt1
- more regular fixes

* Mon May 13 2013 Michael Shigorin <mike@altlinux.org> 0.9.13-alt1
- regular fixes

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 0.9.12-alt1
- four weeks later...

* Mon Mar 25 2013 Michael Shigorin <mike@altlinux.org> 0.9.11-alt1
- persistent icewm

* Mon Mar 18 2013 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- fonts: axios!

* Tue Feb 26 2013 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- regular refactoring

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 0.9.8.1-alt1
- works with make-initrd 0.8.1+ (see #28578)

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- live fixes/tweaks galore

* Mon Feb 11 2013 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- going nightly

* Mon Feb 04 2013 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- assorted fixes

* Mon Jan 21 2013 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- homeros

* Mon Jan 14 2013 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- restricted boot

* Mon Dec 31 2012 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- regular images

* Mon Dec 17 2012 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- enhanced uefi support

* Mon Dec 03 2012 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- initial kde4 support

* Mon Nov 19 2012 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- initial uefi, luks, armh support
- enhanced arm, gnome3/systemd, vm support

* Sun Nov 11 2012 Michael Shigorin <mike@altlinux.org> 0.8.7-alt1
- regressions--

* Mon Nov 05 2012 Michael Shigorin <mike@altlinux.org> 0.8.6-alt1
- docs subpackage (HTML/PDF book)

* Mon Oct 29 2012 Michael Shigorin <mike@altlinux.org> 0.8.5-alt1
- diffable logs
- AMD APU support

* Tue Oct 16 2012 Michael Shigorin <mike@altlinux.org> 0.8.4-alt1
- worked around enhancements in current make-initrd-propagator
  (thus fixed live image boot, finally)

* Mon Oct 15 2012 Michael Shigorin <mike@altlinux.org> 0.8.3-alt1
- make-3.82 support
- fixed live image boot to some extent (see #27640, #27852)

* Mon Sep 24 2012 Michael Shigorin <mike@altlinux.org> 0.8.2-alt1
- fixed build with recent make-initrd-propagator

* Mon Sep 03 2012 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- misc fixes

* Mon Aug 13 2012 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- stage2@live

* Mon Aug 06 2012 Michael Shigorin <mike@altlinux.org> 0.7.6-alt1
- minor improvements

* Mon Jul 30 2012 Michael Shigorin <mike@altlinux.org> 0.7.5-alt1
- a bunch of fixups and cleanups

* Mon Jul 16 2012 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1
- ppc builds

* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 0.7.3-alt1
- arm builds

* Mon Jul 02 2012 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- simply fixes

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- vm improvements and assorted tweaks/fixes

* Mon Jun 18 2012 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- new features:
  + initial build-vm
  + plymouth

* Mon May 28 2012 Michael Shigorin <mike@altlinux.org> 0.6.8-alt1
- minor bugfixes

* Mon May 21 2012 Michael Shigorin <mike@altlinux.org> 0.6.7-alt1
- docs updates

* Mon May 14 2012 Michael Shigorin <mike@altlinux.org> 0.6.6-alt1
- build helpers refactored
- initial frontend support

* Mon May 07 2012 Michael Shigorin <mike@altlinux.org> 0.6.5-alt1
- branding feature

* Mon Apr 23 2012 Michael Shigorin <mike@altlinux.org> 0.6.4-alt1
- simply better (tm)

* Mon Apr 09 2012 Michael Shigorin <mike@altlinux.org> 0.6.3-alt1
- massive squashfs tuning

* Mon Apr 02 2012 Michael Shigorin <mike@altlinux.org> 0.6.2-alt1
- better live-webkiosk and initial live-flightgear
- cleanup, syslinux, xorg feature tweaks

* Mon Mar 26 2012 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- ISO9660 metadata support
- initial alien VE image

* Mon Mar 19 2012 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- reports (targets graph)

* Mon Mar 12 2012 Michael Shigorin <mike@altlinux.org> 0.5.7-alt1
- distro tweaks

* Mon Feb 20 2012 Michael Shigorin <mike@altlinux.org> 0.5.6-alt1
- minor fixups

* Mon Feb 06 2012 Michael Shigorin <mike@altlinux.org> 0.5.5-alt1
- live-related tweaks (including live.hooks support)
- terminal server and webkiosk images

* Mon Jan 16 2012 Michael Shigorin <mike@altlinux.org> 0.5.4-alt1
- better diags for initial deployment

* Mon Jan 02 2012 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- multi-target, multi-arch, single-job builds

* Mon Dec 19 2011 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- THE_{KMODULES,PACKAGES,LISTS,GROUPS}
- incremental development, refactoring and bugfixing

* Fri Dec 02 2011 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- generic VE archive type (added cpio and xz either)
- minor additions/fixes

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- add_feature for autoregistration (simple but invasive)
- added features: isomd5sum, repo, systemd
- changed features: powerbutton -> power

* Tue Nov 08 2011 Michael Shigorin <mike@altlinux.org> 0.4.3.2-alt1
- mkimage version required/checked

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3.1-alt1
- CLEAN by default unless DEBUG

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3-alt2
- include %mpdir/ itself as well

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3-alt1
- enhancements to logging
- NICE variable: employ nice(1) and ionice(1) if available
- features.in/syslinux: banner tweaked to include target name
- features.in/live: set up unicode locale/consolefont

* Wed Nov 02 2011 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- initial package
