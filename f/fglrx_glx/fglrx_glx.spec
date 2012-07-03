%define cat_ver 12-4

# main switch :)
# before 11-2:
#define xfver x760
# from  11-2 xfver was changed to
%define xfver xpic

%ifarch %ix86
%define archdir arch/x86
%define xfdir   %xfver
%endif
%ifarch x86_64
%define archdir arch/x86_64
%define xfdir   %xfver%(echo _64a)
%endif

%define _libexecdir	%_prefix/libexec
%define _switchdir	%_libexecdir/X11/drv.d
%define _fdidir		%_datadir/hal/fdi/policy/20thirdparty

%define drvs	modules/drivers
%define dris	modules/dri
%define lnxs	modules/linux
%define exts	modules/extensions
%define ati_rel 1

Name: fglrx_glx
Version: 8.96.1
Release: alt1
Summary: ATI/AMD Proprietary Linux Display Driver
Group: System/Kernel and hardware

URL: http://ati.amd.com
License: Proprietary

Provides: libGL
Provides: xorg-drv-fglrx

Source0: http://www2.ati.com/drivers/linux/amd-driver-installer-%cat_ver-x86.x86_64.run
Source2: fglrx-switch.c
#Source3: catalyst_1010_linux.pdf

Source7: a-ac-aticonfig
Source8: a-lid-aticonfig
Source9: ati-powermode.sh
Source11: atieventsd.init
Source12: aticonfig.1
Source13: fglrx_create.xinf
Source14: xinf2fdi

Patch1: fglrx-3.11.1-fglrx_gamma.patch
Patch2: fglrx-8.20.8-alt-spinlock.patch

Requires: xorg-server >= 1.5.0 libdrm >= 2.4.5-alt2
Requires: hwdatabase
Requires: libGL libXrandr libXi libXcursor libXinerama

BuildRequires(pre): kernel-build-tools
BuildRequires: imake libXaw-devel libXext-devel libXp-devel libXpm-devel xorg-cf-files
BuildRequires: xorg-inputproto-devel xorg-recordproto-devel xorg-xf86miscproto-devel
BuildRequires: xorg-xf86vidmodeproto-devel
BuildRequires: libGL-devel libXrandr-devel libXi-devel libXcursor-devel libXinerama-devel
BuildRequires: libqt4-devel libdmx-devel xorg-xproto-devel
# libX11-devel 

ExclusiveArch: %ix86 x86_64

Packager: Ilya Mashkin <oddity@altlinux.ru>

%description 
AMD Proprietary Linux Display Driver.

This software suite support following ATI products:
 * ATI Mobility(tm) and Integrated Product Family
 * ATI Desktop and Integrated Product Family
 * All-In-Wonder(tm) variants based on the above are also supported. Video
   capture however is not supported.

The ATI Catalyst(tm) Linux software suite does not support ATI Workstation
products. AMD recommends using the AMD Proprietary Linux software driver
version <= 8.40.4.

%package -n fglrx-tools
Summary: Utilities for ATI/AMD Radeon drivers
Group: System/Configuration/Hardware
Requires: %name = %version-%release, acpid

%description -n fglrx-tools
ATI/AMD Radeon configuration utilities:

The AMD Catalyst Control Center for ATI Radeon graphics cards.

fglrxinfo is an analogue for glxinfo.

aticonfig parses an existing X-Server configuration file and modifies 
it to operate with ATI products.

fglrx_xgamma is a small tool to adjust gamma.

atieventsd is a user-level application that monitors various system events 
such as ACPI or hotplug, then notifies the driver via the X extensions 
interface that the event has occured.

%package -n kernel-source-fglrx-%version
Summary: ATI/AMD fglrx (Radeon video card driver) module sources
Group: Development/Kernel

%description -n kernel-source-fglrx-%version
ATI/AMD fglrx (Radeon video card driver) module sources for Linux kernel.

%prep
%setup -T -c
/bin/sh %SOURCE0 --extract .
%setup -D -T
#export CC=gcc-4.3 CXX=g++-4.3
#add_optflags -fpic -fPIC
#optflags_shared

pushd common/lib/modules/fglrx/build_mod
rm -f make.sh
#patch2 -p1
find . -type f -name '*.orig' -delete
cd ..
mv build_mod kernel-source-fglrx-%version
mv ../../../../%archdir/lib/modules/fglrx/build_mod/* kernel-source-fglrx-%version
tar -cj -f ../../../../kernel-source-fglrx-%version.tar.bz2 kernel-source-fglrx-%version
popd

mkdir fglrx_tools
pushd fglrx_tools
tar -xz -f ../common/usr/src/ati/fglrx_sample_source.tgz
#patch1 -p1 -b .fglrx_gamma
popd

%setup -D -T
#set_verify_elf_method unresolved=relaxed
#add_optflags -fpic -fPIC #optflags_shared


%build
#set_automake_version 1.9
#set_autoconf_version 2.5

#pushd fglrx_tools/lib/fglrx_gamma
#xmkmf
#%%make
#rm -f libfglrx_gamma.so*
#popd

#pushd fglrx_tools/programs/fglrx_gamma
#xmkmf
#%%make
#popd

gcc $RPM_OPT_FLAGS -fpic %SOURCE2 -o fglrx

%install
#set_strip_method executable,shared
%brp_strip_none %_libdir/X11/fgl*.so

#set_verify_elf_method textrel=relaxed,rpath=strict,unresolved=relaxed,lint=relaxed
%set_verify_elf_method textrel=relaxed,rpath=relaxed,unresolved=relaxed,lint=relaxed

mkdir -p %buildroot%_x11bindir
mkdir -p %buildroot%_libdir/X11/{%drvs,%lnxs,fglrx}
#mkdir -p %buildroot%_prefix/X11R6/%_lib/%dris
mkdir -p %buildroot%_libdir/X11/%dris
mkdir -p %buildroot%_x11includedir/X11/extensions
mkdir -p %buildroot{%_man1dir,%_man8dir}
mkdir -p %buildroot%_niconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_sysconfdir/acpi/events
mkdir -p %buildroot%_initrddir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_datadir/ati/amdcccle
mkdir -p %buildroot%_datadir/hwdatabase/videoaliases
mkdir -p %buildroot%_docdir/%name-%version
mkdir -p %buildroot%_libdir/dri

mkdir -p %buildroot%_libdir/fglrx

mkdir -p %kernel_srcdir

install -p -m644 %xfdir/usr/X11R6/%_lib/modules/amdxmm.so %buildroot%_libdir/X11/modules/
install -p -m644 %xfdir/usr/X11R6/%_lib/modules/glesx.so %buildroot%_libdir/X11/modules/
install -p -m644 %xfdir/usr/X11R6/%_lib/%drvs/fglrx_drv.so %buildroot%_libdir/X11/%drvs/
#install -p -m644 %archdir/usr/X11R6/%_lib/%dris/fglrx_dri.so %buildroot%_prefix/X11R6/%_lib/%dris/
install -p -m644 %archdir/usr/X11R6/%_lib/%dris/fglrx_dri.so %buildroot%_libdir/X11/%dris/

#ln -s ../../../../X11R6/%_lib/%dris/fglrx_dri.so %buildroot%_libdir/X11/%dris/fglrx_dri.so
#ln -s ../../X11R6/%_lib/%dris/fglrx_dri.so %buildroot%_libdir/dri/fglrx_dri.so

ln -s ../X11/%dris/fglrx_dri.so %buildroot%_libdir/dri/fglrx_dri.so



ln -s ../%dris/fglrx_dri.so %buildroot%_libdir/X11/fglrx/libdri.so

#ln -s %archdir/usr/X11R6/%_lib/libatiuki.so.1.0 %archdir/usr/X11R6/%_lib/libatiuki.so.1

install -p -m644 %xfdir/usr/X11R6/%_lib/%lnxs/libfglrxdrm.so %buildroot%_libdir/X11/%lnxs/
#install -p -m644 %xfdir/usr/X11R6/%_lib/%exts/*.so %buildroot%_libdir/X11/fglrx/
#
install -p -m644 %xfdir/usr/X11R6/%_lib/%exts/fglrx/fglrx-libglx.so %buildroot%_libdir/X11/fglrx/libglx.so
install -p -m644 %xfdir/usr/X11R6/%_lib/%exts/fglrx/*.so %buildroot%_libdir/X11/fglrx/
#install -p -m644 %archdir/usr/X11R6/%_lib/libGL.so.1.2 %buildroot%_libdir/X11/fglrx/libGL.so.1
#
install -p -m644 %archdir/usr/X11R6/%_lib/fglrx/fglrx-libGL.so.1.2 %buildroot%_libdir/X11/fglrx/libGL.so.1


install -p -m644 %archdir/usr/X11R6/%_lib/libfglrx*.so* %buildroot%_x11libdir/
%ifnarch x86_64
install -p -m644 %archdir/usr/X11R6/%_lib/libAMD* %buildroot%_x11libdir/
install -p -m644 %archdir/usr/X11R6/%_lib/libXv*.so* %buildroot%_x11libdir/
%endif
install -p -m644 %archdir/usr/X11R6/%_lib/libati*.so %buildroot%_x11libdir/
install -p -m644 %archdir/usr/%_lib/libatical*.so %buildroot%_libdir/
install -p -m644 %archdir/usr/%_lib/libatiuki.so* %buildroot%_libdir/
install -p -m644 %archdir/usr/%_lib/fglrx/switchlib* %buildroot%_libdir/fglrx/

#ln -s %buildroot%_x11libdir/libatiuki.so.1.0 %buildroot%_x11libdir/libatiuki.so.1


#pushd fglrx_tools/programs/fglrx_gamma
#%%make install DESTDIR=%%buildroot
#popd

# Create a proper desktop file in the right location
#mkdir -p %buildroot%_datadir/applications
#cat <<EOF > %buildroot%_datadir/applications/ati-controlcenter.desktop
#[Desktop Entry]
#Encoding=UTF-8
#Name=AMD Catalyst Control Center
#GenericName=AMD Catalyst Control Center
#Comment=The ATI Catalyst Control Center For Linux
#Exec=amdcccle
#Icon=ccc.xpm
#Terminal=false
#Type=Application
#Categories=Qt;Application;System;
#Version=%version
#EOF

# amdcccle install
%ifnarch x86_64

install -p -m755 %archdir/usr/X11R6/bin/amdcccle %buildroot%_bindir/
install -p -m644 common/usr/share/icons/ccc_large.xpm %buildroot%_liconsdir/ccc.xpm
#install -p -m644 common/usr/share/icons/ccc_small.xpm %buildroot%_niconsdir/ccc.xpm
install -p -m644 common/usr/share/ati/amdcccle/* %buildroot%_datadir/ati/amdcccle
%endif

# other tools (fgl_glxgears,fglrxinfo,fglrx_xgamma,aticonfig,atieventsd)
install -p %archdir/usr/X11R6/bin/fgl_glxgears %buildroot%_x11bindir/
install -p %archdir/usr/X11R6/bin/fglrxinfo %buildroot%_x11bindir/
install -p %archdir/usr/X11R6/bin/aticonfig %buildroot%_x11bindir/
install -p %archdir/usr/X11R6/bin/atiod* %buildroot%_x11bindir/
install -p common/usr/X11R6/bin/amd* %buildroot%_x11bindir/
#install -p fglrx_tools/programs/fglrx_gamma/fglrx_xgamma %buildroot%_x11bindir/
#install -p -m644 fglrx_tools/programs/fglrx_gamma/fglrx_xgamma.man %buildroot%_man1dir/fglrx_xgamma.1
install -p -m755 {%archdir,common}%_sbindir/* %buildroot%_sbindir/
install -p -m644 %SOURCE7 %SOURCE8 %buildroot%_sysconfdir/acpi/events/
install -p -m755 %SOURCE9 %buildroot%_sysconfdir/acpi/
install -p -m755 %SOURCE11 %buildroot%_initrddir/atieventsd
install -p -m644 %SOURCE12 %buildroot%_man1dir/
install -p -m644 common%_man8dir/* %buildroot%_man8dir/
install -p -m644 kernel-source-fglrx-%version.tar.bz2 %kernel_srcdir/

mkdir -p %buildroot%_switchdir

install -p -m755 fglrx %buildroot%_switchdir/fglrx

# release notes #14277
#install -p -m644 %%SOURCE3 common/usr/share/doc/fglrx/

cp -pr common/etc/ati %buildroot%_sysconfdir

# generate .xinf
sh %SOURCE13 common/lib/modules/fglrx/kernel-source-fglrx-%version/fglrxko_pci_ids.h \
	%buildroot%_datadir/hwdatabase/videoaliases/fglrx.xinf > /dev/null 2>&1
mkdir -p %buildroot%_fdidir
sh %SOURCE14 -x %buildroot%_datadir/hwdatabase/videoaliases/fglrx.xinf -f %buildroot%_fdidir/20-x11-video-fglrx.fdi -d fglrx

%post -n fglrx-tools
%post_service atieventsd

%preun -n fglrx-tools
%preun_service atieventsd

%files
%dir %_sysconfdir/ati
%_sysconfdir/ati/*
#_prefix/X11R6/%_lib/%dris/fglrx_dri.so
%_x11x11libdir/modules/*.so
%_x11x11libdir/%dris/*
%_x11x11libdir/%drvs/*
%_x11x11libdir/%lnxs/*
%_libdir/dri
%_libdir/dri/fglrx_dri.so
%dir %_x11x11libdir/fglrx
%_x11x11libdir/fglrx/*
%_x11libdir/libfglrx*.so*
%_x11libdir/libati*.so*
%ifnarch x86_64
%_x11libdir/libAMD*
%_x11libdir/libXv*.so*
%endif
#_libdir/libamd*.so
%_libdir/libatical*.so
%_libdir/fglrx/switchlib*
%_datadir/hwdatabase/videoaliases/*
%_fdidir/20-x11-video-*.fdi
%doc common/usr/share/doc/fglrx/*
%_switchdir/*

%files -n fglrx-tools
%_x11bindir/amd*
%_x11bindir/ati*
%_x11bindir/fgl*
%ifnarch x86_64
#_bindir/amdcccle
#_niconsdir/*.xpm
%_liconsdir/*.xpm
#_datadir/applications/*.desktop
%dir %_datadir/ati/amdcccle
%_datadir/ati/amdcccle/*
%endif
%_sysconfdir/acpi/*
%_initrddir/*
%_man8dir/*
%_man1dir/*
%_sbindir/*

%files -n kernel-source-fglrx-%version
%_usrsrc/*

%changelog
* Fri Apr 27 2012 Ilya Mashkin <oddity@altlinux.ru> 8.96.1-alt1
- Version 8.96.1 (Catalyst 12.4)

* Fri Mar 29 2012 Ilya Mashkin <oddity@altlinux.ru> 8.95.1-alt1
- Version 8.95.1 (Catalyst 12.3)

* Tue Feb 07 2012 Ilya Mashkin <oddity@altlinux.ru> 8.93-alt1
- Version 8.93 (Catalyst 12.1)

* Sat Dec 17 2011 Ilya Mashkin <oddity@altlinux.ru> 8.92-alt1
- Version 8.92 (Catalyst 11.12)

* Thu Nov 17 2011 Ilya Mashkin <oddity@altlinux.ru> 8.91.1-alt1
- Version 8.91.1 (Catalyst 11.11)
- add support for X.Org 1.11

* Thu Nov 10 2011 Ilya Mashkin <oddity@altlinux.ru> 8.90.2-alt1
- Version 8.90.2 (Catalyst 11.10)

* Wed Oct 12 2011 Ilya Mashkin <oddity@altlinux.ru> 8.89.2-alt1
- Version 8.89.2 (Catalyst 11.9)
- FHS fix
- drop desktop file

* Sat Aug 20 2011 Ilya Mashkin <oddity@altlinux.ru> 8.88.1-alt1
- Version 8.88.1 (Catalyst 11.8)

* Fri Aug 05 2011 Ilya Mashkin <oddity@altlinux.ru> 8.87.2-alt1
- Version 8.87.2 (Catalyst 11.7)
- drop spinlock patch

* Sun Jun 19 2011 Ilya Mashkin <oddity@altlinux.ru> 8.86.1-alt1
- Version 8.86.1 (Catalyst 11.6)

* Sat May 14 2011 Ilya Mashkin <oddity@altlinux.ru> 8.85-alt2
- Try to fix #25536. Add missing files

* Wed May 11 2011 Ilya Mashkin <oddity@altlinux.ru> 8.85-alt1
- Version 8.85 (Catalyst 11.5)

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 8.84.1-alt1
- Version 8.841 (Catalyst 11.4)

* Fri Apr 01 2011 Ilya Mashkin <oddity@altlinux.ru> 8.831.2-alt1
- Version 8.831.2 (Catalyst 11.3)
- drop *gamma

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 8.82.1-alt1
- Version 8.821 (Catalyst 11.2)
- switch xfver to xpic

* Thu Jan 27 2011 Ilya Mashkin <oddity@altlinux.ru> 8.81.2-alt1
- Version 8.812 (Catalyst 11.1):
- support for kernel 2.6.37
- add EnableTearFreeDesktop option

* Wed Dec 15 2010 Ilya Mashkin <oddity@altlinux.ru> 8.80.1-alt1
- Version 8.801 (Catalyst 10.12)

* Wed Nov 24 2010 Ilya Mashkin <oddity@altlinux.ru> 8.79.1-alt1
- Version 8.791 (Catalyst 10.11)

* Sat Oct 23 2010 Ilya Mashkin <oddity@altlinux.ru> 8.78.3-alt1
- Version 8.783 (Catalyst 10.10)
- Support for Xserver 1.9, kernel 2.6.35

* Fri Aug 27 2010 Ilya Mashkin <oddity@altlinux.ru> 8.76.2-alt1
- Version 8.762 (Catalyst 10.8)

* Wed Aug 11 2010 Ilya Mashkin <oddity@altlinux.ru> 8.75.3-alt1
- Version 8.753 (Catalyst 10.7)

* Sun Jun 20 2010 Ilya Mashkin <oddity@altlinux.ru> 8.74.1-alt1
- Version 8.741 (Catalyst 10.6)

* Fri May 28 2010 Ilya Mashkin <oddity@altlinux.ru> 8.73.2-alt1
- Version 8.732 (Catalyst 10.5)

* Sun May 02 2010 Ilya Mashkin <oddity@altlinux.ru> 8.72.3-alt1
- Version 8.723 (Catalyst 10.4)

* Fri Apr 16 2010 Ilya Mashkin <oddity@altlinux.ru> 8.71.2-alt1
- Version 8.712 (Catalyst 10.3)

* Sat Feb 27 2010 Ilya Mashkin <oddity@altlinux.ru> 8.70.2-alt1
- Version 8.702 (Catalyst 10.2)

* Fri Jan 29 2010 Ilya Mashkin <oddity@altlinux.ru> 8.69-alt1
- Version 8.69 (Catalyst 10.1)

* Mon Jan 04 2010 Ilya Mashkin <oddity@altlinux.ru> 8.68.1-alt2
- add libqt4-devel to requires

* Sat Dec 19 2009 Ilya Mashkin <oddity@altlinux.ru> 8.68.1-alt1
- Version 8.681 (Catalyst 9.12)

* Fri Nov 20 2009 Ilya Mashkin <oddity@altlinux.ru> 8.67.1-alt1
- Version 8.671 (Catalyst 9.11)

* Sun Nov 15 2009 Ilya Mashkin <oddity@altlinux.ru> 8.66.1-alt1
- Version 8.661 (Catalyst 9.10)

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 8.65-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for fglrx_glx
  * postclean-05-filetriggers for spec file

* Sun Sep 13 2009 Ilya Mashkin <oddity@altlinux.ru> 8.65-alt1
- Version 8.65 (Catalyst 9.9)

* Wed Aug 19 2009 Ilya Mashkin <oddity@altlinux.ru> 8.64-alt1
- Version 8.64 (Catalyst 9.8)

* Sat Jul 25 2009 Ilya Mashkin <oddity@altlinux.ru> 8.63.2-alt1
- Version 8.632 (aka Catalyst 9.7)

* Thu Jun 18 2009 Ilya Mashkin <oddity@altlinux.ru> 8.62-alt1
- Version 8.62 (aka Catalyst 9.6)

* Sat May 23 2009 Ilya Mashkin <oddity@altlinux.ru> 8.61.2-alt0.M50.1
- Build for ALT Linux 5.0

* Wed May 20 2009 Ilya Mashkin <oddity@altlinux.ru> 8.61.2-alt1
- Version 8.612 (aka Catalyst 9.5)

* Sun May 17 2009 Ilya Mashkin <oddity@altlinux.ru> 8.60.2-alt0.0.M50.1
- build for 5.0

* Sun Apr 19 2009 Ilya Mashkin <oddity@altlinux.ru> 8.60.2-alt0.1
- Version 8.602 (aka Catalyst 9.4)

* Fri Apr 03 2009 Ilya Mashkin <oddity@altlinux.ru> 8.59.3-alt0.1
- Version 8.593 (aka Catalyst 9.3)

* Tue Feb 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 8.58.2-alt3
- fixed switch library
- added hal policy

* Tue Feb 24 2009 Ilya Mashkin <oddity@altlinux.ru> 8.58.2-alt2
- switch to Xorg 7.4 (thanks to Valery Inozemtsev)

* Mon Feb 23 2009 Ilya Mashkin <oddity@altlinux.ru> 8.58.2-alt1
- Version 8.582 (aka Catalyst 9.2)
- technology build, probably not for use right now!

* Mon Feb 23 2009 Ilya Mashkin <oddity@altlinux.ru> 8.57.3-alt2
- Build for Sisyphus

* Sat Jan 31 2009 L.A. Kostis <lakostis@altlinux.ru> 8.57.3-alt1
- Version 8.573 (aka Catalyst 9.1).
- Fix xorg switch for new libglx layout.

* Mon Jan 11 2009 Ilya Mashkin <oddity@altlinux.ru> 8.53.2-alt2
- NMU: fix requires/build
-      remove deprecated macros from spec

* Sat Dec 20 2008 L.A. Kostis <lakostis@altlinux.ru> 8.57-alt0.1
- Unofficial Catalyst 9.1beta.
- Don't use bundled libglx (due problems with AIGLX).

* Sat Dec 13 2008 L.A. Kostis <lakostis@altlinux.ru> 8.56.1-alt1
- Version 8.561 (aka Catalyst 8.12).
- Remove obsoleted macros, update buildreq/provides for new xorg.
- Use new switch scheme.

* Fri Nov 14 2008 L.A. Kostis <lakostis@altlinux.ru> 8.55.2-alt1
- Version 8.552 (aka Catalyst 8.11).

* Sun Oct 19 2008 L.A. Kostis <lakostis@altlinux.ru> 8.54.2-alt1
- Version 8.542 (aka Catalyst 8.10).

* Sat Sep 20 2008 L.A. Kostis <lakostis@altlinux.ru> 8.53.2-alt1
- Version 8.532 (aka Catalyst 8.9).

* Fri Aug 29 2008 L.A. Kostis <lakostis@altlinux.ru> 8.52.2-alt2.1
- One more fixes for x86_64.

* Fri Aug 29 2008 L.A. Kostis <lakostis@altlinux.ru> 8.52.2-alt2
- Fix x86_64 build.
- optimize file list.
- revert "Update libGL.so.1 links for both architectures" patch.

* Fri Aug 22 2008 L.A. Kostis <lakostis@altlinux.ru> 8.52.2-alt1
- Version 8.522 (aka Catalyst 8.8).
- Fix acpi scripts (#14915).
- Fix library paths for aticonfig.
- Add release notes (#14277).

* Tue Aug 05 2008 L.A. Kostis <lakostis@altlinux.ru> 8.51.2-alt1
- Version 8.512 (aka Catalyst 8.7).
- Update libGL.so.1 links for both architectures (#16228).

* Wed Jun 25 2008 L.A. Kostis <lakostis@altlinux.ru> 8.50.1-alt1
- Version 8.50.1 (aka Catalyst 8.6).

* Wed May 28 2008 L.A. Kostis <lakostis@altlinux.ru> 8.49.3.1-alt1
- Version 8.493.1 (aka Catalyst 8.5).

* Thu Apr 17 2008 L.A. Kostis <lakostis@altlinux.org> 8.47.6-alt1
- Version 8.476 (aka Catalyst 8.4).

* Fri Mar 07 2008 L.A. Kostis <lakostis@altlinux.org> 8.47.1-alt1
- Version 8.471 (aka Catalyst 8.3).

* Fri Feb 15 2008 L.A. Kostis <lakostis@altlinux.org> 8.45.5.2-alt1
- Version 8.455.2 (aka Catalyst 8.02).
- fix atieventsd init.script.

* Fri Jan 18 2008 L.A. Kostis <lakostis@altlinux.org> 8.45.2.1-alt1
- Version 8.45.2.1 (aka Catalyst 8.01).
- disable atieventsd by default.

* Wed Dec 26 2007 L.A. Kostis <lakostis@altlinux.org> 8.44.3.1-alt1
- Version 8.44.3.1 (aka Catalyst 7.12).

* Fri Nov 23 2007 L.A. Kostis <lakostis@altlinux.ru> 8.43.3-alt1
- Version 8.43.3 (aka Catalyst 7.11).
- add amdcccle data files.
- add hackish symlink for AIGLX.

* Wed Oct 24 2007 L.A. Kostis <lakostis@altlinux.ru> 8.42.3-alt1
- Version 8.42.3 (official).
- This build is not be used for distribution packages. Blame to AMD :-P
- Fix package intersections.

* Sun Sep 16 2007 L.A. Kostis <lakostis@altlinux.ru> 8.40.4-alt2
- bug fix release:
  + fix switchdir and return to x11setupdrv (#12767).
  + remove fglrx.xinf (now it generated automatically).
  + rework fglrx_create.xinf - now it uses public information 
    for getting ASIC IDs.

* Sun Aug 19 2007 L.A. Kostis <lakostis@altlinux.ru> 8.40.4-alt1
- Version 8.40.4.

* Sat Aug 04 2007 L.A. Kostis <lakostis@altlinux.ru> 8.39.4-alt1
- Version 8.39.4.
- Update aticonfig(1) man page.

* Mon Jul 02 2007 L.A. Kostis <lakostis@altlinux.ru> 8.38.6-alt1
- Version 8.38.6.
- Update .xinf file.
- Remove obsoleted patches.
- Drop fireglcontrol (oops, we haven't way back).
- Switch to x11presetdrv.

* Sun Jun 10 2007 L.A. Kostis <lakostis@altlinux.ru> 8.37.6-alt1
- Version 8.37.6.

* Sun May 06 2007 L.A. Kostis <lakostis@altlinux.ru> 8.37.3-alt0.1
- Version 8.37.3 (internal beta release).

* Sat Apr 21 2007 L.A. Kostis <lakostis@altlinux.ru> 8.36.5-alt1
- Version 8.36.5.
- Add .xinf for alterator-x11 and example creation script.
- Resurrected fireglcontrol (it's last resort for x86-64).

* Mon Apr 09 2007 L.A. Kostis <lakostis@altlinux.ru> 8.35.5-alt2
- Don't package amdcccle for x86_64 (biarch binary).

* Sun Apr 08 2007 L.A. Kostis <lakostis@altlinux.ru> 8.35.5-alt1
- Version 8.35.5.
- add acpi events actions for atieventsd.
- update description.
- remove fglrxcontrol (obsoleted by amdcccle).

* Sun Feb 25 2007 L.A. Kostis <lakostis@altlinux.ru> 8.34.8-alt1
- remove obsoleted files.

* Sat Feb 24 2007 L.A. Kostis <lakostis@altlinux.ru> 8.34.8-alt0.1
- Version 8.34.8.

* Thu Jan 11 2007 L.A. Kostis <lakostis@altlinux.org> 8.33.6-alt1
- Version 8.33.6.
- Update aticonfig(1) man page.

* Mon Dec 18 2006 L.A. Kostis <lakostis@altlinux.ru> 8.32.5-alt1.2
- fix a typo in -switch script.

* Fri Dec 15 2006 L.A. Kostis <lakostis@altlinux.ru> 8.32.5-alt1.1
- Update -switch file according new server layout.

* Thu Dec 14 2006 L.A. Kostis <lakostis@altlinux.ru> 8.32.5-alt1
- Version 8.32.5.
- strict requires for xorg-x11-server.

* Wed Nov 15 2006 L.A. Kostis <lakostis@altlinux.ru> 8.31.5-alt1
- Version 8.31.5.

* Mon Nov 06 2006 L.A. Kostis <lakostis@altlinux.ru> 8.30.3-alt1
- Version 8.30.3;
- merge with trunk;
- revert paths for docs (possible not updated in release build);
- remove filesystem intersections in -tools package. 

* Fri Sep 22 2006 L.A. Kostis <lakostis@altlinux.ru> 8.29.6-alt1
- Version 8.29.6.

* Sun Aug 27 2006 L.A. Kostis <lakostis@altlinux.ru> 8.28.8-alt1
- Version 8.28.8.
- cleanup BuildRequires.
- merge with trunk.

* Sat Aug 12 2006 L.A. Kostis <lakostis@altlinux.ru> 8.28.4-alt0.1
- Version 8.28.4 (internal beta release);
- cleanup & update .spec;
- switch to Xorg-7.1 cause it's trunk build.

* Fri Aug 11 2006 L.A. Kostis <lakostis@altlinux.ru> 8.27.10-alt1
- Version 8.27.10;
- switch back to Xorg-7.0.

* Sat Jul 06 2006 LAKostis <lakostis at altlinux.ru> 8.27.4-alt0.1
- Version 8.27.4 (internal beta release).
- switch to Xorg-7.1
- add atieventsd to -tools package.
- add man page for aticonfig(1).
- update -tools description.

* Sat Jun 01 2006 LAKostis <lakostis at altlinux.ru> 8.25.18-alt2
- Add libstdc++3.3 to BuildRequires.

* Wed May 31 2006 LAKostis <lakostis at altlinux.ru> 8.25.18-alt1
- Version 8.25.18.
- Fix build with new qt3-devel.
- Added patches for kernel module parts (moved here from kernel-modules-fglrx-*
  packages):
  + fglrx-8.20.8-alt-spinlock.patch
- Removed patches for kernel module parts:
  - fglrx-8.10.19-module_param-2.6.x-warn_cleanup.patch (fixed upstream).
  - fglrx-8.24.8-x86-64-no_iommu-cleanup.patch (fixed upstream).

* Fri Apr 14 2006 LAKostis <lakostis at altlinux.ru> 8.24.8-alt1
- Version 8.24.8.

* Wed Mar 22 2006 LAKostis <lakostis at altlinux.ru> 8.24.3-alt0.1
- Version 8.24.3 (internal beta release).
- relax verify-elf checks for libfglrx_*.

* Fri Feb 24 2006 LAKostis <lakostis at altlinux.ru> 8.22.5-alt2
- First working version (tnx vsu@ for suggestions):
  + revert %dris to old location.
  + add missing x11setupdrv for glx.
  + fix %%switchdir location.
+ fix packaging for x86_64.
- fix menu file.

* Tue Feb 21 2006 LAKostis <lakostis at altlinux.ru> 8.22.5-alt1
- add compatibility location.
- fix buildreq for xorg-7.0.

* Sun Feb 12 2006 LAKostis <lakostis at altlinux.ru> 8.22.5-alt0.1
- Version 8.22.5.
- try to adopt to new xorg-7.0 location.

* Sun Jan 22 2006 LAKostis <lakostis at altlinux.ru> 8.21.7-alt0.1
- Version 8.21.7.
- restore build for x86_64.

* Thu Dec 01 2005 LAKostis <lakostis at altlinux.ru> 8.19.10-alt0.1
- Version 8.19.10.
- Temporary disable x86_64 build.

* Sun Oct 16 2005 LAKostis <lakostis at altlinux.ru> 8.18.6-alt0.1
- Version 8.18.6.
- Removed patches:
  - fglrx-8.10.19-pte_unmap-2.4-warn_cleanup.patch

* Wed Jun 29 2005 Anton D. Kachalov <mouse@altlinux.org> 8.14.13-alt2
- Added x86_64 support

* Sat Jun 11 2005 Sergey Vlasov <vsu@altlinux.ru> 8.14.13-alt1
- Version 8.14.13.
- Removed obsolete 2.6.11-compatibility patches:
  - fglrx-8.10.19-agp_backend-2.6.11rc2.patch
  - fglrx-8.10.19-i386-warn_cleanup.patch
  - fglrx-8.10.19-rage3d_4-level-pagetables.patch
  - fglrx-8.10.19-remap_page_range-2.6.11rc1.patch
- Added Provides: x11-driver-fglrx (#6597).
- Updated fglrx-switch script for the new libglx name (libglx-x11.a); added
  dependency on xorg-x11-mesagl >= 6.8.2-alt9 for this file.

* Tue Jun 07 2005 Sergey Vlasov <vsu@altlinux.ru> 8.12.10-alt3
- Moved libGL.so.fglrx to %_x11libdir/fglrx (fixes #6065).

* Tue Jun 07 2005 Anton Farygin <rider@altlinux.ru> 8.12.10-alt2
- added script for setgl (%_switchdir/fglrx)

* Wed Jun 01 2005 Sergey Vlasov <vsu@altlinux.ru> 8.12.10-alt1
- Version 8.12.10.

* Sun Mar 13 2005 Sergey Vlasov <vsu@altlinux.ru> 8.10.19-alt1
- Version 8.10.19.
- Removed patches:
  - fglrx-8.8.25-kernel-2.6.10.patch (obsolete)
- Added patches for compatibility with kernel 2.6.11:
  + fglrx-8.10.19-agp_backend-2.6.11rc2.patch: add compatibility with new AGP
    layer in 2.6.11 (drm_agp_t was removed)
  + fglrx-8.10.19-i386-warn_cleanup.patch: remove x86_64-only functions and
    variables from the i386 build
  + fglrx-8.10.19-module_param-2.6.x-warn_cleanup.patch: use new-style module
    parameters for 2.6.x instead of obsolete MODULE_PARM
  + fglrx-8.10.19-pte_unmap-2.4-warn_cleanup.patch: #undef pte_unmap before
    redefining it to be empty
  + fglrx-8.10.19-rage3d_4-level-pagetables.patch: add support for 4-level page
    tables in 2.6.11
  + fglrx-8.10.19-remap_page_range-2.6.11rc1.patch: use new remap_pfn_range
    function instead of obsolete remap_page_range which was removed in 2.6.11

* Sun Jan 30 2005 Sergey Vlasov <vsu@altlinux.ru> 8.8.25-alt2
- Added patches for kernel module parts (moved here from kernel-modules-fglrx-*
  packages):
  + fglrx-3.2.8-agp-sis.patch: added SiS 745 host bridge IDs to the builtin AGP
    support
  + fglrx-3.2.8-via-agp2.patch: fixed AGP 2.0 support for VIA KT400 and P4X333
  + fglrx-3.2.8-nvidia-nforce.patch: fixed nForce AGP support
  + fglrx-3.7.6-agp-sis-fix.patch: workaround for SiS 648 and 746 chips (seems
    that they need a delay after setting AGP rate)
  + fglrx-3.7.6-sis-agp3-support.patch: AGP3 support for SiS 648
  + fglrx-8.8.25-kernel-2.6.10.patch: fix compilation with kernel 2.6.10
- Removed rpath cleaning (fixed upstream again).
- Updated Requires (this driver is for X.Org 6.8).
- Updated BuildRequires.

* Tue Jan 18 2005 LAKostis <lakostis at altlinux.ru> 8.8.25-alt1
- Version 8.8.25.

* Wed Jan 12 2005 LAKostis <lakostis at altlinux.ru> 3.14.6-alt1.1
- fix fglrx-panel to compile with new qt.

* Fri Nov 12 2004 LAKostis <lakostis at altlinux.ru> 3.14.6-alt1
- Daedalus build.
- Version 3.14.6.

* Fri Oct 01 2004 LAKostis <lakostis at altlinux.ru> 3.14.1-alt1
- Daedalus build.
- Version 3.14.1.

* Mon Aug 16 2004 Sergey Vlasov <vsu@altlinux.ru> 3.11.1-alt1
- Version 3.11.1.
- Added back rpath cleaning.
- Added fglrx_xgamma to fglrx-tools.
- Added documentation.

* Mon Mar 22 2004 Sergey Vlasov <vsu@altlinux.ru> 3.7.6-alt1
- Version 3.7.6.
- Removed rpath cleaning (fixed upstream).
- Added rpath=strict check.
- Updated BuildRequires.

* Sat Jan 03 2004 Sergey Vlasov <vsu@altlinux.ru> 3.7.0-alt1
- Version 3.7.0.
- Use the RPM from ATI as Source instead of a repacked tarball.
- Fixed file modes.
- Relaxed TEXTREL check.
- Merged with Alexey Morozov <morozov@altlinux> changes:
  - build both fglrx_glx and kernel-source-fglrx packages from the single
    official ATI driver rpm package
  - new driver version (3.7.0)
  - fglrx_panel and fglrx_gamma is built and packaged into
    fglrx-tools subpackage
- Excluded *fglrx_gamma* because of wrong soname in libfglrx_gamma.so.1.
- Added README file from the ATI site (not included in the original RPM).
- Updated BuildRequires.

* Sun Oct 12 2003 Sergey Vlasov <vsu@altlinux.ru> 3.2.8-alt1
- new version (3.2.8)

* Tue Sep 09 2003 Rider <rider@altlinux.ru> 3.2.5-alt1
- new version

* Wed Jul 16 2003 Peter Novodvorsky <nidd@altlinux.com> 2.9.12-alt1
- initial release.

