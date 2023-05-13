%define kernel_version   5.10
%define kernel_source /usr/src/kernel/sources/kernel-source-%kernel_version.tar
%define source_dir tools/usb/usbip
%define lname lib%name

%def_disable static

Name: usbip
Version: %kernel_version
Release: alt1

Summary: Utility for manage usbip devices

Group: System/Configuration/Networking
License: GPLv2+
Url: http://www.kernel.org

# used sources from kernel-source package
Source: %name-%version.tar

# Systemd units from Fedora
# TODO: maybe make a systemd user service for usbip, sth like usbip@.service?
# https://wiki.archlinux.org/index.php/USB/IP#Client_setup

Packager: Pavel Vainerman <pv@altlinux.org>

BuildRequires(pre): rpm-macros-systemd
BuildRequires: libudev-devel
BuildRequires: kernel-source-%kernel_version

Obsoletes: %name-client < %EVR
Provides:  %name-client = %EVR


%description
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

%package server
Summary: %name server daemon
Group: System/Configuration/Networking
Requires: %lname = %EVR
Obsoletes: %{name}d < %EVR
Provides:  %{name}d = %EVR

%description server
The USB/IP Project aims to develop a general USB device sharing system
over IP network. To share USB devices between computers with their full
functionality, USB/IP encapsulates "USB requests" into IP packets and
transmits them between computers. Original USB device drivers and
applications can be also used for remote USB devices without any
modification of them. A computer can use remote USB devices as if they
were directly attached; for example, we can:
  - USB storage devices: fdisk, mkfs, mount/umount, file operations,
    play a DVD movie and record a DVD-R media.
  - USB keyboards and USB mice: use with linux console and X Window
    System.
  - USB webcams and USB speakers: view webcam, capture image data and
    play some music.
  - USB printers, USB scanners, USB serial converters and USB Ethernet
    interfaces: ok, use fine.

%{name} server daemon.

%package -n %lname
Summary: %name shared library
Group: System/Libraries
#Requires: %_datadir/hwdata
Requires: hwdata

%description -n %lname
%name shared library.

%package -n %lname-devel
Summary: %name devel files
Group: Development/C

%description -n %lname-devel
%name devel files.

%package -n %lname-devel-static
Summary: %name static library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%name static library.


%prep
%setup
tar -xvf %kernel_source kernel-source-%kernel_version/%source_dir
cp -rf kernel-source-%kernel_version/%source_dir/* ./
rm -rf kernel-source-%kernel_version

%build
 %__subst 's| -Werror||g' configure.ac
./autogen.sh
%add_optflags -fcommon
%configure %{subst_enable static} --with-usbids-dir=%_datadir/hwdata
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_unitdir

install -Dp -m644 usbipd %buildroot%_sysconfdir/sysconfig/%{name}d
install -Dp -m644 usbipd.service %buildroot%_unitdir/%{name}d.service
ln -s %{name}d.service %buildroot%_unitdir/%{name}-server.service
install -Dp -m644 usbip-client.service %buildroot%_unitdir/%{name}-client.service

# Make usbip be inside PATH on client, it does not require root
mkdir -p %buildroot%_bindir
ln -s ../sbin/usbip %buildroot%_bindir/usbip


%post
%systemd_post usbip-client.service

%preun
%systemd_preun usbip-client.service

%postun
%systemd_postun_with_restart usbip-client.service

%post server
%systemd_post usbipd.service

%preun server
%systemd_preun usbipd.service

%postun server
%systemd_postun_with_restart usbipd.service


%files
%doc README
%_bindir/%name
%_sbindir/%name
%_unitdir/%{name}-client.service
%_man8dir/usbip.8*

%files server
%_sbindir/%{name}d
%_sysconfdir/sysconfig/%{name}d
%_unitdir/%{name}d.service
%_unitdir/%{name}-server.service
%doc README
%_man8dir/usbipd.8*

%files -n %lname
%_libdir/libusbip.so.*

%files -n %lname-devel
%_includedir/*
%_libdir/libusbip.so

%if_enabled static
%files -n %lname-devel-static
%_libdir/libusbip.a
%endif

%changelog
* Sat May 13 2023 Vitaly Lipatov <lav@altlinux.ru> 5.10-alt1
- build with sources from linux kernel 5.10 (ALT bug 40036)
- cleanup spec, merge with Fedora's pieces
- rename package usbipd to usbip-server
- obsolete package usbip-client in favor to usbip
- add post/preun service commands
- remove modules-load.d/*.conf packing (see service files)

* Sun Sep 05 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt8
- disable build devel-static

* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.4-alt7
- Fixed FTBFS with -fcommon.

* Tue Sep 18 2018 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt6
- rebuild for kernel 4.18.x

* Mon Sep 03 2018 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt5
- removed 'libwrap-devel' from BuildRequires

* Sat Mar 17 2018 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt4
- up build

* Sat Mar 17 2018 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt3
- added new package usbip-client (modules.conf for client side)
- added modules.conf for usbipd (server side)
- minor fixes

* Thu Feb 15 2018 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt2
- added service file

* Sat Dec 16 2017 Pavel Vainerman <pv@altlinux.ru> 2.0.4-alt1
- added kernel major version for package name

* Thu Dec 14 2017 Pavel Vainerman <pv@altlinux.ru> 2.0.1-alt0.1
- initial commit for build from kernel sources (usbip API 2.0)

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.1.1-alt2
- updated from 3.12 kernel tree

* Thu Aug 08 2013 Led <led@altlinux.ru> 1.1.1-alt1
- 1.1.1
- build from kernel source tree
- subpackages usbip-common and usbip-client replaced with usbip
- subpackage usbip-server replaced with usbipd

* Sat Apr 09 2011 Lenar Shakirov <snejok@altlinux.ru> 0.1.7-alt0.2
- intersections with system packages fixed:
  * %%_usrsrc/ -> %%kernel_src/

* Tue Nov 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt0.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libusbip
  * postun_ldconfig for libusbip

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.1.7-alt0.1
- SVN revision 82

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt2
- fixed kernel-source-usbip

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Jul 30 2007 Led <led@altlinux.ru> 0.1.5-alt1
- Initial build
- added %name-0.1.5-configure.patch
- added %name-0.1.5-alt-hwdatabase.patch
- added %name-0.1.5-zlib.patch
