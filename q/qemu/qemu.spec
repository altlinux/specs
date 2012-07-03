# vim: set ft=spec
# vim600: set fdm=marker:

# {{{ macros define
%def_enable binfmt_misc

%def_with alpha
%def_with arm
%def_without cris
%def_with x86
%def_with m68k
%def_without microblaze
%def_with mips
%def_with ppc
%def_without sh4
%def_with sparc
%def_with s390x
%def_with lm32
%def_with unicore32
%def_without xtensa

%def_disable werror
%def_enable sdl
%def_enable curses
%def_enable bluez
%def_enable vnc
%def_enable vnc_tls
%def_enable vnc_sasl
%def_enable vnc_jpeg
%def_enable vnc_png
%def_enable vde
%def_enable alsa
%def_disable esound
%def_enable pulseaudio
%def_enable oss
%def_enable aio
%def_enable blobs
%def_enable uuid
%def_enable smartcard
%def_enable smartcard_nss
%def_enable usb_redir
%def_disable opengl
%def_enable guest_agent
%def_enable spice
%def_enable libiscsi

%define audio_drv_list %{?_enable_oss:oss} %{?_enable_alsa:alsa} %{?_enable_sdl:sdl} %{?_enable_esound:esd} %{?_enable_pulseaudio:pa}
%define audio_card_list ac97 es1370 sb16 adlib cs4231a gus hda

%define _group vmusers
%define rulenum 90

%global target_list_system %nil
%global target_list_user %nil

%if_with alpha
%global target_list_user %target_list_user alpha-linux-user
%endif

%if_with arm
%global target_list_system %target_list_system arm-softmmu
%global target_list_user %target_list_user arm-linux-user armeb-linux-user
%endif

%if_with cris
%global target_list_system %target_list_system cris-softmmu
%global target_list_user %target_list_user cris-linux-user
%endif

%if_with x86
%global target_list_system %target_list_system i386-softmmu x86_64-softmmu
%global target_list_user %target_list_user i386-linux-user x86_64-linux-user
%endif

%if_with m68k
%global target_list_system %target_list_system m68k-softmmu
%global target_list_user %target_list_user m68k-linux-user
%endif

%if_with microblaze
%global target_list_system %target_list_system microblaze-softmmu microblazeel-softmmu
%global target_list_user %target_list_user microblaze-linux-user microblazeel-linux-user
%endif

%if_with mips
%global target_list_system %target_list_system mips-softmmu mipsel-softmmu mips64-softmmu mips64el-softmmu
%global target_list_user %target_list_user mips-linux-user mipsel-linux-user
%endif

%if_with ppc
%global target_list_system %target_list_system ppc-softmmu ppcemb-softmmu ppc64-softmmu
%global target_list_user %target_list_user ppc-linux-user ppc64-linux-user ppc64abi32-linux-user
%endif

%if_with sh4
%global target_list_system %target_list_system sh4-softmmu sh4eb-softmmu
%global target_list_user %target_list_user sh4-linux-user sh4eb-linux-user
%endif

%if_with sparc
%global target_list_system %target_list_system sparc-softmmu sparc64-softmmu
%global target_list_user %target_list_user sparc-linux-user sparc64-linux-user sparc32plus-linux-user
%endif

%if_with s390x
%global target_list_system %target_list_system s390x-softmmu
%global target_list_user %target_list_user s390x-linux-user
%endif

%if_with lm32
%global target_list_system %target_list_system lm32-softmmu
%endif

%if_with unicore32
%global target_list_user %target_list_user unicore32-linux-user
%endif

%if_with xtensa
%global target_list_system %target_list_system xtensa-softmmu xtensaeb-softmmu
%global target_list_user %target_list_user xtensaeb-linux-user
%endif
# }}}

Name: qemu
Version: 1.0.1
Release: alt2

Summary: QEMU CPU Emulator
License: GPL/LGPL/BSD
Group: Emulators
Requires: %name-system = %version-%release, %name-user = %version-%release

URL: http://www.nongnu.org/qemu/
Source0: %name-%version.tar
Source2: qemu-kvm.control.in
Source3: qemu-kvm.init
Source4: qemu-kvm.rules
Source5: qemu-kvm.sysconfig

Patch0: qemu-alt.patch

%set_verify_elf_method fhs=relaxed

BuildRequires: glibc-devel-static zlib-devel-static glib2-devel-static
BuildRequires: texinfo perl-podlators libcheck-devel libattr-devel
BuildRequires: zlib-devel libcurl-devel libpci-devel glibc-kernheaders
BuildRequires: ipxe-roms-qemu vgabios seabios
%{?_enable_sdl:BuildRequires: libSDL-devel libX11-devel }
%{?_enable_curses:BuildRequires: libncurses-devel}
%{?_enable_bluez:BuildRequires: libbluez-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_esound:BuildRequires: libesd-devel}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_vnc_tls:BuildRequires: libgnutls-devel}
%{?_enable_vnc_sasl:BuildRequires: libsasl2-devel}
%{?_enable_vnc_jpeg:BuildRequires: libjpeg-devel}
%{?_enable_vnc_png:BuildRequires: libpng-devel}
%{?_enable_vde:BuildRequires: libvde-devel}
%{?_enable_aio:BuildRequires: libaio-devel}
%{?_enable_spice:BuildRequires: libspice-server-devel >= 0.6.0 spice-protocol}
%{?_enable_uuid:BuildRequires: libuuid-devel}
%{?_enable_smartcard_nss:BuildRequires: libnss-devel >= 3.12.8}
%{?_enable_usb_redir:BuildRequires: libusbredir-devel}
%{?_enable_opengl:BuildRequires: libGL-devel libX11-devel}
%{?_enable_guest_agent:BuildRequires: glib2-devel python-base}
%{?_enable_libiscsi:BuildRequires: libiscsi-devel}

%description
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.  QEMU has two operating modes:

* Full system emulation.  In this mode, QEMU emulates a full system
  (for example a PC), including a processor and various peripherials.
  It can be used to launch different Operating Systems without rebooting
  the PC or to debug system code.

* User mode emulation.  In this mode, QEMU can launch Linux processes
  compiled for one CPU on another CPU.  It can be used to launch the
  Wine Windows API emulator or to ease cross-compilation and
  cross-debugging.

As QEMU requires no host kernel patches to run, it is very safe and easy
to use.

%package common
Summary: QEMU CPU Emulator - common files
Group: Emulators
BuildArch: noarch
Requires(pre): control >= 0.7.2
Requires(pre): shadow-utils sysvinit-utils
Requires: vgabios
Requires: seabios
Requires: ipxe-roms-qemu
Requires: %name-img = %version-%release

%description common
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.
This package contains common files for qemu.

%package system
Summary: QEMU CPU Emulator - full system emulation
Group: Emulators
Requires: %name-common = %version-%release

%description system
Full system emulation.  In this mode, QEMU emulates a full system
(for example a PC), including a processor and various peripherials.
It can be used to launch different Operating Systems without rebooting
the PC or to debug system code.

%package user
Summary: QEMU CPU Emulator - user mode emulation
Group: Emulators
Requires: %name-common = %version-%release

%description user
User mode emulation.  In this mode, QEMU can launch Linux processes
compiled for one CPU on another CPU.  It can be used to launch the
Wine Windows API emulator or to ease cross-compilation and
cross-debugging.

%package user-binfmt_misc
Summary: QEMU CPU Emulator - user mode emulation, binfmt_misc version
Group: Emulators
Requires: %name-common = %version-%release

%description user-binfmt_misc
User mode emulation.  In this mode, QEMU can launch Linux processes
compiled for one CPU on another CPU.  It can be used to launch the
Wine Windows API emulator or to ease cross-compilation and
cross-debugging.
This package contains static version with enabled binfmt_misc support.
Suitable for hasher.

%package  img
Summary: QEMU command line tool for manipulating disk images
Group: Emulators
Provides: qemu-kvm-img
Obsoletes: qemu-kvm-img < %version-%release

%description img
This package provides a command line tool for manipulating disk images

%package doc
Summary: User documentation for %name
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description doc
User documentation for %name

%prep
%setup -q
%patch0 -p1
cp -f %SOURCE2 qemu-kvm.control.in

%build
export CFLAGS="%optflags"
%if_enabled binfmt_misc
# non-GNU configure
./configure \
	--target-list='%target_list_user' \
	--prefix=%_prefix \
	--static \
	--disable-debug-tcg \
	--disable-sparse \
	--disable-strip \
	--disable-system \
	--disable-check-utests \
	--enable-nptl \
	--enable-guest-base \
	--disable-smartcard \
	--disable-smartcard-nss \
	--disable-usb-redir \
	--disable-linux-aio
%make_build
find -regex '.*linux-user/qemu.*' -perm 755 -exec mv '{}' '{}'.static ';'
%make_build clean
%endif

# non-GNU configure
./configure \
	--target-list='%target_list_system %target_list_user' \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--extra-cflags="%optflags" \
	%{subst_enable werror} \
	%{?_disable_sdl:--disable-sdl} \
	%{?_disable_curses:--disable-curses} \
	%{subst_enable bluez} \
	%{subst_enable vnc} \
	%{?_disable_vnc_tls:--disable-vnc-tls} \
	%{?_disable_vnc_sasl:--disable-vnc-sasl} \
	%{?_disable_vnc_jpeg:--disable-vnc-jpeg} \
	%{?_disable_vnc_png:--disable-vnc-png} \
	%{?_disable_vde:--disable-vde} \
	%{?_disable_aio:--disable-linux-aio} \
	%{?_disable_blobs: --disable-blobs} \
	%{?_disable_spice:--disable-spice} \
	%{?_disable_uuid:--disable-uuid} \
	--disable-debug-tcg \
	--disable-sparse \
	--disable-strip \
	--audio-drv-list="%audio_drv_list" \
	--audio-card-list="%audio_card_list" \
	--enable-mixemu \
	--disable-xen \
	--disable-brlapi \
	--enable-curl \
	--disable-fdt \
	--enable-check-utests \
	--enable-kvm \
	--enable-nptl \
	%{subst_enable smartcard} \
	%{?_enable_smartcard_nss:--enable-smartcard-nss} \
	%{?_enable_usb_redir:--enable-usb-redir} \
	%{subst_enable opengl} \
	%{?_disable_guest_agent:--disable-guest-agent} \
	--enable-guest-base \
	--enable-pie

%make_build

sed -i 's/@GROUP@/%_group/g' qemu-kvm.control.in

%install
%make_install install DESTDIR=%buildroot

mv %buildroot%_defaultdocdir/qemu %buildroot%_defaultdocdir/%name-%version
install -m644 TODO Changelog %buildroot%_defaultdocdir/%name-%version

%if_enabled binfmt_misc
find -regex '.*linux-user/qemu.*\.static' -exec install -m755 '{}' %buildroot%_bindir ';'
%endif

mv %buildroot%_bindir/qemu-system-x86_64 %buildroot%_bindir/qemu-std-system-x86_64
ln -s %_bindir/qemu-std-system-x86_64 %buildroot%_bindir/qemu

rm -f %buildroot%_bindir/check-*
rm -f %buildroot%_sysconfdir/udev/rules.d/*

install -D -m 0755 %SOURCE3 %buildroot%_initdir/%name-kvm
install -D -m 0644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name-kvm
install -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/udev/rules.d/%rulenum-%name-kvm.rules
install -D -m 0755 %name-kvm.control.in %buildroot%_controldir/kvm

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%name.conf
%endif


#rm -f %buildroot%_datadir/*/openbios*
rm -f %buildroot%_datadir/%name/pxe*rom
rm -f %buildroot%_datadir/%name/vgabios*bin
rm -f %buildroot%_datadir/%name/bios.bin
#rm -f %buildroot%_datadir/%name/petalogix-s3adsp1800.dtb
#rm -f %buildroot%_datadir/%name/video.x
#rm -f %buildroot%_datadir/%name/bamboo.dtb
#rm -f %buildroot%_datadir/%name/ppc_rom.bin

# the pxe ipxe images will be symlinks to the images on
# /usr/share/ipxe, as QEMU doesn't know how to look
# for other paths, yet.
pxe_link() {
  ln -s ../../..%_libexecdir/ipxe/$2.rom %buildroot%_datadir/%name/pxe-$1.rom
}

pxe_link rtl8139 rtl8139
pxe_link e1000 e1000_82540
pxe_link virtio virtio-net
pxe_link pcnet pcnet32
pxe_link ne2k_isa ne2k_isa
pxe_link ne2k_pci ns8390
pxe_link eepro100 eepro100

ln -s ../vgabios/VGABIOS-lgpl-latest.bin  %buildroot%_datadir/%name/vgabios.bin
ln -s ../vgabios/VGABIOS-lgpl-latest.cirrus.bin %buildroot%_datadir/%name/vgabios-cirrus.bin
ln -s ../vgabios/VGABIOS-lgpl-latest.qxl.bin %buildroot%_datadir/%name/vgabios-qxl.bin
ln -s ../vgabios/VGABIOS-lgpl-latest.stdvga.bin %buildroot%_datadir/%name/vgabios-stdvga.bin
ln -s ../vgabios/VGABIOS-lgpl-latest.vmware.bin %buildroot%_datadir/%name/vgabios-vmware.bin
ln -s ../../..%_libexecdir/seabios/bios.bin %buildroot%_datadir/%name/bios.bin

cd %buildroot
# Add alternatives for qemu-kvm
mkdir -p ./%_altdir
printf '%_bindir/qemu-system-x86_64\t%_bindir/qemu-std-system-x86_64\t50\n' >./%_altdir/qemu

%check
./check-qdict
./check-qfloat
./check-qint
# disable check-qjson:
#IMPORTANT: The test for "\/" is failing, don't know why.
#Signed-off-by: Luiz Capitulino <lcapitulino@redhat.com>
#./check-qjson
./check-qlist
./check-qstring

%pre common
%_sbindir/groupadd -r -f %_group
if [ -f %_controldir/qemu-kvm ];then
%pre_control qemu-kvm
mv -f /var/run/control/qemu-kvm /var/run/control/kvm
else
%pre_control kvm
fi

%post common
%post_control -s vmusers kvm
%post_service %name-kvm

%preun common
%preun_service %name-kvm

%files

%files common
%_datadir/qemu
%_man1dir/qemu*
%_man8dir/qemu*
%_sysconfdir/udev/rules.d/*
%_initdir/%name-kvm
%config(noreplace) %_sysconfdir/sysconfig/*
%_controldir/*
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%name.conf
%endif
%_sysconfdir/%name

%files system
%_altdir/qemu
%_bindir/qemu
%_bindir/qemu*system*

%files user
%_bindir/qemu-*
%exclude %_bindir/qemu*system*
%if_enabled binfmt_misc
%exclude %_bindir/qemu-*.static
%endif
%exclude %_bindir/qemu-img
%exclude %_bindir/qemu-io
%exclude %_bindir/qemu-nbd
%exclude %_bindir/qemu-ga

%if_enabled binfmt_misc
%files user-binfmt_misc
%_bindir/qemu-*.static
%endif

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_bindir/qemu-ga

%files doc
%_defaultdocdir/%name-%version

%changelog
* Mon Mar 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.1-alt2
- change arm defaults to convenient values

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1
- enable libiscsi support

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0
- add usb-redir support
- enable spice for i686
- enable compile alpha

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1
- 0.15.0
- disable compile alpha
- enable compile s390x, lm32, unicore32
- enable smartcard support
- enable compile guest agent

* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt4
- enable pulseaudio support

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt3
- enable SDL support
- disable pulseaudio support

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt2
- add udev rules,control rules, init script for load kvm kernel module (import from qemu-kvm package)
- drop alternatives for qemu-img
- add doc subpackage
- move man and locales to common subpackage
- use roms and bioses from another packages: vgabios,seabios,gpxe-roms-qemu
- disable SDL support

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0 release

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt0.rc0
- 0.14.0-rc0

* Wed Jan 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.13.50-alt1
- snapshot 5677903453
- add alternatives for qemu-system-%ix86
- add img subpackage, add alternatives for qemu-img and other
- cleanup attr
- add spice support for x86_64 only
- add libalsa-devel to buildreq for alsa support
- add vnc-jpeg and vnc-png support
- add adlib and hda soundcards
- build without esound support
- add libpci-devel to buildreq
- fix bluez buildreq
- drop non devel library from buildreq
- install config for sasl
- fix install /etc/qemu/*.conf
- qemu-common package as noarch

* Thu Jan 14 2010 Kirill A. Shutemov <kas@altlinux.org> 0.12.1-alt1
- v0.12.1-31-g49a3aaa
- Fix NULL pointer dereference on handling -chardev socket

* Mon Dec 14 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.92-alt1
- v0.12.0-rc2-3-g910628f
- UUID support enabled

* Sat Sep 19 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt6
- Fix building binfmt_misc binaries

* Sat Sep 19 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt5
- v0.11.0-rc0-867-gdbf9580
- Do not set uname for linux-user targets
- Use %%check section for tests

* Tue Sep 08 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt4
- v0.11.0-rc0-799-g2637c75
- Compile alpha, m68k, mips and sparc support by default
- Enable Linux AIO
- Enalbe unit tests
- Review configure options
- Update URL
- Update PIE patches

* Tue Sep 01 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt3
- Disable IO thread to fix KVM support

* Tue Sep 01 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt2
- fix building on x86_64

* Fri Aug 21 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt1
- updated to v0.11.0-rc0-564-g757506d
  + no KQEMU support any more
  + fixes CVE-2008-0928 (ALT #20010)
  + keyboard works fine without -k (ALT #15774)
  + framebuffer works fine with -kernel (ALT #11324)
- build linux-user targets as PIE and drop link hack
- enable KVM support
- enable curl support
- enable IO thread
- enable VNC SASL support
- enable bluez support

* Thu Feb 19 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt11
- svn 20090219
- add hack to implement CLONE_CHILD_CLEARTID
- enable more audio drivers and cards
- enable curses support
- enable vde support
- enable VNC TLS support

* Sun Dec 14 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt10
- svn 20081214
  + no need in gcc3 any more
- fixes for mmap() related code

* Mon Oct 13 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt9
- svn 20081013
- fix mmap(), mremap() and shmat() syscalls on 64-bit host with
  32-bit targets

* Fri Oct 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt8
- rename binaries in package qemu-user-binfmt_misc back to *.static
  to make them compatible with hasher

* Fri Oct 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt7
- svn 20081010
  + some changes merged to upstream
- enable/disable binfmt_misc support at compile time
- fix and cleanup system v ipc syscalls
- fix getdents* syscalls
- fix fstatat64()/newfstatat() syscalls
- implement readahead() syscall
- revert some legacy changes

* Sun Sep 14 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt6
- Fix building with glibc-kernheaders-2.6.27-alt1

* Mon Sep 08 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt5
- svn 20080908
- Implement futimesat() syscall
- binfmt-misc-friendly:
  + Use auxv to find out binary file descriptor
- ioctl:
  + Implement ioctls MTIOCTOP, MTIOCGET and MTIOCPOS

* Sun Aug 31 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt4
- 0.9.1 + svn 20080831
- Add option -binfmt-misc-friendly to user emulators

* Fri Aug 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt3
- fix building on i586
- implement fstatat64() syscall

* Sat Aug 23 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt2
- 0.9.1 + svn 20080829
  + CVE-2008-2004
  + Brand new "Tiny Code Generator" by Fabrice Bellard
  + A lot of changes
- Review all changes and patches cleanup
- fix vfork(2) implementation
- Build only x86, arm and ppc architectures by default

* Tue Jan 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt1.cvs20080127
- 0.9.1 + cvs 20080127
- fix-syscalls--iovec
  + do not stop iovec conversion on iov_base == NULL if iov_len is 0
- fix-signals
  + do not show message on uncaught target signal

* Sun Nov 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071124-alt15
- cvs 20071124
- fix-syscalls--getgroups:
  + getgroups: return total number of supplementary group IDs for the
    process if size == 0

* Sat Nov 24 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071123-alt14
- cvs 20071123
- fix-cpu-copy:
  + Handle cpu_model in copy_cpu()

* Mon Nov 19 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071119-alt13
- cvs 20071119
- Branch based git repo
- Fix execve syscall
- Build all targets
- adlib: include missed header
- Cleanup configure options
- Drop obsoleted/unsupported patches:
  + qemu-0.6.2-alt-hdtrans.patch
  + qemu-0.7.0-sigaltstackhack.patch
  + qemu-0.9.0-alt-alpha_syscall_nr.patch
  + qemu-0.9.0-alt-arm_syscall_nr.patch
  + qemu-0.9.0-alt-i386_syscall_nr.patch
  + qemu-0.9.0-alt-m68k_syscall_nr.patch
  + qemu-0.9.0-alt-ppc64_syscall_nr.patch
  + qemu-0.9.0-alt-ppc_syscall_nr.patch
  + qemu-0.9.0-alt-qvm86.patch
  + qemu-0.9.0-alt-sh4_syscall_nr.patch
  + qemu-0.9.0-alt-sparc64_syscall_nr.patch
  + qemu-0.9.0-alt-sparc_syscall_nr.patch
  + qemu-0.9.0-alt-syscall_cleanup.patch
  + qemu-0.9.0-disk-scsi.patch
  + qemu-0.9.0-vmware_vga-fix.patch

* Thu Oct 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070917-alt12
- cvs 20070917
- Added qemu-0.9.0-alt-shm.patch
  + Add shm* syscalls
- Sync patches with new version
- Update qemu-0.9.0-security.patch
  + part of fix is in the upsteam
- qemu-0.9.0-alt-alpha_syscall_nr.patch, qemu-0.9.0-alt-ppc64_syscall_nr.patch
  + sync syscall numbers with kernel
- Drop qemu-0.9.0-alt-statfs.patch
  + fixed in upstream

* Fri Aug 24 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070607-alt11
- qemu-arm: uname -m => armv4l/armv4b
- fix path(): return NULL if NULL passed

* Fri Jun 08 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070607-alt10
- cvs 20070607
- qemu-0.8.2-nptl.patch -> qemu-0.9.0-nptl.patch, qemu-0.9.0-disk-scsi.patch:
  + rejection fix
- Drop qemu-0.9.0-alt-mips_syscall_nr.patch
  + in the upstream now
- Update qemu-0.9.0-alt-sem.patch and qemu-0.9.0-alt-sem.patch
  + part of this patches is in the upstream now

* Mon May 21 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070420-alt9
- Added qemu-0.9.0-alt-getgroups.patch
  + trivial fix
- Moved qemu-0.9.0-sem.patch -> qemu-0.9.0-alt-sem.patch:
  + Fix do_semctl
  + Added standalone syscalls semget, semop, semctl
- Moved qemu-0.9.0-msgop.patch -> qemu-0.9.0-alt-sem.patch
  + Added standalone syscalls msg*
- Dropped qemu-0.9.0-efault.patch

* Tue Apr 03 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070420-alt8
- cvs 20070420
- Added qemu-0.9.0-security.patch:
  + CVE-2007-1320, CVE-2007-1321, CVE-2007-1322, CVE-2007-1323, CVE-2007-1366
- Added qemu-0.9.0-sb16-fix.patch:
  + Fix infinite loop in the SB16 driver
- Disable building alpha emulation due build error
- Update qemu-0.8.2-nptl.patch
  + Fix cpu_env list corruption by disabling CLONE_VM when doing CLONE_VFORK. 
    This is a hack to avoid segfault on vfork.
- Added qemu-0.9.0-nptl-update.patch:
  + implemented/fixed several nptl-related syscalls
  + Fix build on i586
- Added qemu-0.9.0-vmware_vga-fix.patch:
  + Disable -vmwarevga acceleration code for now (missing range checks)
- Fix bug #11363
  + rename qemu to qemu-system-i386
  + add symlink qemu to qemu-system-%%_target_os
- Added qemu-0.8.2-deb-tls-ld.patch
  + Fix segfault of user mode qemu on ix86
- Updated qemu-0.9.0-alt-path.patch
  + content of emulation dir can change
  + some refactoring
- Added qemu-0.9.0-alt-arm-eabi-pread-pwrite.patch:
  + pread and pwrite syscall fix for ARM EABI guest
- Added qemu-0.9.0-alt-statfs.patch
  + fix statfs syscall bug
- Updated qemu-0.9.0-alt-i386-user-fix.patch
  + fix qemu-i386 on x86 host
- Update qemu-0.8.2-alt-qvm86.patch -> qemu-0.9.0-alt-qvm86.patch:
  + rejection fexed
- Updated qemu-0.9.0-disk-scsi.patch
  + rejection fixed
- Update qemu-0.9.0-alt-syscall_cleanup.patch:
  + rejection fixed

* Sun Mar 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070324-alt7
- cvs 20070324
- Sync syscall numbers with linux-2.6.21-rc4
- Update linux-user/syscall.c:
  + build fix
  + cleaup
- Dropped Debian's patches
- Added qemu-0.9.0-alt-i386-user-fix.patch:
  + fix SIGSEGV in qemu-i386 (by Sergey Vlasov aka vsu@)
- Added qemu-0.9.0-efault.patch:
  + fix returning EFAULT from syscalls
- Added qemu-0.9.0-msgop.patch:
  + fix msg* syscalls
- Added qemu-0.9.0-sem.patch:
  + fix sem* syscalls
- Dropped qemu-0.9.0-alt-fcntl64-fix.patch:
  + in upstream now

* Tue Mar 20 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070320-alt6
- cvs 20070320
- Dropped 43_arm_cpustate.patch,
  qemu-0.9.0-alt-syscall-getsockname-fix.patch,
  qemu-0.9.0-alt-syscalls-clock.patch,
  qemu-0.9.0-alt-syscalls-recv-and-recvfrom-fix.patch:
  + fixed in upstream now
- Updated qemu-0.9.0-alt-makefile.patch, qemu-0.9.0-disk-scsi.patch:
  + fix rejections
- Updated qemu-0.9.0-alt-fcntl64-fix.patch:
  + pass host flag to fcntl instead target flag
- Renamed qemu-0.8.2-alt-path.patch -> qemu-0.9.0-alt-path.patch
- Updated qemu-0.9.0-alt-path.patch:
  + fix memory leak by caching
- Spec cleap

* Fri Mar 09 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070304-alt5
- fix fcntl64 syscal: used TARGET_F_*64 instead F_*64
- cdrom name fixed
- option -disk scsi,type=cdrom fixed (bug #11010)

* Sun Mar 04 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070304-alt4
- cvs snapshot
- fix order of ide devices(bug #11004)
- drop mdk patches
- user gcc 3.4 for building(bug #11006)
- fix sigfault
- spec cleanup

* Thu Mar 01 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt3
- cdrom option fixed(bug #10971)
- syscall clock_gettime rewritten
- syscall clock_getres added
- syscalls getsockname, recv and recvfrom fixed

* Wed Feb 28 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt2
- scsi disk support added

* Thu Feb 15 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt1
- lock_user_string used for mount syscall

* Wed Feb 07 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.3
- requires fixed
- docs is in package qemu-common now
- description and summary fixed
- alsa enabled
- spec cleanup

* Wed Feb 07 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.2
- mandriva patches updated
- fix realpath() crash again (by vsu@)

* Tue Feb 06 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.1
- 0.9.0
- separate into four packages: qemu, softmmu, user, user-static
- spec cleanup
- patches updated

* Mon Feb 05 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.8.2-alt1.2
- fix crash with -fstack-protector due to wrong realpath() usage
- patches reorganized, debian patches added
- qemu-0.8.2-alt-path.patch fixed
- qemu-arm: uname -m => armv5l/armv5b
- qemu-0.8.2-alt-mmap.patch added
- support msg* and sem* syscalls
- name for static version: qemu-<arch>.static

* Thu Dec 14 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.2-alt1.1
- build static version of qemu-arm
- patches for qemu-arm and other linux mode emulators

* Wed Aug 23 2006 Alexey Tourbin <at@altlinux.ru> 0.8.2-alt1
- 0.8.0 -> 0.8.2
- sync madriva patches 0.8.2-1mdv2007.0
- removed kernel-source-kqemu from here, which should be packaged
  separately because of its non-free status
- added support for /dev/qvm86

* Wed Dec 21 2005 Kachalov Anton <mouse@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Sep 20 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.2-alt1
- 0.7.2
- Updated Kqemu to 0.7.2

* Thu Aug 04 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.1-alt1
- 0.7.1
- Updated:
  * Kqemu to 0.7.1-1
  * GTK support

* Thu Jun 23 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt2
- Added:
  * GTK support (-use-gtk option)
  * Distribution permission from Fabrice Bellard to Kqemu

* Fri Apr 29 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt1
- 0.7.0
- Kqemu support

* Mon Nov 29 2004 Kachalov Anton <mouse@altlinux.ru> 0.6.2-alt1
- Snapshot of 23-28 Nov 2004
- LARGE disk fix (actual for NT4, win2k, winXP)

* Fri Nov 26 2004 Kachalov Anton <mouse@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sun Oct 17 2004 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt1
- initial revision
