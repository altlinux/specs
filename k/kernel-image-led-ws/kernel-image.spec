%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_with() %{expand:%%force_with %{1}} %{expand:%%undefine _without_%{1}}
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%define intel_64 nocona core2 penryn corei7 nehalem
%define intel_32 pentium pentiumpro pentium_mmx pentium2 pentium3 pentium_m pentium4 prescott atom
%define amd_32 5x86 k5 k6 k6_2 k6_3 geode k7 athlon athlon_xp
%define amd_64 opteron k8 k9 k10 barcelona phenom
%define via_64 nano
%define via_32 c3 c3_2
%define x86_64 x86_64 %intel_64 %amd_64 %via_64

%define extra_modules %nil
%define Extra_modules() BuildRequires: kernel-source-%1 = %2 \
%global extra_modules %extra_modules %1=%2

%define base_flavour led
%define sub_flavour ws
%define flavour %base_flavour-%sub_flavour

Name: kernel-image-%flavour
Version: 3.0.61
Release: alt3

%define kernel_req %nil
%define kernel_prov %nil
%define kernel_branch 3.0
%define kernel_stable_version 61
%define kernel_extra_version .%kernel_stable_version
#define kernel_extra_version %nil

%define krelease %release

%define kmandir %{_man9dir}l
# Build options
# You can change compiler version by editing this line:
%define kgcc_version	4.7

%def_enable smp
%def_disable verbose
%def_disable debug
%def_disable modversions
%def_enable kallsyms
%def_with src
%def_enable docs
%def_enable htmldocs
%def_enable man
%def_disable compat
%def_disable x32
%def_disable debugfs
%def_disable numa
%def_enable acpi
%def_enable pci
%def_disable mca
%def_disable math_emu
%def_disable x86_extended_platform
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
%def_enable yama
%def_enable thp
%def_enable kvm
%def_enable hyperv
%def_disable paravirt_guest
%def_disable kvm_quest
%def_disable nfs_swap
%def_enable fatelf
%def_with lnfs
%def_without x32
%def_enable lnfs
%def_without perf
%def_enable oprofile
%def_enable secrm
%def_with firmware

%def_disable debug_section_mismatch

%define allocator SLAB

%Extra_modules vboxhost 4.1.24
#Extra_modules vboxguest 4.1.22
#Extra_modules fglrx 8.97.100.3
#Extra_modules netatop 0.1.1

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
Source10: Makefile.external

#Patch0000: patch-%kernel_branch.%kernel_stable_version

Patch0001: linux-%kernel_branch.42-fix-Documentation-DocBook.patch
Patch0002: linux-%kernel_branch.42-fix-Documentation-DocBook-man.patch

Patch0011: linux-%kernel_branch.42-fix-arch-ia64.patch
Patch0012: linux-%kernel_branch.51-fix-arch-powerpc.patch
Patch0013: linux-%kernel_branch.42-fix-arch-powerpc-platforms--52xx.patch
Patch0014: linux-%kernel_branch.42-fix-arch-powerpc-platforms--chrp.patch
Patch0015: linux-%kernel_branch.42-fix-arch-powerpc-platforms--pseries.patch
Patch0016: linux-%kernel_branch.43-fix-arch-s390.patch
Patch0017: linux-%kernel_branch.43-fix-arch-s390--lib.patch

Patch0020: linux-%kernel_branch.55-fix-arch-x86.patch
Patch0021: linux-%kernel_branch.42-fix-arch-x86--apic.patch
Patch0022: linux-%kernel_branch.42-fix-arch-x86--apm.patch
Patch0023: linux-%kernel_branch.61-fix-arch-x86--mcheck.patch
Patch0024: linux-%kernel_branch.42-fix-arch-x86--tsc.patch
Patch0025: linux-%kernel_branch.56-fix-arch-x86-boot.patch
Patch0026: linux-%kernel_branch.42-fix-arch-x86-cpu--perf-event.patch
Patch0027: linux-%kernel_branch.47-fix-arch-x86-cpu--rdrand.patch
Patch0028: linux-%kernel_branch.42-fix-arch-x86-platform-olpc.patch

Patch0030: linux-%kernel_branch.51-fix-block.patch
Patch0031: linux-%kernel_branch.42-fix-block--blk-integrity.patch
Patch0032: linux-%kernel_branch.42-fix-block--blk-throttle.patch
Patch0033: linux-%kernel_branch.42-fix-block--cfq-iosched.patch

Patch0050: linux-%kernel_branch.42-fix-drivers--connector.patch

Patch0060: linux-%kernel_branch.61-fix-drivers-acpi.patch
Patch0061: linux-%kernel_branch.42-fix-drivers-acpi--battery.patch
Patch0062: linux-%kernel_branch.42-fix-drivers-acpi--processor.patch
Patch0063: linux-%kernel_branch.42-fix-drivers-acpi--thermal.patch
Patch0064: linux-%kernel_branch.42-fix-drivers-acpi--video.patch
Patch0065: linux-%kernel_branch.42-fix-drivers-acpi-apei--apei.patch
Patch0066: linux-%kernel_branch.42-fix-drivers-acpi-apei--einj.patch
Patch0067: linux-%kernel_branch.42-fix-drivers-acpi-apei--erst-dbg.patch
Patch0068: linux-%kernel_branch.42-fix-drivers-acpi-apei--ghes.patch

Patch0071: linux-%kernel_branch.51-fix-drivers-ata--ahci.patch
Patch0072: linux-%kernel_branch.51-fix-drivers-ata--ata_piix.patch
Patch0073: linux-%kernel_branch.42-fix-drivers-ata--libata.patch
Patch0074: linux-%kernel_branch.43-fix-drivers-ata--pata_amd.patch
Patch0075: linux-%kernel_branch.43-fix-drivers-ata--pata_mpiix.patch
Patch0076: linux-%kernel_branch.43-fix-drivers-ata--pata_oldpiix.patch
Patch0077: linux-%kernel_branch.43-fix-drivers-ata--pata_sch.patch
Patch0078: linux-%kernel_branch.42-fix-drivers-ata--sata_sil.patch

Patch0080: linux-%kernel_branch.43-fix-drivers-base.patch
Patch0081: linux-%kernel_branch.42-fix-drivers-base--memory.patch
Patch0082: linux-%kernel_branch.57-fix-drivers-base-power--opp.patch
Patch0083: linux-%kernel_branch.42-fix-drivers-base-power--runtime.patch

Patch0091: linux-%kernel_branch.42-fix-drivers-block--DAC960.patch
Patch0092: linux-%kernel_branch.43-fix-drivers-block--cciss.patch
Patch0093: linux-%kernel_branch.43-fix-drivers-block--dasd_diag_mod.patch
Patch0094: linux-%kernel_branch.43-fix-drivers-block--dasd_eckd_mod.patch
Patch0095: linux-%kernel_branch.43-fix-drivers-block--dasd_fba_mod.patch
Patch0096: linux-%kernel_branch.51-fix-drivers-block--dasd_mod.patch
Patch0097: linux-%kernel_branch.42-fix-drivers-block--drbd.patch
Patch0098: linux-%kernel_branch.51-fix-drivers-block--floppy.patch
Patch0099: linux-%kernel_branch.43-fix-drivers-block--nbd.patch
Patch0100: linux-%kernel_branch.42-fix-drivers-block--rbd.patch
Patch0101: linux-%kernel_branch.42-fix-drivers-block--virtio_blk.patch

Patch0111: linux-%kernel_branch.42-fix-drivers-bluetooth--ath3k.patch

Patch0121: linux-%kernel_branch.43-fix-drivers-char--con3215.patch
Patch0122: linux-%kernel_branch.42-fix-drivers-char--lp.patch
Patch0123: linux-%kernel_branch.42-fix-drivers-char--mem.patch
Patch0124: linux-%kernel_branch.43-fix-drivers-char--random.patch
Patch0125: linux-%kernel_branch.43-fix-drivers-char--raw3270.patch
Patch0126: linux-%kernel_branch.43-fix-drivers-char--sclp_async.patch
Patch0127: linux-%kernel_branch.43-fix-drivers-char--tape.patch
Patch0128: linux-%kernel_branch.43-fix-drivers-char--tape_34xx.patch
Patch0129: linux-%kernel_branch.43-fix-drivers-char--tape_3590.patch
Patch0130: linux-%kernel_branch.43-fix-drivers-char--virtio_console.patch
Patch0131: linux-%kernel_branch.43-fix-drivers-char--vmur.patch
Patch0132: linux-%kernel_branch.43-fix-drivers-char--zcore_mod.patch
Patch0133: linux-%kernel_branch.42-fix-drivers-char-agp--agpgart.patch
Patch0134: linux-%kernel_branch.43-fix-drivers-char-agp--intel-agp.patch
Patch0135: linux-%kernel_branch.43-fix-drivers-char-hw_random--amd-rng.patch
Patch0136: linux-%kernel_branch.43-fix-drivers-char-hw_random--intel-rng.patch
Patch0137: linux-%kernel_branch.42-fix-drivers-char-hw_random--virtio-rng.patch
Patch0138: linux-%kernel_branch.46-fix-drivers-char-ipmi--ipmi_msghandler.patch
Patch0139: linux-%kernel_branch.46-fix-drivers-char-ipmi--ipmi_si.patch

Patch0140: linux-%kernel_branch.58-fix-drivers-cio.patch
Patch0141: linux-%kernel_branch.43-fix-drivers-cio--ccw_device.patch
Patch0142: linux-%kernel_branch.43-fix-drivers-cio--ccwgroup.patch
Patch0143: linux-%kernel_branch.51-fix-drivers-cio--qdio.patch

Patch0150: linux-%kernel_branch.42-fix-drivers-cpufreq.patch
Patch0151: linux-%kernel_branch.44-fix-drivers-cpufreq--acpi-cpufreq.patch
Patch0152: linux-%kernel_branch.42-fix-drivers-cpufreq--cpufreq_conservative.patch
Patch0153: linux-%kernel_branch.42-fix-drivers-cpufreq--cpufreq_ondemand.patch
Patch0154: linux-%kernel_branch.44-fix-drivers-cpufreq--p4-clockmod.patch
Patch0155: linux-%kernel_branch.50-fix-drivers-cpufreq--powernow-k8.patch

Patch0161: linux-%kernel_branch.43-fix-drivers-crypto--ap.patch
Patch0162: linux-%kernel_branch.42-fix-drivers-crypto--hifn_795x.patch
Patch0163: linux-%kernel_branch.58-fix-drivers-crypto--padlock.patch
Patch0164: linux-%kernel_branch.51-fix-drivers-crypto--s390.patch

Patch0171: linux-%kernel_branch.42-fix-drivers-dma--dmatest.patch
Patch0172: linux-%kernel_branch.43-fix-drivers-dma--intel_mid_dma.patch
Patch0173: linux-%kernel_branch.44-fix-drivers-dma-ioat.patch

Patch0181: linux-%kernel_branch.61-fix-drivers-edac--amd64_edac_mod.patch
Patch0182: linux-%kernel_branch.43-fix-drivers-edac--e752x_edac.patch
Patch0183: linux-%kernel_branch.43-fix-drivers-edac--e7xxx_edac.patch
Patch0184: linux-%kernel_branch.61-fix-drivers-edac--edac_mce_amd.patch
Patch0185: linux-%kernel_branch.43-fix-drivers-edac--i3000_edac.patch
Patch0186: linux-%kernel_branch.43-fix-drivers-edac--i3200_edac.patch
Patch0187: linux-%kernel_branch.43-fix-drivers-edac--i5000_edac.patch
Patch0188: linux-%kernel_branch.61-fix-drivers-edac--i5100_edac.patch
Patch0189: linux-%kernel_branch.43-fix-drivers-edac--i5400_edac.patch
Patch0190: linux-%kernel_branch.43-fix-drivers-edac--i7300_edac.patch
Patch0191: linux-%kernel_branch.61-fix-drivers-edac--i7core_edac.patch
Patch0192: linux-%kernel_branch.43-fix-drivers-edac--i82443bxgx_edac.patch
Patch0193: linux-%kernel_branch.43-fix-drivers-edac--i82860_edac.patch
Patch0194: linux-%kernel_branch.43-fix-drivers-edac--i82875p_edac.patch
Patch0195: linux-%kernel_branch.43-fix-drivers-edac--i82975x_edac.patch
Patch0196: linux-%kernel_branch.43-fix-drivers-edac--x38_edac.patch

Patch0201: linux-%kernel_branch.42-fix-drivers-eisa--pci_eisa.patch

Patch0211: linux-%kernel_branch.47-fix-drivers-firewire--firewire-core.patch
Patch0212: linux-%kernel_branch.59-fix-drivers-firewire--firewire-net.patch
Patch0213: linux-%kernel_branch.47-fix-drivers-firewire--firewire-ohci.patch
Patch0214: linux-%kernel_branch.47-fix-drivers-firewire--firewire-sbp2.patch
Patch0215: linux-%kernel_branch.47-fix-drivers-firewire--nosy.patch

Patch0221: linux-%kernel_branch.42-fix-drivers-firmware--edd.patch
Patch0222: linux-%kernel_branch.51-fix-drivers-firmware--efivars.patch
Patch0223: linux-%kernel_branch.42-fix-drivers-firmware--iscsi_ibft.patch

Patch0231: linux-%kernel_branch.44-fix-drivers-gpu-drm.patch
Patch0232: linux-%kernel_branch.44-fix-drivers-gpu-drm--drm.patch
Patch0233: linux-%kernel_branch.42-fix-drivers-gpu-drm--drm_kms_helper.patch
Patch0234: linux-%kernel_branch.53-fix-drivers-gpu-drm--i915.patch
Patch0235: linux-%kernel_branch.42-fix-drivers-gpu-drm--mga.patch
Patch0236: linux-%kernel_branch.43-fix-drivers-gpu-drm--nouveau.patch
Patch0237: linux-%kernel_branch.43-fix-drivers-gpu-drm--psb_gfx.patch
Patch0238: linux-%kernel_branch.52-fix-drivers-gpu-drm--radeon.patch
Patch0239: linux-%kernel_branch.42-fix-drivers-gpu-drm--via.patch
Patch0240: linux-%kernel_branch.42-fix-drivers-gpu-drm--vmwgfx.patch
Patch0241: linux-%kernel_branch.42-fix-drivers-gpu-vga--vgaarb.patch

Patch0251: linux-%kernel_branch.42-fix-drivers-hid--hid-apple.patch
Patch0252: linux-%kernel_branch.56-fix-drivers-hid--hid-microsoft.patch
Patch0253: linux-%kernel_branch.56-fix-drivers-hid--hid-uclogic.patch
Patch0254: linux-%kernel_branch.42-fix-drivers-hid--usbhid.patch

Patch0260: linux-%kernel_branch.58-fix-drivers-hv.patch

Patch0271: linux-%kernel_branch.43-fix-drivers-hwmon--abituguru.patch
Patch0272: linux-%kernel_branch.43-fix-drivers-hwmon--applesmc.patch
Patch0273: linux-%kernel_branch.43-fix-drivers-hwmon--asc7621.patch
Patch0274: linux-%kernel_branch.43-fix-drivers-hwmon--coretemp.patch
Patch0275: linux-%kernel_branch.43-fix-drivers-hwmon--fam15h_power.patch
Patch0276: linux-%kernel_branch.43-fix-drivers-hwmon--i5k_amb.patch
Patch0277: linux-%kernel_branch.43-fix-drivers-hwmon--k8temp.patch
Patch0278: linux-%kernel_branch.43-fix-drivers-hwmon--k10temp.patch
Patch0279: linux-%kernel_branch.43-fix-drivers-hwmon--via-cputemp.patch
Patch0280: linux-%kernel_branch.43-fix-drivers-hwmon--via686a.patch

Patch0291: linux-%kernel_branch.42-fix-drivers-i2c--i2c-pxa.patch
Patch0292: linux-%kernel_branch.51-fix-drivers-i2c-busses--i2c-i801.patch
Patch0293: linux-%kernel_branch.43-fix-drivers-i2c-busses--i2c-intel-mid.patch
Patch0294: linux-%kernel_branch.42-fix-drivers-i2c-busses--scx200_acb.patch

Patch0300: linux-%kernel_branch.42-fix-drivers-ide.patch

Patch0311: linux-%kernel_branch.43-fix-drivers-idle--i7300_idle.patch
Patch0312: linux-%kernel_branch.53-fix-drivers-idle--intel_idle.patch

Patch0321: linux-%kernel_branch.42-fix-drivers-infiniband-core.patch
Patch0322: linux-%kernel_branch.42-fix-drivers-infiniband-hw-cxgb4.patch
Patch0323: linux-%kernel_branch.42-fix-drivers-infiniband-hw-mlx4.patch
Patch0324: linux-%kernel_branch.42-fix-drivers-infiniband-hw-mthca.patch
Patch0325: linux-%kernel_branch.43-fix-drivers-infiniband-ulp-iser.patch

Patch0331: linux-%kernel_branch.56-fix-drivers-input-mouse--bcm5974.patch
Patch0332: linux-%kernel_branch.57-fix-drivers-input-mouse--elantech.patch
Patch0333: linux-%kernel_branch.42-fix-drivers-input-mouse--synaptics.patch
Patch0334: linux-%kernel_branch.42-fix-drivers-input-serio--i8042.patch
Patch0335: linux-%kernel_branch.56-fix-drivers-input-tablet--wacom_wac.patch

Patch0341: linux-%kernel_branch.42-fix-drivers-isdn-gigaset--gigaset.patch
Patch0342: linux-%kernel_branch.51-fix-drivers-isdn-hardware-mISDN--hfcsusb.patch
Patch0343: linux-%kernel_branch.42-fix-drivers-isdn-mISDN--mISDN_core.patch

Patch0351: linux-%kernel_branch.42-fix-drivers-leds--leds-lp5521.patch

Patch0361: linux-%kernel_branch.42-fix-drivers-macintosh--adb.patch
Patch0362: linux-%kernel_branch.42-fix-drivers-macintosh--adbhid.patch

Patch0371: linux-%kernel_branch.45-fix-drivers-md--dm-mod.patch
Patch0372: linux-%kernel_branch.57-fix-drivers-md--dm-multipath.patch
Patch0373: linux-%kernel_branch.53-fix-drivers-md--md-mod.patch
Patch0374: linux-%kernel_branch.51-fix-drivers-md--multipath.patch
Patch0375: linux-%kernel_branch.51-fix-drivers-md--raid1.patch
Patch0376: linux-%kernel_branch.51-fix-drivers-md--raid10.patch
Patch0377: linux-%kernel_branch.51-fix-drivers-md--raid456.patch

Patch0381: linux-%kernel_branch.42-fix-drivers-media-common-tuners--max2165.patch
Patch0382: linux-%kernel_branch.44-fix-drivers-media-dvb-firewire--firedtv.patch
Patch0383: linux-%kernel_branch.57-fix-drivers-media-video-gspca--pac7302.patch

Patch0391: linux-%kernel_branch.42-fix-drivers-message-fusion.patch

Patch0401: linux-%kernel_branch.50-fix-drivers-misc--hpilo.patch
Patch0402: linux-%kernel_branch.42-fix-drivers-misc--rts_pstor.patch
Patch0403: linux-%kernel_branch.42-fix-drivers-misc--vmw_balloon.patch
Patch0404: linux-%kernel_branch.42-fix-drivers-misc-lis3lv02d--lis3lv02d.patch

Patch0411: linux-%kernel_branch.42-fix-drivers-mmc-card--mmc_block.patch

Patch0420: linux-%kernel_branch.61-fix-drivers-net.patch
Patch0421: linux-%kernel_branch.42-fix-drivers-net--3c509.patch
Patch0422: linux-%kernel_branch.42-fix-drivers-net--3c59x.patch
Patch0423: linux-%kernel_branch.42-fix-drivers-net--at1700.patch
Patch0424: linux-%kernel_branch.42-fix-drivers-net--bna.patch
Patch0425: linux-%kernel_branch.43-fix-drivers-net--bnx2.patch
Patch0426: linux-%kernel_branch.43-fix-drivers-net--bnx2x.patch
Patch0427: linux-%kernel_branch.58-fix-drivers-net--bonding.patch
Patch0428: linux-%kernel_branch.43-fix-drivers-net--claw.patch
Patch0429: linux-%kernel_branch.51-fix-drivers-net--cnic.patch
Patch0430: linux-%kernel_branch.43-fix-drivers-net--ctcm.patch
Patch0431: linux-%kernel_branch.46-fix-drivers-net--cxgb3.patch
Patch0432: linux-%kernel_branch.42-fix-drivers-net--depca.patch
Patch0433: linux-%kernel_branch.42-fix-drivers-net--dl2k.patch
Patch0434: linux-%kernel_branch.42-fix-drivers-net--e1000.patch
Patch0435: linux-%kernel_branch.58-fix-drivers-net--e1000e.patch
Patch0436: linux-%kernel_branch.42-fix-drivers-net--ehea.patch
Patch0437: linux-%kernel_branch.42-fix-drivers-net--hp100.patch
Patch0438: linux-%kernel_branch.42-fix-drivers-net--ibmveth.patch
Patch0439: linux-%kernel_branch.50-fix-drivers-net--igb.patch
Patch0440: linux-%kernel_branch.49-fix-drivers-net--ixgbe.patch
Patch0441: linux-%kernel_branch.43-fix-drivers-net--lcs.patch
Patch0442: linux-%kernel_branch.42-fix-drivers-net--macvtap.patch
Patch0443: linux-%kernel_branch.42-fix-drivers-net--natsemi.patch
Patch0444: linux-%kernel_branch.42-fix-drivers-net--ne3210.patch
Patch0445: linux-%kernel_branch.53-fix-drivers-net--netiucv.patch
Patch0446: linux-%kernel_branch.42-fix-drivers-net--qlcnic.patch
Patch0447: linux-%kernel_branch.46-fix-drivers-net--qlge.patch
Patch0448: linux-%kernel_branch.44-fix-drivers-net--sfc.patch
Patch0449: linux-%kernel_branch.56-fix-drivers-net--skge.patch
Patch0450: linux-%kernel_branch.50-fix-drivers-net--smsguicv.patch
Patch0451: linux-%kernel_branch.51-fix-drivers-net--tg3.patch
Patch0452: linux-%kernel_branch.42-fix-drivers-net--tlan.patch
Patch0453: linux-%kernel_branch.42-fix-drivers-net--vmxnet3.patch
Patch0454: linux-%kernel_branch.42-fix-drivers-net-benet--be2net.patch
Patch0455: linux-%kernel_branch.42-fix-drivers-net-mlx4--mlx4_core.patch
Patch0456: linux-%kernel_branch.46-fix-drivers-net-mlx4--mlx4_en.patch
Patch0457: linux-%kernel_branch.42-fix-drivers-net-netxen.patch
Patch0458: linux-%kernel_branch.42-fix-drivers-net-pcmcia--nmclan_cs.patch
Patch0459: linux-%kernel_branch.53-fix-drivers-net-qeth.patch
Patch0460: linux-%kernel_branch.42-fix-drivers-net-tulip.patch
Patch0461: linux-%kernel_branch.42-fix-drivers-net-tulip--de4x5.patch
Patch0462: linux-%kernel_branch.46-fix-drivers-net-usb--asix.patch
Patch0463: linux-%kernel_branch.42-fix-drivers-net-usb--cdc_ether.patch
Patch0464: linux-%kernel_branch.42-fix-drivers-net-usb--ipheth.patch
Patch0465: linux-%kernel_branch.42-fix-drivers-net-usb--kalmia.patch
Patch0466: linux-%kernel_branch.42-fix-drivers-net-usb--lg-vl600.patch
Patch0467: linux-%kernel_branch.42-fix-drivers-net-usb--smsc75xx.patch
Patch0468: linux-%kernel_branch.42-fix-drivers-net-usb--usbnet.patch
Patch0469: linux-%kernel_branch.43-fix-drivers-net-wireless-brcm80211--brcmfmac.patch
Patch0470: linux-%kernel_branch.42-fix-drivers-net-wireless-libertas--libertas_spi.patch
Patch0471: linux-%kernel_branch.56-fix-drivers-net-wireless-mwifiex--mwifiex.patch
Patch0472: linux-%kernel_branch.56-fix-drivers-net-wireless-mwifiex--mwifiex_sdio.patch
Patch0473: linux-%kernel_branch.53-fix-drivers-net-wireless-rt2x00.patch
Patch0474: linux-%kernel_branch.43-fix-drivers-net-wireless-rtl8192e.patch
Patch0475: linux-%kernel_branch.56-fix-drivers-net-wireless-rtlwifi.patch
Patch0476: linux-%kernel_branch.56-fix-drivers-net-wireless-rtlwifi--rtl8192ce.patch
Patch0477: linux-%kernel_branch.56-fix-drivers-net-wireless-rtlwifi--rtl8192cu.patch
Patch0478: linux-%kernel_branch.56-fix-drivers-net-wireless-rtlwifi--rtl8192se.patch
Patch0479: linux-%kernel_branch.56-fix-drivers-net-wireless-wl12xx--wl12xx.patch

Patch0481: linux-%kernel_branch.42-fix-drivers-parport--parport_pc.patch

Patch0490: linux-%kernel_branch.58-fix-drivers-pci.patch
Patch0491: linux-%kernel_branch.61-fix-drivers-pci--dmar.patch
Patch0492: linux-%kernel_branch.42-fix-drivers-pci--sn.patch
Patch0493: linux-%kernel_branch.46-fix-drivers-pci-hotplug--acpiphp.patch
Patch0494: linux-%kernel_branch.42-fix-drivers-pci-hotplug--pci_hotplug.patch

Patch0501: linux-%kernel_branch.42-fix-drivers-platform--hdaps.patch
Patch0502: linux-%kernel_branch.42-fix-drivers-platform--hp_accel.patch
Patch0503: linux-%kernel_branch.56-fix-drivers-platform--ideapad-laptop.patch
Patch0504: linux-%kernel_branch.43-fix-drivers-platform--intel_ips.patch
Patch0505: linux-%kernel_branch.43-fix-drivers-platform--intel_menlow.patch
Patch0506: linux-%kernel_branch.43-fix-drivers-platform--intel_oaktrail.patch
Patch0507: linux-%kernel_branch.56-fix-drivers-platform--samsung-laptop.patch

Patch0510: linux-%kernel_branch.42-fix-drivers-pnp.patch

Patch0521: linux-%kernel_branch.42-fix-drivers-rtc--rtc-m41t80.patch

Patch0531: linux-%kernel_branch.42-fix-drivers-scsi.patch
Patch0532: linux-%kernel_branch.42-fix-drivers-scsi--aacraid.patch
Patch0533: linux-%kernel_branch.42-fix-drivers-scsi--aha152x.patch
Patch0534: linux-%kernel_branch.42-fix-drivers-scsi--aha1542.patch
Patch0535: linux-%kernel_branch.43-fix-drivers-scsi--be2iscsi.patch
Patch0536: linux-%kernel_branch.42-fix-drivers-scsi--bfa.patch
Patch0537: linux-%kernel_branch.43-fix-drivers-scsi--bnx2fc.patch
Patch0538: linux-%kernel_branch.43-fix-drivers-scsi--bnx2i.patch
Patch0539: linux-%kernel_branch.42-fix-drivers-scsi--fnic.patch
Patch0540: linux-%kernel_branch.42-fix-drivers-scsi--hpsa.patch
Patch0541: linux-%kernel_branch.42-fix-drivers-scsi--ipr.patch
Patch0542: linux-%kernel_branch.42-fix-drivers-scsi--isci.patch
Patch0543: linux-%kernel_branch.43-fix-drivers-scsi--iscsi_boot_sysfs.patch
Patch0544: linux-%kernel_branch.43-fix-drivers-scsi--iscsi_tcp.patch
Patch0545: linux-%kernel_branch.42-fix-drivers-scsi--libfc.patch
Patch0546: linux-%kernel_branch.43-fix-drivers-scsi--libiscsi.patch
Patch0547: linux-%kernel_branch.42-fix-drivers-scsi--libsas.patch
Patch0548: linux-%kernel_branch.58-fix-drivers-scsi--lpfc.patch
Patch0549: linux-%kernel_branch.42-fix-drivers-scsi--mpt2sas.patch
Patch0550: linux-%kernel_branch.42-fix-drivers-scsi--mvsas.patch
Patch0551: linux-%kernel_branch.42-fix-drivers-scsi--pm8001.patch
Patch0552: linux-%kernel_branch.53-fix-drivers-scsi--qla2xxx.patch
Patch0553: linux-%kernel_branch.43-fix-drivers-scsi--qla4xxx.patch
Patch0554: linux-%kernel_branch.44-fix-drivers-scsi--scsi_mod.patch
Patch0555: linux-%kernel_branch.42-fix-drivers-scsi--scsi_transport_fc.patch
Patch0556: linux-%kernel_branch.43-fix-drivers-scsi--scsi_transport_iscsi.patch
Patch0557: linux-%kernel_branch.42-fix-drivers-scsi--scsi_transport_sas.patch
Patch0558: linux-%kernel_branch.42-fix-drivers-scsi--scsi_transport_spi.patch
Patch0559: linux-%kernel_branch.61-fix-drivers-scsi--sd_mod.patch
Patch0560: linux-%kernel_branch.42-fix-drivers-scsi--ses.patch
Patch0561: linux-%kernel_branch.49-fix-drivers-scsi--sg.patch
Patch0562: linux-%kernel_branch.42-fix-drivers-scsi--sim710.patch
Patch0563: linux-%kernel_branch.42-fix-drivers-scsi--sr_mod.patch
Patch0564: linux-%kernel_branch.42-fix-drivers-scsi--st.patch
Patch0565: linux-%kernel_branch.51-fix-drivers-scsi--zfcp.patch
Patch0566: linux-%kernel_branch.43-fix-drivers-scsi-cxgbi--cxgb3i.patch
Patch0567: linux-%kernel_branch.43-fix-drivers-scsi-cxgbi--cxgb4i.patch
Patch0568: linux-%kernel_branch.43-fix-drivers-scsi-cxgbi--libcxgbi.patch
Patch0569: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh.patch
Patch0570: linux-%kernel_branch.45-fix-drivers-scsi-device_handler--scsi_dh_alua.patch
Patch0571: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_emc.patch
Patch0572: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_hp_sw.patch
Patch0573: linux-%kernel_branch.42-fix-drivers-scsi-device_handler--scsi_dh_rdac.patch
Patch0574: linux-%kernel_branch.43-fix-drivers-scsi-fcoe.patch
Patch0575: linux-%kernel_branch.51-fix-drivers-scsi-ibmvscsi--ibmvfc.patch
Patch0576: linux-%kernel_branch.42-fix-drivers-scsi-ibmvscsi--ibmvscsic.patch
Patch0577: linux-%kernel_branch.42-fix-drivers-scsi-megaraid--megaraid_mbox.patch
Patch0578: linux-%kernel_branch.44-fix-drivers-scsi-megaraid--megaraid_sas.patch

Patch0580: linux-%kernel_branch.43-fix-drivers-target.patch

Patch0591: linux-%kernel_branch.42-fix-drivers-telephony--ixj.patch

Patch0601: linux-%kernel_branch.58-fix-drivers-tty--pty.patch
Patch0602: linux-%kernel_branch.42-fix-drivers-tty-serial--8250.patch
Patch0603: linux-%kernel_branch.42-fix-drivers-tty-serial--8250_pci.patch

Patch0610: linux-%kernel_branch.46-fix-drivers-usb.patch
Patch0611: linux-%kernel_branch.42-fix-drivers-usb-atm--ueagle-atm.patch
Patch0612: linux-%kernel_branch.60-fix-drivers-usb-core.patch
Patch0613: linux-%kernel_branch.58-fix-drivers-usb-host--ehci-hcd.patch
Patch0614: linux-%kernel_branch.42-fix-drivers-usb-host--uhci-hcd.patch
Patch0615: linux-%kernel_branch.51-fix-drivers-usb-host--xhci-hcd.patch
Patch0616: linux-%kernel_branch.42-fix-drivers-usb-misc--usbtest.patch
Patch0617: linux-%kernel_branch.42-fix-drivers-usb-mon.patch
Patch0618: linux-%kernel_branch.42-fix-drivers-usb-serial--ftdi_sio.patch
Patch0619: linux-%kernel_branch.42-fix-drivers-usb-serial--ipw.patch
Patch0620: linux-%kernel_branch.42-fix-drivers-usb-serial--pl2303.patch
Patch0621: linux-%kernel_branch.42-fix-drivers-usb-serial--usbserial.patch
Patch0622: linux-%kernel_branch.42-fix-drivers-usb-storage--ums-realtek.patch
Patch0623: linux-%kernel_branch.42-fix-drivers-usb-usbip--usbip-host.patch
Patch0624: linux-%kernel_branch.42-fix-drivers-usb-wusbcore--wusbcore-cbaf.patch

Patch0631: linux-%kernel_branch.42-fix-drivers-video--intelfb.patch
Patch0632: linux-%kernel_branch.43-fix-drivers-video--xgifb.patch
Patch0633: linux-%kernel_branch.42-fix-drivers-video-aty--radeonfb.patch
Patch0634: linux-%kernel_branch.42-fix-drivers-video-via.patch

Patch0641: linux-%kernel_branch.42-fix-drivers-virtio--virtio_ballon.patch

Patch0651: linux-%kernel_branch.49-fix-drivers-watchdog--hpwdt.patch
Patch0652: linux-%kernel_branch.51-fix-drivers-watchdog--iTCO_wdt.patch

Patch0661: linux-%kernel_branch.42-fix-firmware--vicam.patch

Patch0670: linux-%kernel_branch.61-fix-fs.patch
Patch0671: linux-%kernel_branch.51-fix-fs--anon_inodes.patch
Patch0672: linux-%kernel_branch.42-fix-fs--bio-integrity.patch
Patch0673: linux-%kernel_branch.53-fix-fs--block.patch
Patch0674: linux-%kernel_branch.42-fix-fs--eventpoll.patch
Patch0675: linux-%kernel_branch.53-fix-fs-autofs4.patch
Patch0676: linux-%kernel_branch.58-fix-fs-btrfs.patch
Patch0677: linux-%kernel_branch.44-fix-fs-cachefiles.patch
Patch0678: linux-%kernel_branch.42-fix-fs-ceph.patch
Patch0679: linux-%kernel_branch.42-fix-fs-cifs.patch
Patch0680: linux-%kernel_branch.42-fix-fs-dlm.patch
Patch0681: linux-%kernel_branch.42-fix-fs-ecryptfs.patch
Patch0682: linux-%kernel_branch.42-fix-fs-ext3.patch
Patch0683: linux-%kernel_branch.46-fix-fs-ext4.patch
Patch0684: linux-%kernel_branch.56-fix-fs-fat.patch
Patch0685: linux-%kernel_branch.42-fix-fs-hfs.patch
Patch0686: linux-%kernel_branch.54-fix-fs-jbd.patch
Patch0687: linux-%kernel_branch.53-fix-fs-nfs.patch
Patch0688: linux-%kernel_branch.53-fix-fs-ocfs2.patch
Patch0689: linux-%kernel_branch.43-fix-fs-partition--ibm.patch
Patch0690: linux-%kernel_branch.43-fix-fs-s390_hypfs.patch
Patch0691: linux-%kernel_branch.56-fix-fs-squashfs.patch
Patch0692: linux-%kernel_branch.43-fix-fs-proc.patch
Patch0693: linux-%kernel_branch.42-fix-fs-pstore.patch
Patch0694: linux-%kernel_branch.51-fix-fs-reiserfs.patch
Patch0695: linux-%kernel_branch.42-fix-fs-sysfs.patch
Patch0696: linux-%kernel_branch.53-fix-fs-xfs.patch

Patch0700: linux-%kernel_branch.53-fix-include.patch

Patch0711: linux-%kernel_branch.42-fix-init--calibrate.patch

Patch0721: linux-%kernel_branch.42-fix-ipc--mqueue.patch

Patch0730: linux-%kernel_branch.57-fix-kernel.patch
Patch0731: linux-%kernel_branch.42-fix-kernel--cgroup.patch
Patch0732: linux-%kernel_branch.42-fix-kernel--cgroup_freezer.patch
Patch0733: linux-%kernel_branch.49-fix-kernel--events.patch
Patch0734: linux-%kernel_branch.42-fix-kernel--freezer.patch
Patch0735: linux-%kernel_branch.51-fix-kernel--smp.patch
Patch0736: linux-%kernel_branch.42-fix-kernel--watchdog.patch
Patch0737: linux-%kernel_branch.58-fix-kernel-irq.patch
Patch0738: linux-%kernel_branch.42-fix-kernel-power--hibernate.patch
Patch0739: linux-%kernel_branch.44-fix-kernel-time.patch

Patch0740: linux-%kernel_branch.57-fix-lib.patch
Patch0741: linux-%kernel_branch.42-fix-lib--genalloc.patch

Patch0750: linux-%kernel_branch.58-fix-mm.patch
Patch0751: linux-%kernel_branch.58-fix-mm--compaction.patch
Patch0752: linux-%kernel_branch.59-fix-mm--huge_memory.patch
Patch0753: linux-%kernel_branch.43-fix-mm--hugetlb.patch
Patch0754: linux-%kernel_branch.44-fix-mm--memcontrol.patch
Patch0755: linux-%kernel_branch.42-fix-mm--memory-failure.patch
Patch0756: linux-%kernel_branch.51-fix-mm--memory_hotplug.patch
Patch0757: linux-%kernel_branch.59-fix-mm--mmu.patch
Patch0758: linux-%kernel_branch.42-fix-mm--mmu_notofier.patch
Patch0759: linux-%kernel_branch.46-fix-mm--numa.patch
Patch0760: linux-%kernel_branch.42-fix-mm--slab.patch
Patch0761: linux-%kernel_branch.42-fix-mm--slub.patch
Patch0762: linux-%kernel_branch.58-fix-mm--swap.patch
Patch0763: linux-%kernel_branch.42-fix-mm--zcache.patch

Patch0770: linux-%kernel_branch.51-fix-net.patch
Patch0771: linux-%kernel_branch.42-fix-net--batman-adv.patch
Patch0772: linux-%kernel_branch.42-fix-net--dcb.patch
Patch0773: linux-%kernel_branch.42-fix-net--wimax.patch
Patch0774: linux-%kernel_branch.42-fix-net--x25.patch
Patch0775: linux-%kernel_branch.42-fix-net-8021q--vlan-core.patch
Patch0776: linux-%kernel_branch.58-fix-net-bridge--bridge.patch
Patch0777: linux-%kernel_branch.42-fix-net-ceph.patch
Patch0778: linux-%kernel_branch.59-fix-net-core.patch
Patch0779: linux-%kernel_branch.46-fix-net-ipv4.patch
Patch0780: linux-%kernel_branch.51-fix-net-ipv4-netfilter--iptable_nat.patch
Patch0781: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat.patch
Patch0782: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_amanda.patch
Patch0783: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_ftp.patch
Patch0784: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_h323.patch
Patch0785: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_irc.patch
Patch0786: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_pptp.patch
Patch0787: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_sip.patch
Patch0788: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_snmp_basic.patch
Patch0789: linux-%kernel_branch.51-fix-net-ipv4-netfilter--nf_nat_tftp.patch
Patch0790: linux-%kernel_branch.53-fix-net-ipv6.patch
Patch0791: linux-%kernel_branch.43-fix-net-ipv6-netfilter--nf_conntrack_ipv6.patch
Patch0792: linux-%kernel_branch.42-fix-net-ipv6--ip6_tunnel.patch
Patch0793: linux-%kernel_branch.43-fix-net-iucv--af_iucv.patch
Patch0794: linux-%kernel_branch.43-fix-net-iucv--iucv.patch
Patch0795: linux-%kernel_branch.42-fix-net-mac80211.patch
Patch0796: linux-%kernel_branch.51-fix-net-netfilter--nf_conntrack.patch
Patch0797: linux-%kernel_branch.42-fix-net-netfilter--nf_conntrack_ecache.patch
Patch0798: linux-%kernel_branch.42-fix-net-netfilter--nf_conntrack_ftp.patch
Patch0799: linux-%kernel_branch.42-fix-net-netfilter--nf_conntrack_netlink.patch
Patch0800: linux-%kernel_branch.51-fix-net-netfilter-ipset.patch
Patch0801: linux-%kernel_branch.42-fix-net-netfilter-ipvs--ipvs.patch
Patch0802: linux-%kernel_branch.61-fix-net-rds--rds_rdma.patch
Patch0803: linux-%kernel_branch.51-fix-net-sched.patch
Patch0804: linux-%kernel_branch.42-fix-net-sctp.patch
Patch0805: linux-%kernel_branch.43-fix-net-sunrpc.patch
Patch0806: linux-%kernel_branch.58-fix-net-xfrm--xfrm_policy.patch

Patch0810: linux-%kernel_branch.42-fix-scripts.patch

Patch0821: linux-%kernel_branch.42-fix-security--security.patch
Patch0822: linux-%kernel_branch.42-fix-security-selinux.patch

Patch0831: linux-%kernel_branch.42-fix-sound-core--snd-pcm.patch
Patch0832: linux-%kernel_branch.47-fix-sound-firewire--snd-firewire-lib.patch
Patch0833: linux-%kernel_branch.47-fix-sound-firewire--snd-firewire-speakers.patch
Patch0834: linux-%kernel_branch.47-fix-sound-firewire--snd-isight.patch
Patch0835: linux-%kernel_branch.42-fix-sound-oss--pss.patch
Patch0836: linux-%kernel_branch.51-fix-sound-pci-hda.patch
Patch0837: linux-%kernel_branch.42-fix-sound-pci-rme9652--snd-hdspm.patch
Patch0838: linux-%kernel_branch.42-fix-sound-usb-misc--snd-ua101.patch

Patch0841: linux-%kernel_branch.49-fix-tools--perf.patch
Patch0842: linux-%kernel_branch.47-fix-tools-firewire--nosy-dump.patch

Patch0851: linux-%kernel_branch.58-fix-virt-kvm.patch
Patch0852: linux-%kernel_branch.43-fix-virt-kvm--kvm-amd.patch
Patch0853: linux-%kernel_branch.43-fix-virt-kvm--kvm-intel.patch


%{?_with_x32:Patch1001: linux-%kernel_branch.55-feat-arch-x86--x32.patch}

Patch1011: linux-%kernel_branch.42-feat-block--bfq-iosched.patch
Patch1012: linux-%kernel_branch.42-feat-block--bsg-lib.patch
Patch1013: linux-%kernel_branch.42-feat-block--sio-iosched.patch

Patch1021: linux-%kernel_branch.57-feat-crypto--blowfish-x86_64.patch
Patch1022: linux-%kernel_branch.57-feat-crypto--sha1-ssse3.patch

Patch1031: linux-%kernel_branch-feat-drivers-block--cloop.patch
Patch1032: linux-%kernel_branch.42-feat-drivers-block--zram.patch

Patch1040: linux-%kernel_branch.57-feat-drivers-devfreq.patch

Patch1051: linux-%kernel_branch.57-feat-drivers-edac--sb_edac.patch

Patch1061: linux-%kernel_branch-feat-drivers-gpu-drm--cirrus.patch
Patch1062: linux-%kernel_branch.43-feat-drivers-gpu-drm--gma500.patch
Patch1063: linux-%kernel_branch.43-feat-drivers-gpu-drm--psb_gfx.patch

Patch1071: linux-%kernel_branch.56-feat-drivers-hid--hid-speedlink.patch

Patch1081: linux-%kernel_branch.42-feat-drivers-hwmon--ipmisensors.patch

Patch1091: linux-%kernel_branch-feat-drivers-input-lirc.patch
Patch1092: linux-%kernel_branch.42-feat-drivers-input-touchscreen--elousb.patch
Patch1093: linux-%kernel_branch.57-feat-drivers-input-touchscreen--tsc40.patch

Patch1101: linux-%kernel_branch.42-feat-drivers-md--dm-raid45.patch

Patch1111: linux-%kernel_branch.56-feat-drivers-misc--fsa9480.patch
Patch1112: linux-%kernel_branch.42-feat-drivers-misc--rts_pstor.patch
Patch1113: linux-%kernel_branch.42-feat-drivers-misc--xvmalloc.patch

Patch1121: linux-%kernel_branch.57-feat-drivers-scsi--mvumi.patch

Patch1131: linux-%kernel_branch.57-feat-drivers-net-wireless--vt6655.patch
Patch1132: linux-%kernel_branch.57-feat-drivers-net-wireless--vt6656.patch
Patch1133: linux-%kernel_branch.43-feat-drivers-net-wireless-brcm80211.patch
Patch1134: linux-%kernel_branch.43-feat-drivers-net-wireless-rtl8187se.patch
Patch1135: linux-%kernel_branch.43-feat-drivers-net-wireless-rtl8192e.patch
Patch1136: linux-%kernel_branch.43-feat-drivers-net-wireless-rtl8192u.patch
Patch1137: linux-%kernel_branch.43-feat-drivers-net-wireless-rtl8712.patch
Patch1138: linux-%kernel_branch.56-feat-drivers-net-wireless-rtlwifi--rtl8192de.patch

Patch1141: linux-%kernel_branch.56-feat-drivers-platform--samsung-q10.patch
Patch1142: linux-%kernel_branch.42-feat-drivers-platform--thinkpad_ec.patch
Patch1143: linux-%kernel_branch.42-feat-drivers-platform--tp_smapi.patch

Patch1151: linux-%kernel_branch.57-feat-drivers-usb-storage--rts5139.patch
Patch1152: linux-%kernel_branch.42-feat-drivers-usb-usbip.patch

Patch1161: linux-%kernel_branch.53-feat-drivers-video--bootsplash.patch
Patch1162: linux-%kernel_branch.43-feat-drivers-video--xgifb.patch

Patch1171: linux-%kernel_branch-feat-firmware-rtl_nic.patch

Patch1181: linux-%kernel_branch.42-feat-fs--secrm.patch
Patch1182: linux-%kernel_branch-feat-fs-aufs.patch
Patch1183: linux-%kernel_branch.42-feat-fs-binfmt_elf--fatelf.patch
Patch1184: linux-%kernel_branch.43-feat-fs-dazukofs.patch
Patch1185: linux-%kernel_branch.42-feat-fs-ext2--secrm.patch
Patch1186: linux-%kernel_branch.42-feat-fs-ext3--secrm.patch
Patch1187: linux-%kernel_branch.42-feat-fs-ext4--secrm.patch
Patch1188: linux-%kernel_branch.43-feat-fs-f2fs.patch
Patch1189: linux-%kernel_branch.42-feat-fs-fat--secrm.patch
Patch1190: linux-%kernel_branch.42-feat-fs-jbd--secrm.patch
Patch1191: linux-%kernel_branch.42-feat-fs-jbd2--secrm.patch
Patch1192: linux-%kernel_branch.44-feat-fs-overlayfs.patch
Patch1193: linux-%kernel_branch.61-feat-fs-reiser4.patch
Patch1194: linux-%kernel_branch-feat-fs-subfs.patch
Patch1195: linux-%kernel_branch.42-feat-fs-squashfs--write.patch
Patch1196: linux-%kernel_branch.42-feat-fs-unionfs.patch
Patch1197: linux-%kernel_branch.44-feat-fs--lnfs.patch

Patch1201: linux-%kernel_branch.42-feat-kernel--cpe_migrate.patch
Patch1202: linux-%kernel_branch.42-feat-kernel--sched-cfs-boost.patch
Patch1203: linux-%kernel_branch.43-feat-kernel-power-tuxonice.patch

Patch1211: linux-%kernel_branch.42-feat-lib--llist.patch

Patch1221: linux-%kernel_branch.42-feat-mm--slqb.patch
Patch1222: linux-%kernel_branch.43-feat-mm--uksm.patch
Patch1223: linux-%kernel_branch.58-feat-mm--zcache.patch

Patch1231: linux-%kernel_branch-feat-net--netatop.patch
Patch1232: linux-%kernel_branch.58-feat-net-ipv4-netfilter--ipt_NETFLOW.patch
Patch1233: linux-%kernel_branch.42-feat-net-ipv4-netfilter--ipt_ipv4options.patch
Patch1234: linux-%kernel_branch.57-feat-net-netfilter--nf_conntrack_slp.patch

Patch1241: linux-%kernel_branch-feat-security--yama.patch

Patch1251: linux-%kernel_branch.47-feat-sound-firewire--snd-dice.patch
Patch1252: linux-%kernel_branch.44-feat-sound-firewire--snd-fireworks.patch
Patch1253: linux-%kernel_branch.47-feat-sound-firewire--snd-scs1x.patch
Patch1254: linux-%kernel_branch.42-feat-sound-ppc--snd-mpc52xx-ac97.patch

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

%ifnarch x86_64 i486 i586
%set_disable docs
%set_without src
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
%ifarch corei7 nehalem
%define kernel_cpu	COREI7
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
%ifarch core2_32
%define kernel_cpu	CORE2
%endif
%ifarch atom
%define kernel_cpu	ATOM
%endif
%ifarch corei7_32 nehalem_32
%define kernel_cpu	COREI7
%endif
%endif

%if "x%extra_modules" != "x"
%define extra_mods %(echo "%extra_modules" | sed 's/=[^ ]*//g')
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

Requires: bootloader-utils >= 0.4.17
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.9.8.24.1

Provides: kernel = %kversion
Provides: kernel-modules-md-%flavour = %version-%release

Requires: coreutils
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
AutoProv: no, %kernel_prov
AutoReq: no, %kernel_req

%description
This package contains the Linux kernel that is used to boot and run
your system.
Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).
The "ws" flavour of kernel packages is kernel for using on
workstations.

%define kernel_modules_package_add_provides() \
Provides: kernel-modules-%{1}-%flavour = %version-%release \
Provides: kernel-modules-%{1}-%kversion-%flavour-%krelease = %version-%release

%define kernel_modules_package_std_body() \
Group: System/Kernel and hardware \
Provides: kernel-modules-%{1}-%kversion-%flavour-%krelease = %kversion-%release \
Conflicts: kernel-modules-%{1}-%kversion-%flavour-%krelease < %kversion-%release \
Conflicts: kernel-modules-%{1}-%kversion-%flavour-%krelease > %kversion-%release \
Requires: %name = %kversion-%release \
Requires: coreutils \
Requires: module-init-tools >= 3.1 \
AutoProv: no, %kernel_prov \
AutoReq: no, %kernel_req \
%nil

%define kernel_doc_package_std_body() \
Group: Documentation \
%{?base_flavour:Provides: kernel-%{1}-%base_flavour = %version-%release} \
Provides: kernel-%{1}-%flavour = %version-%release \
BuildArch: noarch \
AutoProv: no \
AutoReq: no

%if 0
%define kernel_modules_package_post() \
%post -n kernel-modules-%{1}-%flavour \
%post_kernel_modules %kversion-%flavour-%krelease \
\
%postun -n kernel-modules-%{1}-%flavour \
%postun_kernel_modules %kversion-%flavour-%krelease
%else
%define kernel_modules_package_post() \
%nil
%endif

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


%if_enabled edac
%package -n kernel-modules-edac-%flavour
Summary: EDAC (Error Detection And Correction) driver modules
%kernel_modules_package_std_body ipmi

%description -n kernel-modules-edac-%flavour
This package contains EDAC (Error Detection And Correction) driver modules for
the Linux kernel package %name-%version-%release.
%endif


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
%package -n kernel-modules-sound-%flavour
Summary: The Advanced Linux Sound Architecture modules
%kernel_modules_package_std_body sound
%kernel_modules_package_add_provides alsa

%description -n kernel-modules-sound-%flavour
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.


%package -n kernel-modules-sound-ext-%flavour
Summary: The Advanced Linux Sound Architecture modules for external adapters
%kernel_modules_package_std_body sound-ext
%kernel_modules_package_add_provides alsa-ext

%description -n kernel-modules-sound-ext-%flavour
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.
This package contains modules for extarnal (FireWire, USB) adapters.
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
%kernel_modules_package_std_body drm

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
# Needed for webcams, disabled due wired sisyphus_check
#Requires: kernel-modules-sound-ext-%flavour = %kversion-%release

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


%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%%package -n kernel-modules-$m-%flavour
Summary: $m kernel modules
%kernel_modules_package_std_body $m

%%description -n kernel-modules-$m-%flavour
$m kernel modules.

__PACKAGE__
done)
%endif


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
cd linux-%version
#patch0000 -p1

# fix-arch-*
%patch0001 -p1
%patch0002 -p1

# fix-arch-*
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1

# fix-arch-x86*
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1

%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1

#fix-crypto--*

# fix-drivers--*
%patch0050 -p1

# fix-drivers-acpi*
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1

# fix-drivers-ata--*
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1

# fix-drivers-base*
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1

# fix-drivers-block--*
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1
%patch0095 -p1
%patch0096 -p1
%patch0097 -p1
%patch0098 -p1
%patch0099 -p1
%patch0100 -p1
%patch0101 -p1

# fix-drivers-bluetooth--*
%patch0111 -p1

# fix-drivers-char-*
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
%patch0132 -p1
%patch0133 -p1
%patch0134 -p1
%patch0135 -p1
%patch0136 -p1
%patch0137 -p1
%patch0138 -p1
%patch0139 -p1

# fix-drivers-cio*
%patch0140 -p1
%patch0141 -p1
%patch0142 -p1
%patch0143 -p1

# fix-drivers-cpuqreq--*
%patch0150 -p1
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1
%patch0155 -p1

# fix-drivers-crypto--*
%patch0161 -p1
%patch0162 -p1
%patch0163 -p1
%patch0164 -p1

# fix-drivers-dma--*
%patch0171 -p1
%patch0172 -p1
%patch0173 -p1

# fix-drivers-edac--*
%patch0181 -p1
%patch0182 -p1
%patch0183 -p1
%patch0184 -p1
%patch0185 -p1
%patch0186 -p1
%patch0187 -p1
%patch0188 -p1
%patch0189 -p1
%patch0190 -p1
%patch0191 -p1
%patch0192 -p1
%patch0193 -p1
%patch0194 -p1
%patch0195 -p1
%patch0196 -p1

%patch0201 -p1

# fix-drivers-fireware--*
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1
%patch0214 -p1
%patch0215 -p1

# fix-drivers-firmware--*
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1

%patch0231 -p1
%patch0232 -p1
%patch0233 -p1
%patch0234 -p1
%patch0235 -p1
%patch0236 -p1
%patch0237 -p1
%patch0238 -p1
%patch0239 -p1
%patch0240 -p1
%patch0241 -p1

# fix-drivers-hid--*
%patch0251 -p1
%patch0252 -p1
%patch0253 -p1
%patch0254 -p1

%patch0260 -p1

# fix-drivers-hwmon--*
%patch0271 -p1
%patch0272 -p1
%patch0273 -p1
%patch0274 -p1
%patch0275 -p1
%patch0276 -p1
%patch0277 -p1
%patch0278 -p1
%patch0279 -p1
%patch0280 -p1

# fix-drivers-i2c-*
%patch0291 -p1
%patch0292 -p1
%patch0293 -p1
%patch0294 -p1

%patch0300 -p1

# fix-drivers-idle--*
%patch0311 -p1
%patch0312 -p1

# fix-drivers-infiniband-*
%patch0321 -p1
%patch0322 -p1
%patch0323 -p1
%patch0324 -p1
%patch0325 -p1

# fix-drivers-input-*
%patch0331 -p1
%patch0332 -p1
%patch0333 -p1
%patch0334 -p1
%patch0335 -p1

%patch0341 -p1
%patch0342 -p1
%patch0343 -p1

# fix-drivers-leds--*
%patch0351 -p1

# fix-drivers-macintosh--*
%patch0361 -p1
%patch0362 -p1

# fix-drivers-md--*
%patch0371 -p1
%patch0372 -p1
%patch0373 -p1
%patch0374 -p1
%patch0375 -p1
%patch0376 -p1
%patch0377 -p1

# fix-drivers-media-*
%patch0381 -p1
%patch0382 -p1
%patch0383 -p1

%patch0391 -p1

# fix-drivers-misc-*
%patch0401 -p1
%patch0402 -p1
%patch0403 -p1
%patch0404 -p1

%patch0411 -p1

# fix-drivers-net*
%patch0420 -p1
%patch0421 -p1
%patch0422 -p1
%patch0423 -p1
%patch0424 -p1
%patch0425 -p1
%patch0426 -p1
%patch0427 -p1
%patch0428 -p1
%patch0429 -p1
%patch0430 -p1
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
%patch0469 -p1
%patch0470 -p1
%patch0471 -p1
%patch0472 -p1
%patch0473 -p1
%patch0474 -p1
%patch0475 -p1
%patch0476 -p1
%patch0477 -p1
%patch0478 -p1
%patch0479 -p1

# fix-drivers-parport--*
%patch0481 -p1

%patch0490 -p1
%patch0491 -p1
%patch0492 -p1
%patch0493 -p1
%patch0494 -p1

# fix-drivers-platform--*
%patch0501 -p1
%patch0502 -p1
%patch0503 -p1
%patch0504 -p1
%patch0505 -p1
%patch0506 -p1
%patch0507 -p1

%patch0510 -p1

%patch0521 -p1

# fix-drivers-scsi-*
%patch0531 -p1
%patch0532 -p1
%patch0533 -p1
%patch0534 -p1
%patch0535 -p1
%patch0536 -p1
%patch0537 -p1
%patch0538 -p1
%patch0539 -p1
%patch0540 -p1
%patch0541 -p1
%patch0542 -p1
%patch0543 -p1
%patch0544 -p1
%patch0545 -p1
%patch0546 -p1
%patch0547 -p1
%patch0548 -p1
%patch0549 -p1
%patch0550 -p1
%patch0551 -p1
%patch0552 -p1
%patch0553 -p1
%patch0554 -p1
%patch0555 -p1
%patch0556 -p1
%patch0557 -p1
%patch0558 -p1
%patch0559 -p1
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
%patch0578 -p1

# fix-drivers-target*
%patch0580 -p1

%patch0591 -p1

# fix-drivers-tty-*
%patch0601 -p1
%patch0602 -p1
%patch0603 -p1

# fix-drivers-usb*
%patch0610 -p1
%patch0611 -p1
%patch0612 -p1
%patch0613 -p1
%patch0614 -p1
%patch0615 -p1
%patch0616 -p1
%patch0617 -p1
%patch0618 -p1
%patch0619 -p1
%patch0620 -p1
%patch0621 -p1
%patch0622 -p1
%patch0623 -p1
%patch0624 -p1

# fix-drivers-video-*
%patch0631 -p1
%patch0632 -p1
%patch0633 -p1
%patch0634 -p1

%patch0641 -p1

%patch0651 -p1
%patch0652 -p1

%patch0661 -p1

# fix-fs*
%patch0670 -p1
%patch0671 -p1
%patch0672 -p1
%patch0673 -p1
%patch0674 -p1
%patch0675 -p1
%patch0676 -p1
%patch0677 -p1
%patch0678 -p1
%patch0679 -p1
%patch0680 -p1
%patch0681 -p1
%patch0682 -p1
%patch0683 -p1
%patch0684 -p1
%patch0685 -p1
%patch0686 -p1
%patch0687 -p1
%patch0688 -p1
%patch0689 -p1
%patch0690 -p1
%patch0691 -p1
%patch0692 -p1
%patch0693 -p1
%patch0694 -p1
%patch0695 -p1
%patch0696 -p1

%patch0700 -p1

%patch0711 -p1

%patch0721 -p1

# fix-kernel*
%patch0730 -p1
%patch0731 -p1
%patch0732 -p1
%patch0733 -p1
%patch0734 -p1
%patch0735 -p1
%patch0736 -p1
%patch0737 -p1
%patch0738 -p1
%patch0739 -p1

# fix-lib*
%patch0740 -p1
%patch0741 -p1

# fix-mm*
%patch0750 -p1
%patch0751 -p1
%patch0752 -p1
%patch0753 -p1
%patch0754 -p1
%patch0755 -p1
%patch0756 -p1
%patch0757 -p1
%patch0758 -p1
%patch0759 -p1
%patch0760 -p1
%patch0761 -p1
%patch0762 -p1
%patch0763 -p1

# fix-net*
%patch0770 -p1
%patch0771 -p1
%patch0772 -p1
%patch0773 -p1
%patch0774 -p1
%patch0775 -p1
%patch0776 -p1
%patch0777 -p1
%patch0778 -p1
%patch0779 -p1
%patch0780 -p1
%patch0781 -p1
%patch0782 -p1
%patch0783 -p1
%patch0784 -p1
%patch0785 -p1
%patch0786 -p1
%patch0787 -p1
%patch0788 -p1
%patch0789 -p1
%patch0790 -p1
%patch0791 -p1
%patch0792 -p1
%patch0793 -p1
%patch0794 -p1
%patch0795 -p1
%patch0796 -p1
%patch0797 -p1
%patch0798 -p1
%patch0799 -p1
%patch0800 -p1
%patch0801 -p1
%patch0802 -p1
%patch0803 -p1
%patch0804 -p1
%patch0805 -p1
%patch0806 -p1

%patch0810 -p1

%patch0821 -p1
%patch0822 -p1

# fix-sound-*
%patch0831 -p1
%patch0832 -p1
%patch0833 -p1
%patch0834 -p1
%patch0835 -p1
%patch0836 -p1
%patch0837 -p1
%patch0838 -p1

# fix-tools-*
%patch0841 -p1
%patch0842 -p1

# fix-virt-kvm*
%patch0851 -p1
%patch0852 -p1
%patch0853 -p1


# feat-arch-*
#patch1001 -p1

%patch1011 -p1
%patch1012 -p1
%patch1013 -p1

# feat-crypto--*
%patch1021 -p1
%patch1022 -p1

# feat-drivers-block--*
%patch1031 -p1
%patch1032 -p1

# feat-drivers-devfreq
%patch1040 -p1

# feat-drivers-edac--*
%patch1051 -p1

# feat-drivers-gpu-drm--*
%patch1061 -p1
%patch1062 -p1
%patch1063 -p1

# feat-drivers-hid--*
%patch1071 -p1

# feat-drivers-hwmon--*
%patch1081 -p1

# feat-drivers-input-*
%patch1091 -p1
%patch1092 -p1
%patch1093 -p1

%patch1101 -p1

# feat-drivers-misc--*
%patch1111 -p1
%patch1112 -p1
%patch1113 -p1

# feat-drivers-scsi--*
%patch1121 -p1

# feat-drivers-net-wireless-*
%patch1131 -p1
%patch1132 -p1
%patch1133 -p1
%patch1134 -p1
%patch1135 -p1
%patch1136 -p1
%patch1137 -p1
%patch1138 -p1

# feat-drivers-platform--*
%patch1141 -p1
%patch1142 -p1
%patch1143 -p1

# feat-drivers-usb-*
%patch1151 -p1
%patch1152 -p1

# feat-drivers-video--*
%patch1161 -p1
%patch1162 -p1

# feat-firmware-*
%patch1171 -p1

# feat-fs-*
%patch1181 -p1
%patch1182 -p1
%patch1183 -p1
%patch1184 -p1
%patch1185 -p1
%patch1186 -p1
%patch1187 -p1
%patch1188 -p1
%patch1189 -p1
%patch1190 -p1
%patch1191 -p1
%patch1192 -p1
%patch1193 -p1
%patch1194 -p1
%patch1195 -p1
%patch1196 -p1
%{?_with_lnfs:%patch1197 -p1}

%patch1201 -p1
%patch1202 -p1
%patch1203 -p1

%patch1211 -p1

# feat-mm--*
%patch1221 -p1
%patch1222 -p1
%patch1223 -p1

# feat-net-*
%patch1231 -p1
%patch1232 -p1
%patch1233 -p1
%patch1234 -p1

# feat-security--*
%patch1241 -p1

# feat-sound-*
%patch1251 -p1
%patch1252 -p1
%patch1253 -p1
%patch1254 -p1

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

%ifdef extra_mods
install -m 0644 %SOURCE10 ./Makefile.external
install -d -m 0755 external
for m in %extra_modules; do
	tar -C external -xf %kernel_src/${m%%=*}-${m#*=}.tar*
done
%endif


%build
cd linux-%version
export ARCH=%base_arch

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

%ifarch %ix86
%ifnarch i386 i486 i586
config_disable EISA
%endif
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
	%{?_disable_compat:SYSCTL_SYSCALL ACPI_PROC_EVENT COMPAT_VDSO I2C_COMPAT} \
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
	%{?_disable_smack:SECURITY_SMACK} \
	%{?_disable_yama:SECURITY_YAMA} \
	%{?_disable_thp:TRANSPARENT_HUGEPAGE} \
	%{?_disable_guest:VIRTIO DRM_KVM_CIRRUS DRM_VMWGFX} \
	%{?_disable_kvm:KVM} \
	%{?_disable_hyperv:HYPERV} \
	%{?_disable_paravirt_guest:PARAVIRT_GUEST} \
	%{?_disable_kvm_guest:KVM_GUEST} \
	%{?_disable_bootsplash:BOOTSPLASH} \
	%{?_disable_zcache:ZCACHE} \
	%{?_disable_pci:PCI} \
	%{?_disable_acpi:ACPI} \
	%{?_disable_math_emu:MATH_EMULATION} \
	%{?_disable_kallsyms:KALLSYMS} \
	%{?_disable_oprofile:PROFILING OPROFILE} \
	%{?_disable_fatelf:BINFMT_FATELF} \
	%{?_enable_ext4_for_ext23:EXT[23]_FS}

config_enable \
%ifarch i386 i486 i586 i686
	X86_GENERIC \
%endif
	%{?_enable_debug_section_mismatch:DEBUG_SECTION_MISMATCH} \
	%{?_enable_modversions:MODVERSIONS} \
	%{?_enable_x32:X86_X32_ABI} \
	%{?_enable_x86_extended_platform:X86_EXTENDED_PLATFORM} \
	%{?_enable_ext4_for_ext23:EXT4_USE_FOR_EXT23} \
	%{?_enable_mca:MCA} \
	%{?_enable_debugfs:DEBUG_FS} \
	%{?_enable_pcsp:SND_PCSP=m} \
	%{?_enable_secrm:EXT[234]_SECRM FAT_SECRM} \
	%{?_enable_nfs_swap:NFS_SWAP} \
	%{?_enable_lnfs:NFS_V4_SECURITY_LABEL NFSD_V4_SECURITY_LABEL} \
	%{?_enable_kallsyms:KALLSYMS} \
	%allocator

# arch-specific disables
%ifarch k10
config_disable SENSORS_K8TEMP
%endif
%ifarch corei7 nehalem
config_disable CRYPTO_CRC32C
%endif
%ifarch i386 i486
config_enable CRYPTO_TWOFISH=m CRYPTO_SALSA20=m
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

echo "Building kernel %kversion-%flavour-%krelease"

%make_build oldconfig
%make_build %{?_enable_verbose:V=1} bzImage modules
%if_with perf
%make_build -C tools/perf %{?_enable_verbose:V=1} \
	prefix=%_prefix perfexecdir=%_libexecdir/perf \
	EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}"
%make_build -C tools/perf %{?_enable_verbose:V=1} man
%endif

echo "Kernel built %kversion-%flavour-%krelease"

%ifdef extra_mods
%make_build -f Makefile.external %extra_mods
echo "External modules built"
%endif

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

%ifdef extra_mods
make -f Makefile.external DESTDIR=%buildroot \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	INSTALL_MOD_PATH=%modules_dir \
	%extra_mods
%endif

%{?_enable_oprofile:install -m 0644 vmlinux %buildroot%modules_dir/}

install -d -m 0755 %buildroot%kbuild_dir
cp -aL include %buildroot%kbuild_dir/
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
	scripts/depmod.sh \
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
install -d -m 0755 %kernel_srcdir
t="%__nprocs"
[ $t -gt 1 ] && XZ="pxz -T$t" || XZ="xz"
tar --transform='s,^,kernel-src-%flavour-%kversion-%krelease/,' \
	--owner=root --group=root --mode=u+w,go-w,go+rX \
	-T ../kernel-src-%flavour.list -cf - | \
	$XZ -8e > %kernel_srcdir/kernel-src-%flavour-%kversion-%krelease.tar.xz
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
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/{message/fusion,scsi{,/device_handler}/*,target} | grep -Fxv -f scsi-base.rpmmodlist > scsi.rpmmodlist
mv scsi-base.rpmmodlist scsi-base.rpmmodlist~
gen_rpmmodfile infiniband %buildroot%modules_dir/kernel/{drivers/{infiniband,scsi/scsi_transport_srp.ko},net/{9p/9pnet_rdma.ko,rds,sunrpc/xprtrdma}}
gen_rpmmodfile ipmi %buildroot%modules_dir/kernel/drivers/{acpi/acpi_ipmi,char/ipmi,{acpi/acpi_ipmi,hwmon/i{bm,pmi}*}.ko}
%{?_enable_edac:gen_rpmmodfile edac %buildroot%modules_dir/kernel/drivers/edac}
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
for i in %{?_enable_ide:ide} %{?_enable_media:media} %{?_enable_mtd:mtd} %{?_enable_w1:w1}; do
	gen_rpmmodfile $i %buildroot%modules_dir/kernel/drivers/$i
done
for i in %{?_enable_joystick:joystick} %{?_enable_lirc:lirc} %{?_enable_tablet:tablet} %{?_enable_touchscreen:touchscreen}; do
	gen_rpmmodfile $i %buildroot%modules_dir/kernel/drivers/input/$i
done
%if "%sub_flavour" != "guest"
%{?_enable_guest:gen_rpmmodfile guest %buildroot%modules_dir/kernel/{drivers/{virtio,{char{,/hw_random},net,block}/virtio*%{?_enable_drm:,gpu/drm/{cirrus,vmwgfx}}},net/9p/*_virtio.ko}}
%{?_enable_drm:grep -F -f drm.rpmmodlist guest.rpmmodlist | sed 's/^/%%exclude &/' >> drm.rpmmodlist}
%endif
sed 's/^/%%exclude &/' *.rpmmodlist > exclude-drivers.rpmmodlist

%{?_enable_oprofile:%add_verify_elf_skiplist %modules_dir/vmlinux}


%if 0
%post
[ -x /usr/lib/rpm/boot_kernel.filetrigger ] || /sbin/installkernel %kversion-%flavour-%krelease
%endif

%preun
/sbin/installkernel --remove %kversion-%flavour-%krelease


%kernel_modules_package_post scsi

%kernel_modules_package_post infiniband

%kernel_modules_package_post ipmi

%{?_enable_edac:%kernel_modules_package_post edac}

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

%kernel_modules_package_post fs-extra

%kernel_modules_package_post net-extra

%{?_enable_oss:%kernel_modules_package_post oss}

%{?_enable_ide:%kernel_modules_package_post ide}

%{?_enable_drm:%kernel_modules_package_post drm}

%{?_enable_media:%kernel_modules_package_post media}

%if_enabled alsa
%kernel_modules_package_post sound

%kernel_modules_package_post sound-ext
%endif

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


%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%kernel_modules_package_post $m

__PACKAGE__
done)
%endif


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
%exclude %modules_dir/kernel/drivers/usb/misc/emi*
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
%exclude %modules_dir/kernel/fs/subfs
%exclude %modules_dir/kernel/fs/sysv
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

%{?_enable_edac:%kernel_modules_package_files edac}

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
%modules_dir/kernel/fs/subfs
%modules_dir/kernel/fs/sysv
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
%files -n kernel-modules-sound-%flavour
%modules_dir/kernel/sound
%{?_enable_oss:%exclude %modules_dir/kernel/sound/oss}
%exclude %modules_dir/kernel/sound/*.ko
%exclude %modules_dir/kernel/sound/firewire
%exclude %modules_dir/kernel/sound/usb


%files -n kernel-modules-sound-ext-%flavour
%modules_dir/kernel/sound/firewire
%modules_dir/kernel/sound/usb
%modules_dir/kernel/drivers/usb/misc/emi*
%endif


%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_files guest}
%{?_enable_drm:%dir %modules_dir/kernel/drivers/gpu/drm}
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
%dir /lib/firmware
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
%firmware_dir/rtl_nic
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


%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%%files -n kernel-modules-$m-%flavour -f linux-%kversion/external/$m.rpmmodlist

__PACKAGE__
done)
%endif


%files -n kernel-headers-modules-%flavour-%kernel_branch
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build


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
%_usrsrc/kernel
%endif


%changelog
* Tue Jan 29 2013 Led <led@altlinux.ru> 3.0.61-alt3
- updated:
  + fix-arch-x86--mcheck
  + fix-drivers-acpi
  + fix-drivers-edac--edac_mce_amd
  + fix-drivers-edac--i5100_edac
  + fix-drivers-edac--i7core_edac
  + fix-fs
  + fix-net-rds--rds_rdma
- added:
  + fix-drivers-edac--amd64_edac_mod
  + fix-drivers-net

* Tue Jan 29 2013 Led <led@altlinux.ru> 3.0.61-alt2
- build with SLAB allocator

* Mon Jan 28 2013 Led <led@altlinux.ru> 3.0.61-alt1
- 3.0.61
- updated:
  + fix-drivers-cpufreq--p4-clockmod
  + fix-drivers-edac--e752x_edac
  + fix-drivers-edac--i3000_edac
  + fix-drivers-edac--i5000_edac
  + fix-drivers-edac--i5100_edac
  + fix-drivers-edac--i5400_edac
  + fix-drivers-edac--i7300_edac
  + fix-drivers-edac--i82975x_edac
  + fix-drivers-edac--x38_edac
  + fix-drivers-scsi--sd_mod

* Sat Jan 26 2013 Led <led@altlinux.ru> 3.0.60-alt5
- updated:
  + fix-drivers-net--e1000e
- merged kernel-headers-asm-* to kernel-headers-* subpackage
- set kernel-headers-* as no noarch

* Fri Jan 25 2013 Led <led@altlinux.ru> 3.0.60-alt4
- updated:
  + fix-mm
  + fix-mm--compaction
  + fix-mm--zcache
  + fix-virt-kvm

* Fri Jan 25 2013 Led <led@altlinux.ru> 3.0.60-alt3
- updated:
  + fix-drivers-hv
  + fix-fs-btrfs

* Thu Jan 24 2013 Led <led@altlinux.ru> 3.0.60-alt2
- updated:
  + fix-drivers-cio
  + fix-drivers-net--bonding
  + fix-net-xfrm--xfrm_policy
- added:
  + fix-drivers-tty--pty
  + fix-kernel-irq
  + feat-net-ipv4-netfilter--ipt_NETFLOW
- moved subfs to kernel-modules-fs-extra-* subpackage

* Tue Jan 22 2013 Led <led@altlinux.ru> 3.0.60-alt1
- 3.0.60
- updated:
  + fix-arch-x86
  + fix-drivers-scsi--lpfc
  + fix-drivers-usb-core
- added:
  + feat-firmware-rtl_nic

* Sat Jan 19 2013 Led <led@altlinux.ru> 3.0.59-alt4
- removed:
  + fix-net-bridge
- updated:
  + feat-fs-aufs
- added:
  + fix-net-bridge--bridge

* Sat Jan 19 2013 Led <led@altlinux.ru> 3.0.59-alt3
- removed external modules:
  + fglrx

* Fri Jan 18 2013 Led <led@altlinux.ru> 3.0.59-alt2
- removed:
  + fix-drivers-misc--zcache
  + feat-drivers-misc--zcache
- updated:
  + fix-fs-btrfs
- added:
  + fix-mm--zcache
  + feat-mm--zcache
- disable CRYPTO_FIPS

* Fri Jan 18 2013 Led <led@altlinux.ru> 3.0.59-alt1
- 3.0.59
- updated:
  + fix-drivers-firewire--firewire-net
  + fix-drivers-usb-core
  + fix-mm--huge_memory
  + fix-mm--mmu
  + fix-net-core

* Thu Jan 17 2013 Led <led@altlinux.ru> 3.0.58-alt5
- disabled compat (turn off some COMPAT options in .config)

* Thu Jan 17 2013 Led <led@altlinux.ru> 3.0.58-alt4
- updated:
  + feat-fs--lnfs
- added:
  + fix-drivers-crypto--padlock
- move EDAC modules to separate subpackage kernel-modules-edac-*

* Tue Jan 15 2013 Led <led@altlinux.ru> 3.0.58-alt3
- updated:
  + fix-drivers-md--dm-multipath

* Sat Jan 12 2013 Led <led@altlinux.ru> 3.0.58-alt2
- disabled PM_DEVFREQ

* Sat Jan 12 2013 Led <led@altlinux.ru> 3.0.58-alt1
- 3.0.58
- updated:
  + fix-drivers-pci
  + fix-drivers-usb-host--ehci-hcd
  + fix-fs-btrfs
  + fix-mm--mmu

* Fri Jan 11 2013 Led <led@altlinux.ru> 3.0.57-alt21
- added:
  + fix-drivers-base-power--opp
  + feat-drivers-devfreq
  + feat-drivers-edac--sb_edac
  + feat-drivers-input-touchscreen--tsc40
  + feat-drivers-platform--amilo-rfkill
  + feat-drivers-platform--fujitsu-tablet
  + feat-drivers-scsi--mvumi
  + feat-drivers-usb-storage--rts5139

* Fri Jan 11 2013 Led <led@altlinux.ru> 3.0.57-alt20
- updated:
  + fix-lib

* Thu Jan 10 2013 Led <led@altlinux.ru> 3.0.57-alt19
- added:
  + feat-crypto--blowfish-x86_64
  + feat-crypto--sha1-ssse3

* Thu Jan 10 2013 Led <led@altlinux.ru> 3.0.57-alt18
- removed:
  + fix-crypto--ghash-clmulni-intel
- updated:
  + fix-arch-x86--mcheck
- disabled
  - DEBUG_NX_TEST
  - CRYPTO_TWOFISH
  - CRYPTO_SALSA20

* Thu Jan 10 2013 Led <led@altlinux.ru> 3.0.57-alt17
- updated:
  + fix-kernel

* Thu Jan 10 2013 Led <led@altlinux.ru> 3.0.57-alt16
- added:
  + feat-net-netfilter--nf_conntrack_slp
- updated requires for kernel-image-* package
- updated requires for kernel-modules-* subpackages

* Wed Jan 09 2013 Led <led@altlinux.ru> 3.0.57-alt15
- updated:
  + fix-drivers-firewire--firewire-core
  + fix-drivers-firewire--firewire-net
  + fix-drivers-firewire--firewire-ohci
  + fix-include
  + fix-sound-firewire--snd-firewire-lib
  + feat-sound-firewire--snd-dice
- added:
  + fix-drivers-firewire--firewire-sbp2
  + fix-drivers-firewire--nosy
  + fix-sound-firewire--snd-firewire-speakers
  + fix-sound-firewire--snd-isight
  + fix-tools-firewire--nosy-dump
  + feat-sound-firewire--snd-scs1x
- kernel-modules-media-* requires kernel-modules-sound-ext-* (for webcams)

* Wed Jan 09 2013 Led <led@altlinux.ru> 3.0.57-alt14
- added:
  + fix-drivers-input-mouse--elantech
  + fix-drivers-media-video-gspca--pac7302

* Tue Jan 08 2013 Led <led@altlinux.ru> 3.0.57-alt13
- updated:
  + fix-mm--mmu
- without x32
- disabled x32

* Sat Jan 05 2013 Led <led@altlinux.ru> 3.0.57-alt12
- really enabled X86_X32_ABI

* Thu Jan 03 2013 Led <led@altlinux.ru> 3.0.57-alt11
- updated:
  + fix-mm

* Fri Dec 28 2012 Led <led@altlinux.ru> 3.0.57-alt10
- updated:
  + fix-include
- added:
  + feat-arch-x86--x32
- enabled x32

* Thu Dec 27 2012 Led <led@altlinux.ru> 3.0.57-alt9
- updated:
  + fix-fs-btrfs

* Thu Dec 27 2012 Led <led@altlinux.ru> 3.0.57-alt8
- removed external modules:
  + netatop
- removed:
  + fix-drivers-net--qeth
- updated:
  + fix-fs-ocfs2
- added:
  + fix-drivers-net--netiucv
  + fix-drivers-net-qeth
  + feat-net--netatop

* Tue Dec 25 2012 Led <led@altlinux.ru> 3.0.57-alt7
- removed:
  + fix-kernel--module

* Mon Dec 24 2012 Led <led@altlinux.ru> 3.0.57-alt6
- updated:
  + fix-drivers-scsi--qla2xxx
  + fix-fs-btrfs

* Sun Dec 23 2012 Led <led@altlinux.ru> 3.0.57-alt5
- updated:
  + fix-net-core
- vboxhost 4.1.24
- added external modules:
  + netatop

* Thu Dec 20 2012 Led <led@altlinux.ru> 3.0.57-alt4
- added:
  + feat-drivers-net-wireless--vt6655
  + feat-drivers-net-wireless--vt6656
- revert kernel-image preun script

* Wed Dec 19 2012 Led <led@altlinux.ru> 3.0.57-alt3
- added missed:
  + fix-net-xfrm--xfrm_policy
  + feat-drivers-platform--tp_smapi

* Wed Dec 19 2012 Led <led@altlinux.ru> 3.0.57-alt2
- updated:
  + fix-fs--block
  + fix-mm--huge_memory
  + fix-mm--mmu

* Tue Dec 18 2012 Led <led@altlinux.ru> 3.0.57-alt1
- 3.0.57
- removed:
  + fix-drivers-usb-host--ohci-hcd
- updated:
  + feat-fs-aufs
  + feat-kernel--sched-cfs-boost

* Thu Dec 13 2012 Led <led@altlinux.ru> 3.0.56-alt2
- updated:
  + fix-drivers-md--md-mod
  + fix-drivers-net--e1000e
  + fix-drivers-net-wireless-rt2x00
  + fix-drivers-usb-core
  + fix-fs
  + fix-fs-nfs
  + feat-drivers-misc--rts_pstor
- added:
  + fix-arch-x86-boot
  + fix-drivers-hid--hid-microsoft
  + fix-drivers-hid--hid-uclogic
  + fix-drivers-input-mouse--bcm5974
  + fix-drivers-input-tablet--wacom_wac
  + fix-drivers-net--skge
  + fix-drivers-net-wireless-mwifiex--mwifiex
  + fix-drivers-net-wireless-mwifiex--mwifiex_sdio
  + fix-drivers-net-wireless-rtlwifi
  + fix-drivers-net-wireless-rtlwifi--rtl8192ce
  + fix-drivers-net-wireless-rtlwifi--rtl8192cu
  + fix-drivers-net-wireless-rtlwifi--rtl8192se
  + fix-drivers-net-wireless-wl12xx--wl12xx
  + fix-drivers-platform--ideapad-laptop
  + fix-drivers-platform--samsung-laptop
  + fix-fs-fat
  + fix-fs-squashfs
  + fix-kernel--module
  + feat-drivers-hid--hid-speedlink
  + feat-drivers-misc--fsa9480
  + feat-drivers-net-wireless-rtlwifi--rtl8192de
  + feat-drivers-platform--samsung-q10
- disabled kernel-image and kernel-modules post scripts

* Mon Dec 10 2012 Led <led@altlinux.ru> 3.0.56-alt1
- 3.0.56
- really uksm disabled by default

* Fri Dec 07 2012 Led <led@altlinux.ru> 3.0.55-alt1
- 3.0.55
- updated:
  + fix-arch-x86
  + fix-drivers-gpu-drm--i915
  + fix-drivers-net--bonding
- added:
  + fix-fs-xfs

* Thu Dec 06 2012 Led <led@altlinux.ru> 3.0.54-alt3
- updated:
  + fix-fs-autofs4

* Wed Dec 05 2012 Led <led@altlinux.ru> 3.0.54-alt2
- updated:
  + fix-net-ipv6
  + feat-drivers-video--bootsplash
  + feat-mm--uksm

* Tue Dec 04 2012 Led <led@altlinux.ru> 3.0.54-alt1
- 3.0.54
- removed:
  + fix-arch-x86--microcode_amd
- updated:
  + fix-arch-x86
  + fix-arch-x86--mcheck
  + fix-fs-jbd
  + feat-mm--uksm
- uksm disabled by default

* Fri Nov 30 2012 Led <led@altlinux.ru> 3.0.53-alt5
- updated:
  + fix-fs-btrfs
- added:
  + fix-net-netfilter-ipset

* Thu Nov 29 2012 Led <led@altlinux.ru> 3.0.53-alt4
- updated:
  + fix-drivers-cio--qdio
  + fix-drivers-crypto--s390
  + fix-drivers-net--qeth
  + fix-drivers-pci
  + fix-drivers-scsi--zfcp
  + fix-drivers-usb-host--ehci-hcd

* Thu Nov 29 2012 Led <led@altlinux.ru> 3.0.53-alt3
- updated:
  + fix-drivers-net--cnic
  + fix-drivers-net--tg3
  + fix-net-core
- added:
  + fix-arch-x86--microcode_amd
  + fix-drivers-isdn-hardware-mISDN--hfcsusb
  + fix-net-ipv4-netfilter--iptable_nat
  + fix-net-ipv4-netfilter--nf_nat
  + fix-net-ipv4-netfilter--nf_nat_amanda
  + fix-net-ipv4-netfilter--nf_nat_ftp
  + fix-net-ipv4-netfilter--nf_nat_h323
  + fix-net-ipv4-netfilter--nf_nat_irc
  + fix-net-ipv4-netfilter--nf_nat_pptp
  + fix-net-ipv4-netfilter--nf_nat_sip
  + fix-net-ipv4-netfilter--nf_nat_snmp_basic
  + fix-net-ipv4-netfilter--nf_nat_tftp
  + fix-net-netfilter--nf_conntrack
  + fix-net-sched

* Wed Nov 28 2012 Led <led@altlinux.ru> 3.0.53-alt2
- updated:
  + fix-drivers-ata--ahci
  + fix-drivers-ata--ata_piix
  + fix-drivers-watchdog--iTCO_wdt
  + fix-fs
  + fix-fs-reiserfs
  + fix-sound-pci-hda
- added:
  + fix-drivers-i2c-busses--i2c-i801
  + fix-drivers-usb-host--ohci-hcd
  + fix-fs--anon_inodes
  + fix-fs-autofs4
  + fix-net

* Tue Nov 27 2012 Led <led@altlinux.ru> 3.0.53-alt1
- 3.0.53
- removed:
  + fix-Makefile
- updated:
  + fix-mm

* Tue Nov 27 2012 Led <led@altlinux.ru> 3.0.52-alt5
- updated:
  + fix-arch-powerpc
  + fix-block
  + fix-drivers-block--dasd_mod
  + fix-drivers-md--md-mod
  + fix-drivers-md--raid1
  + fix-drivers-md--raid10
  + fix-drivers-md--raid456
  + fix-fs--block
  + fix-fs-jbd
  + fix-fs-reiserfs
- added:
  + fix-drivers-md--multipath

* Sat Nov 24 2012 Led <led@altlinux.ru> 3.0.52-alt4
- updated:
  + fix-drivers-usb-host--xhci-hcd

* Fri Nov 23 2012 Led <led@altlinux.ru> 3.0.52-alt3
- updated:
  + fix-fs-btrfs

* Thu Nov 22 2012 Led <led@altlinux.ru> 3.0.52-alt2
- updated:
  + fix-fs-btrfs

* Sun Nov 18 2012 Led <led@altlinux.ru> 3.0.52-alt1
- 3.0.52
- updated:
  + fix-drivers-gpu-drm--i915
  + fix-drivers-gpu-drm--radeon
  + fix-drivers-scsi-ibmvscsi--ibmvfc
  + fix-fs--block
  + fix-fs-btrfs
  + fix-fs-nfs
  + fix-net-ipv6
- added:
  + fix-kernel--smp

* Thu Nov 15 2012 Led <led@altlinux.ru> 3.0.51-alt8
- updated:
  + fix-drivers-usb-host--xhci-hcd
- strip external modules
- disabled external modules:
  + vboxguest

* Thu Nov 15 2012 Led <led@altlinux.ru> 3.0.51-alt7
- updated:
  + fix-drivers-usb-core
  + fix-fs-btrfs
- added:
  + fix-mm--memory_hotplug
- added external modules build:
  + vboxguest
  + vboxhost
  + fglrx

* Mon Nov 12 2012 Led <led@altlinux.ru> 3.0.51-alt6
- updated:
  + fix-drivers-firmware--efivars
  + fix-fs

* Thu Nov 08 2012 Led <led@altlinux.ru> 3.0.51-alt5
- updated:
  + fix-drivers-net--igb

* Thu Nov 08 2012 Led <led@altlinux.ru> 3.0.51-alt4
- updated:
  + fix-drivers-gpu-drm--radeon

* Wed Nov 07 2012 Led <led@altlinux.ru> 3.0.51-alt3
- updated:
  + fix-arch-x86
  + fix-drivers-block--dasd_mod
  + fix-mm
- addded:
  + fix-drivers-net--smsguicv

* Tue Nov 06 2012 Led <led@altlinux.ru> 3.0.51-alt2
- updated:
  + fix-virt-kvm

* Mon Nov 05 2012 Led <led@altlinux.ru> 3.0.51-alt1
- 3.0.51
- updated:
  + fix-drivers-block--floppy
  + fix-mm
- added:
  + fix-drivers-idle--intel_idle

* Sat Nov 03 2012 Led <led@altlinux.ru> 3.0.50-alt6
- updated:
  + fix-drivers-cpufreq--powernow-k8
  + fix-fs-btrfs

* Fri Nov 02 2012 Led <led@altlinux.ru> 3.0.50-alt5
- updated post/preun scripts: %%{post,preun}_kernel_image macros obsoleted now

* Fri Nov 02 2012 Led <led@altlinux.ru> 3.0.50-alt4
- updated:
  + fix-arch-x86
- added:
  + fix-drivers-misc--hpilo
- CONFIG_PHYSICAL_ALIGN=0x200000 for x86

* Fri Nov 02 2012 Led <led@altlinux.ru> 3.0.50-alt3
- updated:
  + fix-drivers-net--ixgbe

* Thu Nov 01 2012 Led <led@altlinux.ru> 3.0.50-alt2
- updated:
  + fix-arch-ia64
  + fix-drivers-hv
  + fix-drivers-pci--sn
  + fix-tools--perf
- added:
  + fix-drivers-scsi--sg
  + fix-kernel--events

* Thu Nov 01 2012 Led <led@altlinux.ru> 3.0.50-alt1
- 3.0.50
- removed:
  + fix-drivers-usb-storage--usb-storage
- updated:
  + fix-arch-x86

* Wed Oct 31 2012 Led <led@altlinux.ru> 3.0.49-alt4
- updated:
  + fix-mm
  + firx-mm--swap

* Wed Oct 31 2012 Led <led@altlinux.ru> 3.0.49-alt3
- updated:
  + fix-drivers-watchdog--hpwdt
  + fix-virt-kvm (CVE-2012-1601)

* Mon Oct 29 2012 Led <led@altlinux.ru> 3.0.49-alt2
- added:
  + feat-security--yama

* Sun Oct 28 2012 Led <led@altlinux.ru> 3.0.49-alt1
- 3.0.49
- updated:
  + fix-drivers-gpu-drm--i915
  + fix-drivers-usb-host--xhci-hcd

* Fri Oct 26 2012 Led <led@altlinux.ru> 3.0.48-alt4
- updated:
  + fix-mm--mmu
- added:
  + fix-arch-x86-cpu--rdrand

* Fri Oct 26 2012 Led <led@altlinux.ru> 3.0.48-alt3
- added:
  + fix-fs-ext4

* Thu Oct 25 2012 Led <led@altlinux.ru> 3.0.48-alt2
- updated:
  + fix-drivers-gpu-drm--i915

* Tue Oct 23 2012 Led <led@altlinux.ru> 3.0.48-alt1
- 3.0.48

* Sun Oct 21 2012 Led <led@altlinux.ru> 3.0.47-alt1
- 3.0.47
- updated:
  + fix-drivers-acpi
  + fix-drivers-gpu-drm--radeon
  + fix-drivers-net--tg3

* Sun Oct 21 2012 Led <led@altlinux.ru> 3.0.46-alt10
- updated:
  + fix-drivers-usb-storage--usb-storage

* Sun Oct 21 2012 Led <led@altlinux.ru> 3.0.46-alt9
- updated:
  + fix-drivers-net--qeth
- added:
  + fix-drivers-usb-storage--usb-storage

* Fri Oct 19 2012 Led <led@altlinux.ru> 3.0.46-alt8
- updated:
  + fix-drivers-net-usb--asix
  + fix-drivers-usb
  + fix-drivers-usb-core
  + fix-drivers-usb-host--xhci-hcd
  + fix-include

* Fri Oct 19 2012 Led <led@altlinux.ru> 3.0.46-alt7
- updated:
  + fix-fs-btrfs

* Thu Oct 18 2012 Led <led@altlinux.ru> 3.0.46-alt6
- updated:
  + fix-fs-btrfs

* Thu Oct 18 2012 Led <led@altlinux.ru> 3.0.46-alt5
- updated:
  + fix-drivers-char-ipmi--ipmi_si
  + fix-drivers-net--qeth
  + fix-drivers-net--qlge
  + fix-drivers-net-mlx4--mlx4_en
- added:
  + fix-drivers-char-ipmi--ipmi_msghandler
  + fix-drivers-net--cxgb3
- fixed of unowned dirs

* Tue Oct 16 2012 Led <led@altlinux.ru> 3.0.46-alt4
- updated:
  + fix-fs-btrfs
- enable EISA for i[345]86 only

* Mon Oct 15 2012 Led <led@altlinux.ru> 3.0.46-alt3
- added:
  + fix-drivers-firewire--firewire-core
  + fix-drivers-firewire--firewire-net
  + fix-drivers-firewire--firewire-ohci
  + fix-drivers-media-dvb-firewire--firedtv
  + fix-drivers-media-dvb-firewire--firedtv
  + feat-sound-firewire--snd-dice
  + feat-sound-firewire--snd-fireworks
- fixed typo in description

* Sun Oct 14 2012 Led <led@altlinux.ru> 3.0.46-alt2
- updated:
  + fix-kernel-time

* Sat Oct 13 2012 Led <led@altlinux.ru> 3.0.46-alt1
- 3.0.46
- removed:
  + fix-drivers-net--r8169
- updated:
  + fix-drivers-net--tg3
  + fix-drivers-pci-hotplug--acpiphp
  + fix-drivers-scsi--zfcp
  + fix-mm--numa
  + fix-net-core

* Fri Oct 12 2012 Led <led@altlinux.ru> 3.0.45-alt6
- updated:
  + fix-mm--memcontrol
- added:
  + fix-net-rds--rds_rdma

* Thu Oct 11 2012 Led <led@altlinux.ru> 3.0.45-alt5
- updated:
  + fix-block
  + fix-drivers-scsi--scsi_mod
  + fix-drivers-scsi-device_handler--scsi_dh_alua
  + fix-mm--numa
- added:
  + fix-fs-cachefiles
- enabled:
  + PM_DEBUG
  + PM_ADVANCED_DEBUG

* Tue Oct 09 2012 Led <led@altlinux.ru> 3.0.45-alt4
- updated
  + fix-drivers-gpu-drm
  + fix-drivers-gpu-drm--drm
  + fix-drivers-gpu-drm--i915
  + feat-fs-subfs

* Mon Oct 08 2012 Led <led@altlinux.ru> 3.0.45-alt3
- updated:
  + fix-drivers-net--sfc
  + fix-drivers-scsi-megaraid--megaraid_sas
  + feat-fs-subfs

* Mon Oct 08 2012 Led <led@altlinux.ru> 3.0.45-alt2
- updated:
  + fix-drivers-md--dm-mod
  + feat-fs-subfs

* Mon Oct 08 2012 Led <led@altlinux.ru> 3.0.45-alt1
- 3.0.45
- updated:
  + fix-drivers-md--dm-mod
- added scripts/depmod.sh to kernel-headers-modules-* subpackage

* Sun Oct 07 2012 Led <led@altlinux.ru> 3.0.44-alt6
- updated:
  + fix-drivers-hv
- added:
  + feat-fs-dazukofs
  + feat-fs-f2fs
- moved ufs.ko to kernel-image-* package

* Fri Oct 05 2012 Led <led@altlinux.ru> 3.0.44-alt5
- really move drivers/target to kernel-modules-scsi-* subpackage

* Fri Oct 05 2012 Led <led@altlinux.ru> 3.0.44-alt4
- updated:
  + fix-block
  + fix-drivers-scsi--zfcp
  + fix-kernel
  + fix-mm
  + fix-mm--hugetlb
  + fix-mm--mmu
- added:
  + fix-arch-s390
  + fix-arch-s390--lib
  + fix-drivers-base
  + fix-drivers-block--dasd_diag_mod
  + fix-drivers-block--dasd_eckd_mod
  + fix-drivers-block--dasd_fba_mod
  + fix-drivers-block--dasd_mod
  + fix-drivers-char--con3215
  + fix-drivers-char--random
  + fix-drivers-char--raw3270
  + fix-drivers-char--sclp_async
  + fix-drivers-char--tape
  + fix-drivers-char--tape_34xx
  + fix-drivers-char--tape_3590
  + fix-drivers-char--virtio_console
  + fix-drivers-char--vmur
  + fix-drivers-char--zcore_mod
  + fix-drivers-cio
  + fix-drivers-cio--ccw_device
  + fix-drivers-cio--ccwgroup
  + fix-drivers-cio--qdio
  + fix-drivers-crypto--ap
  + fix-drivers-crypto--s390
  + fix-drivers-net--claw
  + fix-drivers-net--ctcm
  + fix-drivers-net--lcs
  + fix-drivers-net--qeth
  + fix-fs-partition--ibm
  + fix-fs-s390_hypfs
  + fix-net-iucv--af_iucv
  + fix-net-iucv--iucv
- moved drivers/target to kernel-modules-scsi-* subpackage

* Thu Oct 04 2012 Led <led@altlinux.ru> 3.0.44-alt3
- removed:
  + fix-drivers-target--tcm_fc
- updated:
  + fix-drivers-net--bnx2
  + fix-drivers-net--sfc
  + fix-drivers-net-mlx4--mlx4_en
  + fix-drivers-scsi--bnx2fc
  + fix-drivers-scsi--scsi_mod
  + fix-drivers-scsi-cxgbi--libcxgbi
  + fix-drivers-scsi-fcoe
  + fix-net-core
- added:
  + fix-drivers-firmware--iscsi_ibft
  + fix-drivers-infiniband-ulp-iser
  + fix-drivers-net--bnx2x
  + fix-drivers-net--cnic
  + fix-drivers-scsi--be2iscsi
  + fix-drivers-scsi--bnx2i
  + fix-drivers-scsi--iscsi_boot_sysfs
  + fix-drivers-scsi--iscsi_tcp
  + fix-drivers-scsi--libiscsi
  + fix-drivers-scsi--qla4xxx
  + fix-drivers-scsi--scsi_transport_iscsi
  + fix-drivers-scsi-cxgbi--cxgb3i
  + fix-drivers-scsi-cxgbi--cxgb4i
  + fix-drivers-target
  + fix-net-ipv6-netfilter--nf_conntrack_ipv6
- move include/asm/ to new kernel-headers-asm-* subpackage
- fixed Group of kernel-headers subpackage

* Thu Oct 04 2012 Led <led@altlinux.ru> 3.0.44-alt2
- updated:
  + fix-arch-x86
- added:
  + fix-drivers-cpufreq--acpi-cpufreq
  + fix-drivers-cpufreq--p4-clockmod
  + fix-drivers-cpufreq--powernow-k8
  + fix-drivers-dma-ioat

* Wed Oct 03 2012 Led <led@altlinux.ru> 3.0.44-alt1
- 3.0.44
- removed:
  + fix-drivers-bluetooth--btusb
  + fix-net-rds--rds
- updated:
  + fix-arch-x86--mcheck
  + fix-drivers-acpi
  + fix-drivers-md--md-mod
  + fix-drivers-usb-host--xhci-hcd
  + fix-fs
  + fix-kernel
  + feat-fs--lnfs

* Tue Oct 02 2012 Led <led@altlinux.ru> 3.0.43-alt17
- updated:
  + fix-Makefile
  + fix-drivers-gpu-drm--nouveau
  + fix-net-ipv4
  + fix-net-ipv6

* Tue Oct 02 2012 Led <led@altlinux.ru> 3.0.43-alt16
- added:
  + fix-drivers-gpu-drm--nouveau
- enabled DRM_NOUVEAU

* Tue Oct 02 2012 Led <led@altlinux.ru> 3.0.43-alt15
- updated:
  + fix-drivers-gpu-drm--psb_gfx
  + fix-drivers-hwmon--applesmc
  + fix-drivers-hwmon--coretemp
  + fix-drivers-hwmon--k10temp
  + fix-drivers-net-wireless-brcm80211--brcmfmac
- added:
  + fix-drivers-ata--ata_piix
  + fix-drivers-ata--pata_amd
  + fix-drivers-ata--pata_mpiix
  + fix-drivers-ata--pata_oldpiix
  + fix-drivers-ata--pata_sch
  + fix-drivers-char-hw_random--amd-rng
  + fix-drivers-char-hw_random--intel-rng
  + fix-drivers-hwmon--abitguru
  + fix-drivers-hwmon--asc7621
  + fix-drivers-hwmon--fam15h_power
  + fix-drivers-hwmon--i5k_amb
  + fix-drivers-hwmon--k8temp
  + fix-drivers-hwmon--via-cputemp
  + fix-drivers-hwmon--via686a
  + feat-mm--uksm
- cleaned up spec

* Mon Oct 01 2012 Led <led@altlinux.ru> 3.0.43-alt14
- added:
  + fix-drivers-dma--intel_mid_dma
  + fix-drivers-i2c-busses--i2c-intel-mid
  + fix-drivers-platform--intel_ips
  + fix-drivers-platform--intel_menlow
  + fix-drivers-platform--intel_oaktrail
- build with gcc 4.7
- fixed kernel-modules-{alsa,drm,media}-* provides and conflicts
- renamed kernel-modules-alsa to kernel-modules-sound
- moved sound/{firewire,usb} to new kernel-modules-sound-ext-* subpackage
- moved drivers/usb/misc/emi* to kernel-modules-sound-ext-*
- moved net/9p/9pnet_virtio.ko to kernel-modules-guest-*
- disabled TOI_REPLACE_SWSUSP
- cleaned up spec

* Mon Oct 01 2012 Led <led@altlinux.ru> 3.0.43-alt13
- added:
  + fix-Makefile
  + fix-drivers-edac--e752x_edac
  + fix-drivers-edac--e7xxx_edac
  + fix-drivers-edac--i3000_edac
  + fix-drivers-edac--i3200_edac
  + fix-drivers-edac--i5000_edac
  + fix-drivers-edac--i5100_edac
  + fix-drivers-edac--i5400_edac
  + fix-drivers-edac--i82443bxgx_edac
  + fix-drivers-edac--i82860_edac
  + fix-drivers-edac--i82875p_edac
  + fix-drivers-edac--i82975x_edac
  + fix-drivers-edac--x38_edac
  + fix-drivers-gpu-drm--i915
  + fix-drivers-net-wireless-brcm80211--brcmfmac
  + fix-drivers-net-wireless-rtl8192e
  + feat-drivers-gpu-drm--gma500
  + feat-drivers-net-wireless-brcm80211
  + feat-drivers-net-wireless-rtl8187se
  + feat-drivers-net-wireless-rtl8192e
  + feat-drivers-net-wireless-rtl8192u
  + feat-drivers-net-wireless-rtl8712

* Fri Sep 28 2012 Led <led@altlinux.ru> 3.0.43-alt12
- removed:
  + fix-drivers-gpu-drm--gma500
- updated:
  + fix-drivers-char-agp--intel-agp
  + fix-drivers-edac--i7300_edac
  + fix-drivers-edac--i7core_edac
  + fix-drivers-gpu-drm--drm
- added:
  + fix-crypto--ghash-clmulni-intel
  + fix-drivers-gpu-drm--psb_gfx
  + fix-drivers-idle--i7300_idle
  + fix-virt-kvm--kvm-amd
  + fix-virt-kvm--kvm-intel
  + feat-drivers-gpu-drm--gma500
- disabled STUB_POULSBO

* Fri Sep 28 2012 Led <led@altlinux.ru> 3.0.43-alt11
- removed
  + feat-drivers-gpu-drm--gma500
- updated:
  + fix-drivers-gpu-drm--gma500
- added:
  + feat-drivers-gpu-drm--psb_gfx

* Thu Sep 27 2012 Led <led@altlinux.ru> 3.0.43-alt10
- updated:
  + fix-drivers-block--nbd
- added:
  + fix-drivers-gpu-drm--gma500
  + fix-drivers-video--xgifb
  + feat-drivers-gpu-drm--gma500
  + feat-drivers-video--xgifb
- with lnfs
- enabled lnfs

* Wed Sep 26 2012 Led <led@altlinux.ru> 3.0.43-alt9
- updated:
  + fix-drivers-gpu-drm--i915
  + fix-drivers-scsi--scsi_mod
  + fix-fs-proc
  + fix-mm--hugetlb
  + fix-net-sunrpc

* Wed Sep 26 2012 Led <led@altlinux.ru> 3.0.43-alt8
- updated:
  + fix-fs-nfs
  + feat-fs-overlayfs
- added:
  + feat-drivers-hwmon--ipmisensors
  + feat-fs--lnfs
- without lnfs
- disabled lnfs
- moved acpi_ipmi.ko to kernel-modules-ipmi-* subpackage

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
