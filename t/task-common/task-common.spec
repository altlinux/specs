Name: task-common
Version: 1.0
Release: alt3

Summary: Common dependencies
License: GPL-3.0-or-later
Group: Graphical desktop/Other

URL: https://altlinux.org

%description
%summary.

%package system-base
Summary: Common base system dependencies
Group: Graphical desktop/Other

Requires: apt-repo
Requires: apt-rsync
Requires: apt-scripts
Requires: apt-https
Requires: update-kernel
Requires: bash-completion
%ifarch %ix86 x86_64
Requires: cpufreq-simple
%endif
Requires: eject
Requires: bc
%ifnarch %ix86
Requires: ncdu
%endif
Requires: tree
Requires: sysfsutils
Requires: mc
Requires: vim-console
Requires: apf
Requires: tzdata
Requires: ntpdate
Requires: man-pages
Requires: color-prompt-and-man
Requires: lsblk

Requires: f2fs-tools
Requires: ntfs-3g
Requires: dosfstools
Requires: exfatprogs
Requires: fatresize
Requires: gpart

Requires: shadow-change

Requires: openssh
Requires: openssh-blacklist
Requires: iptables
Requires: nftables
Requires: iproute2
Requires: net-tools
Requires: nfs-utils
Requires: wget
Requires: curl

Requires: smartmontools
Requires: system-report
Requires: ps_mem

Requires: inxi
Requires: lm_sensors3
Requires: hdparm
Requires: sdparm
Requires: htop

Requires: strace
%ifarch %ix86 x86_64
Requires: powertop
%endif
Requires: pciutils
Requires: usbutils
Requires: acpi
%ifarch x86_64 aarch64 loongarch64
Requires: dmidecode
%endif

%description system-base
Common base system dependencies.

%package desktop-base
Summary: Common base dependencies for Desktops
Group: Graphical desktop/Other

Requires: %name-system-base = %EVR
Requires: glibc-locales
Requires: fonts-ttf-core
Requires: pam-limits-desktop
Requires: polkit
Requires: udisks2
Requires: dvd+rw-tools
Requires: udev-rules-rfkill-uaccess
Requires: hunspell-en_US
Requires: hunspell-ru-lebedev
Requires: upower
Requires: powertop
Requires: xdg-user-dirs
Requires: mesa-dri-drivers
Requires: bluez

# desktop utils
Requires: mesa-info
Requires: mesa-gears
Requires: vulkan-tools
Requires: clinfo
Requires: wayland-utils
Requires: libinput-tools
Requires: edid-decode

# icons
Requires: menu-icons-default
Requires: gnome-icon-theme
Requires: gnome-icon-theme-symbolic

%ifarch %ix86 x86_64
Requires: blacklist-pcspkr
%endif

%description desktop-base
Common base dependencies for Desktops.

%package desktop-x11
Summary: Common base dependencies for Desktops with X11
Group: Graphical desktop/Other

Requires: %name-desktop-base = %EVR
Requires: xorg-server
Requires: xorg-server-control
Requires: xinit
Requires: xinitrc
# fallback
Requires: xdm
%ifarch %ix86 x86_64
Requires: xorg-drv-intel
%endif
Requires: xorg-drv-radeon
%ifnarch loongarch64 riscv64
Requires: xorg-drv-nouveau
%endif
%ifnarch %arm
Requires: xorg-drv-amdgpu
%endif
Requires: xorg-drv-libinput
Requires: xorg-drv-evdev
%ifarch %ix86 x86_64
#Requires: xorg-drv-mga
#Requires: xorg-drv-mach64
#Requires: xorg-drv-r128
#Requires: xorg-drv-ati
%endif
Requires: xauth
Requires: xorg-utils

%description desktop-x11
Common base dependencies for Desktops with X11.

%pre desktop-base
if [ $1 = 1 ]; then
	graphical_target=%systemd_unitdir/graphical.target
	default_target=%_sysconfdir/systemd/system/default.target
	if [ -f "$graphical_target" ]; then
		rm -f "$default_target"
		ln -s "$graphical_target" "$default_target"
	fi
	INITTAB=/etc/inittab
	if [ -f "$INITTAB" ]; then
		sed -i "s,^\(id:\)\(.*\)\(:initdefault.*\),\\15\\3," "$INITTAB"
	fi
fi

%files system-base
%files desktop-base
%files desktop-x11

%changelog
* Fri Mar 13 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt3
- Exclude ncdu on %%ix86 arches.

* Thu Aug 07 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0-alt2
- NMU: Drop xorg-drv-nouveau on loongarch64 (not supported)
  and riscv64 (not needed).

* Wed Aug 06 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build.
