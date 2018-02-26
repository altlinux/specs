%define _unpackaged_files_terminate_build 1
%def_disable werror
%def_enable sdl
%def_enable curses
%def_enable bluez
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
%def_disable guest_agent
%def_enable spice
%def_enable libiscsi

%define audio_drv_list %{?_enable_oss:oss} %{?_enable_alsa:alsa} %{?_enable_sdl:sdl} %{?_enable_esound:esd} %{?_enable_pulseaudio:pa}
%define audio_card_list ac97 es1370 sb16 adlib cs4231a gus hda

Name: qemu-kvm
Version: 1.0.1
Release: alt1
Summary: Kernel Virtual Machine virtualization environment
Group: Emulators
License: %gpl2plus
URL: http://www.linux-kvm.org
Source0: %name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveArch: %ix86 x86_64
Requires: qemu-common
Requires: qemu-img
Provides: kvm
Obsoletes: kvm

BuildRequires(pre): rpm-build-licenses
BuildRequires: zlib-devel libcurl-devel libpci-devel libcheck-devel libattr-devel glibc-kernheaders
%{?_enable_sdl:BuildRequires: libSDL-devel libX11-devel}
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
The Kernel Virtual Machine provides a virtualization enviroment for
processors with hardware support for virtualization: Intel's VT and
AMD's AMD-V.

%prep
%setup -q
%patch -p1

%build
export CFLAGS="%optflags"
./configure \
    --prefix=%_prefix \
    --sysconfdir=%_sysconfdir \
    --libdir=%_libdir \
    --extra-cflags="%optflags" \
    --disable-docs \
    %{subst_enable werror} \
    %{?_disable_sdl:--disable-sdl} \
    %{?_disable_curses:--disable-curses} \
    %{?_disable_bluez:--disable-bluez} \
    %{?_disable_vnc_tls:--disable-vnc-tls} \
    %{?_disable_vnc_sasl:--disable-vnc-sasl} \
    %{?_disable_vnc_jpeg:--disable-vnc-jpeg} \
    %{?_disable_vnc_png:--disable-vnc-png} \
    %{?_disable_vde:--disable-vde} \
    %{?_disable_aio:--disable-linux-aio} \
    %{?_disable_blobs: --disable-blobs} \
    %{?_disable_spice:--disable-spice} \
    %{?_disable_uuid:--disable-uuid} \
    %{subst_enable smartcard} \
    %{?_enable_smartcard_nss:--enable-smartcard-nss} \
    %{?_enable_usb_redir:--enable-usb-redir} \
    %{?_disable_guest_agent:--disable-guest-agent} \
    --audio-drv-list="%audio_drv_list" \
    --audio-card-list="%audio_card_list" \
    --enable-mixemu
#

%make_build
#vgabios extboot user libfdt

%install
%make_install DESTDIR=%buildroot initdir=%_initdir install

mv %buildroot%_bindir/qemu-system-x86_64 %buildroot%_bindir/qemu-kvm-system-x86_64
ln -s %_bindir/qemu-kvm-system-x86_64 %buildroot%_bindir/qemu-kvm
ln -s %_bindir/qemu-kvm %buildroot%_bindir/kvm

#install -m 0755 %name %buildroot%_bindir/

# save kvm roms
cp -p %buildroot%_datadir/qemu/vapic.bin %buildroot/

# cleanup - use from qemu-common and qemu-img packages
rm -rf %buildroot%_datadir/qemu/* %buildroot%_sysconfdir
rm -f %buildroot%_bindir/qemu-{img,io,nbd}

# move back kvm roms
mv %buildroot/vapic.bin %buildroot%_datadir/qemu/

cd %buildroot
# Add alternatives for qemu-kvm
mkdir -p ./%_altdir
printf '%_bindir/qemu-system-x86_64\t%_bindir/qemu-kvm-system-x86_64\t100\n' >./%_altdir/qemu-kvm

%files
%_altdir/qemu-kvm
%_bindir/qemu-kvm
%_bindir/kvm
%_bindir/qemu-kvm-system-*
%_datadir/qemu/*.bin

%changelog
* Wed Apr 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1
- enable libiscsi support

* Tue Dec 06 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.93-alt1
- 1.0-rc3
- add usb-redir support
- enable spice for i386

* Tue Aug 23 2011 Anton Farygin <rider@altlinux.ru> 0.15.0-alt2
- add host cpu to -cpu ? list

* Fri Aug 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1
- 0.15.0
- enable smartcard support

* Thu Jun 09 2011 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- new version

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt3
- enable pulseaudio support
- don't rm {extboot,vapic}.bin

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt2
- enable SDL support
- disable pulseaudio support

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- move udev rules,control rules, init script for load kvm kernel module to qemu-common package
- move vde subpackage to vde2
- use qemu-img package from qemu (and drop qemu-img alternatives)
- disable SDL support

* Thu Feb 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt0.rc1
- 0.14.0-rc1

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt0.rc0
- 0.14.0-rc0

* Wed Jan 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.13.5-alt7
- new snapshot from upstream
- enable spice support for x86_64 only
- enable vnc-sasl support
- enable vnc-jpeg and vnc-png support
- disable esd support
- add subpackage img
- add alternatives for qemu-img, qemu-io, qemu-system-*, qemu-nbd
- enable uuid support
- use roms and bioses from another packages: vgabios,seabios,gpxe-roms-qemu
- fix bluez support
- qemu-kvm-vde package as noarch

* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 0.13.5-alt6
- new snapshot from upstream

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 0.13.5-alt5
- new snapshot from upstream

* Fri Oct 01 2010 Anton Farygin <rider@altlinux.ru> 0.13.5-alt4
- new snapshot from upstream

* Wed Sep 15 2010 Anton Farygin <rider@altlinux.ru> 0.13.5-alt3
- update from upstream "next" branch

* Tue Aug 31 2010 Anton Farygin <rider@altlinux.ru> 0.13.5-alt2
- update from upstream "next" branch

* Wed Aug 25 2010 Anton Farygin <rider@altlinux.ru> 0.13.5-alt1
- build experimental version from upstream "next" branch

* Fri Aug 13 2010 Anton Farygin <rider@altlinux.ru> 0.12.5-alt1
- new version

* Sun Jul 04 2010 Anton Farygin <rider@altlinux.ru> 0.12.4-alt1
- new version

* Mon Apr 19 2010 Anton Farygin <rider@altlinux.ru> 0.12.3-alt2
- merge with upstream stable-0.12 branch

* Sun Mar 21 2010 Anton Farygin <rider@altlinux.ru> 0.12.3-alt1
- new version

* Thu Jan 21 2010 Anton Farygin <rider@altlinux.ru> 0.12.2-alt1
- new version

* Tue Dec 29 2009 Anton Farygin <rider@altlinux.ru> 0.12.1.1-alt1
- new version
- build kernel-source-kvm from separated package

* Wed Dec 23 2009 Anton Farygin <rider@altlinux.ru> 0.11.1-alt6
- control facility qemu-kvm renamed back to kvm
- fixed default control settigns (fixes #22406)
- use vmusers instead of kvm for group settings in control facility

* Tue Dec 08 2009 Anton Farygin <rider@altlinux.ru> 0.11.1-alt5
- new version

* Sat Nov 28 2009 Anton Farygin <rider@altlinux.ru> 0.11.0-alt4
- default control mode fixed (altbug #22406)

* Wed Nov 25 2009 Anton Farygin <rider@altlinux.ru> 0.11.0-alt3
- build with libcurl

* Tue Nov 24 2009 Dmitry V. Levin <ldv@altlinux.org> 0.11.0-alt2
- Reverted accidental rename kernel-source-kvm -> kernel-source-qemu-kvm
  made in previous package release.
- Updated build requirements.

* Mon Nov 09 2009 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- new version
- package renamed to qemu-kvm

* Mon Nov 02 2009 Anton Farygin <rider@altlinux.ru> 88-alt1
- new version

* Wed Jun 10 2009 Michail Yakushin <silicium@altlinux.ru> 85-alt3
- add option boot=[on|off] to kvm help.

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 85-alt2
- move  {post,preun}_service kvm_vde to kvm-vde subpackage

* Tue Apr 21 2009 Michail Yakushin <silicium@altlinux.ru> 85-alt1
- kvm-85

* Tue Apr 14 2009 Michail Yakushin <silicium@altlinux.ru> 84-alt5
- improved kvm_vde scripts
- move kvm-vde fetures to separated packages

* Wed Apr 08 2009 Michail Yakushin <silicium@altlinux.ru> 84-alt4
- add VDE support
- set RAM to 512 by default

* Tue Mar 24 2009 Michail Yakushin <silicium@altlinux.ru> 84-alt3
- fix evdev keyboard support
- remove junk udev rule
- add check option to initscript
- rename group kvm to vmusers

* Thu Mar 19 2009 Michail Yakushin <silicium@altlinux.ru> 84-alt2
- Build form upstream git

* Tue Mar 10 2009 Michail Yakushin <silicium@altlinux.ru> 84-alt1
- 84

* Sat Jan 24 2009 Led <led@altlinux.ru> 83-alt1
- 83

* Wed Jan 07 2009 Led <led@altlinux.ru> 82-alt1
- 82

* Sun Dec 21 2008 Led <led@altlinux.ru> 81-alt1
- 81

* Sun Dec 14 2008 Led <led@altlinux.ru> 80-alt1
- 80

* Wed Nov 26 2008 Led <led@altlinux.ru> 79-alt2
- Added control(8) support to control /dev/kvm permissions
- Added initscript

* Tue Nov 25 2008 Led <led@altlinux.ru> 79-alt1
- 79

* Tue Nov 25 2008 Led <led@altlinux.ru> 78-alt2
- fixed kernel-source-%name

* Thu Nov 06 2008 Led <led@altlinux.ru> 78-alt1
- 78

* Mon Sep 29 2008 Led <led@altlinux.ru> 76-alt1
- 76
- updated qemu-flags.patch

* Sun Sep 14 2008 Led <led@altlinux.ru> 75-alt1
- 75

* Fri Aug 29 2008 Led <led@altlinux.ru> 74-alt1
- 74

* Fri Aug 29 2008 Led <led@altlinux.ru> 73-alt1
- 73
- added %name-73-alt-eventfd.patch

* Sun Jul 20 2008 Led <led@altlinux.ru> 71-alt1
- 71

* Mon May 19 2008 Led <led@altlinux.ru> 69-alt1
- 69

* Mon May 05 2008 Led <led@altlinux.ru> 68-alt1
- 68

* Thu Apr 17 2008 Led <led@altlinux.ru> 66-alt1
- 66

* Tue Apr 08 2008 Led <led@altlinux.ru> 65-alt1
- 65

* Thu Mar 27 2008 Led <led@altlinux.ru> 64-alt1
- 64

* Mon Mar 17 2008 Led <led@altlinux.ru> 63-alt1
- 63

* Wed Feb 27 2008 Led <led@altlinux.ru> 62-alt1
- 62:
  + fixed vulnerability (SA29129)

* Sat Feb 23 2008 Led <led@altlinux.ru> 61-alt1
- 61:
  + AC97 emulation
  + Adlib emulation
  + Gravis Ultrasound emulation
  + EsounD audio driver
- fixed Kbuild
- added qemu-flags.patch

* Mon Feb 11 2008 Led <led@altlinux.ru> 60-alt0.2
- fixed spec

* Sun Feb 10 2008 Led <led@altlinux.ru> 60-alt0.1
- initial build
