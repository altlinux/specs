#define rev 2459
%define oldmodname kernel-source-virtualbox
%define oldmodnamenetflt kernel-source-virtualbox-netfilter
%define oldmodnamenetadp kernel-source-virtualbox-netadaptor
%define oldmodnameadd kernel-source-virtualbox-addition
%define oldmodnameguest kernel-source-virtualbox-guest
%define oldmodnamevfs kernel-source-virtualbox-vfs
%define oldmodnamevideo kernel-source-virtualbox-video

%define modname kernel-source-vboxdrv
%define modnamepci kernel-source-vboxpci
%define modnamenetflt kernel-source-vboxnetflt
%define modnamenetadp kernel-source-vboxnetadp
%define modnameguest kernel-source-vboxguest
%define modnamevfs kernel-source-vboxsf
%define modnamevideo kernel-source-vboxvideo

%define vboxdir %_libdir/virtualbox
%define vboxdatadir %_datadir/virtualbox
%define vboxadddir %vboxdir/additions

%set_verify_elf_method textrel=relaxed
%add_findprov_lib_path %vboxdir

%define distname VirtualBox

%ifarch %ix86
%define vbox_platform linux.x86
%endif
%ifarch x86_64
%define vbox_platform linux.amd64
%endif
%define build_manual 0
%define build_additions 1
%define build_webservice 0
%def_without java
%def_with vnc

Name: virtualbox
Version: 4.1.12
Release: alt2

Summary: VM VirtualBox OSE - Virtual Machine for x86 hardware
License: GPL
Group: Emulators
Url: http://www.virtualbox.org/

ExclusiveArch: %ix86 x86_64

Packager: Evgeny Sinelnikov <sin@altlinux.ru>

%define distarchive %distname-%{version}_OSE
Source: %distarchive.tar

Source1:	%name.control
Source2:	%name.init
Source3:	%name-addition.rules
Source4:	%name.rules
Source5:	60-vboxadd.perms
Source6:	vboxadd-service.sysconfig
Source7:	vboxadd.init
Source8:	vboxadd-service.init
Source13:	http://download.virtualbox.org/%name/%version/UserManual.pdf
Source15:	os_altlinux.png
Source16:	os_altlinux_64.png
Source17:	http://download.virtualbox.org/%name/%version/%distname.chm
Source18:	xorg-vboxmouse.rules
Source19:	xorg-vboxmouse.conf
Source20:	http://download.virtualbox.org/%name/%version/SDKRef.pdf
Source21:	%distname-HTML-%{version}_OSE.tar

Patch0:		%name-%version-%release.patch

BuildPreReq: dev86 iasl gcc4.3-c++ libstdc++4.3-devel-static
BuildPreReq: libIDL-devel libSDL-devel
BuildPreReq: libXcursor-devel libXext-devel
BuildPreReq: xsltproc
BuildPreReq: kernel-build-tools python-dev
BuildPreReq: libpulseaudio-devel
BuildRequires: libxml2-devel libxslt-devel
BuildRequires: libqt4-devel libalsa-devel
BuildRequires: libcap-devel libcurl-devel
BuildRequires: libXmu-devel libGLU-devel
BuildRequires: libXdamage-devel libXcomposite-devel
BuildRequires: xorg-xf86driproto-devel xorg-glproto-devel
BuildRequires: xorg-sdk
BuildPreReq: yasm kBuild >= 0.1.999
%if %build_webservice
BuildRequires: libgsoap-devel-static
%endif
BuildRequires: libpam-devel
%if %build_manual
BuildRequires: texlive-latex-recommended
%endif
%if_with vnc
BuildRequires: libvncserver-devel
%endif
BuildRequires: rpm-build-xdg

PreReq: %name-common = %version-%release

%description
VirtualBox is a powerful PC virtualization solution allowing
you to run a wide range of PC operating systems on your Linux
system. This includes Windows, Linux, FreeBSD, DOS, OpenBSD
and others. VirtualBox comes with a broad feature set and
excellent performance, making it the premier virtualization
software solution on the market.

%package guest-additions
Summary: Full package of additions for VirtualBox OSE guest systems
Group: Emulators
Requires: xorg-drv-vboxmouse
Requires: xorg-drv-vboxvideo
Requires: %name-guest-utils

%description guest-additions
This packages contains full package of additions for VirtualBox OSE
guest systems. It consists basic utils, which allows to share files and
sync time with host system, and intergrates with xorg-server for mouse
and video driver with OpenGL support, copy/paste between guest and host.

%package guest-utils
Summary: Additions for VirtualBox OSE guest systems
Group: Emulators

%description guest-utils
This packages contains basic utils for VirtualBox OSE guest systems.
It allows to share files and sync time with host system.

%package -n %modname
Summary: Sources for VirtualBox module
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodname = %version-%release

%description -n %modname
Sources for VirtualBox kernel module.

%package -n %modnamepci
Summary: Sources for VirtualBox module for OSE pci
Group: Development/Kernel
BuildArch: noarch

%description -n %modnamepci
Sources for VirtualBox kernel module for OSE pci.

%package -n %modnamenetflt
Summary: Sources for VirtualBox module for OSE netfilter
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnamenetflt = %version-%release

%description -n %modnamenetflt
Sources for VirtualBox kernel module for OSE netfilter.

%package -n %modnamenetadp
Summary: Sources for VirtualBox module for OSE netadaptor
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnamenetadp = %version-%release

%description -n %modnamenetadp
Sources for VirtualBox kernel module for OSE netadaptor.

%package -n %modnameguest
Summary: Sources for VirtualBox module for OSE guest additions
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnameadd = %version-%release
Provides: %oldmodnameguest = %version-%release

%description -n %modnameguest
Sources for VirtualBox kernel module for OSE guest additions.

%package -n %modnamevfs
Summary: Sources for VirtualBox module for OSE VFS
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnamevfs = %version-%release

%description -n %modnamevfs
Sources for VirtualBox kernel module for OSE VFS.

%package -n %modnamevideo
Summary: Sources for VirtualBox module for OSE Video DRM
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnamevideo = %version-%release

%description -n %modnamevideo
Sources for VirtualBox kernel module for OSE Video DRM.

%package -n xorg-drv-vboxmouse
Summary: The X.org driver for mouse in VirtualBox guests
Group: System/X11
Provides: xorg-x11-drv-vboxmouse = %version-%release
Obsoletes: xorg-x11-drv-vboxmouse < %version

%description -n xorg-drv-vboxmouse
The X.org driver for mouse in VirtualBox guests

%package -n xorg-drv-vboxvideo
Summary: The X.org driver for video in VirtualBox guests
Group: System/X11
Provides: xorg-x11-drv-vboxvideo = %version-%release
Obsoletes: xorg-x11-drv-vboxvideo < %version

%description -n xorg-drv-vboxvideo
The X.org driver for video in VirtualBox guests

%package common
Summary: VirtualBox module support files
Group: System/Configuration/Other
BuildArch: noarch
# due to new_summary function and is_builtin_mode bugfix
PreReq: control >= 0.7.2-alt1
PreReq: shadow-utils
# due to /bin/mountpoint
PreReq: sysvinit-utils

%description common
This package contains scripts and other support files which are
required to use the vboxdrv kernel module in the ALT Linux system.
The kernel module itself is not included - you need to install the
appropriate kernel-modules-virtualbox-* package for your kernel.

%package doc
Summary: VirtualBox documentation
Group: Documentation
BuildArch: noarch

%description doc
This package contains VirtualBox User Manual.

%package sdk
Summary: VirtualBox SDK
Group: Development/Other

%description sdk
This package contains VirtualBox SDK.

%prep
%setup -q -n %distarchive
%patch -p1

cp %SOURCE15 %SOURCE16 src/VBox/Frontends/VirtualBox/images

%build
export GCC_VERSION=4.3
./configure --ose \
    --disable-kmods \
%if %build_webservice
    --enable-webservice \
%endif
%if_without java
    --disable-java \
%endif
%if_with vnc
    --enable-vnc \
%endif
%if "%build_manual" == "0"
    --disable-docs \
%endif
    --with-qt-dir=%_qt4dir \
    --with-kbuild=%_bindir
%if "%build_additions" == "0"
echo "VBOX_WITH_X11_ADDITIONS    := " >> LocalConfig.kmk
%endif
%if %build_webservice
echo "VBOX_WITHOUT_SPLIT_SOAPC   := 1" >> LocalConfig.kmk
%endif
# don't build testcases to save time, they are not needed for the package
echo "VBOX_WITH_TESTCASES        :=" >> LocalConfig.kmk
echo "VBOX_WITH_TESTSUITE        :=" >> LocalConfig.kmk
# required for VBOX_PATH_APP_PRIVATE_*
echo "VBOX_DOCBOOK_WITH_LATEX    := 1" >> LocalConfig.kmk
echo "KBUILD_MSG_STYLE           := brief" >> LocalConfig.kmk
echo "VBOX_PATH_APP_PRIVATE_ARCH := %vboxdir" >> LocalConfig.kmk
echo "VBOX_PATH_SHARED_LIBS      := \$(VBOX_PATH_APP_PRIVATE_ARCH)" >> LocalConfig.kmk
echo "VBOX_WITH_RUNPATH          := \$(VBOX_PATH_APP_PRIVATE_ARCH)" >> LocalConfig.kmk
echo "VBOX_PATH_APP_PRIVATE      := %vboxdatadir" >> LocalConfig.kmk
echo "VBOX_PATH_APP_DOCS         := %_defaultdocdir/%name-doc-%version" >> LocalConfig.kmk
echo "VBOX_PATH_PACKAGE_DOCS     := \$(VBOX_PATH_APP_DOCS)" >> LocalConfig.kmk
echo "VBOX_VENDOR                := ALT Linux Team" >> LocalConfig.kmk
echo "VBOX_VENDOR_SHORT          := ALT" >> LocalConfig.kmk
echo "VBOX_PRODUCT               := VM VirtualBox OSE" >> LocalConfig.kmk

source env.sh
[ -n "$NPROCS" ] || NPROCS=%__nprocs
kmk -j$NPROCS VBOXDIR=%vboxdir

%install

source env.sh
[ -n "$NPROCS" ] || NPROCS=%__nprocs
kmk -j$NPROCS VBOXDIR=%vboxdir

mkdir -p %buildroot{%_bindir,%_sbindir,%vboxdir/ExtensionPacks,%vboxdatadir,%kernel_src,%_initrddir,%_sysconfdir/udev/rules.d}

# install common
install -Dp %SOURCE1 %buildroot%_controldir/%name
install -Dp %SOURCE2 %buildroot%_initdir/%name
install -Dp -m644 %SOURCE4 \
	%buildroot%_sysconfdir/udev/rules.d/90-%name.rules

%if %build_additions
# install additions from src
install -Dp %SOURCE7 %buildroot%_initdir/vboxadd
install -Dp %SOURCE8 %buildroot%_initdir/vboxadd-service
install -Dp -m644 %SOURCE3 %buildroot%_sysconfdir/udev/rules.d/60-vboxadd.rules

#install -d %buildroot%_sysconfdir/hal/fdi/policy
#install -m644 src/VBox/Additions/linux/installer/90-vboxguest.fdi %buildroot%_sysconfdir/hal/fdi/policy/90-vboxguest.fdi

install -d %buildroot%_sysconfdir/X11/xinit.d
install -m755 src/VBox/Additions/x11/Installer/98vboxadd-xclient %buildroot%_sysconfdir/X11/xinit.d

install -Dp -m644 %SOURCE18 \
	%buildroot%_sysconfdir/udev/rules.d/70-xorg-vboxmouse.rules
mkdir -p %buildroot%_x11sysconfdir/xorg.conf.d
install -Dp -m644 %SOURCE19 \
	%buildroot%_x11sysconfdir/xorg.conf.d/50-vboxmouse.conf
%endif

# install application
cd out/%vbox_platform/release/bin

#    SUPInstall \
#    SUPUninstall \
#    EfiThunk \
cp -a \
    VBoxBFE \
    VBoxExtPackHelperApp \
    VBoxHeadless \
    VBoxManage \
    VBoxNetAdpCtl \
    VBoxNetDHCP \
    VBoxSDL \
    VBoxSVC \
    VBoxTestOGL \
    VBoxTunctl \
    VBoxXPCOMIPCD \
    VirtualBox \
    xpidl \
    *.gc \
    *.r0 \
    *.so \
    *.fd \
    *.py \
    components/ \
    sdk/ \
    %buildroot%vboxdir

cp -a \
    VBoxCreateUSBNode.sh \
    nls/ \
    %buildroot%vboxdatadir

# create links
for n in VBoxBFE VBoxManage VBoxSDL VirtualBox VBoxTunctl xpidl; do
    ln -s $(relative %vboxdir/$n %_bindir/$n) %buildroot%_bindir
done

# install kernel sources
cp -a src/vboxdrv %buildroot%kernel_src/%modname-%version
cp -a src/vboxpci %buildroot%kernel_src/%modnamepci-%version
cp -a src/vboxnetflt %buildroot%kernel_src/%modnamenetflt-%version
cp -a src/vboxnetadp %buildroot%kernel_src/%modnamenetadp-%version
tar -C %buildroot%kernel_src -c %modname-%version | bzip2 -c > \
    %buildroot%kernel_src/%modname-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modname-%version
tar -C %buildroot%kernel_src -c %modnamepci-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamepci-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modnamepci-%version
tar -C %buildroot%kernel_src -c %modnamenetflt-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamenetflt-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modnamenetflt-%version
tar -C %buildroot%kernel_src -c %modnamenetadp-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamenetadp-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modnamenetadp-%version

cd additions >/dev/null
# install additions kernel sources
  cp -a src/vboxguest %buildroot%kernel_src/%modnameguest-%version
  tar -C %buildroot%kernel_src -c %modnameguest-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnameguest-%version.tar.bz2
  rm -rf %buildroot%kernel_src/%modnameguest-%version

# install VFS kernel sources
  cp -a src/vboxsf %buildroot%kernel_src/%modnamevfs-%version
  tar -C %buildroot%kernel_src -c %modnamevfs-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamevfs-%version.tar.bz2
  rm -rf %buildroot%kernel_src/%modnamevfs-%version

# install VFS kernel sources
  cp -a src/vboxvideo %buildroot%kernel_src/%modnamevideo-%version
  tar -C %buildroot%kernel_src -c %modnamevideo-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamevideo-%version.tar.bz2
  rm -rf %buildroot%kernel_src/%modnamevideo-%version

%if %build_additions
  mkdir -p %buildroot%vboxadddir

# install additions
  cp -a \
    VBoxClient \
    VBoxControl \
    VBoxService \
    VBox*.so \
    %buildroot%vboxadddir

# create links
  for n in VBoxClient VBoxControl VBoxService; do
    ln -s $(relative %vboxadddir/$n %_bindir/$n) %buildroot%_bindir
  done
  ln -s $(relative %vboxadddir/VBoxService %_sbindir/) %buildroot%_sbindir/vboxadd-service

# install sysconfig for vboxadd-service
  mkdir -p %buildroot%_sysconfdir/sysconfig
  cp %SOURCE6 %buildroot%_sysconfdir/sysconfig/vboxadd-service

# install mount vbox share folder
  install -d %buildroot/sbin
  install -m755 mount.vboxsf %buildroot/sbin/mount.vboxsf

  install -d %buildroot%_sysconfdir/security/console.perms.d/
  install -m644 %SOURCE5 %buildroot%_sysconfdir/security/console.perms.d/

# install x11 drivers
  install -d %buildroot%_x11modulesdir/{input,drivers}
  install ../vboxmouse_drv.so %buildroot%_x11modulesdir/input/vboxmouse_drv.so
  install vboxvideo_drv.so %buildroot%_x11modulesdir/drivers/vboxvideo_drv.so
%endif
cd - >/dev/null

# install icons
mkdir -p %buildroot%_niconsdir
install -m644 icons/32x32/*.png %buildroot%_niconsdir/
mkdir -p %buildroot%_miconsdir
install -m644 icons/16x16/*.png %buildroot%_miconsdir/
mkdir -p %buildroot%_liconsdir
install -m644 icons/48x48/*.png %buildroot%_liconsdir/
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
install -m644 icons/64x64/*.png %buildroot%_iconsdir/hicolor/64x64/apps/
mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps
install -m644 icons/128x128/*.png %buildroot%_iconsdir/hicolor/128x128/apps/

# install mime types
mkdir -p %buildroot%_xdgmimedir/packages
install -m644 virtualbox.xml %buildroot%_xdgmimedir/packages/virtualbox.xml

# install menu entries
mkdir -p %buildroot%_desktopdir
install -m644 virtualbox.desktop %buildroot%_desktopdir/

# install docs
mkdir -p %buildroot%_defaultdocdir/%name-doc-%version
cp %SOURCE13 %SOURCE17 %SOURCE20 %buildroot%_defaultdocdir/%name-doc-%version/
tar -xf %SOURCE21 -C %buildroot%_defaultdocdir/%name-doc-%version/

%pre
%pre_control %name

%post
%post_control -s vboxusers %name

%pre common
/usr/sbin/groupadd -r -f vboxusers

%post common
%post_service %name

%preun common
%preun_service %name

%triggerin common -- dev
# If using static /dev, select the same status again to fix permissions
mountpoint -q /dev || {
	status="`/usr/sbin/control %name status`" || status=
	[ -n "$status" ] && /usr/sbin/control %name "$status" ||:
}

%pre guest-additions
/usr/sbin/groupadd -r -f vboxadd

%files
%_bindir/*
%exclude %_bindir/xpidl
%if %build_additions
%exclude %_bindir/VBoxClient
%exclude %_bindir/VBoxControl
%exclude %_bindir/VBoxService
%exclude %vboxadddir
%endif
%dir %vboxdir
%dir %vboxdir/ExtensionPacks
%attr(4710,root,vboxusers) %vboxdir/VBoxHeadless
%attr(4710,root,vboxusers) %vboxdir/VBoxNetDHCP
%attr(4710,root,vboxusers) %vboxdir/VBoxNetAdpCtl
%attr(4710,root,vboxusers) %vboxdir/VBoxSDL
%attr(4710,root,vboxusers) %vboxdir/VirtualBox
%vboxdir/*
%exclude %vboxdir/sdk
%exclude %vboxdir/xpidl
%vboxdatadir/nls
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%_iconsdir/hicolor/64x64/apps/*.png
%_iconsdir/hicolor/128x128/apps/*.png
%_xdgmimedir/packages/*.xml
%_desktopdir/*.desktop
%_controldir/%name

%files -n %modname
%kernel_src/%modname-%version.tar.bz2

%files -n %modnamepci
%kernel_src/%modnamepci-%version.tar.bz2

%files -n %modnamenetflt
%kernel_src/%modnamenetflt-%version.tar.bz2

%files -n %modnamenetadp
%kernel_src/%modnamenetadp-%version.tar.bz2

%files -n %modnameguest
%kernel_src/%modnameguest-%version.tar.bz2

%files -n %modnamevfs
%kernel_src/%modnamevfs-%version.tar.bz2

%files -n %modnamevideo
%kernel_src/%modnamevideo-%version.tar.bz2

%if %build_additions
%files -n xorg-drv-vboxmouse
%_x11modulesdir/input/vboxmouse_drv.so

%files -n xorg-drv-vboxvideo
%_x11modulesdir/drivers/vboxvideo_drv.so

%files guest-utils
/sbin/mount.vboxsf
%_initrddir/vboxadd
%_initrddir/vboxadd-service
%config(noreplace) %_sysconfdir/sysconfig/vboxadd-service
#_sysconfdir/hal/fdi/policy/90-vboxguest.fdi
%config %_sysconfdir/udev/rules.d/60-vboxadd.rules
%_sbindir/vboxadd-service
%_bindir/VBoxControl
%_bindir/VBoxService
%_sysconfdir/security/console.perms.d/60-vboxadd.perms
%dir %vboxadddir
%vboxadddir/VBoxControl
%vboxadddir/VBoxService

%files guest-additions
%_sysconfdir/X11/xinit.d/98vboxadd-xclient
%config %_sysconfdir/udev/rules.d/70-xorg-vboxmouse.rules
%config %_x11sysconfdir/xorg.conf.d/50-vboxmouse.conf
%_bindir/VBoxClient
%vboxadddir/VBoxClient
%vboxadddir/*.so
%endif

%files common
%_initdir/%name
%config %_sysconfdir/udev/rules.d/90-%name.rules
%dir %vboxdatadir
%vboxdatadir/VBoxCreateUSBNode.sh

%files doc
%_defaultdocdir/%name-doc-%version

%files sdk
%_bindir/xpidl
%vboxdir/xpidl
%vboxdir/sdk

%changelog
* Wed Apr 04 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt2
- Enable the built in VNC server
- Avoid conflict with renamed xorg-drv modules

* Wed Apr 04 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt1
- Update to new release for Sisyphus
- Fix build vboxvideo with new xorg-server-1.12

* Sun Apr 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.10-alt1
- Update to new release
- Add subpackage virtualbox-guest-utils with basic guest addition tools
  without dependency to xorg server

* Fri Dec 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.6-alt1
- Update to new release with minor bugfixes:
 + VRDP: fixed screen corruption
 + NAT: the interface stopped working after a lot of failed ICMP requests
 + ATA: fixed a possible crash during ATAPI passthrough with certain guests
 + ATA: improved compatibility with ancient Linux kernels 
 + Main: fixed incorrect framebuffer information after leaving the
   fullscreen mode with X11 guests

* Fri Nov 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.4-alt1.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.4-alt1
- Update to new release
- Added kernel source subpackage for vboxpci module

* Sat Jul 23 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.12-alt1
- Update to new release
- Fix problems with guest addition init scripts.

* Tue May 03 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt4
- Adopt and apply Ubuntu patch for build the X.Org driver only
  for the selected system X Server version with native includes

* Mon May 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt3
- Rebuild with xorg-server-1.10
- Apply patches from Ubuntu build:
 + Fix build failure with kernel 2.6.39-rc1
 + Fix FTBFS with ld --as-needed
 + Make Xsession.d script ignore errors

* Tue Mar 01 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt2
- Add missed VBoxExtPackHelperApp

* Tue Feb 22 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt1
- Update to new release
+ Fix ALT Linux OS type support
+ Set Default OS type to Linux
+ Replace nls files to vboxdatadir
+ Add udev rules for USB (works only for vboxusers group now)
+ Add HTML documentation
+ Register mime types for next extensions:
 *.vbox - VirtualBox Machine Definition
 *.vbox-extpack - VirtualBox Extension Pack
 *.ovf - Open Virtualization Format
 *.ova - Open Virtualization Format Archive

* Wed Jan 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.12-alt1
- Update to new release
- Adjust addittional xorg drivers for xorg-server-1.9.x
- Set fixed rpath to VBOXDIR
- Add SDK Reference to documentation

* Thu Dec 16 2010 Michail Yakushin <silicium@altlinux.ru> 3.2.4-alt4
- Fix build

* Fri Jun 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt3
- Fix RuntimeGuestR3Mini linkage with rtThreadGet() for xorg addition drivers
- Fix vboxmouse default installation (Closes: 23479)

* Thu Jun 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt2
- Add build require for libpam-devel

* Mon Jun 09 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt1
- Update to new release

* Mon May 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.8-alt1
- Update to new release
- Rename kernel-source subpackages (Closes: 22458)
- Copy additional video drivers for xorg-server-1.8

* Sat Mar 27 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.6-alt1
- Update to new release

* Wed Mar 03 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.4-alt1
- Update to lastest release (Closes: 22556)

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.10-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for virtualbox
  * postclean-05-filetriggers for spec file

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.10-alt1.1
- Rebuilt with python 2.6

* Tue Nov 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Update to new release

* Wed Oct 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.8-alt1
- Update to new release
- Add various files for guest-addition (#21727)

* Sun Sep 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.6-alt1
- Update to new release

* Tue Aug 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.4-alt1
- Update to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Fix vboxadd-service sysconfig file installation
- Update to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt3
- Fix guest addition initscripts

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt2
- Add new VBoxNetAdpCtl utility and VBoxNetDHCP feature
- Add support for new kernel modules
- Added kernel source subpackage for netadaptor module
- Added kernel source subpackage for video module

* Wed Jul 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt1
- Update to new release

* Tue Jun 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.4-alt1
- Update to new release
- Build with gcc-4.3

* Sun May 10 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.2-alt1
- Update to new release

* Mon Mar 09 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt5
- Build with last xorg drivers

* Sat Mar 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt4
- Added ALT Linux OS type

* Sat Mar 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt3
- Avoided addition installation to main packages
- Applied vbox-evdev.patch

* Sat Mar 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt2
- Fixed for building witn glibc-kernheaders >= 2.6.28

* Wed Feb 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt1
- Update to new release
- Requires added to base package from common subpackage (#18434)

* Thu Feb 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.2-alt1
- Update to new release

* Wed Feb 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt4
- Fixed SDK package instalation due silly python requires for _xpcom

* Wed Feb 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt3
- Fixed problem with different set of noarch packages for i586
  with x86_64 build

* Wed Feb 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt2
- Build for x86_64
- Remove vbox-guest-additions from modprobe.d and add initscirpt
  instead (#18282)
- Build fixes (thanks for vsu@)
 + Put uncompressed tarball into src.rpm
 + Honor NPROCS and %__nprocs when invoking kmk
 + Add workarounds for missing biarch support and enable x86_64 build

* Fri Dec 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt1
- Update to new release
- Fixed bug with control adjust for setuid binary (#18170)
- Fixed rpath and initscripts patches for new version
- Added kernel source subpackage for vboxnetflt module
- Fixed virtualbox initscript for vboxnetflt module using
- Added sdk subpackage

* Sun Nov 02 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Update to new release

* Thu Sep 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Updated to new release
- Removed not needed and bad patches:
 + vbox-vboxfs-2.6.25.diff - not used
 + virtualbox-missing-Makefiles.diff - fixed in new version
 + use-o3-to-workaround-gcc-ice.diff - bad on gcc-4.1
- Prepared to build for x86_64 (not ready yet)

* Fri Aug 29 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.4-alt1
- Updated to new version
- Added documentation subpackage with UserManual.pdf (#16700)
- Added links for VBoxTunctl, VBoxAddIF and VBoxDeleteIF (#16700)
- Fixed desktop file (#16700)

* Sat Jun 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.2-alt1
- Updated to 1.6.2
- Fixed building patches

* Sat Jun 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.0-alt0
- Updated to 1.6.0
- Fixed requires

* Fri Apr 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt2
- Removed SysVinit version at requires

* Sat Apr 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt1
- Add nls for i18n support

* Thu Mar 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt0.1
- Build new version

* Mon Apr 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.99-alt0.r2155
- SVN r2155
- symlink binaries into %%_bindir
- add udev rules file for /dev/vboxdrv

* Sun Apr 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.99-alt0.r1788
- SVN r1788

* Sat Feb 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.99-alt0.r934
- initial build
