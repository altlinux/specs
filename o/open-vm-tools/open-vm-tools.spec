%define _unpackaged_files_terminate_build 1

# like subst_with, but replacing '_' with '-'
%define subst_enable_dash() %{expand:%%(echo '%%{subst_enable %1}' | sed 's/_/-/g')}

%filter_from_requires /\/usr\/bin\/java/d

%def_enable vgauth
%def_enable xmlsec1
%def_disable xmlsecurity

%def_enable deploypkg
%def_enable multimon
%def_without dnet
%def_enable resolutionkms
%def_enable servicediscovery
%def_enable salt_minion

%def_without gtk2
%def_without gtkmm
%def_with gtk3
%def_with gtkmm3

%global majorversion    12.5
%global minorversion    0
%global toolsbuild      24276846
%global toolsversion    %majorversion.%minorversion
%global toolsdaemon     vmtoolsd
%global vgauthdaemon    vgauthd

Name: open-vm-tools
Version: %toolsversion
Release: alt1
Summary: Open Virtual Machine Tools for virtual machines hosted on VMware
Group: System/Kernel and hardware
License: GPLv2
Url: http://%name.sourceforge.net/
Source0: %name-%version.tar
Source1: %toolsdaemon.service
Source11: %vgauthdaemon.service
Source2: %toolsdaemon.init
Source12: %vgauthdaemon.init
Source3: %name.rules
Source4: %name-desktop.tmpfile
Source5: %toolsdaemon.pam
Source6: %name-%vgauthdaemon.tmpfile
Source90: 90-vmware-guest-tools.rules
Source99: 99-vmware-scsi-udev.rules

Patch100: add-altlinux-open-vm-tools.patch

ExclusiveArch: %ix86 x86_64 aarch64

# Need for vgauth
%{?_enable_xmlsec1:Requires: libxmlsec1-openssl >= 1.2.24-alt2}

BuildRequires: gcc-c++
BuildRequires: doxygen
# Fuse is optional and enables vmblock-fuse
BuildRequires: libfuse3-devel
BuildRequires: glib2-devel >= 2.34.0
BuildRequires: gtk2-devel >= 2.4.0
BuildRequires: libgtkmm2-devel libsigc++2-devel
BuildRequires: libgtk+3-devel >= 2.4.0
BuildRequires: libgtkmm3-devel libsigc++2-devel
BuildRequires: libpam-devel
BuildRequires: libtirpc-devel
BuildRequires: rpcgen
BuildRequires: libgdk-pixbuf-xlib-devel
%{?_with_dnet:BuildRequires: libdnet-devel}
%{?_enable_multimon:BuildRequires: libX11-devel libXext-devel libXinerama-devel libXi-devel libXrender-devel libXrandr-devel libXtst-devel libICE-devel libSM-devel libXcomposite-devel}
%{?_enable_deploypkg:BuildRequires: libmspack-devel}
%{?_enable_vgauth:BuildRequires: libssl-devel}
%{?_enable_xmlsec1:BuildRequires: libxmlsec1-devel libxml2-devel}
%{?_enable_xmlsecurity:BuildRequires: libxml-security-c-devel libxerces-c-devel}
%{?_enable_resolutionkms:BuildRequires: libdrm-devel libudev-devel}

#BuildRequires:          kernel-headers-modules-std-def

Requires: udev-rules-hotplug-cpu

%description
The %name project is an open source implementation of VMware Tools. It
is a suite of open source virtualization utilities and drivers to improve the
functionality, user experience and administration of VMware virtual machines.
This package contains only the core user-space programs and libraries of
%name.

%package desktop
Summary: User experience components for Open Virtual Machine Tools
Group: System/Configuration/Other
Requires: %name = %version-%release

%description desktop
This package contains only the user-space programs and libraries of
%name that are essential for improved user experience of VMware virtual
machines.

%package devel
Summary: Development libraries for Open Virtual Machine Tools
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains only the user-space programs and libraries of
%name that are essential for developing customized applications for
VMware virtual machines.

%package salt-minion
Summary: Script file to install/uninstall salt-minion
Group: System/Configuration/Other
Requires: %name = %version-%release
ExclusiveArch: x86_64

%description salt-minion
This package contains a script to setup Salt Minion on VMware virtual machines.

%package test
Summary: Test utilities for Open Virtual Machine Tools
Group: Development/Other
Requires: %name = %version-%release

%description test
This package contains only the test utilities for %name that are
useful for verifying the functioning of %name in VMware virtual
machines.

%prep
%setup
#%%patch100 -p1

rm -rf autom4te.cache
rm -f configure

%build
export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++11"
%autoreconf

%undefine _configure_gettext
%configure \
    --without-kernel-modules \
    --without-root-privileges \
    %{subst_enable vgauth} \
    %{subst_enable xmlsec1} \
    %{subst_enable xmlsecurity} \
    %{subst_enable deploypkg} \
    %{subst_enable multimon} \
    %{subst_with dnet} \
    %{subst_with gtk2} \
    %{subst_with gtkmm} \
    %{subst_with gtk3} \
    %{subst_with gtkmm3} \
    %{subst_enable resolutionkms} \
    %{subst_enable servicediscovery} \
    %{subst_enable_dash salt_minion} \
    --disable-static
# sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
# export DONT_STRIP=1
%makeinstall_std

mv %buildroot%_sysconfdir/vmware-tools/tools.conf.example %buildroot%_sysconfdir/vmware-tools/tools.conf
chmod a-x %buildroot%_sysconfdir/vmware-tools/*.conf
sed -i '/^\[deployPkg\]/a enable-custom-scripts=true' %buildroot%_sysconfdir/vmware-tools/tools.conf
# Remove exec bit from config files
chmod a-x %buildroot%_sysconfdir/pam.d/*
%if_enabled vgauth
chmod a-x %buildroot%_sysconfdir/vmware-tools/vgauth/schemas/*
%endif

# Remove exec bit on udev rules
chmod a-x %buildroot%_udevrulesdir/99-vmware-scsi-udev.rules

# Remove the DOS line endings
sed -i "s|\r||g" README

# Remove "Encoding" key from the "Desktop Entry"
sed -i "s|^Encoding.*$||g" %buildroot%_sysconfdir/xdg/autostart/vmware-user.desktop

# Remove unnecessary files from packaging
find %buildroot%_libdir -name '*.la' -delete
rm -fr %buildroot%_defaultdocdir
rm -f docs/api/build/html/FreeSans.ttf

# Systemd unit files
install -p -m 644 -D %SOURCE1 %buildroot%_unitdir/%toolsdaemon.service
install -p -m 644 -D %SOURCE11 %buildroot%_unitdir/%vgauthdaemon.service
# SysV init script
install -p -m 755 -D %SOURCE2 %buildroot%_initdir/%toolsdaemon
install -p -m 755 -D %SOURCE12 %buildroot%_initdir/%vgauthdaemon
# udev rules
install -p -m 644 -D %SOURCE3 %buildroot%_udevrulesdir/98-%name.rules
install -p -m 644 -D %SOURCE90 %buildroot%_udevrulesdir/90-vmware-guest-tools.rules
# install fixed udev rules
install -p -m 644 -D %SOURCE99 %buildroot%_udevrulesdir/99-vmware-scsi-udev.rules
# tmpfiles
install -p -m 644 -D %SOURCE4 %buildroot%_tmpfilesdir/%name-desktop.conf
install -p -m 644 -D %SOURCE6 %buildroot%_tmpfilesdir/%name-%vgauthdaemon.conf
# pam
install -p -m 644 -D %SOURCE5 %buildroot%_sysconfdir/pam.d/%toolsdaemon

mkdir -p %buildroot%_runtimedir/vmware
# 'make check' in open-vm-tools rebuilds docs and ends up regenerating
# the font file. We can add %%check secion once 'make check' is fixed
# upstream

%post
# Setup mount point for Shared Folders
if [ -f %_bindir/vmware-checkvm -a                     \
     -f %_bindir/vmhgfs-fuse ] &&                      \
    %_bindir/systemd-detect-virt | grep -iq VMware &&   \
    %_bindir/vmware-checkvm &> /dev/null &&             \
    %_bindir/vmware-checkvm -p | grep -q Workstation && \
    %_bindir/vmhgfs-fuse -e &> /dev/null; then
    mkdir -p /mnt/hgfs
fi

%post_service %vgauthdaemon
%post_service %toolsdaemon

%preun
%preun_service %toolsdaemon
%preun_service %vgauthdaemon
# Tell VMware that open-vm-tools is being uninstalled
if [ "$1" = "0" -a                                      \
    -f %_bindir/vmware-checkvm ] &&                     \
    %_bindir/systemd-detect-virt | grep -iq VMware &&   \
     %_bindir/vmware-checkvm &> /dev/null; then

   # Tell VMware that open-vm-tools is being uninstalled
   if [ -f %_bindir/vmware-rpctool ]; then
      %_bindir/vmware-rpctool 'tools.set.version 0' &> /dev/null || true
   fi

   # Teardown mount point for Shared Folders
   if [ -d /mnt/hgfs ] &&                               \
      %_bindir/vmware-checkvm -p | grep -q Workstation; then
      umount /mnt/hgfs &> /dev/null || /bin/true
      rmdir /mnt/hgfs &> /dev/null || /bin/true
   fi
fi

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %_sysconfdir/pam.d/*
%dir %_sysconfdir/vmware-tools
%if_enabled vgauth
%dir %_sysconfdir/vmware-tools/vgauth
%dir %_sysconfdir/vmware-tools/vgauth/schemas
%config(noreplace) %_sysconfdir/vmware-tools/*.conf
%config %_sysconfdir/vmware-tools/vgauth/schemas/*
%_initdir/%vgauthdaemon
%_unitdir/%vgauthdaemon.service
%_runtimedir/vmware
%_tmpfilesdir/%name-%vgauthdaemon.conf
%_bindir/vmware-vgauth-cmd
%_bindir/VGAuthService
%_libdir/libvgauth.so.*
%endif
%_sysconfdir/vmware-tools/*-vm-default
%_sysconfdir/vmware-tools/scripts
%_sysconfdir/vmware-tools/statechange.subr
%_bindir/vm-support
%_bindir/vmhgfs-fuse
%_bindir/vmtoolsd
%_bindir/vmwgfxctrl
%_bindir/vmware-alias-import
%_bindir/vmware-checkvm
%_bindir/vmware-hgfsclient
%_bindir/vmware-namespace-cmd
%_bindir/vmware-rpctool
%_bindir/vmware-toolbox-cmd
%_bindir/vmware-xferlogs
%_libdir/libDeployPkg.so.*
%_libdir/libguestlib.so.*
%_libdir/libguestStoreClient.so.*
%_libdir/libhgfs.so.*
%_libdir/libvmtools.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/common
%_libdir/%name/plugins/common/*.so
%dir %_libdir/%name/plugins/vmsvc
%_libdir/%name/plugins/vmsvc/*.so
%_datadir/%name/
%_unitdir/%toolsdaemon.service
%_initdir/%toolsdaemon
%_udevrulesdir/*.rules
%if_enabled servicediscovery
%_libdir/%name/serviceDiscovery
%endif

%files desktop
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/vmware-user
%_bindir/vmware-user-suid-wrapper
%_bindir/vmware-vmblock-fuse
%_libdir/%name/plugins/vmusr/
%_tmpfilesdir/%name-desktop.conf

%files devel
%doc docs/api/build/*
%_includedir/vmGuestLib
%_includedir/libDeployPkg
%_libdir/pkgconfig/*.pc
%_libdir/libDeployPkg.so
%_libdir/libguestlib.so
%_libdir/libguestStoreClient.so
%_libdir/libhgfs.so
%_libdir/libvmtools.so
%if_enabled vgauth
%_libdir/libvgauth.so
%endif

%ifarch x86_64
%files salt-minion
%dir %_libdir/%name/componentMgr/
%dir %_libdir/%name/componentMgr/saltMinion/
%_libdir/%name/componentMgr/saltMinion/svtminion.sh
%endif

%if_enabled vgauth
%files test
%_bindir/vmware-vgauth-smoketest
%endif


%changelog
* Thu Oct 10 2024 Andrew A. Vasilyev <andy@altlinux.org> 12.5.0-alt1
- 12.5.0 (CVE-2024-40896)
- remove Java from R: (Closes: #50869)

* Fri Jun 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 12.4.5-alt1
- 12.4.5

* Sun Mar 24 2024 Andrew A. Vasilyev <andy@altlinux.org> 12.4.0-alt1
- 12.4.0

* Fri Oct 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 12.3.5-alt1
- 12.3.5 (CVE-2023-34058, CVE-2023-34059)

* Thu Aug 31 2023 Andrew A. Vasilyev <andy@altlinux.org> 12.3.0-alt1
- 12.3.0 (CVE-2023-20900)

* Tue Aug 29 2023 Anton Midyukov <antohami@altlinux.org> 12.2.5-alt3
- NMU: replace /var/run/ with /run, /var/lock with /run/lock (Closes: 35890)

* Sat Jul 15 2023 Alexey Shabalin <shaba@altlinux.org> 12.2.5-alt2
- add udev rule for autostart vmtoolsd.service
- update pam config
- run vgauthd together with vmtoolsd

* Wed Jun 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 12.2.5-alt1
- 12.2.5 (CVE-2023-20867)

* Wed Mar 08 2023 Andrew A. Vasilyev <andy@altlinux.org> 12.2.0-alt1
- 12.2.0

* Wed Nov 30 2022 Andrew A. Vasilyev <andy@altlinux.org> 12.1.5-alt1
- 12.1.5

* Wed Aug 24 2022 Andrew A. Vasilyev <andy@altlinux.org> 12.1.0-alt1
- 12.1.0

* Wed May 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 12.0.5-alt1
- 12.0.5
- add salt-minion package

* Sat Mar 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 12.0.0-alt1
- 12.0.0

* Fri Sep 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 11.3.5-alt1
- 11.3.5

* Thu Aug 12 2021 Andrew A. Vasilyev <andy@altlinux.org> 11.3.0-alt2
- set enable-custom-scripts=true by default

* Sun Jun 20 2021 Andrew A. Vasilyev <andy@altlinux.org> 11.3.0-alt1
- 11.3.0

* Wed Mar 31 2021 Andrew A. Vasilyev <andy@altlinux.org> 11.2.5-alt2
- fix FTBFS

* Thu Jan 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 11.2.5-alt1
- 11.2.5

* Fri Nov 06 2020 Andrew A. Vasilyev <andy@altlinux.org> 11.2.0-alt1
- 11.2.0

* Tue Sep 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 11.1.5-alt1
- 11.1.5

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 11.1.0-alt1
- 11.1.0
- build for aarch64
- enable servicediscovery

* Fri Mar 06 2020 Alexey Shabalin <shaba@altlinux.org> 11.0.5-alt3
- readd detect ALT Distro

* Thu Mar 05 2020 Alexey Shabalin <shaba@altlinux.org> 11.0.5-alt2
- enable deploypkg support
- add test package

* Fri Feb 21 2020 Alexey Shabalin <shaba@altlinux.org> 11.0.5-alt1
- 11.0.5

* Sat Sep 28 2019 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt1
- 11.0.0

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 10.3.10-alt1
- 10.3.10

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.5-alt1
- 10.3.5

* Mon Sep 10 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.0-alt1
- 10.3.0

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 10.1.10-alt1.S1.1
- NMU: rebuild with new openssl.

* Sun Aug 06 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.10-alt1
- 10.1.10
- build with gtk3 to sisyphus, and with gtk2 to p8
- build with vgauth

* Thu Jul 21 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt4
- add basealt detection

* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt3
- fix to use git repo for source instead of tarball

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt1.M70P.1
- build for M70P

* Wed Feb 24 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt2
- fix search for alt linux
- clean package release from toolsbuild

* Wed Feb 24 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt1.3227872
- new version

* Fri Dec 25 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.5-alt1.3227872
- 10.0.5

* Mon Sep 14 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.0-alt1.3000743
- open-vm-tools-10.0.0-3000743

* Thu Aug 13 2015 Alexey Shabalin <shaba@altlinux.ru> 9.10.2-alt1
- 9.10.2

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.10.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Apr 13 2015 Alexey Shabalin <shaba@altlinux.ru> 9.10.0-alt1
- 9.10.0

* Sat Apr 11 2015 Andrey Cherepanov <cas@altlinux.org> 9.4.6-alt1
- Initial build in Sisyphus (from Fedora)
