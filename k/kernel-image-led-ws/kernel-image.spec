%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_with() %{expand:%%force_with %{1}} %{expand:%%undefine _without_%{1}}
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%define intel_64 nocona core2 corei7 nehalem
%define intel_32 pentium pentiumpro pentium_mmx pentium2 pentium3 pentium_m pentium4 prescott atom
%define amd_32 5x86 k5 k6 k6_2 k6_3 geode k7 athlon athlon_xp
%define amd_64 opteron k8 k9 k10 barcelona phenom
%define via_64 nano
%define via_32 c3 c3_2
%define x86_64 x86_64 %intel_64 %amd_64 %via_64

%define extra_modules %nil
%define Extra_modules() BuildRequires: kernel-src-%1 = %2 \
%global extra_modules %extra_modules %1=%2

%define base_flavour led
%define sub_flavour ws
%define flavour %base_flavour-%sub_flavour

Name: kernel-image-%flavour
Version: 3.4.61
Release: alt4

%define kernel_req %nil
%define kernel_prov %nil
%define kernel_branch 3.4
%define kernel_stable_version 61
%define kernel_extra_version .%kernel_stable_version
#define kernel_extra_version %nil

%define krelease %release

%define kmandir %{_man9dir}l
# Build options
# You can change compiler version by editing this line:
%define kgcc_version	4.7

%def_enable smp
%def_disable optimize_for_size
%def_disable verbose
%def_disable debug
%def_disable modversions
%def_enable kallsyms
%def_with src
%def_enable docs
%def_enable htmldocs
%def_enable man
%def_disable compat
%def_enable x32
%def_enable debugfs
%def_disable numa
%def_disable hotplug_memory
%def_enable acpi
%def_enable pci
%def_disable mca
%def_disable math_emu
%def_disable x86_extended_platform
%def_enable pcmcia
%def_enable isdn
%def_enable telephony
%def_enable atm
%def_enable fddi
%def_enable w1
%def_enable hamradio
%def_enable arcnet
%def_enable caif
%def_enable can
%def_enable hippi
%def_enable fusion
%def_enable drm
%def_enable ipv6
%def_disable apei
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
%def_disable ub
%def_enable watchdog
%def_enable regulator
%def_enable mfd
%def_enable spi
%def_enable mtd
%def_disable rapidio
%def_enable mmc
%def_enable media
%def_enable sound
%def_disable oss
%def_enable alsa
%def_disable pcsp
%def_enable video
%def_enable guest
%def_enable simple_ext2
%def_disable ext4_for_ext2
%def_enable ext4_for_ext3
%def_enable bootsplash
%def_disable crasher
%def_disable logo
%def_enable zcache
%def_enable taskstats
%def_enable security
%def_enable audit
%def_enable selinux
%def_enable tomoyo
%def_enable apparmor
%def_enable smack
%def_enable yama
%def_enable thp
%def_disable kvm
%def_enable hyperv
%def_disable paravirt_guest
%def_disable kvm_guest
%def_disable nfs_swap
%def_enable fatelf
%def_with lnfs
%def_enable lnfs
%def_enable oprofile
%def_enable secrm
%def_with firmware
%def_with perf

%def_disable debug_section_mismatch

#define allocator SLAB

#Extra_modules spl 0.6.2
%Extra_modules zfs 0.6.2
%Extra_modules kvm 3.10.1
#Extra_modules nvidia 319.32
%Extra_modules fglrx 13.20.11
%Extra_modules vboxhost 4.2.18
%Extra_modules vboxguest 4.2.18
%Extra_modules knem 1.1.0
%Extra_modules exfat 1.1.5
#Extra_modules netatop 0.2
#Extra_modules omnibook 20110911

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
Source1: %flavour-%kernel_branch.x86_64.config
Source2: %flavour-%kernel_branch.x86.config
Source10: Makefile.external

#Patch0000: patch-%kernel_branch.%kernel_stable_version

Patch0011: linux-%kernel_branch.20-fix-arch-arm.patch
Patch0012: linux-%kernel_branch.20-fix-arch-arm-mach-omap2.patch
Patch0013: linux-%kernel_branch.20-fix-arch-arm-mm.patch
Patch0014: linux-%kernel_branch.20-fix-arch-ia64.patch
Patch0015: linux-%kernel_branch.20-fix-arch-powerpc.patch
Patch0016: linux-%kernel_branch.20-fix-arch-powerpc--prom_init.patch
Patch0017: linux-%kernel_branch.20-fix-arch-powerpc-platforms-chrp.patch
Patch0018: linux-%kernel_branch.20-fix-arch-powerpc-xmon.patch
Patch0019: linux-%kernel_branch.20-fix-arch-s390.patch

Patch0020: linux-%kernel_branch.42-fix-arch-x86.patch
Patch0021: linux-%kernel_branch.20-fix-arch-x86--apic.patch
Patch0022: linux-%kernel_branch.20-fix-arch-x86--apm.patch
Patch0023: linux-%kernel_branch.20-fix-arch-x86--hpet.patch
Patch0024: linux-%kernel_branch.20-fix-arch-x86--kexec.patch
Patch0025: linux-%kernel_branch.42-fix-arch-x86--mcheck.patch
Patch0026: linux-%kernel_branch.47-fix-arch-x86--microcode.patch
Patch0027: linux-%kernel_branch.47-fix-arch-x86-cpu.patch
Patch0028: linux-%kernel_branch.25-fix-arch-x86-cpu--rdrand.patch

Patch0030: linux-%kernel_branch.53-fix-block.patch
Patch0031: linux-%kernel_branch.35-fix-block--blk-integrity.patch
Patch0032: linux-%kernel_branch.20-fix-block-partitions--efi.patch

Patch0041: linux-%kernel_branch.53-fix-crypto--aes_generic.patch
Patch0042: linux-%kernel_branch.35-fix-crypto--cryptomgr.patch

Patch0050: linux-%kernel_branch.53-fix-drivers-acpi.patch
Patch0051: linux-%kernel_branch.47-fix-drivers-acpi--container.patch
Patch0052: linux-%kernel_branch.20-fix-drivers-acpi--ec_sys.patch
Patch0053: linux-%kernel_branch.47-fix-drivers-acpi--pci_slot.patch
Patch0054: linux-%kernel_branch.20-fix-drivers-acpi--thermal.patch
Patch0055: linux-%kernel_branch.20-fix-drivers-acpi-acpica.patch
Patch0056: linux-%kernel_branch.50-fix-drivers-acpi-apei--apei.patch
Patch0057: linux-%kernel_branch.50-fix-drivers-acpi-apei--ghes.patch

Patch0061: linux-%kernel_branch.56-fix-drivers-ata--ata_piix.patch
Patch0062: linux-%kernel_branch.53-fix-drivers-ata--libata.patch
Patch0063: linux-%kernel_branch.25-fix-drivers-ata--pata_amd.patch
Patch0064: linux-%kernel_branch.25-fix-drivers-ata--pata_mpiix.patch
Patch0065: linux-%kernel_branch.25-fix-drivers-ata--pata_oldpiix.patch
Patch0066: linux-%kernel_branch.25-fix-drivers-ata--pata_sch.patch

Patch0071: linux-%kernel_branch.25-fix-drivers-atm--ambassador.patch

Patch0080: linux-%kernel_branch.50-fix-drivers-base.patch
Patch0081: linux-%kernel_branch.20-fix-drivers-base--dma-contiguous.patch
Patch0082: linux-%kernel_branch.25-fix-drivers-base--dma-buf.patch
Patch0083: linux-%kernel_branch.50-fix-drivers-base--firmware_class.patch
Patch0084: linux-%kernel_branch.50-fix-drivers-base-power.patch
Patch0085: linux-%kernel_branch.38-fix-drivers-base-regmap.patch

Patch0091: linux-%kernel_branch.34-fix-drivers-block--aoe.patch
Patch0092: linux-%kernel_branch.25-fix-drivers-block--drbd.patch
Patch0093: linux-%kernel_branch.53-fix-drivers-block--nbd.patch
Patch0094: linux-%kernel_branch.20-fix-drivers-block--zram.patch

Patch0101: linux-%kernel_branch.39-fix-drivers-bluetooth--btmrvl.patch
Patch0102: linux-%kernel_branch.47-fix-drivers-bluetooth--btusb.patch

Patch0121: linux-%kernel_branch.20-fix-drivers-char--lp.patch
Patch0122: linux-%kernel_branch.25-fix-drivers-char-agp--intel-agp.patch
Patch0123: linux-%kernel_branch.25-fix-drivers-char-hw_random--amd-rng.patch
Patch0124: linux-%kernel_branch.25-fix-drivers-char-hw_random--intel-rng.patch
Patch0125: linux-%kernel_branch.50-fix-drivers-char-hw_random--via-rng.patch

Patch0131: linux-%kernel_branch.20-fix-drivers-connector--cn_proc.patch

Patch0141: linux-%kernel_branch.20-fix-drivers-cpufreq--acpi-cpufreq.patch
Patch0142: linux-%kernel_branch.20-fix-drivers-cpufreq--cpufreq_ondemand.patch
Patch0143: linux-%kernel_branch.25-fix-drivers-cpufreq--p4-clockmod.patch
Patch0144: linux-%kernel_branch.25-fix-drivers-cpufreq--powernow-k8.patch

Patch0151: linux-%kernel_branch.25-fix-drivers-crypto--padlock.patch

Patch0161: linux-%kernel_branch.25-fix-drivers-dma-ioat.patch
Patch0162: linux-%kernel_branch.25-fix-drivers-dma--intel_mid_dma.patch

Patch0171: linux-%kernel_branch.25-fix-drivers-edac--e752x_edac.patch
Patch0172: linux-%kernel_branch.25-fix-drivers-edac--e7xxx_edac.patch
Patch0173: linux-%kernel_branch.25-fix-drivers-edac--i3000_edac.patch
Patch0174: linux-%kernel_branch.25-fix-drivers-edac--i3200_edac.patch
Patch0175: linux-%kernel_branch.25-fix-drivers-edac--i5000_edac.patch
Patch0176: linux-%kernel_branch.25-fix-drivers-edac--i5100_edac.patch
Patch0177: linux-%kernel_branch.25-fix-drivers-edac--i5400_edac.patch
Patch0178: linux-%kernel_branch.25-fix-drivers-edac--i7300_edac.patch
Patch0179: linux-%kernel_branch.25-fix-drivers-edac--i82443bxgx_edac.patch
Patch0180: linux-%kernel_branch.25-fix-drivers-edac--i82860_edac.patch
Patch0181: linux-%kernel_branch.25-fix-drivers-edac--i82875p_edac.patch
Patch0182: linux-%kernel_branch.25-fix-drivers-edac--i82975x_edac.patch
Patch0183: linux-%kernel_branch.25-fix-drivers-edac--x38_edac.patch

Patch0191: linux-%kernel_branch.53-fix-drivers-firewire--firewire-core.patch
Patch0192: linux-%kernel_branch.53-fix-drivers-firewire--firewire-ohci.patch
Patch0193: linux-%kernel_branch.53-fix-drivers-firewire--firewire-sbp2.patch
Patch0194: linux-%kernel_branch.53-fix-drivers-firewire--nosy.patch

Patch0201: linux-%kernel_branch.39-fix-drivers-gpio--gpio-ks8695.patch
Patch0202: linux-%kernel_branch.53-fix-drivers-gpio--gpio-langwell.patch
Patch0203: linux-%kernel_branch.39-fix-drivers-gpio--gpio-mcp23s08.patch
Patch0204: linux-%kernel_branch.53-fix-drivers-gpio--gpio-ml-ioh.patch
Patch0205: linux-%kernel_branch.39-fix-drivers-gpio--gpio-nomadik.patch
Patch0206: linux-%kernel_branch.53-fix-drivers-gpio--gpio-sch.patch
Patch0207: linux-%kernel_branch.53-fix-drivers-gpio--gpio-sodaville.patch
Patch0208: linux-%kernel_branch.39-fix-drivers-gpio--gpio-tegra.patch
Patch0209: linux-%kernel_branch.39-fix-drivers-gpio--gpio-timberdale.patch
Patch0210: linux-%kernel_branch.39-fix-drivers-gpio--gpio-ucb1400.patch
Patch0211: linux-%kernel_branch.39-fix-drivers-gpio--gpio-wm831x.patch
Patch0212: linux-%kernel_branch.39-fix-drivers-gpio--gpio-wm8994.patch
Patch0213: linux-%kernel_branch.39-fix-drivers-gpio--gpiolib.patch

Patch0221: linux-%kernel_branch.50-fix-drivers-gpu-drm--drm.patch
Patch0222: linux-%kernel_branch.25-fix-drivers-gpu-drm--exynosdrm.patch
Patch0223: linux-%kernel_branch.50-fix-drivers-gpu-drm--gma500_gfx.patch
Patch0224: linux-%kernel_branch.50-fix-drivers-gpu-drm--i915.patch
Patch0225: linux-%kernel_branch.20-fix-drivers-gpu-drm--nouveau.patch
Patch0226: linux-%kernel_branch.38-fix-drivers-gpu-drm--radeon.patch
Patch0227: linux-%kernel_branch.53-fix-drivers-gpu-drm--ttm.patch
Patch0228: linux-%kernel_branch.45-fix-drivers-gpu-vga--vga_switcheroo.patch

Patch0231: linux-%kernel_branch.38-fix-drivers-hid--hid.patch
Patch0232: linux-%kernel_branch.20-fix-drivers-hid--hid-apple.patch
Patch0233: linux-%kernel_branch.20-fix-drivers-hid--hid-hyperv.patch
Patch0234: linux-%kernel_branch.38-fix-drivers-hid--hid-picolcd.patch
Patch0235: linux-%kernel_branch.38-fix-drivers-hid--hid-wiimote.patch

Patch0241: linux-%kernel_branch.25-fix-drivers-hsi.patch
Patch0242: linux-%kernel_branch.25-fix-drivers-hsi--hsi.patch

Patch0250: linux-%kernel_branch.53-fix-drivers-hv.patch
Patch0251: linux-%kernel_branch.53-fix-drivers-hv--hv_utils.patch
Patch0252: linux-%kernel_branch.53-fix-drivers-hv--hv_vmbus.patch

Patch0261: linux-%kernel_branch.25-fix-drivers-hwmon--applesmc.patch
Patch0262: linux-%kernel_branch.25-fix-drivers-hwmon--asc7621.patch
Patch0263: linux-%kernel_branch.38-fix-drivers-hwmon--asus_atk0110.patch
Patch0264: linux-%kernel_branch.42-fix-drivers-hwmon--coretemp.patch
Patch0265: linux-%kernel_branch.25-fix-drivers-hwmon--fam15h_power.patch
Patch0266: linux-%kernel_branch.25-fix-drivers-hwmon--i5k_amb.patch
Patch0267: linux-%kernel_branch.25-fix-drivers-hwmon--k10temp.patch
Patch0268: linux-%kernel_branch.25-fix-drivers-hwmon--k8temp.patch
Patch0269: linux-%kernel_branch.25-fix-drivers-hwmon--via-cputemp.patch

Patch0271: linux-%kernel_branch.25-fix-drivers-i2c--i2c-boardinfo.patch
Patch0272: linux-%kernel_branch.25-fix-drivers-i2c--i2c-pxa.patch
Patch0273: linux-%kernel_branch.53-fix-drivers-i2c-busses--i2c-amd8111.patch
Patch0274: linux-%kernel_branch.53-fix-drivers-i2c-busses--i2c-i801.patch
Patch0275: linux-%kernel_branch.25-fix-drivers-i2c-busses--i2c-intel-mid.patch
Patch0276: linux-%kernel_branch.53-fix-drivers-i2c-busses--i2c-isch.patch

Patch0281: linux-%kernel_branch.25-fix-drivers-idle--i7300_idle.patch
Patch0282: linux-%kernel_branch.32-fix-drivers-idle--intel_idle.patch

Patch0291: linux-%kernel_branch.25-fix-drivers-infiniband-hw--mlx4.patch

Patch0300: linux-%kernel_branch.25-fix-drivers-input.patch
Patch0301: linux-%kernel_branch.53-fix-drivers-input-mouse--appletouch.patch
Patch0302: linux-%kernel_branch.20-fix-drivers-input-keyboard--omap4-keypad.patch
Patch0303: linux-%kernel_branch.20-fix-drivers-input-serio--i8042.patch

Patch0311: linux-%kernel_branch.38-fix-drivers-iommu--amd_iommu.patch
Patch0312: linux-%kernel_branch.38-fix-drivers-iommu--intel-iommu.patch

Patch0321: linux-%kernel_branch.25-fix-drivers-isdn--sc.patch
Patch0322: linux-%kernel_branch.25-fix-drivers-isdn-gigaset--gigaset.patch
Patch0323: linux-%kernel_branch.20-fix-drivers-isdn-mISDN--mISDN_core.patch

Patch0331: linux-%kernel_branch.34-fix-drivers-leds--led-core.patch
Patch0332: linux-%kernel_branch.34-fix-drivers-leds--led-triggers.patch
Patch0333: linux-%kernel_branch.34-fix-drivers-leds--ledtrig-ide-disk.patch

Patch0341: linux-%kernel_branch.20-fix-drivers-macintosh--adb.patch
Patch0342: linux-%kernel_branch.20-fix-drivers-macintosh--adbhid.patch

Patch0351: linux-%kernel_branch.20-fix-drivers-md--dm-mod.patch
Patch0352: linux-%kernel_branch.20-fix-drivers-md--dm-multipath.patch
Patch0353: linux-%kernel_branch.44-fix-drivers-md--md-mod.patch

Patch0361: linux-%kernel_branch.25-fix-drivers-media-common-tuners--tda18212.patch
Patch0362: linux-%kernel_branch.25-fix-drivers-media-common-tuners--tda18218.patch
Patch0363: linux-%kernel_branch.25-fix-drivers-media-dvb-dvb-usb--dvb-usb-mxl111sf.patch
Patch0364: linux-%kernel_branch.25-fix-drivers-media-dvb-ttpci--budget-av.patch
Patch0365: linux-%kernel_branch.31-fix-drivers-media-radio--radio-rtrack2.patch
Patch0366: linux-%kernel_branch.25-fix-drivers-media-rc--lirc_dev.patch
Patch0367: linux-%kernel_branch.25-fix-drivers-media-rc-lirc.patch
Patch0368: linux-%kernel_branch.25-fix-drivers-media-rc-lirc--lirc_imon.patch
Patch0369: linux-%kernel_branch.25-fix-drivers-media-rc-lirc--lirc_sasem.patch
Patch0370: linux-%kernel_branch.25-fix-drivers-media-rc-lirc--lirc_serial.patch
Patch0371: linux-%kernel_branch.25-fix-drivers-media-video--uvcvideo.patch
Patch0372: linux-%kernel_branch.25-fix-drivers-media-video-gspca--pac7302.patch

Patch0381: linux-%kernel_branch.39-fix-drivers-mfd--ab8500-gpadc.patch
Patch0382: linux-%kernel_branch.39-fix-drivers-mfd--adp5520.patch
Patch0383: linux-%kernel_branch.53-fix-drivers-mfd--cs5535-mfd.patch
Patch0384: linux-%kernel_branch.53-fix-drivers-mfd--lpc_sch.patch
Patch0385: linux-%kernel_branch.25-fix-drivers-mfd--rc5t583.patch
Patch0386: linux-%kernel_branch.25-fix-drivers-mfd--rc5t583-irq.patch
Patch0387: linux-%kernel_branch.53-fix-drivers-mfd--timberdale.patch
Patch0388: linux-%kernel_branch.32-fix-drivers-mfd--twl4030-core.patch
Patch0389: linux-%kernel_branch.39-fix-drivers-mfd--wm8994.patch

Patch0391: linux-%kernel_branch.20-fix-drivers-misc--pti.patch
Patch0392: linux-%kernel_branch.38-fix-drivers-misc--vmw_balloon.patch

Patch0401: linux-%kernel_branch.39-fix-drivers-mmc-core.patch
Patch0402: linux-%kernel_branch.20-fix-drivers-mmc-host--mmci.patch
Patch0403: linux-%kernel_branch.39-fix-drivers-mmc-host--sdhci-pci.patch

Patch0411: linux-%kernel_branch.27-fix-drivers-net-ethernet-alacritech--slicoss.patch
Patch0412: linux-%kernel_branch.25-fix-drivers-net-ethernet-amd--depca.patch
Patch0413: linux-%kernel_branch.25-fix-drivers-net-ethernet-amd--nmclan_cs.patch
Patch0414: linux-%kernel_branch.53-fix-drivers-net-ethernet-broadcom--bnx2x.patch
Patch0415: linux-%kernel_branch.25-fix-drivers-net-ethernet-dec--ewrk3.patch
Patch0416: linux-%kernel_branch.20-fix-drivers-net-ethernet-dec-tulip--tulip.patch
Patch0417: linux-%kernel_branch.25-fix-drivers-net-ethernet-fujitsu--at1700.patch
Patch0418: linux-%kernel_branch.25-fix-drivers-net-ethernet-i825xx--znet.patch
Patch0419: linux-%kernel_branch.20-fix-drivers-net-ethernet-ibm--ehea.patch
Patch0420: linux-%kernel_branch.39-fix-drivers-net-ethernet-intel--ixgbe.patch
Patch0421: linux-%kernel_branch.45-fix-drivers-net-ethernet-qlogic--qlge.patch
Patch0422: linux-%kernel_branch.25-fix-drivers-net-ethernet-via--via-rhine.patch

Patch0431: linux-%kernel_branch.38-fix-drivers-net--bonding.patch
Patch0432: linux-%kernel_branch.38-fix-drivers-net--sb1000.patch
Patch0433: linux-%kernel_branch.53-fix-drivers-net--vmxnet3.patch
Patch0434: linux-%kernel_branch.39-fix-drivers-net-caif--caif_serial.patch
Patch0435: linux-%kernel_branch.39-fix-drivers-net-caif--cfspi_slave.patch
Patch0436: linux-%kernel_branch.50-fix-drivers-net-hyperv.patch
Patch0437: linux-%kernel_branch.39-fix-drivers-net-wimax-i2400m--i2400m.patch

Patch0441: linux-%kernel_branch.25-fix-drivers-net-wireless--iwlwifi.patch
Patch0442: linux-%kernel_branch.47-fix-drivers-net-wireless--rtl8187se.patch
Patch0443: linux-%kernel_branch.53-fix-drivers-net-wireless-brcm80211--brcmsmac.patch
Patch0444: linux-%kernel_branch.25-fix-drivers-net-wireless-ipw2x00--libipw.patch
Patch0445: linux-%kernel_branch.39-fix-drivers-net-wireless-mwifiex--mwifiex.patch
Patch0446: linux-%kernel_branch.20-fix-drivers-net-wireless-rt2x00--rt2800lib.patch
Patch0447: linux-%kernel_branch.39-fix-drivers-net-wireless-wl12xx.patch

Patch0450: linux-%kernel_branch.50-fix-drivers-pci.patch
Patch0451: linux-%kernel_branch.50-fix-drivers-pci-pcie-aer--aerdriver.patch

Patch0461: linux-%kernel_branch.53-fix-drivers-platform--apple-gmux.patch
Patch0462: linux-%kernel_branch.27-fix-drivers-platform--asus_oled.patch
Patch0463: linux-%kernel_branch.20-fix-drivers-platform--hdaps.patch
Patch0464: linux-%kernel_branch.25-fix-drivers-platform--intel_ips.patch
Patch0465: linux-%kernel_branch.25-fix-drivers-platform--intel_menlow.patch
Patch0466: linux-%kernel_branch.25-fix-drivers-platform--intel_oaktrail.patch

Patch0471: linux-%kernel_branch.39-fix-drivers-power--ab8500.patch
Patch0472: linux-%kernel_branch.39-fix-drivers-power--charger-manager.patch
Patch0473: linux-%kernel_branch.39-fix-drivers-power--da9030_battery.patch

Patch0481: linux-%kernel_branch.47-fix-drivers-ptp--ptp_pch.patch

Patch0491: linux-%kernel_branch.39-fix-drivers-regulator--88pm8607.patch
Patch0492: linux-%kernel_branch.39-fix-drivers-regulator--ab8500.patch
Patch0493: linux-%kernel_branch.39-fix-drivers-regulator--regulator.patch

Patch0501: linux-%kernel_branch.25-fix-drivers-rtc--rtc-m41t80.patch

Patch0511: linux-%kernel_branch.25-fix-drivers-scsi--aha1542.patch
Patch0512: linux-%kernel_branch.25-fix-drivers-scsi--aic94xx.patch
Patch0513: linux-%kernel_branch.36-fix-drivers-scsi--hv_storvsc.patch
Patch0514: linux-%kernel_branch.53-fix-drivers-scsi--lpfc.patch
Patch0515: linux-%kernel_branch.25-fix-drivers-scsi--mpt2sas.patch
Patch0516: linux-%kernel_branch.25-fix-drivers-scsi--mvsas.patch
Patch0517: linux-%kernel_branch.53-fix-drivers-scsi--scsi_mod.patch
Patch0518: linux-%kernel_branch.20-fix-drivers-scsi--scsi_netlink.patch
Patch0519: linux-%kernel_branch.42-fix-drivers-scsi--sd_mod.patch
Patch0520: linux-%kernel_branch.29-fix-drivers-scsi--st.patch
Patch0521: linux-%kernel_branch.20-fix-drivers-scsi-device_handler--scsi_dh.patch
Patch0522: linux-%kernel_branch.39-fix-drivers-scsi-fcoe--fcoe.patch
Patch0523: linux-%kernel_branch.53-fix-drivers-scsi-ibmvscsi--ibmvfc.patch
Patch0524: linux-%kernel_branch.20-fix-drivers-scsi-ibmvscsi--ibmvscsic.patch
Patch0525: linux-%kernel_branch.20-fix-drivers-scsi-megaraid--megaraid_mbox.patch

Patch0531: linux-%kernel_branch.25-fix-drivers-spi--spi.patch
Patch0532: linux-%kernel_branch.38-fix-drivers-spi--spi-dw.patch

Patch0540: linux-%kernel_branch.43-fix-drivers-tty.patch
Patch0541: linux-%kernel_branch.39-fix-drivers-tty-hvc--hvc_console.patch
Patch0542: linux-%kernel_branch.38-fix-drivers-tty-serial--ifx6x60.patch
Patch0543: linux-%kernel_branch.38-fix-drivers-tty-serial--mfd.patch
Patch0544: linux-%kernel_branch.38-fix-drivers-tty-serial--mrst_max3110.patch
Patch0545: linux-%kernel_branch.32-fix-drivers-tty-serial--pch_uart.patch
Patch0546: linux-%kernel_branch.20-fix-drivers-tty-serial-8250--8250.patch

Patch0550: linux-%kernel_branch.34-fix-drivers-usb.patch
Patch0551: linux-%kernel_branch.39-fix-drivers-usb-core.patch
Patch0552: linux-%kernel_branch.39-fix-drivers-usb-dwc3--dwc3.patch
Patch0553: linux-%kernel_branch.25-fix-drivers-usb-gadget--g_audio.patch
Patch0554: linux-%kernel_branch.39-fix-drivers-usb-host--isp116x-hcd.patch
Patch0555: linux-%kernel_branch.39-fix-drivers-usb-host--uhci-hcd.patch
Patch0556: linux-%kernel_branch.56-fix-drivers-usb-host--xhci-hcd.patch
Patch0557: linux-%kernel_branch.39-fix-drivers-usb-musb--musb_hdrc.patch
Patch0558: linux-%kernel_branch.39-fix-drivers-usb-otg--otg.patch
Patch0559: linux-%kernel_branch.53-fix-drivers-usb-usbip.patch
Patch0560: linux-%kernel_branch.53-fix-drivers-usb-usbip-userspace.patch

Patch0571: linux-%kernel_branch.20-fix-drivers-video-aty--radeonfb.patch
Patch0572: linux-%kernel_branch.53-fix-drivers-video-backlight--apple_bl.patch
Patch0573: linux-%kernel_branch.20-fix-drivers-video-console--vgacon.patch
Patch0574: linux-%kernel_branch.20-fix-drivers-video-geode.patch
Patch0575: linux-%kernel_branch.20-fix-drivers-video-omap2-dss.patch

Patch0581: linux-%kernel_branch.53-fix-drivers-watchdog--i6300esb.patch
Patch0582: linux-%kernel_branch.53-fix-drivers-watchdog--iTCO_wdt.patch
Patch0583: linux-%kernel_branch.53-fix-drivers-watchdog--sbc_epx_c3.patch
Patch0584: linux-%kernel_branch.53-fix-drivers-watchdog--sc520_wdt.patch
Patch0585: linux-%kernel_branch.53-fix-drivers-watchdog--sp5100_tco.patch
Patch0586: linux-%kernel_branch.53-fix-drivers-watchdog--via_wdt.patch
Patch0587: linux-%kernel_branch.39-fix-drivers-watchdog--watchdog.patch

Patch0591: linux-%kernel_branch.25-fix-firmware--vicam.patch
Patch0592: linux-%kernel_branch-fix-firmware-radeon.patch

Patch0600: linux-%kernel_branch.44-fix-fs.patch
Patch0601: linux-%kernel_branch.37-fix-fs--block.patch
Patch0602: linux-%kernel_branch.35-fix-fs-9p.patch
Patch0603: linux-%kernel_branch.50-fix-fs-autofs4.patch
Patch0604: linux-%kernel_branch.32-fix-fs-btrfs.patch
Patch0605: linux-%kernel_branch.38-fix-fs-ceph.patch
Patch0606: linux-%kernel_branch.53-fix-fs-cifs.patch
Patch0607: linux-%kernel_branch.35-fix-fs-debugfs.patch
Patch0608: linux-%kernel_branch.53-fix-fs-ext2.patch
Patch0609: linux-%kernel_branch.37-fix-fs-ext3.patch
Patch0610: linux-%kernel_branch.53-fix-fs-ext4.patch
Patch0611: linux-%kernel_branch.42-fix-fs-fuse.patch
Patch0612: linux-%kernel_branch.35-fix-fs-gfs2.patch
Patch0613: linux-%kernel_branch.20-fix-fs-hfs.patch
Patch0614: linux-%kernel_branch.35-fix-fs-jfs.patch
Patch0615: linux-%kernel_branch.29-fix-fs-logfs.patch
Patch0616: linux-%kernel_branch.35-fix-fs-nfs.patch
Patch0617: linux-%kernel_branch.35-fix-fs-nilfs2.patch
Patch0618: linux-%kernel_branch.50-fix-fs-ocfs2.patch
Patch0619: linux-%kernel_branch.31-fix-fs-proc.patch
Patch0620: linux-%kernel_branch.28-fix-fs-ramfs.patch
Patch0621: linux-%kernel_branch.53-fix-fs-reiserfs.patch
Patch0622: linux-%kernel_branch.35-fix-fs-ubifs.patch
Patch0623: linux-%kernel_branch.53-fix-fs-xfs.patch

Patch0631: linux-%kernel_branch.60-fix-include-linux.patch
Patch0632: linux-%kernel_branch.50-fix-include-trace.patch

Patch0640: linux-%kernel_branch.20-fix-init.patch

Patch0650: linux-%kernel_branch.34-fix-kernel.patch
Patch0651: linux-%kernel_branch.53-fix-kernel--compat.patch
Patch0652: linux-%kernel_branch.41-fix-kernel--rcutree.patch
Patch0653: linux-%kernel_branch.39-fix-kernel-irq.patch
Patch0654: linux-%kernel_branch.39-fix-kernel-power.patch

Patch0660: linux-%kernel_branch.25-fix-lib.patch
Patch0661: linux-%kernel_branch.29-fix-lib--btree.patch
Patch0662: linux-%kernel_branch.25-fix-lib--crc32.patch
Patch0663: linux-%kernel_branch.35-fix-lib-lzo.patch

Patch0670: linux-%kernel_branch.50-fix-mm.patch
Patch0671: linux-%kernel_branch.35-fix-mm--bounce.patch
Patch0672: linux-%kernel_branch.39-fix-mm--cleancache.patch
Patch0673: linux-%kernel_branch.20-fix-mm--compaction.patch
Patch0674: linux-%kernel_branch.39-fix-mm--memblock.patch
Patch0675: linux-%kernel_branch.20-fix-mm--memcontrol.patch
Patch0676: linux-%kernel_branch.20-fix-mm--memory-failure.patch
Patch0677: linux-%kernel_branch.20-fix-mm--memory_hotplug.patch
Patch0678: linux-%kernel_branch.43-fix-mm--mmu.patch
Patch0679: linux-%kernel_branch.35-fix-mm--slab.patch
Patch0680: linux-%kernel_branch.35-fix-mm--slub.patch
Patch0681: linux-%kernel_branch.35-fix-mm--swap.patch
Patch0682: linux-%kernel_branch.20-fix-mm--zcache.patch
Patch0683: linux-%kernel_branch.20-fix-mm--zsmalloc.patch

Patch0691: linux-%kernel_branch.30-fix-net--dns_resolver.patch
Patch0692: linux-%kernel_branch.39-fix-net-802--fc.patch
Patch0693: linux-%kernel_branch.31-fix-net-bridge--bridge.patch
Patch0694: linux-%kernel_branch.53-fix-net-ceph.patch
Patch0695: linux-%kernel_branch.42-fix-net-core.patch
Patch0696: linux-%kernel_branch.39-fix-net-dcb.patch
Patch0697: linux-%kernel_branch.35-fix-net-ipv4--xfrm.patch
Patch0698: linux-%kernel_branch.31-fix-net-ipv6.patch
Patch0699: linux-%kernel_branch.35-fix-net-ipv6--xfrm.patch
Patch0700: linux-%kernel_branch.53-fix-net-key--af_key.patch
Patch0701: linux-%kernel_branch.39-fix-net-l2tp--l2tp_core.patch
Patch0702: linux-%kernel_branch.53-fix-net-mac80211.patch
Patch0703: linux-%kernel_branch.20-fix-net-netfilter--nf_conntrack_ftp.patch
Patch0704: linux-%kernel_branch.47-fix-net-netfilter--xt_LOG.patch
Patch0705: linux-%kernel_branch.28-fix-net-rds--rds_rdma.patch
Patch0706: linux-%kernel_branch.49-fix-net-sunrpc.patch
Patch0707: linux-%kernel_branch.42-fix-net-unix--unix.patch
Patch0708: linux-%kernel_branch.39-fix-net-wimax.patch
Patch0709: linux-%kernel_branch.35-fix-net-wireless--cfg80211.patch

Patch0711: linux-%kernel_branch.20-fix-scripts--kconfig.patch

Patch0721: linux-%kernel_branch.20-fix-security--apparmor.patch
Patch0722: linux-%kernel_branch.20-fix-security--security.patch
Patch0723: linux-%kernel_branch.35-fix-security--selinux.patch

Patch0731: linux-%kernel_branch.53-fix-sound-firewire--snd-firewire-lib.patch
Patch0732: linux-%kernel_branch.53-fix-sound-firewire--snd-firewire-speakers.patch
Patch0733: linux-%kernel_branch.53-fix-sound-firewire--snd-isight.patch
Patch0734: linux-%kernel_branch.47-fix-sound-pci-hda--snd-hda-codec.patch
Patch0735: linux-%kernel_branch.47-fix-sound-pci-hda--snd-hda-codec-analog.patch
Patch0736: linux-%kernel_branch.47-fix-sound-pci-hda--snd-hda-codec-idt.patch
Patch0737: linux-%kernel_branch.20-fix-sound-pci-hda--snd-hda-codec-realtek.patch
Patch0738: linux-%kernel_branch.47-fix-sound-pci-hda--snd-hda-intel.patch
Patch0739: linux-%kernel_branch.53-fix-sound-pci-oxygen--snd-virtuoso.patch
Patch0740: linux-%kernel_branch.20-fix-sound-soc-omap--snd-soc-omap.patch
Patch0741: linux-%kernel_branch.20-fix-sound-soc-omap--snd-soc-omap-mcbsp.patch

Patch0751: linux-%kernel_branch.20-fix-tools--perf.patch
Patch0752: linux-%kernel_branch.20-fix-tools-hv.patch
Patch0753: linux-%kernel_branch.53-fix-tools-firewire--nosy-dump.patch

Patch0760: linux-%kernel_branch.49-fix-virt-kvm.patch
Patch0761: linux-%kernel_branch.50-fix-virt-kvm--kvm-amd.patch
Patch0762: linux-%kernel_branch.50-fix-virt-kvm--kvm-intel.patch


Patch1001: linux-%kernel_branch.20-feat-arch-arm-mach-omap2--drm.patch

Patch1011: linux-%kernel_branch-feat-block--bfq-iosched.patch
Patch1012: linux-%kernel_branch-feat-block--sio-iosched.patch

Patch1021: linux-%kernel_branch.50-feat-crypto--lz4.patch

Patch1031: linux-%kernel_branch.41-feat-drivers-acpi--bbswitch.patch

Patch1041: linux-%kernel_branch.35-feat-drivers-block--btier.patch
Patch1042: linux-%kernel_branch.20-feat-drivers-block--cloop.patch
Patch1043: linux-%kernel_branch.31-feat-drivers-block--rxdsk.patch
Patch1044: linux-%kernel_branch.25-feat-drivers-block--zram.patch

Patch1051: linux-%kernel_branch.20-feat-drivers-char--crasher.patch

Patch1061: linux-%kernel_branch.20-feat-drivers-gpu-drm--cirrus.patch

Patch1071: linux-%kernel_branch.20-feat-drivers-hwmon--ipmisensors.patch

Patch1081: linux-%kernel_branch.20-feat-drivers-input-touchscreen--elousb.patch

Patch1091: linux-%kernel_branch.20-feat-drivers-md--dm-raid45.patch

Patch1101: linux-%kernel_branch.20-feat-drivers-media-rc-lirc.patch

Patch1111: linux-%kernel_branch.31-feat-drivers-misc--emlog.patch
Patch1112: linux-%kernel_branch.20-feat-drivers-misc--rts_pstor.patch

Patch1121: linux-%kernel_branch.27-feat-drivers-net-ethernet-alacritech.patch
Patch1122: linux-%kernel_branch.27-feat-drivers-net-ethernet-alacritech--slicoss.patch
Patch1123: linux-%kernel_branch.50-feat-drivers-net-ethernet-atheros--alx.patch
Patch1124: linux-%kernel_branch.53-feat-drivers-net-wireless--vt6655.patch
Patch1125: linux-%kernel_branch.53-feat-drivers-net-wireless--vt6656.patch
Patch1126: linux-%kernel_branch.20-feat-drivers-net-wireless-rtl8187se.patch
Patch1127: linux-%kernel_branch.20-feat-drivers-net-wireless-rtl8192e.patch
Patch1128: linux-%kernel_branch.20-feat-drivers-net-wireless-rtl8192u.patch
Patch1129: linux-%kernel_branch.20-feat-drivers-net-wireless-rtl8712.patch

Patch1131: linux-%kernel_branch.27-feat-drivers-platform--asus_oled.patch
Patch1132: linux-%kernel_branch.31-feat-drivers-platform--omnibook.patch
Patch1133: linux-%kernel_branch.20-feat-drivers-platform--thinkpad_ec.patch
Patch1134: linux-%kernel_branch.20-feat-drivers-platform--tp_smapi.patch

Patch1141: linux-%kernel_branch.34-feat-drivers-scsi--vhba.patch

Patch1151: linux-%kernel_branch.53-feat-drivers-target-sbp--sbp_target.patch

Patch1161: linux-%kernel_branch.35-feat-drivers-usb-storage--rts5139.patch
Patch1162: linux-%kernel_branch.20-feat-drivers-usb-usbip.patch

Patch1171: linux-%kernel_branch.39-feat-drivers-video--bootsplash.patch
Patch1172: linux-%kernel_branch.25-feat-drivers-video--xgifb.patch

Patch1181: linux-%kernel_branch-feat-firmware-rtl_nic.patch

Patch1191: linux-%kernel_branch.25-feat-fs--lnfs.patch
Patch1192: linux-%kernel_branch.20-feat-fs--richacl.patch
Patch1193: linux-%kernel_branch.18-feat-fs--secrm.patch
Patch1194: linux-%kernel_branch-feat-fs-aufs.patch
Patch1195: linux-%kernel_branch.20-feat-fs-binfmt_elf--fatelf.patch
Patch1196: linux-%kernel_branch.20-feat-fs-dazukofs.patch
Patch1198: linux-%kernel_branch.18-feat-fs-ext2--secrm.patch
Patch1199: linux-%kernel_branch.18-feat-fs-ext3--secrm.patch
Patch1200: linux-%kernel_branch.44-feat-fs-ext4--richacl.patch
Patch1201: linux-%kernel_branch.50-feat-fs-ext4--secrm.patch
Patch1202: linux-%kernel_branch.20-feat-fs-f2fs.patch
Patch1203: linux-%kernel_branch.18-feat-fs-fat--secrm.patch
Patch1204: linux-%kernel_branch.18-feat-fs-jbd--secrm.patch
Patch1205: linux-%kernel_branch.18-feat-fs-jbd2--secrm.patch
Patch1206: linux-%kernel_branch.25-feat-fs-overlayfs.patch
Patch1207: linux-%kernel_branch.20-feat-fs-reiser4.patch
Patch1208: linux-%kernel_branch.20-feat-fs-squashfs--write.patch
Patch1209: linux-%kernel_branch.28-feat-fs-tmpfs--root.patch
Patch1210: linux-%kernel_branch.20-feat-fs-unionfs.patch

Patch1221: linux-%kernel_branch.53-feat-kernel--sched-cfs-boost.patch
Patch1222: linux-%kernel_branch.27-feat-kernel-power-tuxonice.patch
Patch1223: linux-%kernel_branch.27-feat-kernel-power-tuxonice--frontswap.patch

Patch1231: linux-%kernel_branch.50-feat-lib--lz4.patch
Patch1232: linux-%kernel_branch.20-feat-lib--unwind.patch

Patch1241: linux-%kernel_branch.35-feat-mm--frontswap.patch
Patch1242: linux-%kernel_branch.20-feat-mm--slqb.patch
Patch1243: linux-%kernel_branch.24-feat-mm--uksm.patch
Patch1244: linux-%kernel_branch.20-feat-mm--zcache.patch
Patch1245: linux-%kernel_branch.20-feat-mm--zsmalloc.patch
Patch1246: linux-%kernel_branch.35-feat-mm--zswap.patch

Patch1251: linux-%kernel_branch.20-feat-net--netatop.patch
Patch1252: linux-%kernel_branch.27-feat-net-ipv4-netfilter--ipt_NETFLOW.patch
Patch1253: linux-%kernel_branch.20-feat-net-netfilter--nf_conntrack_slp.patch

Patch1261: linux-%kernel_branch.53-feat-sound-firewire--snd-dice.patch
Patch1262: linux-%kernel_branch.53-feat-sound-firewire--snd-fireworks.patch
Patch1263: linux-%kernel_branch.53-feat-sound-firewire--snd-scs1x.patch


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
%define base_arch x86
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

%{?_disable_media:%set_disable lirc}

%if_disabled sound
%set_disable oss
%set_disable alsa
%endif

%{?_disable_alsa:%set_disable pcsp}

%if_disabled video
%set_disable bootsplash
%endif

%{?_enable_debug:%set_enable debugfs}

%{!?allocator:#define allocator SLAB}

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

%if %(echo "%extra_mods" | grep -q '\bkvm\b' && echo 1 || echo 0)
%def_enable kvm_ext
%endif

BuildPreReq: rpm-build-kernel >= 0.103
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
%{?kgcc_version:BuildRequires: gcc%kgcc_version}
BuildRequires: module-init-tools >= 3.1
BuildRequires: patch >= 2.6.1-alt1
%{?_with_src:BuildRequires: pxz}

%{?_enable_htmldocs:BuildRequires: xmlto transfig ghostscript}
%{?_enable_man:BuildRequires: xmlto}
%{?_with_perf:BuildRequires: binutils-devel libelf-devel asciidoc elfutils-devel >= 0.138 pkgconfig(gtk+-2.0) libnewt-devel python-dev}

Requires: bootloader-utils >= 0.4.21
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.9.8.24.1

Provides: kernel = %kversion
Provides: kernel-modules-md-%flavour = %version-%release
%{?_enable_w1:Provides: kernel-modules-w1-%flavour = %version-%release}

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
AutoProv: no, %kernel_prov \
AutoReq: no, %kernel_req \
PreReq: coreutils module-init-tools >= 3.1 %name = %kversion-%release

%define kernel_doc_package_std_body() \
Group: Documentation \
%{?base_flavour:Provides: kernel-%{1}-%base_flavour = %version-%release} \
Obsoletes: kernel-%{1}-%flavour-%kernel_branch \
Provides: kernel-%{1}-%flavour-%kernel_branch = %version-%release \
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

%define kernel_extmods_package_post() \
%post -n kernel-modules-%{1}-%flavour \
%post_kernel_modules %kversion-%flavour-%krelease \
\
%postun -n kernel-modules-%{1}-%flavour \
%postun_kernel_modules %kversion-%flavour-%krelease
%else
%define kernel_modules_package_post() \
%nil

%define kernel_extmods_package_post() \
%nil
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
%kernel_modules_package_add_provides sound-ext

%description -n kernel-modules-sound-%flavour
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
# Needed for webcams
Requires: kernel-modules-alsa-%flavour = %kversion-%release
%kernel_modules_package_std_body media

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


%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
%{?kgcc_version:Requires: gcc%kgcc_version}
Obsoletes: kernel-headers-modules-%flavour-%kernel_branch
Provides: kernel-headers-modules-%flavour-%kernel_branch = %version-%release
Provides: kernel-devel-%flavour = %version-%release
%{?base_flavour:Provides: kernel-devel-%base_flavour = %version-%release}
Provides: kernel-devel = %version-%release
#Obsoletes: kernel-headers-modules-%flavour = %version
AutoProv: no

%description -n kernel-headers-modules-%flavour
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
License: GPLv2, Redistributable
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


%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
%{?base_flavour:Provides: kernel-headers-%base_flavour = %version}
Obsoletes: kernel-headers-%flavour-%kernel_branch
Provides: kernel-headers-%flavour-%kernel_branch = %version-%release
#Obsoletes: kernel-headers-%flavour = %version
Provides: %kheaders_dir/include
AutoProv: no

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).


%if_enabled docs
%package -n kernel-doc-%flavour
Summary: Linux kernel %kversion-%flavour documentation
%kernel_doc_package_std_body doc

%description -n kernel-doc-%flavour
This package contains documentation files for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.


%if_enabled htmldocs
%package -n kernel-docbook-%flavour
Summary: Linux kernel %kversion-%flavour HTML API documentation
%kernel_doc_package_std_body docbook

%description -n kernel-docbook-%flavour
This package contains API documentation HTML files for Linux kernel
package kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.
%endif


%if_enabled man
%package -n kernel-man-%flavour
Summary: Linux kernel %kversion-%flavour man pages
%kernel_doc_package_std_body man
Provides: kernel-man = %version-%release
Conflicts: kernel-man > %version-%release
Conflicts: kernel-man < %version-%release

%description -n kernel-man-%flavour
This package contains man pages for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The man pages contained in this package may be different from the similar
files in upstream kernel distributions, because some patches applied to
the corresponding kernel packages may change things in the kernel and
update the documentation to reflect these changes.
%endif
%endif


%if_with src
%package -n kernel-src-%flavour
Summary: Linux kernel %kversion-%flavour sources
Group: Development/Kernel
%{?base_flavour:Provides: kernel-src-%base_flavour = %version-%release}
Obsoletes: kernel-src-%flavour-%kernel_branch
Provides: kernel-src-%flavour-%kernel_branch = %version-%release
BuildArch: noarch
AutoProv: no
AutoReq: no

%description -n kernel-src-%flavour
This package contains sources for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
%endif


%ifdef extra_mods
%(for M in %extra_modules; do
m="${M%%=*}"
v="${M#*=}"
for p in $(rpmquery --whatprovides kernel-src-$m 2>/dev/null); do
	rpmquery --provides $p | grep -q "^kernel-src-$m = $v-"'*' && break || p=;
done
[ -n "$p" ] || p="kernel-src-$m-$v"
License="$(rpmquery --qf '%%{LICENSE}\n' $p 2>/dev/null)"
[ -n "$License" -a "$License" != "(none)" ] && License="License: $License" || License=
S="$(rpmquery --qf '%%{SUMMARY}\n' $p 2>/dev/null | sed -n 's/\( modules*\) sources/\1/p')"
[ -n "$S" ] || S="$m kernel modules v$v"
Desc="$(rpmquery --qf '%%{DESCRIPTION}\n' $p 2>/dev/null | sed -n -z 's/\( modules*\) sources/\1/gp')"
[ -n "$Desc" ] || Desc="$S."
cat <<__PACKAGE__
%%package -n kernel-modules-$m-%flavour
Version: ${v}_%kversion
Summary: $S
$License
%kernel_modules_package_std_body $m
Provides: kernel-extmods-$m-%flavour = %version-%release
Provides: kernel-modules-$m-%flavour = %kversion-%release

%%description -n kernel-modules-$m-%flavour
$Desc

__PACKAGE__
done)
%define version %kversion
%endif


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
cd linux-%version
#patch0000 -p1

# fix-arch-*
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1

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

# fix-block*
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1

# fix-crypto--*
%patch0041 -p1
%patch0042 -p1

# fix-drivers-acpi*
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1

# fix-drivers-ata-*
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1

# fix-drivers-atm--*
%patch0071 -p1

# fix-drivers-base*
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1

# fix-drivers-block--*
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1

# fix-drivers-bluetooth--*
%patch0101 -p1
%patch0102 -p1

# fix-drivers-cdrom--*

# fix-drivers-char-*
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1

# fix-drivers-connector--*
%patch0131 -p1

# fix-drivers-cpufreq--*
%patch0141 -p1
%patch0142 -p1
%patch0143 -p1
%patch0144 -p1

# fix-drivers-crypto--*
%patch0151 -p1

# fix-drivers-dma-*
%patch0161 -p1
%patch0162 -p1

# fix-drivers-edac--*
%patch0171 -p1
%patch0172 -p1
%patch0173 -p1
%patch0174 -p1
%patch0175 -p1
%patch0176 -p1
%patch0177 -p1
%patch0178 -p1
%patch0179 -p1
%patch0180 -p1
%patch0181 -p1
%patch0182 -p1
%patch0183 -p1

# fix-drivers-firewire--*
%patch0191 -p1
%patch0192 -p1
%patch0193 -p1
%patch0194 -p1

# fix-drivers-gpio--*
%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
%patch0205 -p1
%patch0206 -p1
%patch0207 -p1
%patch0208 -p1
%patch0209 -p1
%patch0210 -p1
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1

# fix-drivers-gpu-drm--*
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1
%patch0224 -p1
%patch0225 -p1
%patch0226 -p1
%patch0227 -p1
%patch0228 -p1

# fix-drivers-hid--*
%patch0231 -p1
%patch0232 -p1
%patch0233 -p1
%patch0234 -p1
%patch0235 -p1

# fix-drivers-hsi*
%patch0241 -p1
%patch0242 -p1

# fix-drivers-hv*
%patch0250 -p1
%patch0251 -p1
%patch0252 -p1

# fix-drivers-hwmon--*
%patch0261 -p1
%patch0262 -p1
%patch0263 -p1
%patch0264 -p1
%patch0265 -p1
%patch0266 -p1
%patch0267 -p1
%patch0268 -p1
%patch0269 -p1

# fix-drivers-i2c--*
%patch0271 -p1
%patch0272 -p1
%patch0273 -p1
%patch0274 -p1
%patch0275 -p1
%patch0276 -p1

# fix-drivers-idle--*
%patch0281 -p1
%patch0282 -p1

# fix-drivers-infiniband-*
%patch0291 -p1

# fix-drivers-input*
%patch0300 -p1
%patch0301 -p1
%patch0302 -p1
%patch0303 -p1

# fix-drivers-iommu--*
%patch0311 -p1
%patch0312 -p1

# fix-drivers-isdn-*
%patch0321 -p1
%patch0322 -p1
%patch0323 -p1

# fix-drivers-leds--*
%patch0331 -p1
%patch0332 -p1
%patch0333 -p1

# fix-drivers-macintosh--*
%patch0341 -p1
%patch0342 -p1

# fix-drivers-md--*
%patch0351 -p1
%patch0352 -p1
%patch0353 -p1

# fix-drivers-media-*
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
%patch0372 -p1

# fix-drivers-mfd--*
%patch0381 -p1
%patch0382 -p1
%patch0383 -p1
%patch0384 -p1
%patch0385 -p1
%patch0386 -p1
%patch0387 -p1
%patch0388 -p1
%patch0389 -p1

# fix-drivers-misc--*
%patch0391 -p1
%patch0392 -p1

# fix-drivers-mmc-*
%patch0401 -p1
%patch0402 -p1
%patch0403 -p1

# fix-drivers-net-ethernet-*
%patch0411 -p1
%patch0412 -p1
%patch0413 -p1
%patch0414 -p1
%patch0415 -p1
%patch0416 -p1
%patch0417 -p1
%patch0418 -p1
%patch0419 -p1
%patch0420 -p1
%patch0421 -p1
%patch0422 -p1

# fix-drivers-net-*
%patch0431 -p1
%patch0432 -p1
%patch0433 -p1
%patch0434 -p1
%patch0435 -p1
%patch0436 -p1
%patch0437 -p1

# fix-drivers-net-wireless-*
%patch0441 -p1
%patch0442 -p1
%patch0443 -p1
%patch0444 -p1
%patch0445 -p1
%patch0446 -p1
%patch0447 -p1

# fix-drivers-pci*
%patch0450 -p1
%patch0451 -p1

# fix-drivers-platform--*
%patch0461 -p1
%patch0462 -p1
%patch0463 -p1
%patch0464 -p1
%patch0465 -p1
%patch0466 -p1

# fix-drivers-power--*
%patch0471 -p1
%patch0472 -p1
%patch0473 -p1

# fix-drivers-ptp--*
%patch0481 -p1

# fix-drivers-regulator--*
%patch0491 -p1
%patch0492 -p1
%patch0493 -p1

# fix-drivers-rtc--*
%patch0501 -p1

# fix-drivers-scsi-*
%patch0511 -p1
%patch0512 -p1
%patch0513 -p1
%patch0514 -p1
%patch0515 -p1
%patch0516 -p1
%patch0517 -p1
%patch0518 -p1
%patch0519 -p1
%patch0520 -p1
%patch0521 -p1
%patch0522 -p1
%patch0523 -p1
%patch0524 -p1
%patch0525 -p1

# fix-drivers-spi--*
%patch0531 -p1
%patch0532 -p1

# fix-drivers-tty*
%patch0540 -p1
%patch0541 -p1
%patch0542 -p1
%patch0543 -p1
%patch0544 -p1
%patch0545 -p1
%patch0546 -p1

# fix-drivers-usb*
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

# fix-drivers-video-*
%patch0571 -p1
%patch0572 -p1
%patch0573 -p1
%patch0574 -p1
%patch0575 -p1

# fix-drivers-watchdog--*
%patch0581 -p1
%patch0582 -p1
%patch0583 -p1
%patch0584 -p1
%patch0585 -p1
%patch0586 -p1
%patch0587 -p1

# fix-firmware-*
%patch0591 -p1
%patch0592 -p1

# fix-fs*
%patch0600 -p1
%patch0601 -p1
%patch0602 -p1
%patch0603 -p1
%patch0604 -p1
%patch0605 -p1
%patch0606 -p1
%patch0607 -p1
%patch0608 -p1
%patch0609 -p1
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

# fix-include-*
%patch0631 -p1
%patch0632 -p1

# fix-init
%patch0640 -p1

# fix-kernel*
%patch0650 -p1
%patch0651 -p1
%patch0652 -p1
%patch0653 -p1
%patch0654 -p1

# fix-lib*
%patch0660 -p1
%patch0661 -p1
%patch0662 -p1
%patch0663 -p1

# fix-mm*
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

# fix-net-*
%patch0691 -p1
%patch0692 -p1
%patch0693 -p1
%patch0694 -p1
%patch0695 -p1
%patch0696 -p1
%patch0697 -p1
%patch0698 -p1
%patch0699 -p1
%patch0700 -p1
%patch0701 -p1
%patch0702 -p1
%patch0703 -p1
%patch0704 -p1
%patch0705 -p1
%patch0706 -p1
%patch0707 -p1
%patch0708 -p1
%patch0709 -p1

# fix-scripts--*
%patch0711 -p1

# fix-security--*
%patch0721 -p1
%patch0722 -p1
%patch0723 -p1

# fix-sound-*
%patch0731 -p1
%patch0732 -p1
%patch0733 -p1
%patch0734 -p1
%patch0735 -p1
%patch0736 -p1
%patch0737 -p1
%patch0738 -p1
%patch0739 -p1
%patch0740 -p1
%patch0741 -p1

# fix-tools-*
%patch0751 -p1
%patch0752 -p1
%patch0753 -p1

# fix-virt-kvm*
%patch0760 -p1
%patch0761 -p1
%patch0762 -p1


# feat-arch-*
%patch1001 -p1

# feat-block--*
%patch1011 -p1
%patch1012 -p1

# feat-drivers-acpi--*
%patch1021 -p1

# feat-crypto--*
%patch1031 -p1

# feat-drivers-block--*
%patch1041 -p1
%patch1042 -p1
%patch1043 -p1
%patch1044 -p1

# feat-drivers-char--*
%patch1051 -p1

# feat-drivers-gpu-drm--*
%patch1061 -p1

# feat-drivers-hwmon--*
%patch1071 -p1

# feat-drivers-input-*
%patch1081 -p1

# feat-drivers-md--*
%patch1091 -p1

# feat-drivers-media--*
%patch1101 -p1

# feat-drivers-misc--*
%patch1111 -p1
%patch1112 -p1

# feat-drivers-net-*
%patch1121 -p1
%patch1122 -p1
%patch1123 -p1
%patch1124 -p1
%patch1125 -p1
%patch1126 -p1
%patch1127 -p1
%patch1128 -p1
%patch1129 -p1

# feat-drivers-platform--*
%patch1131 -p1
%patch1132 -p1
%patch1133 -p1
%patch1134 -p1

# feat-drivers-scsi--*
%patch1141 -p1

# feat-drivers-target-*
%patch1151 -p1

# feat-drivers-usb-*
%patch1161 -p1
%patch1162 -p1

# feat-drivers-video--*
%patch1171 -p1
%patch1172 -p1

# feat-firmware-*
%patch1181 -p1

# feat-fs-*
%{?_with_lnfs:%patch1191 -p1}
%patch1192 -p1
%patch1193 -p1
%patch1194 -p1
%patch1195 -p1
%patch1196 -p1
%patch1198 -p1
%patch1199 -p1
%patch1200 -p1
%patch1201 -p1
%patch1202 -p1
%patch1203 -p1
%patch1204 -p1
%patch1205 -p1
%patch1206 -p1
%patch1207 -p1
%patch1208 -p1
%patch1209 -p1
%patch1210 -p1

# feat-kernel-*
%patch1221 -p1
%patch1222 -p1
%patch1223 -p1

# feat-lib--*
%patch1231 -p1
%patch1232 -p1

# feat-mm--*
%patch1241 -p1
%patch1242 -p1
%patch1243 -p1
%patch1244 -p1
%patch1245 -p1
%patch1246 -p1

# feat-net--*
%patch1251 -p1
%patch1252 -p1
%patch1253 -p1

# feat-sound-*
%patch1261 -p1
%patch1262 -p1
%patch1263 -p1


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

sed -i 's/CC.*$(CROSS_COMPILE)gcc/CC\t\t:= '"gcc-$GCC_VERSION/g" Makefile

%if_with src
cd ..
find linux-%kversion -type f -or -type l -not -name '*.orig' -not -name '*~' -not -name '.git*' > kernel-src-%flavour.list
cd -
%endif

install -m644 %SOURCE1 %SOURCE2 .

%ifdef extra_mods
install -m 0644 %SOURCE10 ./Makefile.external
install -d -m 0755 external
for m in $(echo " %extra_modules " | sed 's/ zfs\(=.* \)/ spl\1&/'); do
	tar -C external -xf %kernel_src/${m%%=*}-${m#*=}.tar*
done
%endif


%build
cd linux-%version

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

if [ -f %flavour-%kernel_branch.%_target_cpu.config ]; then
	cp -vf %flavour-%kernel_branch.%_target_cpu.config .config
else
	cp -vf %flavour-%kernel_branch.%base_arch.config .config
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

%ifarch %intel_64 %intel_32
config_disable CPU_SUP_\.*
config_enable CPU_SUP_INTEL
%endif

%ifarch %amd_64 %amd_32
config_disable CPU_SUP_\.*
config_enable CPU_SUP_AMD
%endif

%ifarch %via_64 %via_32
config_disable CPU_SUP_\.*
config_enable CPU_SUP_CENTAUR
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
	%{?_disable_compat:SYSCTL_SYSCALL ACPI_PROC_EVENT COMPAT_VDSO I2C_COMPAT PROC_PID_CPUSET SYSFS_DEPRECATED USB_DEVICEFS USB_DEVICE_CLASS} \
	%{?_disable_x32:X86_X32} \
	%{?_disable_numa:NUMA} \
	%{?_disable_video:FB VIDEO_OUTPUT_CONTROL BACKLIGHT_LCD_SUPPORT} \
	%{?_disable_drm:DRM VGA_SWITCHEROO} \
	%{?_disable_ipv6:IPV6} \
	%{?_disable_apei:ACPI_APEI} \
	%{?_disable_edac:EDAC} \
	%{?_disable_arcnet:ARCNET} \
	%{?_disable_caif:CAIF} \
	%{?_disable_can:CAN} \
	%{?_disable_hippi:HIPPI} \
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
	%{?_disable_fddi:FDDI} \
	%{?_disable_hamradio:HAMRADIO} \
	%{?_disable_w1:W1} \
	%{?_disable_ub:BLK_DEV_UB USB_LIBUSUAL} \
	%{?_disable_watchdog:WATCHDOG} \
	%{?_disable_spi:SPI} \
	%{?_disable_mfd:MFD_\.*} \
	%{?_disable_regulator:REGULATOR} \
	%{?_disable_mtd:MTD} \
	%{?_disable_rapidio:RAPIDIO} \
	%{?_disable_media:MEDIA_SUPPORT} \
	%{?_disable_mmc:MMC} \
	%{?_disable_wireless:WLAN WIRELESS CFG80211 WIMAX} \
	%{?_disable_isdn:ISDN} \
	%{?_disable_telephony:PHONE} \
	%{?_disable_taskstats:TASKSTATS} \
	%{?_disable_security:SECURITY} \
	%{?_disable_audit:AUDIT} \
	%{?_disable_selinux:SECURITY_SELINUX} \
	%{?_disable_tomoyo:SECURITY_TOMOYO} \
	%{?_disable_apparmor:SECURITY_APPARMOR} \
	%{?_disable_smack:SECURITY_SMACK} \
	%{?_disable_yama:SECURITY_YAMA} \
	%{?_disable_thp:TRANSPARENT_HUGEPAGE} \
	%{?_disable_guest:VIRTIO DRM_KVM_CIRRUS DRM_VMWGFX VMWARE_BALLOON} \
	%{?_disable_kvm:KVM} \
	%{?_disable_hyperv:HYPERV} \
	%{?_disable_paravirt_guest:PARAVIRT_GUEST} \
	%{?_disable_kvm_guest:KVM_GUEST} \
	%{?_disable_bootsplash:BOOTSPLASH} \
	%{?_disable_crasher:CRASHER} \
	%{?_disable_logo:LOGO} \
	%{?_disable_zcache:ZCACHE} \
	%{?_disable_pci:PCI} \
	%{?_disable_acpi:ACPI} \
	%{?_disable_pcsp:SND_PCSP=m} \
	%{?_disable_nfs_swap:NFS_SWAP} \
	%{?_disable_hotplug_memory:MEMORY_HOTPLUG} \
	%{?_disable_math_emu:MATH_EMULATION} \
	%{?_disable_kallsyms:KALLSYMS} \
	%{?_disable_oprofile:PROFILING OPROFILE} \
	%{?_disable_fatelf:BINFMT_FATELF} \
	%{?_enable_simple_ext2:EXT2_FS_XATTR EXT2_FS_POSIX_ACL EXT2_FS_SECURITY} \
	%{?_enable_ext4_for_ext2:EXT2_FS} %{?_enable_ext4_for_ext3:EXT3_FS}

config_enable \
%ifarch i386 i486 i586 i686
	X86_GENERIC \
	%{?_enable_optimize_for_size:CC_OPTIMIZE_FOR_SIZE} \
%endif
	%{?_enable_debug_section_mismatch:DEBUG_SECTION_MISMATCH} \
	%{?_enable_modversions:MODVERSIONS} \
	%{?_enable_x86_extended_platform:X86_EXTENDED_PLATFORM} \
	%{?_enable_ext4_for_ext2:EXT4_USE_FOR_EXT2} %{?_enable_ext4_for_ext3:EXT4_USE_FOR_EXT3} \
	%{?_enable_mca:MCA} \
	%{?_enable_debugfs:DEBUG_FS} \
	%{?_enable_secrm:EXT[234]_SECRM FAT_SECRM} \
	%{?_enable_kvm_ext:KVM_EXTERNAL} \
	%{?_enable_lnfs:NFS_V4_SECURITY_LABEL NFSD_V4_SECURITY_LABEL} \
	%{?_enable_kallsyms:KALLSYMS} \
	%{?allocator:%allocator}

# arch-specific
%ifarch corei7 nehalem
config_disable CRYPTO_CRC32C
%endif
%ifarch i386 i486
config_enable CRYPTO_AES=m CRYPTO_TWOFISH=m CRYPTO_SALSA20=m
%endif

%ifarch %intel_64 %via_64 %via_32
sed -i '/^CONFIG_USB_UHCI_HCD=/s/=m/=y/' .config
config_disable USB_OHCI_HCD
%endif
%ifarch K9 K10 barcelona phenom
sed -i '/^CONFIG_USB_OHCI_HCD=/s/=m/=y/' .config
config_disable USB_UHCI_HCD
%endif
%ifarch %amd_64 %amd_32 %via_64 %via_32
config_disable SCHED_SMT NET_DMA PCH_DMA
%endif
%ifarch %ix86
config_disable SCHED_MC
%endif

# FIXME
config_disable ISCSI_IBFT_FIND FIRMWARE_MEMMAP GPIO_SX150X
# non-modularized mfd drivers
config_disable MFD_88PM860X MFD_AAT2870_CORE AB8500_CORE \
	MFD_DA9052_SPI MFD_DA9052_I2C \
	MFD_MAX8925 MFD_MAX8997 MFD_MAX8998 \
	MFD_RC5T583 MFD_S5M_CORE MFD_STMPE MFD_TC3589X \
	MFD_TPS6586X MFD_TPS65910 MFD_TPS65912_I2C MFD_TPS65912_SPI \
	MFD_WM831X_I2C MFD_WM831X_SPI MFD_WM8350_I2C

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

%{?extra_mods:%make_build -f Makefile.external %extra_mods && echo "External modules built"}

# psdocs, pdfdocs don't work yet
%{?_enable_htmldocs:%def_enable builddocs}
%{?_enable_man:%def_enable builddocs}
%if_enabled builddocs
%{?_enable_htmldocs:%make_build htmldocs}
%{?_enable_man:%make_build mandocs 2>&1 | tee mandocs.log | grep -vE --line-buffered '^((Warn|Note): (meta author |AUTHOR sect\.):|Note: Writing) '}
echo "Kernel docs built %kversion-%flavour-%krelease"
%endif


%install
cd linux-%version

install -Dp -m644 System.map %buildroot/boot/System.map-%kversion-%flavour-%krelease
install -Dp -m644 arch/%base_arch/boot/bzImage %buildroot/boot/vmlinuz-%kversion-%flavour-%krelease
install -Dp -m644 .config %buildroot/boot/config-%kversion-%flavour-%krelease

%make_install \
	INSTALL_MOD_PATH=%buildroot \
	INSTALL_FW_PATH=%buildroot%firmware_dir \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	modules_install
cp %buildroot%modules_dir/modules.dep{,.inkernel}

%ifdef extra_mods
make -f Makefile.external DESTDIR=%buildroot \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	INSTALL_MOD_PATH=%modules_dir \
	$(echo " %extra_mods " | sed 's/ zfs / zfs_spl /')
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
find %buildroot%kbuild_dir/{include,arch} -type f \( -name Kbuild -or -name '.*.cmd' \) -delete

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
	scripts/pnmtologo \
	scripts/recordmcount.pl \
	scripts/basic/fixdep \
	scripts/genksyms/genksyms \
	scripts/kconfig/conf \
	scripts/mod/{modpost,mk_elfconfig} \
	gcc_version.inc
do
	if [ -f "$f" ]; then
		[ -x "$f" ] && mode=0755 || mode=0644
		install -Dp -m $mode {,%buildroot%kbuild_dir/}$f
	fi
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
%makeinstall_std -C tools/perf %{?_enable_verbose:V=1} \
	prefix=%_prefix perfexecdir=%_libexecdir/perf \
	EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}" install-man
install -d -m 0755 %buildroot%_docdir/perf-%version
install -m 0644 tools/perf/{CREDITS,design.txt,Documentation/examples.txt} %buildroot%_docdir/perf-%version/
%endif

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%flavour/
for I in Documentation/*; do
	case "$(basename "$I")" in
		DocBook)
%if_enabled htmldocs
			for J in "$I"/*.tmpl; do
				j=$(basename "$J" .tmpl)
				[ -d "$I/$j" ] || continue
				install -d -m 0755 %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"
				install -m 0644 "$I/$j"/*.html %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"/
				install -m 0644 "$I/$j.html" %buildroot%_docdir/kernel-doc-%flavour/DocBook/
			done
%endif
			;;
		[a-z][a-z]_[A-Z][A-Z]|Makefile|dontdiff) ;;
		*) cp -aL "$I" %buildroot%_docdir/kernel-doc-%flavour/ ;;
	esac
done
find %buildroot%_docdir/kernel-doc-%flavour -type f -name Makefile -delete
%if_enabled man
install -d %buildroot%kmandir
install -m 0644 Documentation/DocBook/man/* %buildroot%kmandir/
%endif
%endif

cd -

%if_with src
install -d -m 0755 %kernel_srcdir
t="%__nprocs"
[ $t -gt 1 ] && XZ="pxz -T$t" || XZ="xz"
tar	--transform='s/^linux-%kversion/&-%flavour-%krelease/' \
	--owner=root --group=root --mode=u+w,go-w,go+rX \
	-T kernel-src-%flavour.list \
	-cf - | \
	$XZ -8e > %kernel_srcdir/linux-%kversion-%flavour-%krelease.tar.xz
%endif

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
	%buildroot%modules_dir/kernel/drivers/scsi/{virtio*,{,lib}iscsi*,scsi_transport_iscsi.ko} \
%endif
	%buildroot%modules_dir/kernel/drivers/scsi/{{*_mod,scsi_{tgt,transport_srp},vhba}.ko,osd,device_handler{,/scsi_dh.ko}}
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/{message/fusion,scsi{,/device_handler}/*,target} | grep -Fxv -f scsi-base.rpmmodlist | grep -v '^%modules_dir/kernel/drivers/scsi/virtio.*' > scsi.rpmmodlist
mv scsi-base.rpmmodlist scsi-base.rpmmodlist~
gen_rpmmodfile infiniband %buildroot%modules_dir/kernel/{drivers/{infiniband,scsi/scsi_transport_srp.ko},net/{9p/9pnet_rdma.ko,rds,sunrpc/xprtrdma}}
gen_rpmmodfile ipmi %buildroot%modules_dir/kernel/drivers/{acpi/acpi_ipmi,char/ipmi,{acpi/acpi_ipmi,hwmon/i{bm,pmi}*}.ko}
%{?_enable_atm:gen_rpmmodfile atm %buildroot%modules_dir/kernel/{drivers{,/usb},net}/atm}
%{?_enable_drm:gen_rpmmodfile drm %buildroot%modules_dir/kernel/drivers/gpu}
%{?_enable_fddi:gen_rpmmodfile fddi %buildroot%modules_dir/kernel/{drivers/net,net/802}/fddi*}
%{?_enable_hamradio:gen_rpmmodfile hamradio %buildroot%modules_dir/kernel/{drivers/net/hamradio,net/{netrom,rose,ax25}}}
%{?_enable_irda:gen_rpmmodfile irda %buildroot%modules_dir/kernel/{,drivers/}net/irda}
%{?_enable_isdn:gen_rpmmodfile isdn %buildroot%modules_dir/kernel/{drivers/isdn,net/bluetooth/cmtp}}
%{?_enable_usb_gadget:gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/usb/gadget/* | grep -xv '%modules_dir/kernel/drivers/usb/gadget/udc-core.ko' > usb-gadget.rpmmodlist}
%{?_enable_watchdog:gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/watchdog/* | grep -Ev '^%modules_dir/kernel/drivers/watchdog/(watch|soft)dog.ko$' > watchdog.rpmmodlist}
%if_enabled video
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/video/* | grep -xv '%modules_dir/kernel/drivers/video/uvesafb.ko' | grep -xv '%modules_dir/kernel/drivers/video/sis' | grep -xv '%modules_dir/kernel/drivers/video/backlight' | grep -v '^%modules_dir/kernel/drivers/video/.*sys.*\.ko$' > video.rpmmodlist
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/video/backlight/* | grep -xv '%modules_dir/kernel/drivers/video/backlight/lcd.ko' >> video.rpmmodlist
%endif
%if_enabled media
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/media/* | grep -xv '%modules_dir/kernel/drivers/media/media.ko' | grep -xv '%modules_dir/kernel/drivers/media/video' > media.rpmmodlist
gen_rpmmodlist %buildroot%modules_dir/kernel/drivers/media/video/* | grep -xv '%modules_dir/kernel/drivers/media/video/videodev.ko' >> media.rpmmodlist
%endif
%{?_enable_ide:gen_rpmmodfile ide %buildroot%modules_dir/kernel/drivers/{ide,leds/ledtrig-ide-disk.ko}}
for i in %{?_enable_edac:edac} %{?_enable_mtd:mtd}; do
	gen_rpmmodfile $i %buildroot%modules_dir/kernel/drivers/$i
done
for i in %{?_enable_joystick:joystick} %{?_enable_tablet:tablet} %{?_enable_touchscreen:touchscreen}; do
	gen_rpmmodfile $i %buildroot%modules_dir/kernel/drivers/input/$i
done
%if "%sub_flavour" != "guest"
%{?_enable_guest:gen_rpmmodfile guest %buildroot%modules_dir/kernel/{drivers/{virtio,{char{,/hw_random},net,block,scsi}/virtio*%{?_enable_drm:,gpu/drm/{cirrus,vmwgfx}},misc/vmw_balloon.ko},net/9p/*_virtio.ko}}
%{?_enable_drm:grep -F -f drm.rpmmodlist guest.rpmmodlist | sed 's/^/%%exclude &/' >> drm.rpmmodlist}
%endif
sed 's/^/%%exclude &/' *.rpmmodlist > exclude-drivers.rpmmodlist

%{?_enable_oprofile:%add_verify_elf_skiplist %modules_dir/vmlinux}


%if 0
%post
[ -x /usr/lib/rpm/boot_kernel.filetrigger ] || /sbin/installkernel %kversion-%flavour-%krelease

%preun
/sbin/installkernel --remove %kversion-%flavour-%krelease
%endif


%if 0
%post -n kernel-headers-%flavour
%post_kernel_headers %kversion-%flavour-%krelease

%postun -n kernel-headers-%flavour
%postun_kernel_headers %kversion-%flavour-%krelease
%endif


%kernel_modules_package_post scsi

%kernel_modules_package_post infiniband

%kernel_modules_package_post ipmi

%{?_enable_edac:%kernel_modules_package_post edac}

%{?_enable_video:%kernel_modules_package_post video}

%{?_enable_irda:%kernel_modules_package_post irda}

%{?_enable_joystick:%kernel_modules_package_post joystick}

%{?_enable_tablet:%kernel_modules_package_post tablet}

%{?_enable_touchscreen:%kernel_modules_package_post touchscreen}

%{?_enable_usb_gadget:%kernel_modules_package_post usb-gadget}

%{?_enable_atm:%kernel_modules_package_post atm}

%{?_enable_hamradio:%kernel_modules_package_post hamradio}

%{?_enable_watchdog:%kernel_modules_package_post watchdog}

%{?_enable_mtd:%kernel_modules_package_post mtd}

%kernel_modules_package_post fs-extra

%kernel_modules_package_post net-extra

%{?_enable_oss:%kernel_modules_package_post oss}

%{?_enable_ide:%kernel_modules_package_post ide}

%{?_enable_drm:%kernel_modules_package_post drm}

%{?_enable_media:%kernel_modules_package_post media}

%{?_enable_alsa:%kernel_modules_package_post sound}

%{?_enable_isdn:%kernel_modules_package_post isdn}

%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_post guest}
%endif

%{?_enable_kvm:%kernel_modules_package_post kvm}

%{?_enable_hyperv:%kernel_modules_package_post hyperv}

%{?_enable_oprofile:%kernel_modules_package_post oprofile}

%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%kernel_extmods_package_post $m

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
%exclude %modules_dir/kernel/fs/qnx?
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
%{?_enable_arcnet:%exclude %modules_dir/kernel/drivers/net/arcnet}
%{?_enable_can:%exclude %modules_dir/kernel/net/can}
%{?_enable_can:%exclude %modules_dir/kernel/drivers/net/can}
%exclude %modules_dir/kernel/net/batman-adv
%{?_enable_caif:%exclude %modules_dir/kernel/net/caif}
%{?_enable_caif:%exclude %modules_dir/kernel/drivers/net/caif}
%{?_enable_hippi:%exclude %modules_dir/kernel/drivers/net/hippi}
%exclude %modules_dir/kernel/drivers/net/plip
%exclude %modules_dir/kernel/drivers/net/slip/slip.ko
%exclude %modules_dir/kernel/net/dccp
%exclude %modules_dir/kernel/net/decnet
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

%{?_enable_usb_gadget:%kernel_modules_package_files usb-gadget}

%{?_enable_atm:%kernel_modules_package_files atm}

%{?_enable_hamradio:%kernel_modules_package_files hamradio}

%{?_enable_mtd:%kernel_modules_package_files mtd}

%{?_enable_watchdog:%kernel_modules_package_files watchdog}


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
%modules_dir/kernel/fs/qnx?
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
%{?_enable_arcnet:%modules_dir/kernel/drivers/net/arcnet}
%if_enabled can
%modules_dir/kernel/net/can
%modules_dir/kernel/drivers/net/can
%endif
%if_enabled fddi
%modules_dir/kernel/drivers/net/fddi
%modules_dir/kernel/net/802/fddi.ko
%endif
%modules_dir/kernel/net/batman-adv
%{?_enable_caif:%modules_dir/kernel/net/caif}
%{?_enable_caif:%modules_dir/kernel/drivers/net/caif}
%{?_enable_hippi:%modules_dir/kernel/drivers/net/hippi}
%modules_dir/kernel/drivers/net/plip
%modules_dir/kernel/drivers/net/slip/slip.ko
#modules_dir/kernel/net/ceph
%modules_dir/kernel/net/dccp
%modules_dir/kernel/net/decnet
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
%modules_dir/kernel/drivers/usb/misc/emi*
%{?_enable_oss:%exclude %modules_dir/kernel/sound/oss}
%exclude %modules_dir/kernel/sound/*.ko
%endif


%if "%sub_flavour" != "guest"
%{?_enable_guest:%kernel_modules_package_files guest}
%if_enabled drm
%dir %modules_dir/kernel/drivers/gpu
%dir %modules_dir/kernel/drivers/gpu/drm
%endif
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


%files -n kernel-headers-%flavour
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
%_libexecdir/perf
%_man1dir/*
%endif


%ifdef extra_mods
%(for m in %extra_mods; do
cat <<__PACKAGE__
%%files -n kernel-modules-$m-%flavour -f linux-%kversion/external/$m.rpmmodlist

__PACKAGE__
done)
%endif


%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build


%if_enabled docs
%files -n kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour
%{?_enable_htmldocs:%exclude %_docdir/kernel-doc-%flavour/DocBook}


%if_enabled htmldocs
%files -n kernel-docbook-%flavour
%doc %dir %_docdir/kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour/DocBook
%endif


%if_enabled man
%files -n kernel-man-%flavour
%kmandir
%endif
%endif


%if_with src
%files -n kernel-src-%flavour
%_usrsrc/kernel
%endif


%changelog
* Wed Sep 11 2013 Led <led@altlinux.ru> 3.4.61-alt4
- updated:
  + fix-fs-cifs

* Tue Sep 10 2013 Led <led@altlinux.ru> 3.4.61-alt3
- added:
  + fix-drivers-ata--libata
- vboxguest 4.2.18
- vboxhost 4.2.18
- GPIO_GENERIC=m (x86)
- enabled USB_DUMMY_HCD (x86_64)

* Mon Sep 09 2013 Led <led@altlinux.ru> 3.4.61-alt2
- updated:
  + feat-fs-aufs

* Sun Sep 08 2013 Led <led@altlinux.ru> 3.4.61-alt1
- 3.4.61

* Fri Sep 06 2013 Led <led@altlinux.ru> 3.4.60-alt5
- updated:
  + fix-drivers-hv
  + fix-drivers-hv--hv_util
  + fix-drivers-hv--hv_vmbus
  + feat-drivers-block--rxdsk

* Mon Sep 02 2013 Led <led@altlinux.ru> 3.4.60-alt4
- updated:
  + feat-fs-aufs

* Sun Sep 01 2013 Led <led@altlinux.ru> 3.4.60-alt3
- updated:
  + feat-net--netatop

* Fri Aug 30 2013 Led <led@altlinux.ru> 3.4.60-alt2
- added:
  + fix-drivers-net--vmxnet3

* Fri Aug 30 2013 Led <led@altlinux.ru> 3.4.60-alt1
- 3.4.60
- updated:
  + fix-include-linux

* Wed Aug 28 2013 Led <led@altlinux.ru> 3.4.59-alt3
- updated:
  + feat-drivers-block--btier
- fglrx 13.20.11

* Tue Aug 27 2013 Led <led@altlinux.ru> 3.4.59-alt2
- moved virtio_scsi.ko to kernel-modules-guest-* subpackage
- zfs 0.6.2

* Wed Aug 21 2013 Led <led@altlinux.ru> 3.4.59-alt1
- 3.4.59
- updated:
  + feat-fs-aufs
- enabled simple_ext2 (disable XATTR, POSIX_ACL and SECURITY)

* Sun Aug 18 2013 Led <led@altlinux.ru> 3.4.58-alt3
- updated:
  + fix-drivers-net-ethernet-broadcom--bnx2x

* Sat Aug 17 2013 Led <led@altlinux.ru> 3.4.58-alt2
- updated:
  + fix-drivers-gpu-drm--gma500_gfx
- added external modules:
  + exfat

* Thu Aug 15 2013 Led <led@altlinux.ru> 3.4.58-alt1
- 3.4.58
- updated:
  + fix-drivers-hv
  + fix-drivers-hv--hv_utils
  + fix-drivers-hv--hv_vmbus

* Thu Aug 15 2013 Led <led@altlinux.ru> 3.4.57-alt2
- updated:
  + feat-fs-aufs

* Mon Aug 12 2013 Led <led@altlinux.ru> 3.4.57-alt1
- 3.4.57
- removed:
  + fix-fs-notify-fanotify--fanotify_user
- added external modules:
  + fglrx

* Mon Aug 12 2013 Led <led@altlinux.ru> 3.4.56-alt9
- updated:
  + fix-fs-ext4
  + feat-fs-aufs
- removed ext4_for_ext23
- disaled ext4_for_ext2
- enabled ext4_for_ext3

* Sun Aug 11 2013 Led <led@altlinux.ru> 3.4.56-alt8
- updated:
  + feat-drivers-block--btier
- rebuilt with updated knem, spl and zfs

* Thu Aug 08 2013 Led <led@altlinux.ru> 3.4.56-alt7
- updated:
  + fix-drivers-gpu-drm--i915
  + fix-drivers-gpu-drm--gma500_gfx

* Thu Aug 08 2013 Led <led@altlinux.ru> 3.4.56-alt6
- added:
  + fix-drivers-usb-usbip
  + fix-drivers-usb-usbip-userspace
  + fix-fs-ext2
- cleaned up kernel-headers-modules-*
- fixed tarball creation of kernel-src

* Tue Aug 06 2013 Led <led@altlinux.ru> 3.4.56-alt5
- updated:
  + fix-fs-reiserfs

* Tue Aug 06 2013 Led <led@altlinux.ru> 3.4.56-alt4
- updated:
  + fix-drivers-acpi

* Mon Aug 05 2013 Led <led@altlinux.ru> 3.4.56-alt3
- kvm 3.10.1

* Mon Aug 05 2013 Led <led@altlinux.ru> 3.4.56-alt2
- updated:
  + fix-tools--perf
- updated BuildRequires for perf

* Sun Aug 04 2013 Led <led@altlinux.ru> 3.4.56-alt1
- 3.4.56
- updated:
  + fix-drivers-ata--ata_piix
  + fix-drivers-usb-host--xhci-hcd

* Sat Aug 03 2013 Led <led@altlinux.ru> 3.4.55-alt10
- removed:
  + fix-drivers-gpu-drm
- updated:
  + fix-drivers-gpu-drm--drm
- added:
  + fix-drivers-gpu-drm--ttm

* Sat Aug 03 2013 Led <led@altlinux.ru> 3.4.55-alt9
- added:
  + feat-drivers-net-wireless--vt6655
  + feat-drivers-net-wireless--vt6656
- enabled taskstats

* Sat Aug 03 2013 Led <led@altlinux.ru> 3.4.55-alt8
- added:
  + fix-drivers-firewire--firewire-core
  + fix-drivers-firewire--firewire-ohci
  + fix-drivers-firewire--firewire-sbp2
  + fix-drivers-firewire--nosy
  + fix-sound-firewire--snd-firewire-lib
  + fix-sound-firewire--snd-firewire-speakers
  + fix-sound-firewire--snd-isight
  + fix-tools-firewire--nosy-dump
  + feat-drivers-target-sbp--sbp_target
  + feat-sound-firewire--snd-dice
  + feat-sound-firewire--snd-fireworks
  + feat-sound-firewire--snd-scs1x

* Fri Aug 02 2013 Led <led@altlinux.ru> 3.4.55-alt7
- updated:
  + fix-fs-xfs (CVE-2013-1819)
- added:
  + fix-net-key--af_key (CVE-2013-2237)

* Thu Aug 01 2013 Led <led@altlinux.ru> 3.4.55-alt6
- added:
  + fix-kernel--compat

* Wed Jul 31 2013 Led <led@altlinux.ru> 3.4.55-alt5
- knem 1.1.0

* Wed Jul 31 2013 Led <led@altlinux.ru> 3.4.55-alt4
- added:
  + fix-drivers-ata--ata_piix

* Tue Jul 30 2013 Led <led@altlinux.ru> 3.4.55-alt3
- removed:
  + fix-drivers-ata--ata_piix
- added:
  + fix-drivers-watchdog--i6300esb
  + fix-drivers-watchdog--iTCO_wdt
  + fix-drivers-watchdog--sbc_epx_c3
  + fix-drivers-watchdog--sc520_wdt
  + fix-drivers-watchdog--sp5100_tco
  + fix-drivers-watchdog--via_wdt

* Tue Jul 30 2013 Led <led@altlinux.ru> 3.4.55-alt2
- updated:
  + fix-drivers-usb-host--xhci-hcd

* Mon Jul 29 2013 Led <led@altlinux.ru> 3.4.55-alt1
- 3.4.55

* Mon Jul 29 2013 Led <led@altlinux.ru> 3.4.54-alt8
- updated:
  + fix-drivers-hid--hid-apple
- added:
  + fix-drivers-input-mouse--appletouch
  + fix-drivers-platform--apple-gmux
  + fix-drivers-video-backlight--apple_bl
- moved {watch,soft}dog.ko modules from kernel-modules-watchdog-*
  to kernel-image-*

* Sun Jul 28 2013 Led <led@altlinux.ru> 3.4.54-alt7
- added:
  + fix-crypto--aes_generic

* Sat Jul 27 2013 Led <led@altlinux.ru> 3.4.54-alt6
- added:
  + fix-drivers-mfd--timberdale
- kvm 3.9.10

* Sat Jul 27 2013 Led <led@altlinux.ru> 3.4.54-alt5
- enabled:
  + EXT4_FS_SECURITY

* Sat Jul 27 2013 Led <led@altlinux.ru> 3.4.54-alt4
- removed:
  + feat-fs-exfat
- added:
  + fix-drivers-gpio--gpio-langwell
  + fix-drivers-gpio--gpio-ml-ioh
  + fix-drivers-gpio--gpio-sodaville
  + fix-drivers-i2c-busses--i2c-amd8111
  + fix-drivers-i2c-busses--i2c-i801
  + fix-drivers-mfd--cs5535-mfd
  + fix-sound-pci-oxygen--snd-virtuoso

* Fri Jul 26 2013 Led <led@altlinux.ru> 3.4.54-alt3
- added:
  + fix-drivers-gpio--gpio-sch
  + fix-drivers-i2c-busses--i2c-isch
  + fix-drivers-mfd--lpc_sch
- cleaned up configs

* Wed Jul 24 2013 Led <led@altlinux.ru> 3.4.54-alt2
- removed:
  + fix-drivers-regulator
- updated:
  + fix-drivers-regulator--regulator
  + fix-drivers-usb-otg--otg

* Mon Jul 22 2013 Led <led@altlinux.ru> 3.4.54-alt1
- 3.4.54

* Mon Jul 22 2013 Led <led@altlinux.ru> 3.4.53-alt10
- updated:
  + feat-fs-reiser4

* Sun Jul 21 2013 Led <led@altlinux.ru> 3.4.53-alt9
- updated:
  + feat-drivers-net-ethernet-atheros--alx
  + feat-drivers-scsi--vhba

* Sun Jul 21 2013 Led <led@altlinux.ru> 3.4.53-alt8
- updated:
  + fix-drivers-net-wireless-brcm80211--brcmsmac
  + feat-drivers-block--rxdsk
  + feat-drivers-platform--omnibook

* Fri Jul 19 2013 Led <led@altlinux.ru> 3.4.53-alt7
- updated:
  + feat-drivers-block--cloop
- added:
  + feat-kernel--sched-cfs-boost

* Thu Jul 18 2013 Led <led@altlinux.ru> 3.4.53-alt6
- updated:
  + fix-net-mac80211

* Thu Jul 18 2013 Led <led@altlinux.ru> 3.4.53-alt5
- updated:
  + fix-drivers-scsi--lpfc

* Thu Jul 18 2013 Led <led@altlinux.ru> 3.4.53-alt4
- updated:
  + fix-drivers-net-hyperv
  + fix-drivers-scsi--scsi_mod
  + fix-firmware-radeon
  + fix-fs-cifs

* Wed Jul 17 2013 Led <led@altlinux.ru> 3.4.53-alt3
- updated:
  + feat-fs-aufs

* Tue Jul 16 2013 Led <led@altlinux.ru> 3.4.53-alt2
- updated:
  + fix-fs-xfs
  + feat-fs-ext4--secrm
- added:
  + fix-drivers-scsi-ibmvscsi--ibmvfc

* Sun Jul 14 2013 Led <led@altlinux.ru> 3.4.53-alt1
- 3.4.53
- removed:
  + fix-drivers-cdrom--cdrom
  + fix-drivers-scsi-osd--osd
- updated:
  + fix-block
  + fix-drivers-block--nbd
  + fix-net-ceph

* Sat Jul 13 2013 Led <led@altlinux.ru> 3.4.52-alt12
- added:
  + fix-drivers-cdrom--cdrom (CVE-2013-2164)

* Fri Jul 12 2013 Led <led@altlinux.ru> 3.4.52-alt11
- updated:
  + fix-virt-kvm--kvm-amd
- added:
  + fix-virt-kvm--kvm-intel
  + feat-crypto--lz4
  + feat-lib--lz4

* Wed Jul 10 2013 Led <led@altlinux.ru> 3.4.52-alt10
- updated:
  + fix-drivers-net-hyperv
  + fix-mm

* Wed Jul 10 2013 Led <led@altlinux.ru> 3.4.52-alt9
- added:
  + fix-drivers-char-hw_random--via-rng

* Tue Jul 09 2013 Led <led@altlinux.ru> 3.4.52-alt8
- added:
  + fix-drivers-acpi-apei--apei
  + fix-drivers-acpi-apei--ghes
  + fix-drivers-pci-pcie-aer--aerdriver
  + fix-include-trace

* Mon Jul 08 2013 Led <led@altlinux.ru> 3.4.52-alt7
- added:
  + fix-drivers-pci

* Sun Jul 07 2013 Led <led@altlinux.ru> 3.4.52-alt6
- added:
  + fix-fs-notify-fanotify--fanotify_user (CVE-2013-2148)
- knem 1.0.90

* Sat Jul 06 2013 Led <led@altlinux.ru> 3.4.52-alt5
- updated:
  + fix-drivers-usb-host--xhci-hcd
- vboxguest 4.2.16
- vboxhost 4.2.16

* Fri Jul 05 2013 Led <led@altlinux.ru> 3.4.52-alt4
- updated:
  + fix-drivers-base
  + fix-drivers-base-power
  + fix-include-linux
- added:
  + fix-drivers-base--firmware_class

* Fri Jul 05 2013 Led <led@altlinux.ru> 3.4.52-alt3
- updated:
  + feat-drivers-acpi--bbswitch

* Thu Jul 04 2013 Led <led@altlinux.ru> 3.4.52-alt2
- updated:
  + fix-block (CVE-2013-2851)
  + fix-drivers-block--nbd (CVE-2013-2851)
- added:
  + fix-drivers-scsi-osd--osd (CVE-2013-2851)

* Thu Jul 04 2013 Led <led@altlinux.ru> 3.4.52-alt1
- 3.4.52

* Wed Jul 03 2013 Led <led@altlinux.ru> 3.4.51-alt5
- added:
  + feat-fs-exfat
- removed external modules:
  + exfat

* Tue Jul 02 2013 Led <led@altlinux.ru> 3.4.51-alt4
- updated:
  + fix-net-ceph (CVE-2013-1059)

* Tue Jul 02 2013 Led <led@altlinux.ru> 3.4.51-alt3
- updated:
  + fix-block
  + fix-fs-ocfs2

* Tue Jul 02 2013 Led <led@altlinux.ru> 3.4.51-alt2
- updated:
  + feat-drivers-net-ethernet-atheros--alx
- Makefile.external: fixed unowned dirs
- removed external modules:
  + nvidia
- added external modules:
  + spl
  + zfs

* Sun Jun 30 2013 Led <led@altlinux.ru> 3.4.51-alt1
- 3.4.51
- updated:
  + fix-drivers-gpu-drm--i915
- added external modules:
  + exfat
- kvm 3.9.8

* Thu Jun 27 2013 Led <led@altlinux.ru> 3.4.50-alt4
- updated:
  + fix-fs-ext4
- fixed %%files of kernel-modules-guest-*
- added external modules:
  + knem

* Wed Jun 26 2013 Led <led@altlinux.ru> 3.4.50-alt3
- updated:
  + fix-fs-ocfs2
- added:
  + fix-drivers-gpu-drm--drm
  + fix-fs-autofs4
- nvidia 319.32

* Sun Jun 23 2013 Led <led@altlinux.ru> 3.4.50-alt2
- updated:
  + fix-virt-kvm
- disabled:
  + ATH9K_AHB
- cleaned up configs
- disabled kvm
- added external modules:
  + kvm
- vboxhost 4.2.14
- vboxguest 4.2.14
- disabled kernel-headers post scripts

* Thu Jun 20 2013 Led <led@altlinux.ru> 3.4.50-alt1
- 3.4.50
- disabled:
  + ATH9K_LEGACY_RATE_CONTROL

* Thu Jun 20 2013 Led <led@altlinux.ru> 3.4.49-alt5
- updated:
  + fix-net-sunrpc

* Tue Jun 18 2013 Led <led@altlinux.ru> 3.4.49-alt4
- enabled:
  + DRM_LOAD_EDID_FIRMWARE

* Sat Jun 15 2013 Led <led@altlinux.ru> 3.4.49-alt3
- updated:
  + fix-net-sunrpc
- added:
  + fix-arch-x86-cpu
  + fix-drivers-net-wireless--rtl8187se

* Fri Jun 14 2013 Led <led@altlinux.ru> 3.4.49-alt2
- removed:
  + fix-drivers-usb-serial--io_ti
- updated:
  + fix-firmware-radeon

* Thu Jun 13 2013 Led <led@altlinux.ru> 3.4.49-alt1
- 3.4.49

* Thu Jun 13 2013 Led <led@altlinux.ru> 3.4.48-alt6
- PCI_IOAPIC=m
- enabled:
  + CRYPTO_MANAGER_DISABLE_TESTS
- disabled:
  + OSF_PARTITION
  + UNIXWARE_DISKLABEL
  + TASK*

* Tue Jun 11 2013 Led <led@altlinux.ru> 3.4.48-alt5
- updated:
  + fix-drivers-acpi
- added:
  + fix-drivers-acpi--container
  + fix-drivers-acpi--pci_slot

* Mon Jun 10 2013 Led <led@altlinux.ru> 3.4.48-alt4
- updated:
  + fix-arch-x86--microcode
- disabled:
  + PPS_CLIENT_KTIMER

* Mon Jun 10 2013 Led <led@altlinux.ru> 3.4.48-alt3
- added:
  + fix-arch-x86--microcode

* Sun Jun 09 2013 Led <led@altlinux.ru> 3.4.48-alt2
- updated:
  + feat-drivers-block--btier
- added:
  + fix-drivers-ptp--ptp_pch
- renamed external modules to kernel-modules-*

* Sat Jun 08 2013 Led <led@altlinux.ru> 3.4.48-alt1
- 3.4.48
- removed:
  + fix-drivers-target-iscsi
- added:
  + fix-drivers-bluetooth--btusb
  + fix-sound-pci-hda--snd-hda-codec
  + fix-sound-pci-hda--snd-hda-codec-analog
  + fix-sound-pci-hda--snd-hda-codec-idt
  + fix-sound-pci-hda--snd-hda-intel

* Sat Jun 01 2013 Led <led@altlinux.ru> 3.4.47-alt5
- updated:
  + fix-fs-reiserfs

* Fri May 31 2013 Led <led@altlinux.ru> 3.4.47-alt4
- added:
  + fix-drivers-target-iscsi (CVE-2013-2850)
  + fix-net-netfilter--xt_LOG

* Tue May 28 2013 Led <led@altlinux.ru> 3.4.47-alt3
- updated:
  + feat-drivers-block--btier
- added:
  + fix-firmware-radeon
- fixed License of firmware-kernel-* subpackage

* Sat May 25 2013 Led <led@altlinux.ru> 3.4.47-alt2
- nvidia 319.23
- added external modules:
  + vboxguest

* Sat May 25 2013 Led <led@altlinux.ru> 3.4.47-alt1
- 3.4.47

* Tue May 21 2013 Led <led@altlinux.ru> 3.4.46-alt4
- updated:
  + fix-fs-xfs

* Mon May 20 2013 Led <led@altlinux.ru> 3.4.46-alt3
- updated:
  + fix-fs-xfs

* Mon May 20 2013 Led <led@altlinux.ru> 3.4.46-alt2
- updated:
  + fix-net-sunrpc

* Sun May 19 2013 Led <led@altlinux.ru> 3.4.46-alt1
- 3.4.46
- updated:
  + fix-drivers-gpu-drm

* Sun May 19 2013 Led <led@altlinux.ru> 3.4.45-alt7
- updated:
  + fix-drivers-gpu-vga--vga_switcheroo
  + fix-net-dcb

* Sun May 19 2013 Led <led@altlinux.ru> 3.4.45-alt6
- updated:
  + fix-drivers-gpu-vga--vga_switcheroo

* Fri May 17 2013 Led <led@altlinux.ru> 3.4.45-alt5
- added:
  + fix-drivers-base-power
- updated:
  + fix-drivers-gpu-vga--vga_switcheroo
- enabled:
  + fix-drivers-gpu-vga--vga_switcheroo

* Fri May 17 2013 Led <led@altlinux.ru> 3.4.45-alt4
- added:
  + fix-drivers-net-ethernet-qlogic--qlge
- disabled:
  + fix-drivers-gpu-vga--vga_switcheroo
- nvidia 319.17

* Tue May 14 2013 Led <led@altlinux.ru> 3.4.45-alt3
- added:
  + fix-drivers-md--md-mod

* Tue May 14 2013 Led <led@altlinux.ru> 3.4.45-alt2
- updated:
  + fix-fs

* Sun May 12 2013 Led <led@altlinux.ru> 3.4.45-alt1
- 3.4.45
- updated:
  + fix-drivers-usb-host--xhci-hcd

* Sat May 11 2013 Led <led@altlinux.ru> 3.4.44-alt3
- updated:
  + fix-virt-kvm
- renamed external modules to kernel-extmod-*

* Fri May 10 2013 Led <led@altlinux.ru> 3.4.44-alt2
- added:
  + fix-drivers-usb-host--xhci-hcd

* Wed May 08 2013 Led <led@altlinux.ru> 3.4.44-alt1
- 3.4.44
- updated:
  + feat-fs-ext4--richacl

* Tue May 07 2013 Led <led@altlinux.ru> 3.4.43-alt1
- 3.4.43
- updated:
  + fix-drivers-tty
  + fix-mm--mmu
  + fix-net-core (CVE-2013-0290)
- added:
  + fix-net-unix--unix (CVE-2013-0290)
- disabled:
  + UCB1400_CORE
  + GPIO_UCB1400
  + TOUCHSCREEN_UCB1400

* Tue Apr 30 2013 Led <led@altlinux.ru> 3.4.42-alt6
- updated:
  + fix-drivers-hwmon--coretemp
- added:
  + fix-fs-fuse
- disabled:
  + IP6_NF_QUEUE
  + ECONET
  + USB_DEVICE_CLASS
- cleaned up spec

* Mon Apr 29 2013 Led <led@altlinux.ru> 3.4.42-alt5
- updated:
  + fix-arch-x86

* Mon Apr 29 2013 Led <led@altlinux.ru> 3.4.42-alt4
- updated:
  + fix-drivers-tty
- changed versioning for external modules

* Mon Apr 29 2013 Led <led@altlinux.ru> 3.4.42-alt3
- removed:
  + feat-fs-hfs
- updated:
  + fix-arch-x86
  + fix-arch-x86--mcheck
- added:
  + fix-fs-hfs
- cleaned up spec
- added external modules:
  + nvidia

* Sat Apr 27 2013 Led <led@altlinux.ru> 3.4.42-alt2
- updated:
  + fix-drivers-scsi--sd_mod

* Fri Apr 26 2013 Led <led@altlinux.ru> 3.4.42-alt1
- 3.4.42
- updated:
  + fix-virt-kvm

* Fri Apr 26 2013 Led <led@altlinux.ru> 3.4.41-alt5
- added:
  + feat-drivers-acpi--bbswitch
- disabled:
  + ACPI_HED

* Wed Apr 24 2013 Led <led@altlinux.ru> 3.4.41-alt4
- added:
  + fix-kernel--rcutree
  + feat-drivers-block--btier

* Mon Apr 22 2013 Led <led@altlinux.ru> 3.4.41-alt3
- updated:
  + feat-drivers-net-ethernet-atheros--alx

* Wed Apr 17 2013 Led <led@altlinux.ru> 3.4.41-alt2
- updated:
  + feat-net--netatop

* Wed Apr 17 2013 Led <led@altlinux.ru> 3.4.41-alt1
- 3.4.41

* Mon Apr 15 2013 Led <led@altlinux.ru> 3.4.40-alt2
- vboxhost 4.2.12

* Fri Apr 12 2013 Led <led@altlinux.ru> 3.4.40-alt1
- 3.4.40

* Fri Apr 12 2013 Led <led@altlinux.ru> 3.4.39-alt10
- updated:
  + fix-net-wimax

* Thu Apr 11 2013 Led <led@altlinux.ru> 3.4.39-alt9
- moved videodev.ko form kernel-modules-media-* subpackage to kernel-image-*

* Thu Apr 11 2013 Led <led@altlinux.ru> 3.4.39-alt8
- removed subpackage kernel-modules-w1-*
- moved udc-core.ko form kernel-modules-usb-gadget-* subpackage to kernel-image-*
- moved media.ko form kernel-modules-media-* subpackage to kernel-image-*
- moved lcd.ko, fb_sys_fops.ko, syscopyarea.ko, sysfillrect.ko, sysimgblt.ko,
  sisfb.ko from kernel-modules-video-* subpackage to kernel-image-*

* Thu Apr 11 2013 Led <led@altlinux.ru> 3.4.39-alt7
- updated:
  + fix-drivers-tty
  + fix-net-core
  + feat-drivers-block--btier
- added:
  + fix-drivers-mfd--adp5520
  + fix-drivers-mmc-host--sdhci-pci
  + fix-drivers-net-ethernet-broadcom--bnx2x
  + fix-drivers-net-ethernet-intel--ixgbe
  + fix-drivers-net-wireless-wl12xx
  + fix-drivers-scsi-fcoe--fcoe
  + fix-drivers-tty-hvc--hvc_console
  + fix-drivers-usb-otg--otg
  + fix-net-802--fc
  + fix-net-dcb
- disabled:
  + rapidio
  + PMIC_DA903X
  + HTC_I2CPLD
  + HTC_PASIC3
  + MFD_WM8994
  + FB_TMIO
  + FB_VIRTUAL
  + SCSI_DEBUG
- updated Requires
- disabled preun script

* Wed Apr 10 2013 Led <led@altlinux.ru> 3.4.39-alt6
- updated:
  + fix-drivers-gpu-drm--nouveau
  + fix-drivers-gpu-drm--radeon
- added:
  + fix-drivers-gpio--gpio-timberdale
  + fix-drivers-gpio--gpio-ucb1400
  + fix-drivers-vga--vga_switcheroo
  + fix-kernel-irq

* Tue Apr 09 2013 Led <led@altlinux.ru> 3.4.39-alt5
- removed:
  + fix-drivers-mfd--wm8994-core
- updated:
  + fix-drivers-base-regmap
  + fix-drivers-mmc-core
  + fix-drivers-usb-core
  + feat-drivers-video--bootsplash
- added:
  + fix-drivers-mfd--ab8500-gpadc
  + fix-drivers-mfd--wm8994
  + fix-drivers-power--ab8500
  + fix-drivers-power--charger-manager
  + fix-drivers-regulator--88pm8607
  + fix-drivers-regulator--ab8500
  + fix-drivers-regulator--regulator
  + fix-drivers-watchdog--watchdog
- disabled BLK_DEV_HD

* Sun Apr 07 2013 Led <led@altlinux.ru> 3.4.39-alt4
- updated:
  + fix-drivers-regulator
  + fix-mm
- added:
  + fix-drivers-usb-core

* Sun Apr 07 2013 Led <led@altlinux.ru> 3.4.39-alt3
- updated:
  + fix-arch-x86--mcheck
  + fix-drivers-acpi
  + fix-mm
  + feat-mm--frontswap
- added:
  + fix-kernel-power
  + fix-mm--cleancache
  + fix-mm--memblock
- disabled ACPI_EC_DEBUGFS

* Sun Apr 07 2013 Led <led@altlinux.ru> 3.4.39-alt2
- updated:
  + fix-drivers-hid--hid
  + fix-drivers-net-caif--cfspi_slave
  + fix-drivers-spi--spi-dw
- added:
  + fix-net-l2tp--l2tp_core
  + fix-net-wimax
- disabled:
  + MMC_TEST
  + L2TP_DEBUGFS
- enabled debugfs

* Sat Apr 06 2013 Led <led@altlinux.ru> 3.4.39-alt1
- 3.4.39
- updated:
  + fix-drivers-misc--vmw_balloon
  + fix-drivers-platform--intel_ips
  + feat-drivers-block--btier
- added:
  + fix-drivers-bluetooth--btmrvl
  + fix-drivers-gpio--gpiolib
  + fix-drivers-gpio--gpio-ks8695
  + fix-drivers-gpio--gpio-mcp23s08
  + fix-drivers-gpio--gpio-nomadik
  + fix-drivers-gpio--gpio-tegra
  + fix-drivers-gpio--gpio-wm831x
  + fix-drivers-gpio--gpio-wm8994
  + fix-drivers-mmc-core
  + fix-drivers-net-caif--caif_serial
  + fix-drivers-net-caif--cfspi_slave
  + fix-drivers-net-wimax-i2400m--i2400m
  + fix-drivers-net-wireless-mwifiex--mwifiex
  + fix-drivers-power--da9030_battery
  + fix-drivers-usb-dwc3--dwc3
  + fix-drivers-usb-host--uhci-hcd
  + fix-drivers-usb-host--isp116x-hcd
  + fix-drivers-usb-musb--musb_hdrc

* Fri Apr 05 2013 Led <led@altlinux.ru> 3.4.38-alt6
- updated:
  + fix-drivers-tty-serial--pch_uart
  + feat-drivers-block--btier
- added:
  + fix-drivers-tty-serial--ifx6x60
  + fix-drivers-tty-serial--mfd
  + fix-drivers-tty-serial--mrst_max3110

* Fri Apr 05 2013 Led <led@altlinux.ru> 3.4.38-alt5
- updated:
  + fix-drivers-scsi--lpfc
  + fix-fs-ocfs2
- added:
  + fix-drivers-hid--hid
  + fix-drivers-hid--hid-picolcd
  + fix-drivers-hid--hid-wiimote
  + fix-drivers-hwmon--asus_atk0110
  + fix-drivers-iommu--amd_iommu
  + fix-drivers-iommu--intel-iommu
  + fix-drivers-misc--vmw_balloon
  + fix-drivers-net--sb1000
  + fix-drivers-regulator
  + fix-drivers-spi--spi-dw
- enabled HID_BATTERY_STRENGTH
- moved arcnet drivers to kernel-modules-net-extra-* subpackage
- moved arcnet, hippi, plip and slip drivers to kernel-modules-net-extra-*
  subpackage
- cleaned up spec

* Sun Mar 31 2013 Led <led@altlinux.ru> 3.4.38-alt4
- updated:
  + fix-drivers-gpu-drm--i915
  + feat-fs-aufs
- added:
  + fix-drivers-base-regmap
  + fix-drivers-gpu-drm
  + fix-drivers-gpu-drm--radeon
  + fix-drivers-net--bonding
  + fix-fs-ceph
  + fix-net-ceph
- moved vmw_balloon.ko to kernel-modules-guest-* subpackage
- moved caif drivers to kernel-modules-net-extra-* subpackage
- disabled:
  + ACPI_APEI_EINJ
  + ACPI_CUSTOM_METHOD

* Sat Mar 30 2013 Led <led@altlinux.ru> 3.4.38-alt3
- enabled:
  + TIMER_STATS

* Fri Mar 29 2013 Led <led@altlinux.ru> 3.4.38-alt2
- updated:
  + fix-mm

* Fri Mar 29 2013 Led <led@altlinux.ru> 3.4.38-alt1
- 3.4.38
- updated:
  + fix-drivers-gpu-drm--i915

* Mon Mar 25 2013 Led <led@altlinux.ru> 3.4.37-alt6
- added:
  + fix-drivers-usb-serial--io_ti

* Sun Mar 24 2013 Led <led@altlinux.ru> 3.4.37-alt5
- added:
  + feat-drivers-usb-storage--rts5139

* Sun Mar 24 2013 Led <led@altlinux.ru> 3.4.37-alt4
- removed:
  + fix-drivers-net-wireless--b43
- disabled crasher

* Sat Mar 23 2013 Led <led@altlinux.ru> 3.4.37-alt3
- updated:
  + fix-mm
  + feat-drivers-block--btier

* Thu Mar 21 2013 Led <led@altlinux.ru> 3.4.37-alt2
- added:
  + feat-drivers-block--btier

* Thu Mar 21 2013 Led <led@altlinux.ru> 3.4.37-alt1
- 3.4.37
- removed:
  + fix-drivers-block--loop
  + fix-drivers-tty--pty
- updated:
  + fix-fs--block
  + fix-fs-ext3
  + fix-net-core
  + fix-virt-kvm
- with perf
- updated BuildRequires for perf

* Wed Mar 20 2013 Led <led@altlinux.ru> 3.4.36-alt8
- updated:
  + fix-block
  + fix-fs
  + fix-fs--block
  + fix-fs-ext3
  + fix-fs-ext4
  + fix-mm
- added:
  + fix-block--blk-integrity
  + fix-fs-9p
  + fix-fs-gfs2
  + fix-fs-nilfs2
  + fix-fs-ocfs2
  + fix-fs-ubifs
  + fix-mm--bounce

* Tue Mar 19 2013 Led <led@altlinux.ru> 3.4.36-alt7
- updated:
  + fix-fs-reiserfs
- added:
  + fix-fs-jfs
  + fix-net-ipv4--xfrm
  + fix-net-ipv6--xfrm

* Tue Mar 19 2013 Led <led@altlinux.ru> 3.4.36-alt6
- enabled:
  + VM_EVENT_COUNTERS

* Tue Mar 19 2013 Led <led@altlinux.ru> 3.4.36-alt5
- updated:
  + fix-virt-kvm
- added:
  + fix-fs-xfs

* Mon Mar 18 2013 Led <led@altlinux.ru> 3.4.36-alt4
- added:
  + fix-net-wireless--cfg80211
- disabled debugfs

* Mon Mar 18 2013 Led <led@altlinux.ru> 3.4.36-alt3
- updated:
  + fix-fs-reiserfs
  + feat-fs-aufs
- enabled debugfs

* Mon Mar 18 2013 Led <led@altlinux.ru> 3.4.36-alt2
- updated:
  + fix-mm--swap
  + feat-mm--frontswap
- added:
  + fix-drivers-block--loop
  + fix-fs--block
- disabled debugfs
- vboxhost 4.2.10

* Fri Mar 15 2013 Led <led@altlinux.ru> 3.4.36-alt1
- 3.4.36
- updated:
  + fix-drivers-scsi--hv_storvsc

* Thu Mar 14 2013 Led <led@altlinux.ru> 3.4.35-alt9
- updated:
  + fix-drivers-gpu-drm--i915
  + fix-mm--swap
  + fix-mm--zcache
  + feat-mm--frontswap
- enabled debugfs

* Thu Mar 14 2013 Led <led@altlinux.ru> 3.4.35-alt8
- updated:
  + fix-drivers-block--zram
  + fix-mm--swap
  + fix-mm--zcache
  + fix-mm--zsmalloc
  + feat-block--bfq-iosched
  + feat-fs-aufs
- added:
  + fix-fs-debugfs
  + fix-fs-ext3
  + feat-mm--zswap

* Wed Mar 13 2013 Led <led@altlinux.ru> 3.4.35-alt7
- added:
  + feat-drivers-net-ethernet-atheros--alx

* Tue Mar 12 2013 Led <led@altlinux.ru> 3.4.35-alt6
- enabled:
  + BLK_DEV_INTEGRITY
- SCSI=y
- BLK_DEV_SD=y

* Mon Mar 11 2013 Led <led@altlinux.ru> 3.4.35-alt5
- set DEFAULT_HOSTNAME to default value
- moved content of kernel-modules-sound-ext-* subpackage to
  kernel-modules-sound-* subpackage
- removed kernel-modules-sound-ext-* subpackage
- vboxhost 4.2.8

* Mon Mar 11 2013 Led <led@altlinux.ru> 3.4.35-alt4
- updated:
  + fix-fs-nfs
  + fix-mm--swap
  + fix-net-core
  + fix-net-sunrpc
  + fix-virt-kvm
  + feat-kernel-power-tuxonice
  + feat-mm--frontswap
- added:
  + fix-security--selinux

* Wed Mar 06 2013 Led <led@altlinux.ru> 3.4.35-alt3
- updated:
  + fix-mm
  + fix-mm--mmu
  + fix-net-core
  + feat-kernel-power-tuxonice
  + feat-mm--frontswap
- added:
  + fix-drivers-block--nbd
  + fix-mm--slab
  + fix-mm--slub

* Mon Mar 04 2013 Led <led@altlinux.ru> 3.4.35-alt2
- added:
  + fix-crypto--cryptomgr
  + fix-lib-lzo
  + feat-drivers-video--bootsplash

* Mon Mar 04 2013 Led <led@altlinux.ru> 3.4.35-alt1
- 3.4.35
- removed:
  + fix-fs-quota
- moved ledtrig-ide-disk.ko to kernel-image-ide-* subpackage

* Sat Mar 02 2013 Led <led@altlinux.ru> 3.4.34-alt4
- added:
  + fix-drivers-leds--led-core
  + fix-drivers-leds--led-triggers
  + fix-drivers-leds--ledtrig-ide-disk
- disabled:
  + KEYS_DEBUG_PROC_KEYS
  + ASYNC_RAID6_TEST
  + CPU_NOTIFIER_ERROR_INJECT
  + BACKTRACE_SELF_TEST
  + LKDTM
  + RCU_TORTURE_TEST
  + TIMER_STATS
  + DEBUG_KERNEL
  + PROC_KCORE
  + QFMT_V1
  + QUOTA_NETLINK_INTERFACE
  + DMATEST
  + RTC_DRV_TEST
  + ACCESSIBILITY
  + USB_G_DBGP
  + USB_DEVICEFS
  + FB_FOREIGN_ENDIAN
- enabled:
  + IO_DELAY_0XED (x86)
  + IO_DELAY_NONE (x86_64)
  + FRAME_WARN=2560
  + MMC_CLKGATE
  + USB_HWA_HCD
  + USB_ANNOUNCE_NEW_DEVICES
  + SND_VXPOCKET
  + SND_PDAUDIOCF
  + SND_HRTIMER
  + SND_SEQ_HRTIMER_DEFAULT
  + VIDEO_MEYE

* Sat Mar 02 2013 Led <led@altlinux.ru> 3.4.34-alt3
- added:
  + feat-drivers-scsi--vhba

* Fri Mar 01 2013 Led <led@altlinux.ru> 3.4.34-alt2
- updated:
  + feat-drivers-video--bootsplash
- added:
  + fix-drivers-block--aoe
  + fix-drivers-usb
  + fix-include-linux
- build with default (SLUB) allocator

* Thu Feb 28 2013 Led <led@altlinux.ru> 3.4.34-alt1
- 3.4.34
- removed:
  + fix-arch-x86-cpu
- updated:
  + fix-kernel
  + fix-mm
  + fix-net-core
- decreased RCU_FANOUT
- disabled:
  + PROC_PID_CPUSET
  + CGROUP_PERF

* Wed Feb 27 2013 Led <led@altlinux.ru> 3.4.33-alt6
- updated:
  + fix-mm (CVE-2013-1767)

* Wed Feb 27 2013 Led <led@altlinux.ru> 3.4.33-alt5
- disabled:
  + LOGO
  + FONT_MINI_4x6
  + PROC_PAGE_MONITOR
  + PM_DEVFREQ
  + SGI_PARTITION
  + ULTRIX_PARTITION
  + SUN_PARTITION
  + VM_EVENT_COUNTERS

* Tue Feb 26 2013 Led <led@altlinux.ru> 3.4.33-alt4
- updated:
  + fix-net-core
- disabled:
  + FB_ASILIANT
  + FB_IMSTT
  + EXYNOS_VIDEO
- enabled:
  + FB_S3
  + FONT_SUN12x22

* Mon Feb 25 2013 Led <led@altlinux.ru> 3.4.33-alt3
- updated:
  + feat-fs-ext4--secrm
  + feat-fs-overlayfs
- added:
  + fix-drivers-tty
  + fix-net-core (CVE-2013-1763)

* Sat Feb 23 2013 Led <led@altlinux.ru> 3.4.33-alt2
- updated:
  + fix-fs-btrfs
  + feat-drivers-gpu-drm--cirrus
  + feat-fs--lnfs
  + feat-fs-ext2--secrm
  + feat-fs-ext3--secrm
  + feat-fs-ext4--secrm
  + feat-kernel-power-tuxonice

* Fri Feb 22 2013 Led <led@altlinux.ru> 3.4.33-alt1
- 3.4.33
- added:
  + fix-drivers-idle--intel_idle
- USB_EHCI_HCD=y (x86_64)

* Tue Feb 19 2013 Led <led@altlinux.ru> 3.4.32-alt2
- added:
  + fix-drivers-mfd--twl4030-core
  + fix-drivers-scsi--lpfc
  + fix-drivers-tty-serial--pch_uart
  + fix-net-ipv6
- enabled CPU_SUP_CENTAUR
- vboxhost 4.2.6

* Sun Feb 17 2013 Led <led@altlinux.ru> 3.4.32-alt1
- 3.4.32
- disabled ub (BLK_DEV_UB)

* Sun Feb 17 2013 Led <led@altlinux.ru> 3.4.31-alt4
- added:
  + feat-drivers-platform--omnibook

* Sun Feb 17 2013 Led <led@altlinux.ru> 3.4.31-alt3
- updated:
  + feat-drivers-block--zram
- added:
  + feat-drivers-block--rxdsk
  + feat-drivers-misc--emlog

* Sat Feb 16 2013 Led <led@altlinux.ru> 3.4.31-alt2
- updated:
  + feat-drivers-video--bootsplash
  + fix-fs-proc
- disabled USB_LIBUSUAL
- enabled spi
- I2C=y

* Sat Feb 16 2013 Led <led@altlinux.ru> 3.4.31-alt1
- 3.4.31
- updated:
  + fix-fs-nfs
  + fix-mm
  + fix-net-bridge--bridge
  + feat-mm--uksm
- added:
  + fix-drivers-media-radio--radio-rtrack2
  + fix-fs-cifs
  + fix-net--dns_resolver
- modularized:
  + INET_LRO
  + NET_CLS_CGROUP
  + DNS_RESOLVER
  + MAC_EMUMOUSEBTN
  + POWER_SUPPLY
  + THERMAL
  + AGP
  + AGP_AMD64
- enabled:
  + CIFS_UPCALL
  + CIFS_DFS_UPCALL
- disabled spi
- USB_COMMON=y
- USB=y

* Tue Feb 12 2013 Led <led@altlinux.ru> 3.4.30-alt1
- 3.4.30

* Mon Feb 11 2013 Led <led@altlinux.ru> 3.4.29-alt7
- updated:
  + fix-mm
- added:
  + fix-fs-logfs

* Fri Feb 08 2013 Led <led@altlinux.ru> 3.4.29-alt6
- added:
  + fix-drivers-scsi--st
  + fix-lib--btree
- updated configs
- BTREE=m

* Wed Feb 06 2013 Led <led@altlinux.ru> 3.4.29-alt5
- disabled apei (ACPI_APEI)
- RTC_DRV_CMOS=y
- updated configs

* Wed Feb 06 2013 Led <led@altlinux.ru> 3.4.29-alt4
- updated:
  + feat-fs-tmpfs--root
- fixed led-ws-3.4.x86_64.config
- add missed feat-fs-tmpfs--root

* Tue Feb 05 2013 Led <led@altlinux.ru> 3.4.29-alt3
- added:
  + fix-fs-quota
- add missed fix-fs-ramfs

* Mon Feb 04 2013 Led <led@altlinux.ru> 3.4.29-alt2
- updated:
  + feat-fs-aufs
- updated configs

* Mon Feb 04 2013 Led <led@altlinux.ru> 3.4.29-alt1
- 3.4.29

* Sun Feb 03 2013 Led <led@altlinux.ru> 3.4.28-alt7
- added:
  + fix-fs-ramfs
  + feat-fs-tmpfs--root

* Sat Feb 02 2013 Led <led@altlinux.ru> 3.4.28-alt6
- updated:
  + fix-drivers-scsi--hv_storvsc
- added:
  + feat-fs-squashfs--write

* Fri Feb 01 2013 Led <led@altlinux.ru> 3.4.28-alt5
- removed:
  + feat-fs-squashfs--write

* Thu Jan 31 2013 Led <led@altlinux.ru> 3.4.28-alt4
- updated:
  + fix-mm--zcache
  + feat-kernel-power-tuxonice
  + feat-mm--zsmalloc

* Tue Jan 29 2013 Led <led@altlinux.ru> 3.4.28-alt3
- updated:
  + fix-arch-x86--mcheck
  + fix-drivers-acpi
  + fix-fs
- added:
  + fix-net-rds--rds_rdma

* Tue Jan 29 2013 Led <led@altlinux.ru> 3.4.28-alt2
- updated:
  + fix-drivers-edac--e752x_edac
  + fix-drivers-edac--i3000_edac
  + fix-drivers-edac--i5000_edac
  + fix-drivers-edac--i5100_edac
  + fix-drivers-edac--i5400_edac
  + fix-drivers-edac--i7300_edac
  + fix-drivers-edac--i82975x_edac
  + fix-drivers-edac--x38_edac
  + fix-mm--zcache

* Mon Jan 28 2013 Led <led@altlinux.ru> 3.4.28-alt1
- 3.4.28
- build with SLAB allocator

* Fri Jan 25 2013 Led <led@altlinux.ru> 3.4.27-alt4
- updated:
  + fix-mm--zcache
- merged kernel-headers-asm-* to kernel-headers-* subpackage
- set kernel-headers-* as no noarch
- kernel-modules-media-* requires kernel-modules-sound-ext-* (for webcams)

* Thu Jan 24 2013 Led <led@altlinux.ru> 3.4.27-alt3
- added:
  + fix-drivers-net-ethernet-alacritech--slicoss
  + fix-drivers-platform--asus_oled
  + feat-drivers-net-ethernet-alacritech
  + feat-drivers-net-ethernet-alacritech--slicoss
  + feat-drivers-platform--asus_oled

* Wed Jan 23 2013 Led <led@altlinux.ru> 3.4.27-alt2
- added:
  + fix-drivers-tty--pty
  + feat-net-ipv4-netfilter--ipt_NETFLOW
- moved content of kernel-modules-lirc-* subpackage to kernel-modules-media-*
  subpackage.
- removed kernel-modules-lirc-* subpackage
- moved qnx6 to kernel-modules-fs-extra-* subpackage

* Tue Jan 22 2013 Led <led@altlinux.ru> 3.4.27-alt1
- 3.4.27

* Mon Jan 21 2013 Led <led@altlinux.ru> 3.4.26-alt5
- added:
  + feat-firmware-rtl_nic

* Mon Jan 21 2013 Led <led@altlinux.ru> 3.4.26-alt4
- added:
  + fix-lib
- spec: support build for corei7 CPU

* Sat Jan 19 2013 Led <led@altlinux.ru> 3.4.26-alt3
- updated:
  + fix-net-bridge--bridge
  + feat-fs-aufs
- removed external modules:
  + fglrx

* Fri Jan 18 2013 Led <led@altlinux.ru> 3.4.26-alt2
- updated:
  + fix-mm--zcache
  + feat-mm--zcache
- disable CRYPTO_FIPS

* Fri Jan 18 2013 Led <led@altlinux.ru> 3.4.26-alt1
- 3.4.26
- removed:
  + fix-drivers-misc--zcache
  + fix-lib--zsmalloc
  + fix-mm--huge_memory
  + fix-mm--mmu
- updated:
  + feat-fs-ext4--richacl
  + feat-kernel-power-tuxonice
- added:
  + fix-mm--zcache
  + fix-mm--zsmalloc
  + feat-drivers-block--zram
  + feat-drivers-video--xgifb
  + feat-kernel-power-tuxonice--frontswap
  + feat-mm--frontswap
  + feat-mm--zcache
  + feat-mm--zsmalloc
- disabled compat (turn off some COMPAT options in .config)

* Thu Jan 17 2013 Led <led@altlinux.ru> 3.4.25-alt2
- added:
  + fix-arch-x86-cpu
  + fix-drivers-net-ethernet-via--via-rhine

* Wed Jan 16 2013 Led <led@altlinux.ru> 3.4.25-alt1
- initial build based on kernel-image-led-ws-3.0.57-alt11 spec
