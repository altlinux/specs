
%def_disable vgauth
%def_disable grabbitmqproxy
%def_disable deploypkg
%def_enable multimon
%def_with dnet
%def_with gtk2
%def_with gtkmm

%global majorversion    10.0
%global minorversion    7
%global toolsbuild      3227872
%global toolsversion    %majorversion.%minorversion
%global toolsdaemon     vmtoolsd

Name: open-vm-tools
Version: %toolsversion
Release: alt3
Summary: Open Virtual Machine Tools for virtual machines hosted on VMware
Group: System/Kernel and hardware
License: GPLv2
Url: http://%name.sourceforge.net/
Source0: %name-%version.tar
Source1: %toolsdaemon.service
Source2: %toolsdaemon.init
Source3: %name.udev
Source4: %name-desktop.tmpfile
Source5: %toolsdaemon.pam

Patch100: add-altlinux-open-vm-tools.patch

BuildRequires: gcc-c++
BuildRequires: doxygen
# Fuse is optional and enables vmblock-fuse
BuildRequires: libfuse-devel
BuildRequires: glib2-devel >= 2.14.0
%{?_with_gtk2:BuildRequires: gtk2-devel >= 2.4.0}
%{?_with_gtkmm:BuildRequires: libgtkmm2-devel}
BuildRequires: libicu-devel
BuildRequires: libpam0-devel
BuildRequires: libprocps-devel
%{?_with_dnet:BuildRequires: libdnet-devel}
%{?_enable_multimon:BuildRequires: libX11-devel libXext-devel libXinerama-devel libXi-devel libXrender-devel libXrandr-devel libXtst-devel libICE-devel libSM-devel libXcomposite-devel}
%{?_enable_deploypkg:BuildRequires: libmspack-devel}
%{?_enable_vgauth:BuildRequires: libssl-devel libxerces-c-devel libxml-security-c-devel}
%{?_enable_grabbitmqproxy:BuildRequires: libssl-devel}

#BuildRequires:          kernel-headers-modules-std-def

%description
The %name project is an open source implementation of VMware Tools. It
is a suite of open source virtualization utilities and drivers to improve the
functionality, user experience and administration of VMware virtual machines.
This package contains only the core user-space programs and libraries of
%name.

%package desktop
Summary: User experience components for Open Virtual Machine Tools
Group: System/Libraries
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

%prep
%setup
%patch100 -p1

rm -rf autom4te.cache
rm -f configure

%build
export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++11"
export CUSTOM_PROCPS_NAME=procps
%autoreconf
%undefine _configure_gettext
%configure \
    --without-kernel-modules \
    --without-root-privileges \
    %{subst_enable vgauth} \
    %{subst_enable grabbitmqproxy} \
    %{subst_enable deploypkg} \
    %{subst_enable multimon} \
    %{subst_with dnet} \
    %{subst_with gtk2} \
    %{subst_with gtkmm} \
    --disable-static
# sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
# export DONT_STRIP=1
%makeinstall_std

# Remove exec bit from config files
chmod a-x %buildroot%_sysconfdir/pam.d/*
%if_enabled vgauth
chmod a-x %buildroot%_sysconfdir/vmware-tools/*.conf
chmod a-x %buildroot%_sysconfdir/vmware-tools/vgauth/schemas/*
%endif
# Remove the DOS line endings
sed -i "s|\r||g" README

# Remove "Encoding" key from the "Desktop Entry"
sed -i "s|^Encoding.*$||g" %buildroot%_sysconfdir/xdg/autostart/vmware-user.desktop

# Remove unnecessary files from packaging
find %buildroot%_libdir -name '*.la' -delete
rm -fr %buildroot%_defaultdocdir
rm -f docs/api/build/html/FreeSans.ttf

# Remove mount.vmhgfs & symlink
rm -fr %buildroot%_sbindir %buildroot/sbin/mount.vmhgfs

# Move vm-support to /usr/bin
mv %buildroot%_sysconfdir/vmware-tools/vm-support %buildroot%_bindir

# Systemd unit files
install -p -m 644 -D %SOURCE1 %buildroot%_unitdir/%toolsdaemon.service
# SysV init script
install -p -m 755 -D %SOURCE2 %buildroot%_initdir/%toolsdaemon
# udev rules
install -p -m 644 -D %SOURCE3 %buildroot%_udevrulesdir/98-%name.rules
# tmpfiles
install -p -m 644 -D %SOURCE4 %buildroot%_tmpfilesdir/%name-desktop.conf
# pam
install -p -m 644 -D %SOURCE5 %buildroot%_sysconfdir/pam.d/%toolsdaemon

# 'make check' in open-vm-tools rebuilds docs and ends up regenerating
# the font file. We can add %%check secion once 'make check' is fixed
# upstream

%post
%post_service %toolsdaemon

%preun
%preun_service %toolsdaemon
# Tell VMware that open-vm-tools is being uninstalled
if [ "$1" = "0" -a                      \
     -e %_bindir/vmware-checkvm -a    \
     -e %_bindir/vmware-rpctool ] &&  \
     %_bindir/vmware-checkvm &> /dev/null; then
   %_bindir/vmware-rpctool 'tools.set.version 0' &> /dev/null || /bin/true
fi

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %_sysconfdir/pam.d/*
%dir %_sysconfdir/vmware-tools
%if_enabled vgauth
%dir %_sysconfdir/vmware-tools/vgauth
%dir %_sysconfdir/vmware-tools/vgauth/schemas
%config(noreplace) %_sysconfdir/vmware-tools/vgauth.conf
%config %_sysconfdir/vmware-tools/vgauth/schemas/*
%endif
%_sysconfdir/vmware-tools/*-vm-default
%_sysconfdir/vmware-tools/scripts
%_sysconfdir/vmware-tools/statechange.subr
%_bindir/vmtoolsd
%_bindir/vmware-checkvm
%_bindir/vmware-hgfsclient
%_bindir/vmware-namespace-cmd
%_bindir/vmware-rpctool
%_bindir/vmware-toolbox-cmd
%_bindir/vmware-xferlogs
%_bindir/vm-support
%_libdir/libguestlib.so.*
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

%files desktop
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/vmware-user-suid-wrapper
%_bindir/vmware-vmblock-fuse
%_bindir/vmhgfs-fuse
%_libdir/%name/plugins/vmusr/
%_tmpfilesdir/*.conf

%files devel
%doc docs/api/build/*
%_includedir/vmGuestLib/
%_libdir/pkgconfig/*.pc
%_libdir/libguestlib.so
%_libdir/libhgfs.so
%_libdir/libvmtools.so

%changelog
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
