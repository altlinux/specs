%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}

%define intel_64 nocona core2 corei7
%define intel_32 pentium pentiumpro pentium_mmx pentium2 pentium3 pentium_m pentium4 prescott atom
%define amd_32 5x86 k5 k6 k6_2 k6_3 geode k7 athlon athlon_xp
%define amd_64 opteron k8 k9 k10 barcelona phenom
%define via_64 nano
%define via_32 c3 c3_2
%define x86_64 x86_64 %intel_64 %amd_64 %via_64

%define base_flavour	led
%define sub_flavour	ws
%define flavour		%base_flavour-%sub_flavour

Name: kernel-image-%flavour
Version: 3.0.43
Release: alt7

%define kernel_req %nil
%define kernel_prov %nil
%define kernel_branch 3.0
%define kernel_stable_version 43
%define kernel_extra_version	.%kernel_stable_version
#define kernel_extra_version	%nil

%define krelease %release

%define kmandir %{_man9dir}l
# Build options
# You can change compiler version by editing this line:
%define kgcc_version	4.6

%def_enable smp
%def_disable verbose
%def_disable debug
%def_disable modversions
%def_enable kallsyms
%def_disable docs
%def_enable htmldocs
%def_enable man
%def_disable debugfs
%def_disable numa
%def_enable acpi
%def_enable pci
%def_disable mca
%def_disable math_emu
%def_enable pcmcia
%def_enable isdn
%def_enable telephony
%def_enable atm
%def_disable tokenring
%def_enable fddi
%def_enable w1
%def_enable hamradio
%def_enable can
%def_enable fusion
%def_enable drm
%def_enable ipv6
%def_enable edac
%def_enable ide
%def_enable pata
%def_enable firewire
%def_enable bluetooth
%def_enable irda
%def_enable joystick
%def_enable gameport
%def_enable usb_gadget
%def_enable tablet
%def_enable touchscreen
%def_enable lirc
%def_enable watchdog
%def_enable mtd
%def_enable mmc
%def_enable media
%def_enable sound
%def_disable oss
%def_enable alsa
%def_disable pcsp
%def_enable video
%def_enable guest
%def_enable ext4_for_ext23
%def_enable bootsplash
%def_enable zcache
%def_enable security
%def_enable audit
%def_enable selinux
%def_enable tomoyo
%def_enable apparmor
%def_enable smack
%def_enable thp
%def_enable kvm
%def_enable hyperv
%def_disable paravirt_guest
%def_disable kvm_quest
%def_disable nfs_swap
%def_enable fatelf
%def_without perf
%def_enable oprofile
%def_enable secrm
%def_with firmware

%def_disable debug_section_mismatch

%define allocator SLQB

%define strip_mod_opts --strip-unneeded -R .comment

## Don't edit below this line ##################################

%define kversion	%kernel_branch%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease
%define firmware_dir	/lib/firmware/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kernel_branch-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/

Source0: linux-%version.tar
Source1: %flavour-%kernel_branch-config-x86_64
Source2: %flavour-%kernel_branch-config-i386

#Patch0000: patch-%kernel_branch.%kernel_stable_version

Patch0001: linux-%kernel_branch.42-fix-Documentation-DocBook.patch
Patch0002: linux-%kernel_branch.42-fix-Documentation-DocBook-man.patch

Patch0011: linux-%kernel_branch.42-fix-arch-ia64.patch
Patch0012: linux-%kernel_branch.42-fix-arch-powerpc.patch
Patch0013: linux-%kernel_branch.42-fix-arch-powerpc-platforms--52xx.patch
Patch0014: linux-%kernel_branch.42-fix-arch-powerpc-platforms--chrp.patch
Patch0015: linux-%kernel_branch.42-fix-arch-powerpc-platforms--pseries.patch
Patch0016: linux-%kernel_branch.42-fix-arch-x86.patch
Patch0017: linux-%kernel_branch.42-fix-arch-x86--apic.patch
Patch0018: linux-%kernel_branch.42-fix-arch-x86--apm.patch
Patch0019: linux-%kernel_branch.42-fix-arch-x86--mcheck.patch
Patch0020: linux-%kernel_branch.42-fix-arch-x86--tsc.patch
Patch0021: linux-%kernel_branch.42-fix-arch-x86-cpu--perf-event.patch
Patch0022: linux-%kernel_branch.42-fix-arch-x86-platform-olpc.patch

Patch0030: linux-%kernel_branch.42-fix-block.patch
Patch0031: linux-%kernel_branch.42-fix-block--blk-integrity.patch
Patch0032: linux-%kernel_branch.42-fix-block--blk-throttle.patch
Patch0033: linux-%kernel_branch.42-fix-block--cfq-iosched.patch

Patch0040: linux-%kernel_branch.42-fix-drivers--connector.patch

Patch0050: linux-%kernel_branch.42-fix-drivers-acpi.patch
Patch0051: linux-%kernel_branch.42-fix-drivers-acpi--battery.patch
Patch0052: linux-%kernel_branch.42-fix-drivers-acpi--processor.patch
Patch0053: linux-%kernel_branch.42-fix-drivers-acpi--thermal.patch
Patch0054: linux-%kernel_branch.42-fix-drivers-acpi--video.patch
Patch0055: linux-%kernel_branch.42-fix-drivers-acpi-apei--apei.patch
Patch0056: linux-%kernel_branch.42-fix-drivers-acpi-apei--einj.patch
Patch0057: linux-%kernel_branch.42-fix-drivers-acpi-apei--erst-dbg.patch
Patch0058: linux-%kernel_branch.42-fix-drivers-acpi-apei--ghes.patch

Patch0061: linux-%kernel_branch.42-fix-drivers-ata--ahci.patch
Patch0062: linux-%kernel_branch.42-fix-drivers-ata--libata.patch
Patch0063: linux-%kernel_branch.42-fix-drivers-ata--sata_sil.patch

Patch0071: linux-%kernel_branch.42-fix-drivers-base--memory.patch
Patch0072: linux-%kernel_branch.42-fix-drivers-base-power--runtime.patch

Patch0081: linux-%kernel_branch.42-fix-drivers-block--DAC960.patch
Patch0082: linux-%kernel_branch.43-fix-drivers-block--cciss.patch
Patch0083: linux-%kernel_branch.42-fix-drivers-block--drbd.patch
Patch0084: linux-%kernel_branch.42-fix-drivers-block--floppy.patch
Patch0085: linux-%kernel_branch.42-fix-drivers-block--nbd.patch
Patch0086: linux-%kernel_branch.42-fix-drivers-block--rbd.patch
Patch0087: linux-%kernel_branch.42-fix-drivers-block--virtio_blk.patch

Patch0091: linux-%kernel_branch.42-fix-drivers-bluetooth--ath3k.patch
Patch0092: linux-%kernel_branch.42-fix-drivers-bluetooth--btusb.patch

Patch0101: linux-%kernel_branch.42-fix-drivers-char--lp.patch
Patch0102: linux-%kernel_branch.42-fix-drivers-char--mem.patch
Patch0103: linux-%kernel_branch.42-fix-drivers-char-agp--agpgart.patch
Patch0104: linux-%kernel_branch.42-fix-drivers-char-agp--intel-agp.patch
Patch0105: linux-%kernel_branch.42-fix-drivers-char-hw_random--virtio-rng.patch
Patch0106: linux-%kernel_branch.42-fix-drivers-char-ipmi--ipmi_si.patch

Patch0110: linux-%kernel_branch.42-fix-drivers-cpufreq.patch
Patch0111: linux-%kernel_branch.42-fix-drivers-cpufreq--cpufreq_conservative.patch
Patch0112: linux-%kernel_branch.42-fix-drivers-cpufreq--cpufreq_ondemand.patch

Patch0121: linux-%kernel_branch.42-fix-drivers-crypto--hifn_795x.patch

Patch0131: linux-%kernel_branch.42-fix-drivers-dma--dmatest.patch

Patch0141: linux-%kernel_branch.42-fix-drivers-edac--edac_mce_amd.patch
Patch0142: linux-%kernel_branch.42-fix-drivers-edac--i7300_edac.patch
Patch0143: linux-%kernel_branch.42-fix-drivers-edac--i7core_edac.patch

Patch0151: linux-%kernel_branch.42-fix-drivers-eisa--pci_eisa.patch

Patch0161: linux-%kernel_branch.42-fix-drivers-firmware--edd.patch
Patch0162: linux-%kernel_branch.42-fix-drivers-firmware--efivars.patch

Patch0171: linux-%kernel_branch.42-fix-drivers-gpu-drm.patch
Patch0172: linux-%kernel_branch.42-fix-drivers-gpu-drm--drm.patch
Patch0173: linux-%kernel_branch.42-fix-drivers-gpu-drm--drm_kms_helper.patch
Patch0174: linux-%kernel_branch.42-fix-drivers-gpu-drm--i915.patch
Patch0175: linux-%kernel_branch.42-fix-drivers-gpu-drm--mga.patch
Patch0176: linux-%kernel_branch.42-fix-drivers-gpu-drm--radeon.patch
Patch0177: linux-%kernel_branch.42-fix-drivers-gpu-drm--via.patch
Patch0178: linux-%kernel_branch.42-fix-drivers-gpu-drm--vmwgfx.patch
Patch0179: linux-%kernel_branch.42-fix-drivers-gpu-vga--vgaarb.patch

Patch0181: linux-%kernel_branch.42-fix-drivers-hid--hid-apple.patch
Patch0182: linux-%kernel_branch.42-fix-drivers-hid--usbhid.patch

Patch0190: linux-%kernel_branch.42-fix-drivers-hv.patch

Patch0201: linux-%kernel_branch.42-fix-drivers-hwmon--applesmc.patch
Patch0202: linux-%kernel_branch.42-fix-drivers-hwmon--coretemp.patch
Patch0203: linux-%kernel_branch.42-fix-drivers-hwmon--k10temp.patch

Patch0211: linux-%kernel_branch.42-fix-drivers-i2c--i2c-pxa.patch
Patch0212: linux-%kernel_branch.42-fix-drivers-i2c-busses--scx200_acb.patch

Patch0220: linux-%kernel_branch.42-fix-drivers-ide.patch

Patch0231: linux-%kernel_branch.42-fix-drivers-infiniband-core.patch
Patch0232: linux-%kernel_branch.42-fix-drivers-infiniband-hw-cxgb4.patch
Patch0233: linux-%kernel_branch.42-fix-drivers-infiniband-hw-mlx4.patch
Patch0234: linux-%kernel_branch.42-fix-drivers-infiniband-hw-mthca.patch

Patch0241: linux-%kernel_branch.42-fix-drivers-input-mouse--synaptics.patch
Patch0242: linux-%kernel_branch.42-fix-drivers-input-serio--i8042.patch

Patch0251: linux-%kernel_branch.42-fix-drivers-isdn-gigaset--gigaset.patch
Patch0252: linux-%kernel_branch.42-fix-drivers-isdn-mISDN--mISDN_core.patch

Patch0261: linux-%kernel_branch.42-fix-drivers-leds--leds-lp5521.patch

Patch0271: linux-%kernel_branch.42-fix-drivers-macintosh--adb.patch
Patch0272: linux-%kernel_branch.42-fix-drivers-macintosh--adbhid.patch

Patch0281: linux-%kernel_branch.42-fix-drivers-md--dm-mod.patch
Patch0282: linux-%kernel_branch.42-fix-drivers-md--dm-multipath.patch
Patch0283: linux-%kernel_branch.42-fix-drivers-md--md-mod.patch
Patch0284: linux-%kernel_branch.42-fix-drivers-md--raid1.patch
Patch0285: linux-%kernel_branch.42-fix-drivers-md--raid10.patch
Patch0286: linux-%kernel_branch.42-fix-drivers-md--raid456.patch

Patch0291: linux-%kernel_branch.42-fix-drivers-media-common-tuners--max2165.patch

Patch0301: linux-%kernel_branch.42-fix-drivers-message-fusion.patch

Patch0311: linux-%kernel_branch.42-fix-drivers-misc--rts_pstor.patch
Patch0312: linux-%kernel_branch.42-fix-drivers-misc--vmw_balloon.patch
Patch0313: linux-%kernel_branch.42-fix-drivers-misc--zcache.patch
Patch0314: linux-%kernel_branch.42-fix-drivers-misc-lis3lv02d--lis3lv02d.patch

Patch0321: linux-%kernel_branch.42-fix-drivers-mmc-card--mmc_block.patch

Patch0331: linux-%kernel_branch.42-fix-drivers-net--3c509.patch
Patch0332: linux-%kernel_branch.42-fix-drivers-net--3c59x.patch
Patch0333: linux-%kernel_branch.42-fix-drivers-net--at1700.patch
Patch0334: linux-%kernel_branch.42-fix-drivers-net--bna.patch
Patch0335: linux-%kernel_branch.42-fix-drivers-net--bnx2.patch
Patch0336: linux-%kernel_branch.42-fix-drivers-net--bonding.patch
Patch0337: linux-%kernel_branch.42-fix-drivers-net--depca.patch
Patch0338: linux-%kernel_branch.42-fix-drivers-net--dl2k.patch
Patch0339: linux-%kernel_branch.42-fix-drivers-net--e1000.patch
Patch0340: linux-%kernel_branch.42-fix-drivers-net--e1000e.patch
Patch0341: linux-%kernel_branch.42-fix-drivers-net--ehea.patch
Patch0342: linux-%kernel_branch.42-fix-drivers-net--hp100.patch
Patch0343: linux-%kernel_branch.42-fix-drivers-net--ibmveth.patch
Patch0344: linux-%kernel_branch.42-fix-drivers-net--igb.patch
Patch0345: linux-%kernel_branch.42-fix-drivers-net--ixgbe.patch
Patch0346: linux-%kernel_branch.42-fix-drivers-net--macvtap.patch
Patch0347: linux-%kernel_branch.42-fix-drivers-net--natsemi.patch
Patch0348: linux-%kernel_branch.42-fix-drivers-net--ne3210.patch
Patch0349: linux-%kernel_branch.42-fix-drivers-net--qlcnic.patch
Patch0350: linux-%kernel_branch.42-fix-drivers-net--qlge.patch
Patch0351: linux-%kernel_branch.42-fix-drivers-net--r8169.patch
Patch0352: linux-%kernel_branch.42-fix-drivers-net--sfc.patch
Patch0353: linux-%kernel_branch.42-fix-drivers-net--tg3.patch
Patch0354: linux-%kernel_branch.42-fix-drivers-net--tlan.patch
Patch0355: linux-%kernel_branch.42-fix-drivers-net--vmxnet3.patch
Patch0356: linux-%kernel_branch.42-fix-drivers-net-benet--be2net.patch
Patch0357: linux-%kernel_branch.42-fix-drivers-net-mlx4--mlx4_core.patch
Patch0358: linux-%kernel_branch.42-fix-drivers-net-mlx4--mlx4_en.patch
Patch0359: linux-%kernel_branch.42-fix-drivers-net-netxen.patch
Patch0360: linux-%kernel_branch.42-fix-drivers-net-pcmcia--nmclan_cs.patch
Patch0361: linux-%kernel_branch.42-fix-drivers-net-tulip.patch
Patch0362: linux-%kernel_branch.42-fix-drivers-net-tulip--de4x5.patch
Patch0363: linux-%kernel_branch.42-fix-drivers-net-usb--asix.patch
Patch0364: linux-%kernel_branch.42-fix-drivers-net-usb--cdc_ether.patch
Patch0365: linux-%kernel_branch.42-fix-drivers-net-usb--ipheth.patch
Patch0366: linux-%kernel_branch.42-fix-drivers-net-usb--kalmia.patch
Patch0367: linux-%kernel_branch.42-fix-drivers-net-usb--lg-vl600.patch
Patch0368: linux-%kernel_branch.42-fix-drivers-net-usb--smsc75xx.patch
Patch0369: linux-%kernel_branch.42-fix-drivers-net-usb--usbnet.patch
Patch0370: linux-%kernel_branch.42-fix-drivers-net-wireless--rt2x00.patch
Patch0371: linux-%kernel_branch.42-fix-drivers-net-wireless-libertas--libertas_spi.patch

Patch0381: linux-%kernel_branch.42-fix-drivers-parport--parport_pc.patch

Patch0390: linux-%kernel_branch.42-fix-drivers-pci.patch
Patch0391: linux-%kernel_branch.42-fix-drivers-pci--dmar.patch
Patch0392: linux-%kernel_branch.42-fix-drivers-pci--sn.patch
Patch0393: linux-%kernel_branch.42-fix-drivers-pci-hotplug--acpiphp.patch
Patch0394: linux-%kernel_branch.42-fix-drivers-pci-hotplug--pci_hotplug.patch

Patch0401: linux-%kernel_branch.42-fix-drivers-platform--hdaps.patch
Patch0402: linux-%kernel_branch.42-fix-drivers-platform--hp_accel.patch

Patch0410: linux-%kernel_branch.42-fix-drivers-pnp.patch

Patch0421: linux-%kernel_branch.42-fix-drivers-rtc--rtc-m41t80.patch

Patch0431: linux-%kernel_branch.42-fix-drivers-scsi.patch
Patch0432: linux-%kernel_branch.42-fix-drivers-scsi--aacraid.patch
Patch0433: linux-%kernel_branch.42-fix-drivers-scsi--aha152x.patch
Patch0434: linux-%kernel_branch.42-fix-drivers-scsi--aha1542.patch
Patch0435: linux-%kernel_branch.42-fix-drivers-scsi--bfa.patch
Patch0436: linux-%kernel_branch.42-fix-drivers-scsi--bnx2fc.patch
Patch0437: linux-%kernel_branch.42-fix-drivers-scsi--fnic.patch
Patch0438: linux-%kernel_branch.42-fix-drivers-scsi--hpsa.patch
Patch0439: linux-%kernel_branch.42-fix-drivers-scsi--ipr.patch
Patch0440: linux-%kernel_branch.42-fix-drivers-scsi--isci.patch
Patch0441: linux-%kernel_branch.42-fix-drivers-scsi--libfc.patch
Patch0442: linux-%kernel_branch.42-fix-drivers-scsi--libsas.patch
Patch0443: linux-%kernel_branch.42-fix-drivers-scsi--lpfc.patch
Patch0444: linux-%kernel_branch.42-fix-drivers-scsi--mpt2sas.patch
Patch0445: linux-%kernel_branch.42-fix-drivers-scsi--mvsas.patch
Patch0446: linux-%kernel_branch.42-fix-drivers-scsi--pm8001.patch
Patch0447: linux-%kernel_branch.42-fix-drivers-scsi--qla2xxx.patch
Patch0448: linux-%kernel_branch.42-fix-drivers-scsi--scsi_mod.patch
Patch0449: linux-%kernel_branch.42-fix-drivers-scsi--scsi_transport_fc.patch
Patch0450: linux-%kernel_branch.42-fix-drivers-scsi--scsi_transport_sas.patch
Patch0451: linux-%kernel_branch.42-fix-drivers-scsi--scsi_transport_spi.patch
Patch0452: linux-%kernel_branch.42-fix-drivers-scsi--sd_mod.patch
Patch0453: linux-%kernel_branch.42-fix-drivers-scsi--ses.patch
Patch0454: linux-%kernel_branch.42-fix-drivers-scsi--sim710.patch
Patch0455: linux-%kernel_branch.42-fix-drivers-scsi--sr_mod.patch
Patch0456: linux-%kernel_branch.42-fix-drivers-scsi--st.patch
Patch0457: linux-%kernel_branch.42-fix-drivers-scsi--zfcp.patch
Patch0458: linux-%kernel_branch.42-fix-drivers-scsi-cxgbi--libcxgbi.patch
Patch0459: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh.patch
Patch0460: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_alua.patch
Patch0461: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_emc.patch
Patch0462: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_hp_sw.patch
Patch0463: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_rdac.patch
Patch0464: linux-%kernel_branch.42-fix-drivers-scsi-fcoe.patch
Patch0465: linux-%kernel_branch.42-fix-drivers-scsi-ibmvscsi--ibmvfc.patch
Patch0466: linux-%kernel_branch.42-fix-drivers-scsi-ibmvscsi--ibmvscsic.patch
Patch0467: linux-%kernel_branch.42-fix-drivers-scsi-megaraid--megaraid_mbox.patch
Patch0468: linux-%kernel_branch.42-fix-drivers-scsi-megaraid--megaraid_sas.patch

Patch0471: linux-%kernel_branch.42-fix-drivers-target--tcm_fc.patch

Patch0481: linux-%kernel_branch.42-fix-drivers-telephony--ixj.patch

Patch0491: linux-%kernel_branch.42-fix-drivers-tty-serial--8250.patch
Patch0492: linux-%kernel_branch.42-fix-drivers-tty-serial--8250_pci.patch

Patch0500: linux-%kernel_branch.42-fix-drivers-usb.patch
Patch0501: linux-%kernel_branch.42-fix-drivers-usb-atm--ueagle-atm.patch
Patch0502: linux-%kernel_branch.42-fix-drivers-usb-core.patch
Patch0503: linux-%kernel_branch.42-fix-drivers-usb-host--ehci-hcd.patch
Patch0504: linux-%kernel_branch.42-fix-drivers-usb-host--uhci-hcd.patch
Patch0505: linux-%kernel_branch.42-fix-drivers-usb-host--xhci-hcd.patch
Patch0506: linux-%kernel_branch.42-fix-drivers-usb-misc--usbtest.patch
Patch0507: linux-%kernel_branch.42-fix-drivers-usb-mon.patch
Patch0508: linux-%kernel_branch.42-fix-drivers-usb-serial--ftdi_sio.patch
Patch0509: linux-%kernel_branch.42-fix-drivers-usb-serial--ipw.patch
Patch0510: linux-%kernel_branch.42-fix-drivers-usb-serial--pl2303.patch
Patch0511: linux-%kernel_branch.42-fix-drivers-usb-serial--usbserial.patch
Patch0512: linux-%kernel_branch.42-fix-drivers-usb-storage--ums-realtek.patch
Patch0513: linux-%kernel_branch.42-fix-drivers-usb-usbip--usbip-host.patch
Patch0514: linux-%kernel_branch.42-fix-drivers-usb-wusbcore--wusbcore-cbaf.patch

Patch0521: linux-%kernel_branch.42-fix-drivers-video--intelfb.patch
Patch0522: linux-%kernel_branch.42-fix-drivers-video-aty--radeonfb.patch
Patch0523: linux-%kernel_branch.42-fix-drivers-video-via.patch

Patch0531: linux-%kernel_branch.42-fix-drivers-virtio--virtio_ballon.patch

Patch0541: linux-%kernel_branch.42-fix-drivers-watchdog--hpwdt.patch
Patch0542: linux-%kernel_branch.42-fix-drivers-watchdog--iTCO_wdt.patch

Patch0551: linux-%kernel_branch.42-fix-firmware--vicam.patch

Patch0560: linux-%kernel_branch.42-fix-fs.patch
Patch0561: linux-%kernel_branch.42-fix-fs--bio-integrity.patch
Patch0562: linux-%kernel_branch.42-fix-fs--block.patch
Patch0563: linux-%kernel_branch.42-fix-fs--eventpoll.patch
Patch0564: linux-%kernel_branch.42-fix-fs-btrfs.patch
Patch0565: linux-%kernel_branch.42-fix-fs-ceph.patch
Patch0566: linux-%kernel_branch.42-fix-fs-cifs.patch
Patch0567: linux-%kernel_branch.42-fix-fs-dlm.patch
Patch0568: linux-%kernel_branch.42-fix-fs-ecryptfs.patch
Patch0569: linux-%kernel_branch.42-fix-fs-ext3.patch
Patch0570: linux-%kernel_branch.42-fix-fs-hfs.patch
Patch0571: linux-%kernel_branch.42-fix-fs-jbd.patch
Patch0572: linux-%kernel_branch.42-fix-fs-nfs.patch
Patch0573: linux-%kernel_branch.42-fix-fs-ocfs2.patch
Patch0574: linux-%kernel_branch.42-fix-fs-proc.patch
Patch0575: linux-%kernel_branch.42-fix-fs-pstore.patch
Patch0576: linux-%kernel_branch.42-fix-fs-reiserfs.patch
Patch0577: linux-%kernel_branch.42-fix-fs-sysfs.patch

Patch0580: linux-%kernel_branch.42-fix-include.patch

Patch0591: linux-%kernel_branch.42-fix-init--calibrate.patch

Patch0601: linux-%kernel_branch.42-fix-ipc--mqueue.patch

Patch0610: linux-%kernel_branch.42-fix-kernel.patch
Patch0611: linux-%kernel_branch.42-fix-kernel--cgroup.patch
Patch0612: linux-%kernel_branch.42-fix-kernel--cgroup_freezer.patch
Patch0613: linux-%kernel_branch.42-fix-kernel--freezer.patch
Patch0614: linux-%kernel_branch.42-fix-kernel--watchdog.patch
Patch0615: linux-%kernel_branch.42-fix-kernel-power--hibernate.patch
Patch0616: linux-%kernel_branch.42-fix-kernel-time.patch

Patch0620: linux-%kernel_branch.42-fix-lib.patch
Patch0621: linux-%kernel_branch.42-fix-lib--genalloc.patch

Patch0630: linux-%kernel_branch.42-fix-mm.patch
Patch0631: linux-%kernel_branch.42-fix-mm--compaction.patch
Patch0632: linux-%kernel_branch.42-fix-mm--huge_memory.patch
Patch0633: linux-%kernel_branch.42-fix-mm--hugetlb.patch
Patch0634: linux-%kernel_branch.42-fix-mm--memcontrol.patch
Patch0635: linux-%kernel_branch.42-fix-mm--memory-failure.patch
Patch0636: linux-%kernel_branch.42-fix-mm--mmu.patch
Patch0637: linux-%kernel_branch.42-fix-mm--mmu_notofier.patch
Patch0638: linux-%kernel_branch.42-fix-mm--numa.patch
Patch0639: linux-%kernel_branch.42-fix-mm--slab.patch
Patch0640: linux-%kernel_branch.42-fix-mm--slub.patch
Patch0641: linux-%kernel_branch.42-fix-mm--swap.patch

Patch0651: linux-%kernel_branch.42-fix-net--batman-adv.patch
Patch0652: linux-%kernel_branch.42-fix-net--dcb.patch
Patch0653: linux-%kernel_branch.42-fix-net--wimax.patch
Patch0654: linux-%kernel_branch.42-fix-net--x25.patch
Patch0655: linux-%kernel_branch.42-fix-net-8021q--vlan-core.patch
Patch0656: linux-%kernel_branch.42-fix-net-bridge.patch
Patch0657: linux-%kernel_branch.42-fix-net-ceph.patch
Patch0658: linux-%kernel_branch.42-fix-net-core.patch
Patch0659: linux-%kernel_branch.42-fix-net-ipv4.patch
Patch0660: linux-%kernel_branch.42-fix-net-ipv6.patch
Patch0661: linux-%kernel_branch.42-fix-net-ipv6--ip6_tunnel.patch
Patch0662: linux-%kernel_branch.42-fix-net-mac80211.patch
Patch0663: linux-%kernel_branch.42-fix-net-netfilter--nf_conntrack_ecache.patch
Patch0664: linux-%kernel_branch.42-fix-net-netfilter--nf_conntrack_ftp.patch
Patch0665: linux-%kernel_branch.42-fix-net-netfilter--nf_conntrack_netlink.patch
Patch0666: linux-%kernel_branch.42-fix-net-netfilter-ipvs--ipvs.patch
Patch0667: linux-%kernel_branch.42-fix-net-rds--rds.patch
Patch0668: linux-%kernel_branch.42-fix-net-sctp.patch
Patch0669: linux-%kernel_branch.42-fix-net-sunrpc.patch
Patch0670: linux-%kernel_branch.42-fix-net-xfrm--xfrm_policy.patch

Patch0680: linux-%kernel_branch.42-fix-scripts.patch

Patch0691: linux-%kernel_branch.42-fix-security--security.patch
Patch0692: linux-%kernel_branch.42-fix-security-selinux.patch

Patch0701: linux-%kernel_branch.42-fix-sound-core--snd-pcm.patch
Patch0702: linux-%kernel_branch.42-fix-sound-oss--pss.patch
Patch0703: linux-%kernel_branch.42-fix-sound-pci-hda.patch
Patch0704: linux-%kernel_branch.42-fix-sound-pci-rme9652--snd-hdspm.patch
Patch0705: linux-%kernel_branch.42-fix-sound-usb-misc--snd-ua101.patch

Patch0711: linux-%kernel_branch.42-fix-tools--perf.patch

Patch0721: linux-%kernel_branch.42-fix-virt-kvm.patch


Patch1001: linux-%kernel_branch.42-feat-block--bfq-iosched.patch
Patch1002: linux-%kernel_branch.42-feat-block--bsg-lib.patch
Patch1003: linux-%kernel_branch.42-feat-block--sio-iosched.patch

Patch1011: linux-%kernel_branch-feat-drivers-block--cloop.patch
Patch1012: linux-%kernel_branch.42-feat-drivers-block--zram.patch

Patch1021: linux-%kernel_branch-feat-drivers-gpu-drm--cirrus.patch

Patch1031: linux-%kernel_branch-feat-drivers-input-lirc.patch
Patch1032: linux-%kernel_branch.42-feat-drivers-input-touchscreen--elousb.patch

Patch1041: linux-%kernel_branch.42-feat-drivers-md--dm-raid45.patch

Patch1051: linux-%kernel_branch.42-feat-drivers-misc--rts_pstor.patch
Patch1052: linux-%kernel_branch.42-feat-drivers-misc--xvmalloc.patch
Patch1053: linux-%kernel_branch.42-feat-drivers-misc--zcache.patch

Patch1061: linux-%kernel_branch.42-feat-drivers-platform--thinkpad_ec.patch
Patch1062: linux-%kernel_branch.42-feat-drivers-platform--tp_smapi.patch

Patch1071: linux-%kernel_branch.42-feat-drivers-usb-usbip.patch

Patch1081: linux-%kernel_branch.42-feat-drivers-video--bootsplash.patch

Patch1091: linux-%kernel_branch.42-feat-fs--secrm.patch
Patch1092: linux-%kernel_branch-feat-fs-aufs.patch
Patch1093: linux-%kernel_branch.42-feat-fs-binfmt_elf--fatelf.patch
Patch1094: linux-%kernel_branch.42-feat-fs-ext2--secrm.patch
Patch1095: linux-%kernel_branch.42-feat-fs-ext3--secrm.patch
Patch1096: linux-%kernel_branch.42-feat-fs-ext4--secrm.patch
Patch1097: linux-%kernel_branch.42-feat-fs-fat--secrm.patch
Patch1098: linux-%kernel_branch.42-feat-fs-jbd--secrm.patch
Patch1099: linux-%kernel_branch.42-feat-fs-jbd2--secrm.patch
Patch1100: linux-%kernel_branch.42-feat-fs-overlayfs.patch
Patch1101: linux-%kernel_branch.42-feat-fs-reiser4.patch
Patch1102: linux-%kernel_branch-feat-fs-subfs.patch
Patch1103: linux-%kernel_branch.42-feat-fs-squashfs--write.patch
Patch1104: linux-%kernel_branch.42-feat-fs-unionfs.patch

Patch1111: linux-%kernel_branch.42-feat-kernel--cpe_migrate.patch
Patch1112: linux-%kernel_branch.42-feat-kernel--sched-cfs-boost.patch
Patch1113: linux-%kernel_branch.43-feat-kernel-power-tuxonice.patch

Patch1121: linux-%kernel_branch.42-feat-lib--llist.patch

Patch1131: linux-%kernel_branch.42-feat-mm--slqb.patch

Patch1141: linux-%kernel_branch.42-feat-net-ipv4-netfilter--ipt_ipv4options.patch

Patch1151: linux-%kernel_branch.42-feat-sound-ppc--snd-mpc52xx-ac97.patch

ExclusiveOS: Linux
ExclusiveArch: %x86_64 %ix86

%ifarch %x86_64 %ix86
%define kernel_arch x86
%else
%define kernel_arch %_target_cpu
%endif

%ifarch %x86_64
%define base_arch x86_64
%endif
%ifarch %ix86
%define base_arch i386
%endif

%ifarch i586 i686
%set_enable docs
%def_with src
%else
%if "%base_arch" == "%_target_cpu"
%set_enable docs
%def_with src
%endif
%endif

%if_disabled docs
%set_disable htmldocs
%set_disable man
%endif

%ifarch i386
%set_disable pci
%set_disable acpi
%set_disable edac
%set_disable media
%set_disable kvm
%set_disable hyperv
%set_disable oprofile
%endif

%ifnarch i386 i486
%set_disable math_emu
%set_disable mca
%endif

%{?_disable_pci:%set_disable drm}

%if_disabled sound
%set_disable oss
%set_disable alsa
%endif

%{?_disable_alsa:%set_disable pcsp}

%if_disabled video
%set_disable bootsplash
%endif

%{?_enable_debug:%set_enable debugfs}

%{!?allocator:%define allocator SLAB}

%ifarch %x86_64
%define kernel_base_cpu	GENERIC_CPU
%ifarch k8
%define kernel_cpu	K8
%endif
%ifarch k9
%define kernel_cpu	K9
%endif
%ifarch k10
%define kernel_cpu	K10
%endif
%ifarch nocona
%define kernel_cpu	PSC
%endif
%ifarch core2
%define kernel_cpu	CORE2
%endif
%endif

%ifarch %ix86
%define kernel_base_cpu	M386
%ifarch i486
%define kernel_cpu	486
%endif
%ifarch i586
%define kernel_cpu	586
%endif
%ifarch i686
%define kernel_cpu	686
%endif
%ifarch k6
%define kernel_cpu	K6
%endif
%ifarch athlon
%define kernel_cpu	K7
%endif
%ifarch pentium4
%define kernel_cpu	PENTIUM4
%endif
%ifarch k8_32
%define kernel_cpu	K8
%endif
%ifarch k9_32
%define kernel_cpu	K9
%endif
%ifarch k10_32
%define kernel_cpu	K10
%endif
%ifarch core2_32 atom
%define kernel_cpu	CORE2
%endif
%endif

BuildPreReq: rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
%{?kgcc_version:BuildRequires: gcc%kgcc_version}
BuildRequires: module-init-tools >= 3.1
BuildRequires: patch >= 2.6.1-alt1
%{?_with_src:BuildRequires: pxz}

%{?_enable_htmldocs:BuildRequires: xmlto transfig ghostscript}
%{?_enable_man:BuildRequires: xmlto}
%{?_with_perf:BuildRequires: binutils-devel libelf-devel asciidoc elfutils-devel >= 0.138}

Requires: bootloader-utils >= 0.4.6.1
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.9.8.24.1

Provides: kernel = %kversion
Provides: kernel-modules-md-%flavour = %version-%release

PreReq: coreutils
PreReq: module-init-tools >= 3.1
PreReq: mkinitrd >= 1:2.9.9-alt1
AutoProv: no, %kernel_prov
AutoReq: no, %kernel_req

%description
This package contains the Linux kernel that is used to boot and run
your system.
Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).
The "cx-ws" flavour of kernel packages is kernel for using on
workstations.

%define kernel_modules_package_add_provides() \
Provides: kernel-modules-%{1}-%flavour = %version-%release \
Provides: kernel-modules-%{1}-%kversion-%flavour-%krelease = %version-%release

%define kernel_modules_package_std_body() \
Group: System/Kernel and hardware \
Provides: kernel-modules-%{1}-%kversion-%flavour-%krelease = %version-%release \
Conflicts: kernel-modules-%{1}-%kversion-%flavour-%krelease < %version-%release \
Conflicts: kernel-modules-%{1}-%kversion-%flavour-%krelease > %version-%release \
Requires(postun): %name = %version-%release \
AutoProv: no, %kernel_prov \
AutoReq: no, %kernel_req \
PreReq: coreutils module-init-tools >= 3.1 %name = %version-%release

%define kernel_doc_package_std_body() \
Group: Documentation \
%{?base_flavour:Provides: kernel-%{1}-%base_flavour = %version-%release} \
Provides: kernel-%{1}-%flavour = %version-%release \
BuildArch: noarch \
AutoProv: no \
AutoReq: no

%define kernel_modules_package_post() \
%post -n kernel-modules-%{1}-%flavour \
%post_kernel_modules %kversion-%flavour-%krelease \
\
%postun -n kernel-modules-%{1}-%flavour \
%postun_kernel_modules %kversion-%flavour-%krelease

%define kernel_modules_package_files() \
%files -n kernel-modules-%{1}-%flavour -f %{1}.rpmmodlist

%package -n kernel-modules-scsi-%flavour
Summary: SCSI driver modules
%kernel_modules_package_std_body scsi

%description -n kernel-modules-scsi-%flavour
This package contains SCSI modules for the Linux kernel package
%name-%version-%release.


%package -n kernel-modules-infiniband-%flavour
Summary: InfiniBand core and support driver modules
%kernel_modules_package_std_body infiniband
%kernel_modules_package_add_provides ib

%description -n kernel-modules-infiniband-%flavour
This package contains InfiniBand core and support driver modules for the Linux
kernel package %name-%version-%release.


%package -n kernel-modules-ipmi-%flavour
Summary: IPMI core and support driver modules
%kernel_modules_package_std_body ipmi

%description -n kernel-modules-ipmi-%flavour
This package contains IPMI core and support driver modules for the Linux kernel
package %name-%version-%release.


%if_enabled video
%package -n kernel-modules-video-%flavour
Summary: Video graphics driver modules
%kernel_modules_package_std_body video
%kernel_modules_package_add_provides fb
%kernel_modules_package_add_provides framebuffer

%description -n kernel-modules-video-%flavour
This package contains Video graphics modules for the Linux kernel package
%name-%version-%release.
%endif


%if_enabled irda
%package -n kernel-modules-irda-%flavour
Summary: Linux IrDA (TM) protocols and device drivers modules
%kernel_modules_package_std_body irda

%description -n kernel-modules-irda-%flavour
This package contains IrDA (TM) protocols and device drivers modules for
the Linux kernel package %name-%version-%release.
%endif


%if_enabled joystick
%package -n kernel-modules-joystick-%flavour
Summary: Linux joystick/gamepad driver modules
%kernel_modules_package_std_body joystick
%kernel_modules_package_add_provides gamepad

%description -n kernel-modules-joystick-%flavour
This package contains Linux joystick, 6dof controller, gamepad,
steering wheel, weapon control system or something like driver modules
for the kernel package %name-%version-%release.
%endif


%if_enabled tablet
%package -n kernel-modules-tablet-%flavour
Summary: Linux tablets driver modules
%kernel_modules_package_std_body tablet

%description -n kernel-modules-tablet-%flavour
This package contains Linux tablets driver modules for the kernel package
%name-%version-%release.
%endif


%if_enabled touchscreen
%package -n kernel-modules-touchscreen-%flavour
Summary: Linux touchscreens driver modules
%kernel_modules_package_std_body touchscreen

%description -n kernel-modules-touchscreen-%flavour
This package contains Linux touchscreens driver modules for the kernel
package %name-%version-%release.
%endif


%if_enabled lirc
%package -n kernel-modules-lirc-%flavour
Summary: Linux Infrared Remote Control IR receiver/transmitter driver modules
%kernel_modules_package_std_body lirc

%description -n kernel-modules-lirc-%flavour
This package contains Linux Infrared Remote Control IR
receiver/transmitter driver modules for the kernel package
%name-%version-%release.
%endif


%if_enabled usb_gadget
%package -n kernel-modules-usb-gadget-%flavour
Summary: Linux USB Gadget driver modules
%kernel_modules_package_std_body usb-gadget

%description -n kernel-modules-usb-gadget-%flavour
USB Gadget support on a system involves a peripheral controller,
and the gadget driver using it.
This package contains Linux USB Gadget driver modules for the kernel
package %name-%version-%release.
%endif


%if_enabled atm
%package -n kernel-modules-atm-%flavour
Summary: Linux ATM driver modules
%kernel_modules_package_std_body atm

%description -n kernel-modules-atm-%flavour
ATM is a high-speed networking technology for Local Area Networks and
Wide Area Networks. It uses a fixed packet size and is connection
oriented, allowing for the negotiation of minimum bandwidth requirements.
This package contains ATM driver modules for the Linux kernel package
%name-%version-%release.
%endif


%if_enabled hamradio
%package -n kernel-modules-hamradio-%flavour
Summary: Linux Amateur Radio driver modules
%kernel_modules_package_std_body hamradio

%description -n kernel-modules-hamradio-%flavour
This package contains Amateur Radio driver modules for the Linux kernel
package %name-%version-%release.
%endif


%if_enabled w1
%package -n kernel-modules-w1-%flavour
Summary: Linux Dallas' 1-wire bus driver modules
%kernel_modules_package_std_body w1

%description -n kernel-modules-w1-%flavour
Dallas' 1-wire bus is useful to connect slow 1-pin devices such as
iButtons and thermal sensors.
This package contains Dallas' 1-wire bus driver modules for the Linux
kernel package %name-%version-%release.
%endif


%if_enabled watchdog
%package -n kernel-modules-watchdog-%flavour
Summary: Linux Watchdog Timer driver modules
%kernel_modules_package_std_body watchdog

%description -n kernel-modules-watchdog-%flavour
This package contains Watchdog Timer driver modules for the Linux kernel
package %name-%version-%release.
%endif


%if_enabled mtd
%package -n kernel-modules-mtd-%flavour
Summary: Linux Memory Technology Devices driver and fs modules
%kernel_modules_package_std_body mtd

%description -n kernel-modules-mtd-%flavour
Memory Technology Devices are flash, RAM and similar chips, often used
for solid state file systems on embedded devices.
This package contains Memory Technology Devices driver and fs modules for
the Linux kernel package %name-%version-%release.
%endif


%if_enabled wireless
%package -n kernel-modules-net-wireless-%flavour
Summary: Linux Wireless LAN driver modules
%kernel_modules_package_std_body wireless
%kernel_modules_package_add_provides wimax

%description -n kernel-modules-net-wireless-%flavour
This package contains Wireless LAN modules for the Linux kernel package
%name-%version-%release.
%endif


%package -n kernel-modules-fs-extra-%flavour
Summary: Linux extra filesystems drivers modules
%kernel_modules_package_std_body fs-extra

%description -n kernel-modules-fs-extra-%flavour
This package contains extra filesystems drivers modules modules for the
Linux kernel package %name-%version-%release.


%package -n kernel-modules-net-extra-%flavour
Summary: Linux extra net drivers modules
%kernel_modules_package_std_body net-extra

%description -n kernel-modules-net-extra-%flavour
This package contains extra net drivers modules modules for the Linux
kernel package %name-%version-%release.


%if_enabled oss
%package -n kernel-modules-oss-%flavour
Summary: OSS sound driver modules (obsolete)
%kernel_modules_package_std_body oss

%description -n kernel-modules-oss-%flavour
This package contains OSS sound driver modules for the Linux kernel
package %name-%version-%release.
These drivers are declared obsolete by the kernel maintainers; ALSA
drivers should be used instead.  However, the older OSS drivers may be
still useful for some hardware, if the corresponding ALSA drivers do
not work well.
Install this package only if you really need it.
%endif


%if_enabled alsa
%package -n kernel-modules-alsa-%flavour
Summary: The Advanced Linux Sound Architecture modules
%kernel_modules_package_std_body alsa
Obsoletes: firmware-alsa-%kversion-%flavour-%krelease = %version-%release
Provides: firmware-alsa-%kversion-%flavour-%krelease = %version-%release

%description -n kernel-modules-alsa-%flavour
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.
%endif


%if_enabled ide
%package -n kernel-modules-ide-%flavour
Summary: The IDE modules (old)
%kernel_modules_package_std_body ide

%description -n kernel-modules-ide-%flavour
Integrated Disk Electronics (IDE aka ATA-1) is a connecting standard for
mass storage units such as hard disks.
These are old IDE modules for your Linux system.
%endif


%if_enabled drm
%package -n kernel-modules-drm-%flavour
Summary: The Direct Rendering Infrastructure modules
%kernel_modules_package_std_body alsa
Obsoletes: firmware-drm-%kversion-%flavour-%krelease = %version-%release
Provides: firmware-drm-%kversion-%flavour-%krelease = %version-%release

%description -n kernel-modules-drm-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.
These are DRM modules for your Linux system.
%endif


%if_enabled media
%package -n kernel-modules-media-%flavour
Summary: Linux media driver modules
%kernel_modules_package_std_body media
Obsoletes: firmware-media-%kversion-%flavour-%krelease = %version-%release
Provides: firmware-media-%kversion-%flavour-%krelease = %version-%release

%description -n kernel-modules-media-%flavour
V4L kernel modules support for video capture and overlay devices,
webcams and AM/FM radio cards.
DVB kernel modules for DVB/ATSC device handling, software fallbacks etc.
%endif


%if_enabled isdn
%package -n kernel-modules-isdn-%flavour
Summary: The Integrated Services Digital Networks (ISDN) modules
%kernel_modules_package_std_body isdn

%description -n kernel-modules-isdn-%flavour
ISDN ("Integrated Services Digital Networks", called RNIS in France) is
a special type of fully digital telephone service; it's mostly used to
connect to your Internet service provider (with SLIP or PPP). The main
advantage is that the speed is higher than ordinary modem/telephone
connections, and that you can have voice conversations while
downloading stuff. It only works if your computer is equipped with an
ISDN card and both you and your service provider purchased an ISDN line
from the phone company. For details, read
http://www.alumni.caltech.edu/~dank/isdn/ on the WWW.
These are ISDN modules for your Linux system.
%endif


%if_enabled guest
%if "%sub_flavour" != "guest"
%package -n kernel-modules-guest-%flavour
Summary: Linux guest driver modules
%kernel_modules_package_std_body guest

%description -n kernel-modules-guest-%flavour
This package contains Linux guest driver modules for the kernel package
%name-%version-%release.
%endif
%endif


%if_enabled kvm
%package -n kernel-modules-kvm-%flavour
Summary: Kernel-based Virtual Machine (KVM) modules
%kernel_modules_package_std_body kvm

%description -n kernel-modules-kvm-%flavour
Support hosting fully virtualized guest machines using hardware
virtualization extensions. You will need a fairly recent processor
equipped with virtualization extensions.
These are KVM modules for your Linux system.
%endif


%if_enabled hyperv
%package -n kernel-modules-hyperv-%flavour
Summary: Microsoft Hyper-V client drivers modules
%kernel_modules_package_std_body hyperv

%description -n kernel-modules-hyperv-%flavour
Microsoft Hyper-V client drivers modules.
Install this package to run Linux as a Hyper-V client operating system.
%endif


%if_enabled oprofile
%package -n kernel-modules-oprofile-%flavour
Summary: OProfile system profiling module
%kernel_modules_package_std_body oprofile

%description -n kernel-modules-oprofile-%flavour
OProfile is a profiling system capable of profiling the whole system,
include the kernel, kernel modules, libraries, and applications.
These are OProfile module and vmlinux file for your Linux system.
%endif


%package -n kernel-headers-%flavour-%kernel_branch
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
%{?base_flavour:Provides: kernel-headers-%base_flavour = %version}
Provides: kernel-headers-%flavour = %version-%release
#Obsoletes: kernel-headers-%flavour = %version
Provides: %kheaders_dir/include
AutoProv: no

%description -n kernel-headers-%flavour-%kernel_branch
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).


%package -n kernel-headers-modules-%flavour-%kernel_branch
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
%{?kgcc_version:Requires: gcc%kgcc_version}
Provides: kernel-headers-modules-%flavour = %version-%release
Provides: kernel-devel-%flavour = %version-%release
%{?base_flavour:Provides: kernel-devel-%base_flavour = %version-%release}
Provides: kernel-devel = %version-%release
#Obsoletes: kernel-headers-modules-%flavour = %version
AutoProv: no

%description -n kernel-headers-modules-%flavour-%kernel_branch
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source directory.


%if_with firmware
%package -n firmware-kernel-%flavour
Summary: Firmware for drivers from %name
Group: System/Kernel and hardware
AutoProv: no
AutoReq: no

%description -n firmware-kernel-%flavour
Firmware for drivers from %name.
%endif


%if_with perf
%package -n perf
Summary: Performance analysis tools for Linux
Group: Development/Tools
AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

%description -n perf
Performance counters for Linux are are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features (software
counters, tracepoints) as well.
This package contains performance analysis tools for Linux
%endif


%if_enabled docs
%package -n kernel-doc-%flavour-%kernel_branch
Summary: Linux kernel %kversion-%flavour documentation
%kernel_doc_package_std_body doc

%description -n kernel-doc-%flavour-%kernel_branch
This package contains documentation files for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.


%if_enabled htmldocs
%package -n kernel-docbook-%flavour-%kernel_branch
Summary: Linux kernel %kversion-%flavour HTML API documentation
%kernel_doc_package_std_body docbook

%description -n kernel-docbook-%flavour-%kernel_branch
This package contains API documentation HTML files for Linux kernel
package kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.
%endif


%if_enabled man
%package -n kernel-man-%flavour-%kernel_branch
Summary: Linux kernel %kversion-%flavour man pages
%kernel_doc_package_std_body man
Conflicts: kernel-man > %version-%release
Conflicts: kernel-man < %version-%release

%description -n kernel-man-%flavour-%kernel_branch
This package contains man pages for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The man pages contained in this package may be different from the similar
files in upstream kernel distributions, because some patches applied to
the corresponding kernel packages may change things in the kernel and
update the documentation to reflect these changes.
%endif
%endif


%if_with src
%package -n kernel-src-%flavour-%kernel_branch
Summary: Linux kernel %kversion-%flavour sources
Group: Development/Kernel
%{?base_flavour:Provides: kernel-src-%base_flavour = %version-%release}
Provides: kernel-src-%flavour = %version-%release
BuildArch: noarch
AutoProv: no
AutoReq: no

%description -n kernel-src-%flavour-%kernel_branch
This package contains sources for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
%endif


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
cd linux-%version
#patch0000 -p1

%patch0001 -p1
%patch0002 -p1

%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1

%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1

%patch0040 -p1

%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1

%patch0061 -p1
%patch0062 -p1
%patch0063 -p1

%patch0071 -p1
%patch0072 -p1

%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1

%patch0091 -p1
%patch0092 -p1

%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1

%patch0110 -p1
%patch0111 -p1
%patch0112 -p1

%patch0121 -p1

%patch0131 -p1

%patch0141 -p1
%patch0142 -p1
%patch0143 -p1

%patch0151 -p1

%patch0161 -p1
%patch0162 -p1

%patch0171 -p1
%patch0172 -p1
%patch0173 -p1
%patch0174 -p1
%patch0175 -p1
%patch0176 -p1
%patch0177 -p1
%patch0178 -p1
%patch0179 -p1

%patch0181 -p1
%patch0182 -p1

%patch0190 -p1

%patch0201 -p1
%patch0202 -p1
%patch0203 -p1

%patch0211 -p1
%patch0212 -p1

%patch0220 -p1

%patch0231 -p1
%patch0232 -p1
%patch0233 -p1
%patch0234 -p1

%patch0241 -p1
%patch0242 -p1

%patch0251 -p1
%patch0252 -p1

%patch0261 -p1

%patch0271 -p1
%patch0272 -p1

%patch0281 -p1
%patch0282 -p1
%patch0283 -p1
%patch0284 -p1
%patch0285 -p1
%patch0286 -p1

%patch0291 -p1

%patch0301 -p1

%patch0311 -p1
%patch0312 -p1
%patch0313 -p1
%patch0314 -p1

%patch0321 -p1

%patch0331 -p1
%patch0332 -p1
%patch0333 -p1
%patch0334 -p1
%patch0335 -p1
%patch0336 -p1
%patch0337 -p1
%patch0338 -p1
%patch0339 -p1
%patch0340 -p1
%patch0341 -p1
%patch0342 -p1
%patch0343 -p1
%patch0344 -p1
%patch0345 -p1
%patch0346 -p1
%patch0347 -p1
%patch0348 -p1
%patch0349 -p1
%patch0350 -p1
%patch0351 -p1
%patch0352 -p1
%patch0353 -p1
%patch0354 -p1
%patch0355 -p1
%patch0356 -p1
%patch0357 -p1
%patch0358 -p1
%patch0359 -p1
%patch0360 -p1
%patch0361 -p1
%patch0362 -p1
%patch0363 -p1
%patch0364 -p1
%patch0365 -p1
%patch0366 -p1
%patch0367 -p1
%patch0368 -p1
%patch0369 -p1
%patch0370 -p1
%patch0371 -p1

%patch0381 -p1

%patch0390 -p1
%patch0391 -p1
%patch0392 -p1
%patch0393 -p1
%patch0394 -p1

%patch0401 -p1
%patch0402 -p1

%patch0410 -p1

%patch0421 -p1

%patch0431 -p1
%patch0432 -p1
%patch0433 -p1
%patch0434 -p1
%patch0435 -p1
%patch0436 -p1
%patch0437 -p1
%patch0438 -p1
%patch0439 -p1
%patch0440 -p1
%patch0441 -p1
%patch0442 -p1
%patch0443 -p1
%patch0444 -p1
%patch0445 -p1
%patch0446 -p1
%patch0447 -p1
%patch0448 -p1
%patch0449 -p1
%patch0450 -p1
%patch0451 -p1
%patch0452 -p1
%patch0453 -p1
%patch0454 -p1
%patch0455 -p1
%patch0456 -p1
%patch0457 -p1
%patch0458 -p1
%patch0459 -p1
%patch0460 -p1
%patch0461 -p1
%patch0462 -p1
%patch0463 -p1
%patch0464 -p1
%patch0465 -p1
%patch0466 -p1
%patch0467 -p1
%patch0468 -p1

%patch0471 -p1

%patch0481 -p1

%patch0491 -p1
%patch0492 -p1

%patch0500 -p1
%patch0501 -p1
%patch0502 -p1
%patch0503 -p1
%patch0504 -p1
%patch0505 -p1
%patch0506 -p1
%patch0507 -p1
%patch0508 -p1
%patch0509 -p1
%patch0510 -p1
%patch0511 -p1
%patch0512 -p1
%patch0513 -p1
%patch0514 -p1

%patch0521 -p1
%patch0522 -p1
%patch0523 -p1

%patch0531 -p1

%patch0541 -p1
%patch0542 -p1

%patch0551 -p1

%patch0560 -p1
%patch0561 -p1
%patch0562 -p1
%patch0563 -p1
%patch0564 -p1
%patch0565 -p1
%patch0566 -p1
%patch0567 -p1
%patch0568 -p1
%patch0569 -p1
%patch0570 -p1
%patch0571 -p1
%patch0572 -p1
%patch0573 -p1
%patch0574 -p1
%patch0575 -p1
%patch0576 -p1
%patch0577 -p1

%patch0580 -p1

%patch0591 -p1

%patch0601 -p1

%patch0610 -p1
%patch0611 -p1
%patch0612 -p1
%patch0613 -p1
%patch0614 -p1
%patch0615 -p1
%patch0616 -p1

%patch0620 -p1
%patch0621 -p1

%patch0630 -p1
%patch0631 -p1
%patch0632 -p1
%patch0633 -p1
%patch0634 -p1
%patch0635 -p1
%patch0636 -p1
%patch0637 -p1
%patch0638 -p1
%patch0639 -p1
%patch0640 -p1
%patch0641 -p1

%patch0651 -p1
%patch0652 -p1
%patch0653 -p1
%patch0654 -p1
%patch0655 -p1
%patch0656 -p1
%patch0657 -p1
%patch0658 -p1
%patch0659 -p1
%patch0660 -p1
%patch0661 -p1
%patch0662 -p1
%patch0663 -p1
%patch0664 -p1
%patch0665 -p1
%patch0666 -p1
%patch0667 -p1
%patch0668 -p1
%patch0669 -p1
%patch0670 -p1

%patch0680 -p1

%patch0691 -p1
%patch0692 -p1

%patch0701 -p1
%patch0702 -p1
%patch0703 -p1
%patch0704 -p1
%patch0705 -p1

%patch0711 -p1

%patch0721 -p1


%patch1001 -p1
%patch1002 -p1
%patch1003 -p1

%patch1011 -p1
%patch1012 -p1

%patch1021 -p1

%patch1031 -p1
%patch1032 -p1

%patch1041 -p1

%patch1051 -p1
%patch1052 -p1
%patch1053 -p1

%patch1061 -p1
%patch1062 -p1

%patch1071 -p1

%patch1081 -p1

# fix-fs-*
%patch1091 -p1
%patch1092 -p1
%patch1093 -p1
%patch1094 -p1
%patch1095 -p1
%patch1096 -p1
%patch1097 -p1
%patch1098 -p1
%patch1099 -p1
%patch1100 -p1
%patch1101 -p1
%patch1102 -p1
%patch1103 -p1
%patch1104 -p1

%patch1111 -p1
%patch1112 -p1
%patch1113 -p1

%patch1121 -p1

%patch1131 -p1

%patch1141 -p1

%patch1151 -p1

# get rid of unwanted files resulting from patch fuzz
#find . -name "*.orig" -delete -or -name "*~" -delete

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
%ifdef kgcc_version
GCC_VERSION="%kgcc_version"
%else
GCC_VERSION="$(%__cc --version | head -1 | cut -d' ' -f3 | cut -d. -f1-2)"
%endif
echo -n "export GCC_VERSION=$GCC_VERSION" > gcc_version.inc

sed -i	-e 's/CC.*$(CROSS_COMPILE)gcc/CC\t\t:= '"gcc-$GCC_VERSION/g" Makefile

%{?_with_src:find . -type f -not -empty -not -name '*.orig' -not -name '*~' -not -name '.git*' > ../kernel-src-%flavour.list}

install -m644 %SOURCE1 %SOURCE2 .


%build
cd linux-%version
export ARCH=%base_arch

echo "Building kernel %kversion-%flavour-%krelease"

%make_build distclean

config_disable()
{
local e
while [ -n "$1" ]; do
	e="$e"'/^CONFIG_'$1'=/s|^\(.*\)=.*$|# \1 is not set|;'
	shift
done
sed -i "$e" .config
}

config_enable()
{
local e s a
while [ -n "$1" ]; do
	a=${1%%=*}
	[ "$a" = "$1" ] && s="=y" || s=
	e="$e"'/^#[[:blank:]]*CONFIG_'$a'[[:blank:]]/s/^#[[:blank:]]*\(CONFIG_'$a'\) .*$/\1'$s'/;'
	shift
done
sed -i "$e" .config
}

if [ -f %flavour-%kernel_branch-config-%_target_cpu ]; then
	cp -vf %flavour-%kernel_branch-config-%_target_cpu .config
else
	cp -vf %flavour-%kernel_branch-config-%base_arch .config
%ifdef kernel_cpu
%if "%base_arch" != "%_target_cpu"
	config_disable %kernel_base_cpu
	config_enable M%kernel_cpu
%endif
%endif
fi

sed -i '/^CONFIG_LOCALVERSION=/s/=.*$/="-%flavour-%krelease"/' .config

%ifarch atom
sed -i '/^CONFIG_NR_CPUS=/s/^\(.*=\).*$/\14/' .config
%endif

%ifarch %intel_64
config_disable CPU_SUP_AMD
%endif

%ifarch %amd_64
config_disable CPU_SUP_INTEL
%endif

config_disable \
%if_disabled sound
	SOUND USB_EMI\.* \
%else
	%{?_disable_oss:SOUND_PRIME} %{?_disable_alsa:SND}
%endif
config_disable \
	%{?_disable_smp:SMP} \
	%{?_disable_modversions:MODVERSIONS} \
	%{?_disable_numa:NUMA} \
	%{?_disable_video:FB DISPLAY_SUPPORT VIDEO_OUTPUT_CONTROL BACKLIGHT_LCD_SUPPORT} \
	%{?_disable_drm:DRM} \
	%{?_disable_ipv6:IPV6} \
	%{?_disable_edac:EDAC} \
	%{?_disable_can:CAN} \
	%{?_disable_fusion:FUSION} \
	%{?_disable_ide:IDE} \
	%{?_disable_pata:PATA_.\*} \
	%{?_disable_firewire:FIREWIRE} \
	%{?_disable_irda:IRDA} \
	%{?_disable_joystick:INPUT_JOYSTICK} \
	%{?_disable_tablet:INPUT_TABLET} \
	%{?_disable_touchscreen:INPUT_TOUCHSCREEN} \
	%{?_disable_lirc:LIRC} \
	%{?_disable_gameport:GAMEPORT} \
	%{?_disable_usb_gadget:USB_GADGET} \
	%{?_disable_pcmcia:PCCARD PCMCIA} \
	%{?_disable_atm:ATM} \
	%{?_disable_tokenring:TR} \
	%{?_disable_fddi:FDDI} \
	%{?_disable_hamradio:HAMRADIO} \
	%{?_disable_w1:W1} \
	%{?_disable_watchdog:WATCHDOG} \
	%{?_disable_mtd:MTD} \
	%{?_disable_media:MEDIA_SUPPORT} \
	%{?_disable_mmc:MMC} \
	%{?_disable_wireless:WLAN WIRELESS CFG80211 WIMAX} \
	%{?_disable_isdn:ISDN} \
	%{?_disable_telephony:PHONE} \
	%{?_disable_security:SECURITY} \
	%{?_disable_audit:AUDIT} \
	%{?_disable_selinux:SECURITY_SELINUX} \
	%{?_disable_tomoyo:SECURITY_TOMOYO} \
	%{?_disable_apparmor:SECURITY_APPARMOR} \
	%{?_disable_tomoyo:SECURITY_SMACK} \
	%{?_disable_thp:TRANSPARENT_HUGEPAGE} \
	%{?_disable_guest:VIRTIO DRM_KVM_CIRRUS DRM_VMWGFX} \
	%{?_disable_kvm:KVM} \
	%{?_disable_hyperv:HYPERV} \
	%{?_disable_paravirt_guest:PARAVIRT_GUEST} \
	%{?_disable_kvm_guest:KVM_GUEST} \
	%{?_disable_bootsplash:BOOTSPLASH} \
	%{?_disable_zcache:ZCACHE} \
	%{?_disable_pci:PCI} \
	%{?_disable_mca:MCA} \
	%{?_disable_acpi:ACPI} \
	%{?_disable_math_emu:MATH_EMULATION} \
	%{?_disable_kallsyms:KALLSYMS} \
	%{?_disable_oprofile:PROFILING OPROFILE} \
	%{?_disable_fatelf:BINFMT_FATELF} \
	%{?_enable_ext4_for_ext23:EXT[23]_FS}

%ifarch i386 i486 i586 i686
config_enable X86_GENERIC
%endif

config_enable \
	%{?_enable_debug_section_mismatch:DEBUG_SECTION_MISMATCH} \
	%{?_enable_modversions:MODVERSIONS} \
	%{?_enable_ext4_for_ext23:EXT4_USE_FOR_EXT23} \
	%{?_enable_debugfs:DEBUG_FS} \
	%{?_enable_pcsp:SND_PCSP=m} \
	%{?_enable_secrm:EXT[234]_SECRM FAT_SECRM} \
	%{?_enable_nfs_swap:NFS_SWAP} \
	%{?_enable_kallsyms:KALLSYMS} \
	%allocator

# arch-specific disables
%ifarch k8 k9 k10
config_disable SENSORS_APPLESMC SENSORS_CORETEMP SENSORS_I5K_AMB
%endif
%ifarch k10 core2 atom penryn nehalem
config_disable SENSORS_K8TEMP
%endif
%ifarch core2 atom penryn nehalem
config_disable SENSORS_K10TEMP
%endif
%ifarch %x86_64
config_disable SENSORS_ABITUGURU HW_RANDOM_AMD HW_RANDOM_INTEL
%endif

%if_enabled debug
config_enable \
	KALLSYMS_ALL \
	KALLSYMS_EXTRA_PASS \
	DEBUG_KERNEL \
	DETECT_SOFTLOCKUP \
	BOOTPARAM_SOFTLOCKUP_PANIC_VALUE=0 \
	DEBUG_MUTEXES \
	DEBUG_SLAB \
	DEBUG_SLAB_LEAK \
%if 0
	DEBUG_SPINLOCK \
	DEBUG_LOCK_ALLOC \
	PROVE_LOCKING \
	LOCK_STAT \
%endif
	LOCKDEP \
	DEBUG_LOCKDEP \
	DEBUG_SPINLOCK_SLEEP \
	DEBUG_BUGVERBOSE \
	DEBUG_INFO \
	DEBUG_WRITECOUNT \
	FRAME_POINTER
%endif

%ifarch %intel_64 %intel_32 c3 c3_2
sed -i '/^CONFIG_USB_OHCI_HCD=y$/s/=y/=m/' .config
%else
%ifnarch i386 i486 i586 i686 x86_64
sed -i '/^CONFIG_USB_UHCI_HCD=y$/s/=y/=m/' .config
%endif
%endif

%make_build oldconfig
%make_build %{?_enable_verbose:V=1} bzImage modules
%if_with perf
%make_build -C tools/perf %{?_enable_verbose:V=1} \
	prefix=%_prefix perfexecdir=%_libexecdir/perf \
	EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}"
%make_build -C tools/perf %{?_enable_verbose:V=1} man
%endif

echo "Kernel built %kversion-%flavour-%krelease"

# psdocs, pdfdocs don't work yet
%{?_enable_htmldocs:%def_enable builddocs}
%{?_enable_man:%def_enable builddocs}
%if_enabled builddocs
%{?_enable_htmldocs:%make_build htmldocs}
%{?_enable_man:%make_build mandocs 2>&1 | tee mandocs.log | grep -vE --line-buffered '^((Warn|Note): (meta author |AUTHOR sect\.):|Note: Writing) '}
echo "Kernel docs built %kversion-%flavour-%krelease"
%endif


%install
export ARCH=%base_arch
pushd linux-%version

install -Dp -m644 System.map %buildroot/boot/System.map-%kversion-%flavour-%krelease
install -Dp -m644 arch/%base_arch/boot/bzImage %buildroot/boot/vmlinuz-%kversion-%flavour-%krelease
install -Dp -m644 .config %buildroot/boot/config-%kversion-%flavour-%krelease

%make_install \
	INSTALL_MOD_PATH=%buildroot \
	INSTALL_FW_PATH=%buildroot%firmware_dir \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	modules_install

%{?_enable_oprofile:install -m 0644 vmlinux %buildroot%modules_dir/}

install -d -m 0755 %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/
find %buildroot%kbuild_dir/include/config -type f -empty -delete
find %buildroot%kbuild_dir/include/config -type d -empty -delete
for d in arch/%kernel_arch/include; do
	a="$(dirname "$d")"
	install -d -m 0755 %buildroot%kbuild_dir/$a
	cp -a $d %buildroot%kbuild_dir/$a/
	install -p -m 0644 $a/Makefile* %buildroot%kbuild_dir/$a/
done
find %buildroot%kbuild_dir/{include,arch} -type f -name Kbuild -delete

%if 0
# drivers-headers install
install -d -m 0755 %buildroot%kbuild_dir/{drivers/{scsi,md,usb/core,net/wireless},net/mac80211,kernel,lib}
install -m 0644 drivers/scsi/scsi{{,_typedefs}.h,_module.c} %buildroot%kbuild_dir/drivers/scsi/
install -m 0644 drivers/md/dm*.h %buildroot%kbuild_dir/drivers/md/
install -m 0644 drivers/usb/core/*.h %buildroot%kbuild_dir/drivers/usb/core/
install -m 0644 drivers/net/wireless/Kconfig %buildroot%kbuild_dir/drivers/net/wireless/
install -m 0644 lib/hexdump.c %buildroot%kbuild_dir/lib/
install -m 0644 kernel/workqueue.c %buildroot%kbuild_dir/kernel/
install -m 0644 net/mac80211/{ieee80211_i,sta_info}.h %buildroot%kbuild_dir/net/mac80211/
%endif

# Install files required for building external modules (in addition to headers)
for f in \
	.config \
	Makefile \
	Module.symvers \
	scripts/Kbuild.include \
	scripts/Makefile{,.{build,clean,host,lib,mod*}} \
	scripts/bin2c \
	scripts/check{includes,version}.pl \
	scripts/conmakehash \
	scripts/extract-ikconfig \
	scripts/gcc-*.sh \
	scripts/kallsyms \
	scripts/makelst \
	scripts/mk{compile_h,makefile,version} \
	scripts/module-common.lds \
	%{?_enable_video:scripts/pnmtologo} \
	scripts/recordmcount.pl \
	scripts/basic/fixdep \
	%{?_enable_modversions:scripts/genksyms/genksyms} \
	scripts/kconfig/conf \
	scripts/mod/{modpost,mk_elfconfig} \
	gcc_version.inc
do
	[ -x "$f" ] && mode=0755 || mode=0644
	install -Dp -m $mode {,%buildroot%kbuild_dir/}$f
done

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make -j%__nprocs headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir
find %buildroot%kheaders_dir -type f -a \( -name .install -o -name ..install.cmd \) -delete

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

%if_with perf
%makeinstall_std -C tools/perf prefix=%_prefix perfexecdir=%_libexecdir/perf install install-man
install -d -m 0755 %buildroot%_docdir/perf-%version
install -m 0644 tools/perf/{CREDITS,design.txt,Documentation/examples.txt} %buildroot%_docdir/perf-%version/
%endif

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%flavour-%kernel_branch/
for I in Documentation/*; do
	case "$(basename "$I")" in
		DocBook)
%if_enabled htmldocs
			for J in "$I"/*; do
				if [ -d "$J" ]; then
					j=$(basename "$J")
					case "$j" in
						man|dvb|v4l) ;;
						*)
							install -d -m 0755 %buildroot%_docdir/kernel-doc-%flavour-%kernel_branch/DocBook/"$j"
							install -m 0644 "$J"/*.html %buildroot%_docdir/kernel-doc-%flavour-%kernel_branch/DocBook/"$j"/
							;;
					esac
				fi
			done
			install -m 0644 "$I"/*.html %buildroot%_docdir/kernel-doc-%flavour-%kernel_branch/DocBook/
%endif
			;;
		[a-z][a-z]_[A-Z][A-Z]|Makefile|dontdiff) ;;
		*) cp -aL "$I" %buildroot%_docdir/kernel-doc-%flavour-%kernel_branch/ ;;
	esac
done
find %buildroot%_docdir/kernel-doc-%flavour-%kernel_branch -type f -name Makefile -delete
%if_enabled man
install -d %buildroot%kmandir
install -m 0644 Documentation/DocBook/man/* %buildroot%kmandir/
%endif
%endif

%if_with src
install -d -m 0755 %buildroot%kernel_src
tar --transform='s,^,kernel-src-%flavour-%kversion-%krelease/,' \
	--owner=root --group=root --mode=u+w,go-w,go+rX \
	-T ../kernel-src-%flavour.list -cf - | \
	pxz -8e -T%__nprocs > %buildroot%kernel_src/kernel-src-%flavour-%kversion-%krelease.tar.xz
%endif

popd

rm -rf *.rpmmodlist{,~}
gen_rpmmodlist() {
	ls -d $@ | sed 's|^%buildroot||'
}
gen_rpmmodfile() {
	local F=$1.rpmmodlist
	shift
	gen_rpmmodlist $@ > $F
}
gen_rpmmodfile scsi-base \
%if "%sub_flavour" == "guest"
	%buildroot%modules_dir/kernel/drivers/scsi/{{,lib}iscsi*,scsi_transport_iscsi.ko} \
%endif
	%buildroot%modules_dir/kernel/drivers/scsi/{{*_mod,scsi_{tgt,transport_srp}}.ko,osd,device_handler{,/scsi_dh.ko}}
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/{message/fusion,scsi{,/device_handler}/*} | grep -Fxv -f scsi-base.rpmmodlist > scsi.rpmmodlist
mv scsi-base.rpmmodlist scsi-base.rpmmodlist~
gen_rpmmodfile infiniband %buildroot%modules_dir/kernel/{drivers/{infiniband,scsi/scsi_transport_srp.ko},net/{9p/9pnet_rdma.ko,rds,sunrpc/xprtrdma}}
gen_rpmmodfile ipmi %buildroot%modules_dir/kernel/drivers/{char/ipmi,hwmon/ibm*.ko}
%{?_enable_atm:gen_rpmmodfile atm %buildroot%modules_dir/kernel/{drivers{,/usb},net}/atm}
%{?_enable_drm:gen_rpmmodfile drm %buildroot%modules_dir/kernel/drivers/gpu/drm}
%{?_enable_fddi:gen_rpmmodfile fddi %buildroot%modules_dir/kernel/{drivers/net/{defxx.ko,skfp},net/802/fddi.ko}}
%{?_enable_hamradio:gen_rpmmodfile hamradio %buildroot%modules_dir/kernel/{drivers/net/hamradio,net/{netrom,rose,ax25}}}
%{?_enable_irda:gen_rpmmodfile irda %buildroot%modules_dir/kernel/{,drivers/}net/irda}
%{?_enable_isdn:gen_rpmmodfile isdn %buildroot%modules_dir/kernel/{drivers/isdn,net/bluetooth/cmtp}}
%{?_enable_tokenring:gen_rpmmodfile tokenring %buildroot%modules_dir/kernel/{drivers/net/{tokenring,pcmcia/ibmtr_cs.ko},net/802/tr.ko}}
%{?_enable_usb_gadget:gen_rpmmodfile usb-gadget %buildroot%modules_dir/kernel/drivers/usb/gadget}
%{?_enable_video:gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/video/* | grep -xv '%modules_dir/kernel/drivers/video/uvesafb.ko' > video.rpmmodlist}
%{?_enable_watchdog:gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/watchdog/* | grep -xv '%modules_dir/kernel/drivers/watchdog/softdog.ko' > watchdog.rpmmodlist}
%{?_enable_wireless:gen_rpmmodfile net-wireless %buildroot%modules_dir/kernel/{{,drivers/}net/wi{max,reless},net/mac80211}}
for i in %{?_enable_ide:ide} %{?_enable_media:media} %{?_enable_mtd:mtd} %{?_enable_w1:w1}; do
	gen_rpmmodfile $i %buildroot%modules_dir/kernel/drivers/$i
done
for i in %{?_enable_joystick:joystick} %{?_enable_lirc:lirc} %{?_enable_tablet:tablet} %{?_enable_touchscreen:touchscreen}; do
	gen_rpmmodfile $i %buildroot%modules_dir/kernel/drivers/input/$i
done
%if "%sub_flavour" != "guest"
%{?_enable_guest:gen_rpmmodfile guest %buildroot%modules_dir/kernel/drivers/{virtio,{char{,/hw_random},net,block}/virtio*%{?_enable_drm:,gpu/drm/{cirrus,vmwgfx}}}}
%{?_enable_drm:grep -F -f drm.rpmmodlist guest.rpmmodlist | sed 's/^/%%exclude &/' >> drm.rpmmodlist}
%endif
sed 's/^/%%exclude &/' *.rpmmodlist > exclude-drivers.rpmmodlist

%{?_enable_oprofile:%add_verify_elf_skiplist %modules_dir/vmlinux}


%post
if ! [ -x /usr/lib/rpm/boot_kernel.filetrigger ]; then
	%post_kernel_image %kversion-%flavour-%krelease
fi

%preun
if ! [ -x /usr/lib/rpm/boot_kernel.filetrigger ]; then
	%preun_kernel_image %kversion-%flavour-%krelease
fi


%kernel_modules_package_post scsi

%kernel_modules_package_post infiniband

%kernel_modules_package_post ipmi

%{?_enable_video:%kernel_modules_package_post video}

%{?_enable_irda:%kernel_modules_package_post irda}

%{?_enable_joystick:%kernel_modules_package_post joystick}

%{?_enable_tablet:%kernel_modules_package_post tablet}

%{?_enable_touchscreen:%kernel_modules_package_post touchscreen}

%{?_enable_lirc:%kernel_modules_package_post lirc}

%{?_enable_usb_gadget:%kernel_modules_package_post usb-gadget}

%{?_enable_atm:%kernel_modules_package_post atm}

%{?_enable_hamradio:%kernel_modules_package_post hamradio}

%{?_enable_w1:%kernel_modules_package_post w1}

%{?_enable_watchdog:%kernel_modules_package_post watchdog}

%{?_enable_mtd:%kernel_modules_package_post mtd}

%{?_enable_wireless:%kernel_modules_package_post net-wireless}

%kernel_modules_package_post fs-extra

%kernel_modules_package_post net-extra

%{?_enable_oss:%kernel_modules_package_post oss}

%{?_enable_ide:%kernel_modules_package_post ide}

%{?_enable_drm:%kernel_modules_package_post drm}

%{?_enable_media:%kernel_modules_package_post media}

%{?_enable_alsa:%kernel_modules_package_post alsa}

%{?_enable_isdn:%kernel_modules_package_post isdn}

%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_post guest}
%endif

%{?_enable_kvm:%kernel_modules_package_post kvm}

%{?_enable_hyperv:%kernel_modules_package_post hyperv}

%{?_enable_oprofile:%kernel_modules_package_post oprofile}

%post -n kernel-headers-%flavour-%kernel_branch
%post_kernel_headers %kversion-%flavour-%krelease

%postun -n kernel-headers-%flavour-%kernel_branch
%postun_kernel_headers %kversion-%flavour-%krelease


%files -f exclude-drivers.rpmmodlist
/boot/*
%dir %modules_dir
%modules_dir/modules.alias*
%modules_dir/modules.builtin
%modules_dir/modules.dep*
%modules_dir/modules.order
%modules_dir/modules.symbols*
#modules_dir/modules.*map
%ghost %modules_dir/modules.builtin.bin
%ghost %modules_dir/modules.devname
%ghost %modules_dir/modules.softdep
%dir %modules_dir/kernel
%modules_dir/kernel/arch
%modules_dir/kernel/block
%modules_dir/kernel/crypto
%modules_dir/kernel/drivers
%modules_dir/kernel/fs
%modules_dir/kernel/kernel
%modules_dir/kernel/lib
%modules_dir/kernel/net
%modules_dir/kernel/security
%if_enabled sound
%dir %modules_dir/kernel/sound
%{?_enable_pci:%modules_dir/kernel/sound/ac97_bus.ko}
%modules_dir/kernel/sound/soundcore.ko
%endif
%{?_enable_kvm:%exclude %modules_dir/kernel/arch/*/kvm}
%if_enabled hyperv
%exclude %modules_dir/kernel/drivers/hv
%exclude %modules_dir/kernel/drivers/hid/hid-hyperv.ko
%exclude %modules_dir/kernel/drivers/net/hyperv
%exclude %modules_dir/kernel/drivers/scsi/hv_storvsc.ko
%endif
%if_enabled oprofile
%exclude %modules_dir/vmlinux
%exclude %modules_dir/kernel/arch/*/oprofile
%endif
# extra fs
%exclude %modules_dir/kernel/fs/afs
%exclude %modules_dir/kernel/fs/adfs
%exclude %modules_dir/kernel/fs/affs
%exclude %modules_dir/kernel/fs/befs
%exclude %modules_dir/kernel/fs/bfs
%exclude %modules_dir/kernel/fs/coda
%exclude %modules_dir/kernel/fs/dlm
%exclude %modules_dir/kernel/fs/efs
%exclude %modules_dir/kernel/fs/exofs
%exclude %modules_dir/kernel/fs/freevxfs
%exclude %modules_dir/kernel/fs/gfs2
%exclude %modules_dir/kernel/fs/hfs*
%exclude %modules_dir/kernel/fs/hpfs
%exclude %modules_dir/kernel/fs/minix
%exclude %modules_dir/kernel/fs/ncpfs
%exclude %modules_dir/kernel/fs/ocfs2
%exclude %modules_dir/kernel/fs/omfs
%exclude %modules_dir/kernel/fs/qnx4
%exclude %modules_dir/kernel/fs/sysv
%exclude %modules_dir/kernel/fs/ufs
%if_enabled mtd
%exclude %modules_dir/kernel/fs/jffs2
%exclude %modules_dir/kernel/fs/romfs
%exclude %modules_dir/kernel/fs/ubifs
%endif
# extra net
%exclude %modules_dir/kernel/net/802/p8023.ko
%exclude %modules_dir/kernel/net/appletalk
%exclude %modules_dir/kernel/drivers/net/appletalk
%{?_enable_can:%exclude %modules_dir/kernel/net/can}
%{?_enable_can:%exclude %modules_dir/kernel/drivers/net/can}
%exclude %modules_dir/kernel/net/batman-adv
%exclude %modules_dir/kernel/net/caif
%exclude %modules_dir/kernel/net/dccp
%exclude %modules_dir/kernel/net/decnet
%exclude %modules_dir/kernel/net/econet
%exclude %modules_dir/kernel/net/ieee802154
%exclude %modules_dir/kernel/drivers/ieee802154
%exclude %modules_dir/kernel/net/ipx
%exclude %modules_dir/kernel/net/lapb
%exclude %modules_dir/kernel/net/llc/llc2.ko
%exclude %modules_dir/kernel/net/phonet
%exclude %modules_dir/kernel/drivers/net/usb/cdc-phonet.ko
%exclude %modules_dir/kernel/net/rxrpc
%exclude %modules_dir/kernel/net/sctp
%exclude %modules_dir/kernel/net/tipc
%exclude %modules_dir/kernel/net/wanrouter
%exclude %modules_dir/kernel/drivers/net/wan
%exclude %modules_dir/kernel/drivers/tty/synclink*
%{?_enable_pcmcia:%exclude %modules_dir/kernel/drivers/char/pcmcia/synclink*}
%exclude %modules_dir/kernel/net/x25


%kernel_modules_package_files scsi
%{?_enable_hyperv:%exclude %modules_dir/kernel/drivers/scsi/hv_storvsc.ko}


%kernel_modules_package_files infiniband

%kernel_modules_package_files ipmi


%{?_enable_video:%kernel_modules_package_files video}

%{?_enable_irda:%kernel_modules_package_files irda}

%{?_enable_joystick:%kernel_modules_package_files joystick}

%{?_enable_tablet:%kernel_modules_package_files tablet}

%{?_enable_touchscreen:%kernel_modules_package_files touchscreen}

%{?_enable_lirc:%kernel_modules_package_files lirc}

%{?_enable_usb_gadget:%kernel_modules_package_files usb-gadget}

%{?_enable_atm:%kernel_modules_package_files atm}

%{?_enable_hamradio:%kernel_modules_package_files hamradio}

%{?_enable_w1:%kernel_modules_package_files w1}

%{?_enable_watchdog:%kernel_modules_package_files watchdog}

%{?_enable_mtd:%kernel_modules_package_files mtd}

%{?_enable_wireless:%kernel_modules_package_files net-wireless}


%files -n kernel-modules-fs-extra-%flavour
%modules_dir/kernel/fs/afs
%modules_dir/kernel/fs/adfs
%modules_dir/kernel/fs/affs
%modules_dir/kernel/fs/befs
%modules_dir/kernel/fs/bfs
#modules_dir/kernel/fs/ceph
%modules_dir/kernel/fs/coda
%modules_dir/kernel/fs/dlm
%modules_dir/kernel/fs/efs
%modules_dir/kernel/fs/exofs
%modules_dir/kernel/fs/freevxfs
%modules_dir/kernel/fs/gfs2
%modules_dir/kernel/fs/hfs*
%modules_dir/kernel/fs/hpfs
%modules_dir/kernel/fs/minix
%modules_dir/kernel/fs/ncpfs
%modules_dir/kernel/fs/ocfs2
%modules_dir/kernel/fs/omfs
%modules_dir/kernel/fs/qnx4
%modules_dir/kernel/fs/sysv
%modules_dir/kernel/fs/ufs
%if_enabled mtd
%modules_dir/kernel/fs/jffs2
%modules_dir/kernel/fs/romfs
%modules_dir/kernel/fs/ubifs
%endif


%files -n kernel-modules-net-extra-%flavour
%modules_dir/kernel/net/802/p8023.ko
%modules_dir/kernel/net/appletalk
%modules_dir/kernel/drivers/net/appletalk
%if_enabled can
%modules_dir/kernel/net/can
%modules_dir/kernel/drivers/net/can
%endif
%if_enabled tokenring
%{?_enable_pcmcia:%modules_dir/kernel/drivers/net/pcmcia/ibmtr_cs.ko}
%modules_dir/kernel/drivers/net/tokenring
%modules_dir/kernel/net/802/tr.ko
%endif
%if_enabled fddi
%modules_dir/kernel/drivers/net/defxx.ko
%modules_dir/kernel/drivers/net/skfp
%modules_dir/kernel/net/802/fddi.ko
%endif
%modules_dir/kernel/net/batman-adv
%modules_dir/kernel/net/caif
#modules_dir/kernel/net/ceph
%modules_dir/kernel/net/dccp
%modules_dir/kernel/net/decnet
%modules_dir/kernel/net/econet
%modules_dir/kernel/net/ieee802154
%modules_dir/kernel/drivers/ieee802154
%modules_dir/kernel/net/ipx
%modules_dir/kernel/net/lapb
%modules_dir/kernel/net/llc/llc2.ko
%modules_dir/kernel/net/phonet
%modules_dir/kernel/drivers/net/usb/cdc-phonet.ko
%modules_dir/kernel/net/rxrpc
%modules_dir/kernel/net/sctp
%modules_dir/kernel/net/tipc
%modules_dir/kernel/net/wanrouter
%modules_dir/kernel/drivers/net/wan
%modules_dir/kernel/drivers/tty/synclink*
%{?_enable_pcmcia:%modules_dir/kernel/drivers/char/pcmcia/synclink*}
%modules_dir/kernel/net/x25


%if_enabled oss
%files -n kernel-modules-oss-%flavour
%modules_dir/kernel/sound/oss
%modules_dir/kernel/sound/sound_firmware.ko
%endif


%if_enabled alsa
%files -n kernel-modules-alsa-%flavour
%modules_dir/kernel/sound
%{?_enable_oss:%exclude %modules_dir/kernel/sound/oss}
%exclude %modules_dir/kernel/sound/*.ko
%endif


%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_files guest}
%endif


%if_enabled kvm
%files -n kernel-modules-kvm-%flavour
%modules_dir/kernel/arch/*/kvm
%endif


%if_enabled hyperv
%files -n kernel-modules-hyperv-%flavour
%modules_dir/kernel/drivers/hv
%modules_dir/kernel/drivers/hid/hid-hyperv.ko
%modules_dir/kernel/drivers/net/hyperv
%modules_dir/kernel/drivers/scsi/hv_storvsc.ko
%endif


%files -n kernel-headers-%flavour-%kernel_branch
%kheaders_dir


%files -n kernel-headers-modules-%flavour-%kernel_branch
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build


%{?_enable_ide:%kernel_modules_package_files ide}

%{?_enable_drm:%kernel_modules_package_files drm}

%{?_enable_media:%kernel_modules_package_files media}

%{?_enable_isdn:%kernel_modules_package_files isdn}


%if_enabled oprofile
%files -n kernel-modules-oprofile-%flavour
%modules_dir/vmlinux
%modules_dir/kernel/arch/*/oprofile
%endif


%if_with firmware
%files -n firmware-kernel-%flavour
%dir %firmware_dir
%{?_enable_atm:%{?_enable_pci:%firmware_dir/atm*}}
%firmware_dir/3com
%firmware_dir/acenic
%firmware_dir/adaptec
%firmware_dir/advansys
%firmware_dir/bnx2*
%{?_enable_pcmcia:%firmware_dir/cis}
%firmware_dir/cxgb3
%firmware_dir/e100
%firmware_dir/edgeport
%{?_enable_sound:%firmware_dir/emi*}
%firmware_dir/isci
%firmware_dir/kaweth
%firmware_dir/keyspan*
%firmware_dir/mts_*
%{?_enable_pcmcia:%firmware_dir/ositech}
%firmware_dir/qlogic
%firmware_dir/sun
%firmware_dir/tehuti
%firmware_dir/ti_*
%firmware_dir/tigon
%{?_enable_hamradio:%firmware_dir/yam}
%ifarch %ix86
%{?_enable_tokenring:%firmware_dir/tr_smctr.*}
%endif
%firmware_dir/whiteheat*
%if_enabled alsa
%{?_enable_pci:%firmware_dir/ess}
%{?_enable_pci:%firmware_dir/korg}
%ifarch %ix86
%firmware_dir/sb16
%endif
%{?_enable_pci:%firmware_dir/yamaha}
%endif
%if_enabled drm
%firmware_dir/matrox
%firmware_dir/r128
%firmware_dir/radeon
%endif
%if_enabled media
%firmware_dir/av7110
%firmware_dir/cpia2
%firmware_dir/ttusb*
%firmware_dir/vicam
%endif
%endif


%if_with perf
%files -n perf
%doc %_docdir/perf-%version
%_bindir/*
%exclude %_libexecdir
%_man1dir/*
%endif


%if_enabled docs
%files -n kernel-doc-%flavour-%kernel_branch
%doc %_docdir/kernel-doc-%flavour-%kernel_branch
%{?_enable_htmldocs:%exclude %_docdir/kernel-doc-%flavour-%kernel_branch/DocBook}


%if_enabled htmldocs
%files -n kernel-docbook-%flavour-%kernel_branch
%doc %dir %_docdir/kernel-doc-%flavour-%kernel_branch
%doc %_docdir/kernel-doc-%flavour-%kernel_branch/DocBook
%endif


%if_enabled man
%files -n kernel-man-%flavour-%kernel_branch
%kmandir
%endif
%endif


%if_with src
%files -n kernel-src-%flavour-%kernel_branch
%kernel_src/*
%endif


%changelog
* Tue Sep 25 2012 Led <led@altlinux.ru> 3.0.43-alt7
- updated:
  + fix-arch-x86-cpu--perf-event
  + fix-net-core
  + feat-fs-overlayfs
  + feat-fs-reiser4
- added:
  + feat-fs-binfmt_elf--fatelf
  + feat-mm--slqb
- build with SLQB allocator

* Sat Sep 22 2012 Led <led@altlinux.ru> 3.0.43-alt6
- updated:
  + fix-arch-x86--mcheck
  + fix-block
  + fix-drivers-gpu-drm
  + fix-drivers-gpu-drm--drm
  + fix-drivers-gpu-drm--i915
  + fix-drivers-net--igb
  + fix-drivers-scsi--sd_mod
  + fix-drivers-scsi-device_handler--scsi_dh_rdac
  + fix-fs
  + fix-kernel
  + fix-net-ipv4
  + feat-fs-overlayfs
- added:
  + fix-drivers-net--sfc
  + fix-net-rds--rds
  + feat-fs-reiser4
- disabled feat-fs-overlayfs

* Thu Sep 20 2012 Led <led@altlinux.ru> 3.0.43-alt5
- updated:
  + fix-drivers-scsi--sd_mod
  + fix-drivers-scsi-device_handler--scsi_dh_alua
  + fix-drivers-scsi-megaraid--megaraid_sas
  + fix-fs-btrfs
  + fix-mm--memcontrol
- added:
  + fix-arch-ia64
  + fix-drivers-pci--sn
  + feat-fs-overlayfs
  + feat-kernel--cpe_migrate

* Tue Sep 18 2012 Led <led@altlinux.ru> 3.0.43-alt4
- updated:
  + fix-drivers-misc--zcache
  + fix-fs-btrfs
- added:
  + fix-drivers-gpu-drm--vmwgfx
  + feat-drivers-block--cloop
  + feat-drivers-gpu-drm--cirrus
- enabled modesetting by default:
  + DRM_RADEON_KMS
  + DRM_I915_KMS
- enabled DRM_VMWGFX
- renamed kernel-modules-virtio-* to kernel-module-guest-*

* Mon Sep 17 2012 Led <led@altlinux.ru> 3.0.43-alt3
- updated:
  + fix-drivers-scsi--aha152x
  + fix-fs-proc
  + feat-fs-aufs
- added:
  + feat-kernel-power-tuxonice

* Mon Sep 17 2012 Led <led@altlinux.ru> 3.0.43-alt2
- updated:
  + fix-kernel
- added:
  + fix-drivers-usb-usbip--usbip-host
  + feat-drivers-block--zram
  + feat-drivers-misc--xvmalloc
  + feat-drivers-misc--zcache
  + feat-drivers-usb-usbip
  + feat-kernel--sched-cfs-boost
- enabled:
  + SCHED_SYSCTL
  + SCHED_CFS_BOOST

* Sun Sep 16 2012 Led <led@altlinux.ru> 3.0.43-alt1
- 3.0.43
- removed:
  + fix-kernel--audit_tree
- updated:
  + fix-drivers-block--cciss
  + fix-fs
  + fix-fs-proc
  + fix-kernel
  + fix-mm
  + fix-mm--hugetlb
  + feat-fs-unionfs
- added:
  + fix-security--security
  + feat-fs-aufs
- disabled SCHED_DEBUG

* Sat Sep 15 2012 Led <led@altlinux.ru> 3.0.42-alt7
- updated:
  + fix-drivers-gpu-drm
  + fix-drivers-gpu-drm--i915
  + fix-drivers-gpu-drm--radeon
  + fix-drivers-scsi--scsi_mod
  + fix-drivers-target--tcm_fc
  + fix-fs
  + fix-fs-btrfs
  + fix-fs-nfs
  + fix-sound-pci-hda
- added:
  + fix-arch-x86-platform-olpc
  + fix-drivers-eisa--pci_eisa
  + fix-drivers-gpu-drm--mga
  + fix-drivers-gpu-drm--via
  + fix-drivers-i2c--i2c-pxa
  + fix-drivers-i2c-busses--scx200_acb
  + fix-drivers-mmc-card--mmc_block
  + fix-drivers-net--3c509
  + fix-drivers-net--3c59x
  + fix-drivers-net--at1700
  + fix-drivers-net--depca
  + fix-drivers-net--hp100
  + fix-drivers-net--ne3210
  + fix-drivers-net-tulip--de4x5
  + fix-drivers-scsi--aha1542
  + fix-drivers-scsi--sim710
  + fix-fs-ceph
  + fix-fs-ecryptfs
  + feat-block--bfq-iosched
  + feat-fs-squashfs--write
- use ext4 driver for ext2 and ext3
- enabled CONFIG_CEPH_FS

* Thu Sep 13 2012 Led <led@altlinux.ru> 3.0.42-alt6
- updated:
  + fix-drivers-scsi--st
  + fix-fs-btrfs
- without perf
- build docs and src for i586

* Wed Sep 12 2012 Led <led@altlinux.ru> 3.0.42-alt5
- updated:
  + fix-block--blk-integrity
  + fix-drivers-scsi--mvsas
  + fix-drivers-scsi--pm8001
  + fix-drivers-video-via
- added:
  + fix-drivers-leds--leds-lp5521
  + fix-drivers-net-pcmcia--nmclan_cs
  + fix-drivers-telephony--ixj
  + fix-drivers-video--intelfb
  + fix-fs-cifs

* Tue Sep 11 2012 Led <led@altlinux.ru> 3.0.42-alt4
- updated:
  + fix-drivers-infiniband-hw-mlx4
- added:
  + fix-block--blk-integrity
  + fix-drivers-ata--sata_sil
  + fix-drivers-block--DAC960
  + fix-drivers-block--drbd
  + fix-drivers-dma--dmatest
  + fix-drivers-gpu-drm--drm_kms_helper
  + fix-drivers-edac--i7300_edac
  + fix-drivers-hwmon--applesmc
  + fix-drivers-media-common-tuners--max2165
  + fix-drivers-misc--vmw_balloon
  + fix-sound-pci-rme9652--snd-hdspm

* Sat Sep 08 2012 Led <led@altlinux.ru> 3.0.42-alt3
- updated:
  + fix-drivers-gpu-drm--drm
  + fix-drivers-gpu-drm--i915
  + fix-fs-btrfs
- added kernel-modules-hyperv-* subpackage

* Fri Sep 07 2012 Led <led@altlinux.ru> 3.0.42-alt2
- updated:
  + fix-drivers-md--dm-mod
  + fix-drivers-net-mlx4--mlx4_en
  + fix-drivers-scsi--mpt2sas
  + fix-virt-kvm
- added:
  + fix-drivers-isdn-gigaset--gigaset
  + fix-drivers-net-wireless-libertas--libertas_spi
  + fix-drivers-platform--hdaps
  + fix-drivers-rtc--rtc-m41t80
  + fix-drivers-video-via
  + fix-fs--bio-integrity
  + fix-sound-usb-misc--snd-ua101
  + feat-block--sio-iosched
  + feat-drivers-platform--thinkpad_ec
  + feat-drivers-platform--tp_smapi
  + feat-fs-unionfs
- set SIO as default I/O scheduler
- disabled nfs_swap

* Fri Sep 07 2012 Led <led@altlinux.ru> 3.0.42-alt1
- zero build
