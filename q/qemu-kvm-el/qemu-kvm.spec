%define _unpackaged_files_terminate_build 1
%def_disable werror
%def_enable sdl
%def_enable curses
%def_enable bluez
%def_enable vnc_tls
%def_enable alsa
%def_enable esound
%def_enable pulseaudio
%def_enable aio
%def_enable blobs
%def_enable spice

%define audio_drv_list oss %{?_enable_alsa:alsa} %{?_enable_sdl:sdl} %{?_enable_esound:esd} %{?_enable_pulseaudio:pa}
%define audio_card_list ac97 adlib cs4231a gus

%define _group vmusers
%define rulenum 90
Name: qemu-kvm-el
Version: 0.12.1.2
Release: alt13
Summary: Kernel Virtual Machine virtualization environment
Group: Emulators
License: %gpl2plus
URL: http://www.linux-kvm.org
Source0: %name-%version.tar
ExclusiveArch: x86_64
Requires(pre): control >= 0.7.2
Requires(pre): shadow-utils sysvinit-utils
Provides: kvm
Obsoletes: kvm
Conflicts: qemu-kvm qemu-common

BuildRequires(pre): rpm-build-licenses
BuildRequires: libX11-devel zlib-devel libcurl-devel libaio-devel libuuid-devel perl-podlators tetex-core libpci-devel vgabios seabios
%{?_enable_sdl:BuildRequires: libSDL-devel}
%{?_enable_curses:BuildRequires: libncurses-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_esound:BuildRequires: libesd-devel}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_vnc_tls:BuildRequires: libgnutls-devel}
%{?_enable_spice:BuildRequires: libspice-server-devel spice-protocol}

%description
The Kernel Virtual Machine provides a virtualization enviroment for
processors with hardware support for virtualization: Intel's VT and
AMD's AMD-V.

%package -n qemu-img-el
Summary: QEMU command line tool for manipulating disk images
Group: Development/Tools
Conflicts: qemu-img

%description -n qemu-img-el
This package provides a command line tool for manipulating disk images

%prep
%setup -q
sed -i 's|#define SHARE_SUFFIX "/share/qemu"|#define SHARE_SUFFIX "/share/qemu-kvm-el"|' vl.c
sed -i 's|datasuffix="/share/qemu"|datasuffix="/share/qemu-kvm-el"|' configure
sed -i 's|docsuffix="/share/doc/qemu"|docsuffix="/share/doc/qemu-kvm-el"|' configure

%build
export CFLAGS="%optflags"
./configure \
    --prefix=%_prefix \
    --sysconfdir=%_sysconfdir \
    --cpuconfdir=%_sysconfdir/%name \
    --extra-cflags="%optflags" \
    --disable-docs \
    %{subst_enable werror} \
    %{subst_enable spice} \
    %{?_disable_sdl:--disable-sdl} \
    %{?_disable_curses:--disable-curses} \
    %{?_disable_bluez:--disable-bluez} \
    %{?_disable_vnc_tls:--disable-vnc-tls} \
    %{?_disable_aio: --disable-aio} \
    %{?_disable_blobs: --disable-blobs} \
    --audio-drv-list="%audio_drv_list" \
    --audio-card-list="%audio_card_list" \
    --enable-mixemu \
    --enable-docs
#

%make_build
#vgabios extboot user libfdt
sed -i 's/@GROUP@/%_group/g' %name.control.in

%install
%makeinstall_std initdir=%_initdir

rm -f %buildroot%_datadir/*/openbios*
rm -f %buildroot%_datadir/*/vgabios*
rm -f %buildroot%_datadir/*/bios.bin

rm -f %buildroot%_bindir/kvm

mv %buildroot%_bindir/qemu-system-x86_64 %buildroot%_bindir/kvm
mv %buildroot%_man1dir/qemu-kvm.1 %buildroot%_man1dir/kvm.1

rm -f %buildroot%_bindir/qemu-nbd
rm -f %buildroot%_man8dir/qemu-nbd.*

rm -f %buildroot%_sysconfdir/udev/rules.d/*

#install -m 0755 %name %buildroot%_bindir/
install -D -m 0755 %name.init %buildroot%_initdir/%name
install -D -m 0644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -D -m 0644 %name.rules %buildroot%_sysconfdir/udev/rules.d/%rulenum-%name.rules
install -D -m 0755 %name.control.in %buildroot%_controldir/kvm

ln -s /usr/share/vgabios/VGABIOS-lgpl-latest.bin  %buildroot/%_datadir/%name/vgabios.bin
ln -s /usr/share/vgabios/VGABIOS-lgpl-latest.cirrus.bin %buildroot/%_datadir/%name/vgabios-cirrus.bin
ln -s /usr/share/vgabios/VGABIOS-lgpl-latest.qxl.bin %buildroot/%_datadir/%name/vgabios-qxl.bin
ln -s /usr/share/vgabios/VGABIOS-lgpl-latest.stdvga.bin %buildroot/%_datadir/%name/vgabios-stdvga.bin
ln -s /usr/lib/seabios/bios.bin %buildroot/%_datadir/%name/bios.bin

%pre
%_sbindir/groupadd -r -f %_group
if [ -f %_controldir/qemu-kvm-el ];then
%pre_control qemu-kvm-el
mv -f /var/run/control/qemu-kvm-el /var/run/control/kvm
else
%pre_control kvm
fi

%post
%post_control -s vmusers kvm
%post_service %name

%preun
%preun_service %name

%files
%exclude %_bindir/qemu-io
%exclude %_bindir/qemu-img
%_bindir/*
%_sysconfdir/udev/rules.d/*
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/*
%_controldir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_datadir/%name
%_man1dir/kvm.*
%_docdir/%name

%files -n qemu-img-el
%_bindir/qemu-img
%_bindir/qemu-io
%_man1dir/qemu-img.*

%changelog
* Tue Jan 24 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt13
- qemu-kvm-0.12.1.2-2.209.el6_2.4

* Wed Dec 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt12
- qemu-kvm-0.12.1.2-2.209.el6_2.1

* Wed Aug 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt11
- qemu-kvm-0.12.1.2-2.160.el6_1.8
- add stdvga bios link

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt10
- qemu-kvm-0.12.1.2-2.160.el6_1.6

* Mon Jul 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt9
- qemu-kvm-0.12.1.2-2.160.el6_1.3

* Wed Jul 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt8
- qemu-kvm-0.12.1.2-2.160.el6_1.2

* Fri May 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt7
- qemu-kvm-0.12.1.2-2.160.el6

* Mon Mar 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt6
- build with spice support
- remove internal vgabios*, seabios (use external ones)

* Fri Mar 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt5
- qemu-kvm-0.12.1.2-2.113.el6_0.8

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt4
- add qemu-img-el package
- add conflict with qemu-common, qemu-img (ALT #25163)
- build man

* Sun Jan 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt3
- qemu-kvm-0.12.1.2-2.113.el6_0.6

* Wed Aug 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1.2-alt1
- qemu-kvm-0.12.1.2-2.90.el6

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
