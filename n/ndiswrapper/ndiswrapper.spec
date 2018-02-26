%define _sbinrootdir /sbin

Name: ndiswrapper
Version: 1.57
Release: alt1

Group: System/Configuration/Hardware
Summary: NdisWrapper allows you to use Windows WLAN card drivers
License: GPL
Url: http://ndiswrapper.sourceforge.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>

#Source0: 	http://prdownloads.sourceforge.net/ndiswrapper/%name-%version.tar.gz
Source0: %name-%version.tar.gz
# Mdk:
#Patch0: 	ndiswrapper-1.0-spaces.patch
# analogous to nvidia_glx deps:
#Requires: 	NDISWRAPPER_kernel

%description
Some vendors do not release specifications of the hardware
or provide a linux driver for their wireless network cards.
The NdisWrapper project provides a linux kernel module that
loads and runs Ndis (Windows network driver API) drivers
supplied by the vendors.

This package contains only userspace tools from NdisWrapper.
The kernel module comes in a separte package
(kernel-modules-ndiswrapper...).

%define module_name %name
%define module_version %version

%package -n kernel-source-%module_name-%module_version
Group: Development/Kernel
Summary: Linux %module_name modules sources

%description -n kernel-source-%module_name-%module_version
%module_name modules sources for Linux kernel.

%prep
%setup
#patch0 -p1 -b .spaces

%build
pushd utils
%make_build
popd

%install
pushd utils
#%make_install DESTDIR="$RPM_BUILD_ROOT" \
#	sbindir="$RPM_BUILD_ROOT"%_sbinrootdir \
#	usrsbindir="$RPM_BUILD_ROOT"%_sbindir \
#	mandir="$RPM_BUILD_ROOT"%_mandir \
#	install
make DESTDIR=$RPM_BUILD_ROOT install

popd

%__mkdir_p $RPM_BUILD_ROOT%_sysconfdir/%name

%__mkdir_p $RPM_BUILD_ROOT%_man8dir
%__install -m 644 ndiswrapper.8 $RPM_BUILD_ROOT%_man8dir
%__install -m 644 loadndisdriver.8 $RPM_BUILD_ROOT%_man8dir

# place to store packaged Windows drivers (ndis-driver-* pkgs)
%__mkdir_p $RPM_BUILD_ROOT%_libdir/ndis

# kernel-source install
%__mkdir_p $RPM_BUILD_ROOT%_usrsrc/kernel/sources/
cp %SOURCE0 $RPM_BUILD_ROOT%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.gz

%post
echo -e "please download binary driver at http://ndiswrapper.sourceforge.net/wiki/index.php/List\nuse ndiswrapper -i <inffile.inf> as root to install driver"

%files
%doc AUTHORS README ChangeLog INSTALL
/sbin/loadndisdriver
%_sbindir/ndiswrapper
%_sbindir/ndiswrapper-buginfo
%dir %_sysconfdir/%name
%_man8dir/*
# place to store packaged Windows drivers (ndis-driver-* pkgs)
%_libdir/ndis

%files -n kernel-source-%module_name-%module_version
%_usrsrc/kernel/sources/*ndis*

%changelog
* Sat Jan 14 2012 Ilya Mashkin <oddity@altlinux.ru> 1.57-alt1
- 1.57

* Mon Feb 28 2011 Ilya Mashkin <oddity@altlinux.ru> 1.56-alt2
- fix build

* Mon Feb 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.56-alt1
- 1.56

* Thu Jul 09 2009 Ilya Mashkin <oddity@altlinux.ru> 1.55-alt1
- 1.55

* Fri Jan 23 2009 Ilya Mashkin <oddity@altlinux.ru> 1.54-alt1
- New version 1.54

* Thu Jul 03 2008 Ilya Mashkin <oddity@altlinux.ru> 1.53-alt1
- New version 1.53

* Mon Feb 04 2008 Ilya Mashkin <oddity@altlinux.ru> 1.52-alt1
- New version 1.52

* Fri Nov 30 2007 Ilya Mashkin <oddity@altlinux.ru> 1.50-alt1
- New version 1.50

* Mon Nov 05 2007 Ilya Mashkin <oddity@altlinux.ru> 1.49-alt1
- New version 1.49
- Dropped support for 2.4 kernels (and very old 2.6 kernels)

* Tue Aug 07 2007 Ilya Mashkin <oddity@altlinux.ru> 1.47-alt1
- New version 1.47

* Wed Jun 06 2007 Ilya Mashkin <oddity@altlinux.ru> 1.46-alt1
- New version 1.46

* Sat Apr 21 2007 Ilya Mashkin <oddity@altlinux.ru> 1.42-alt1
- New version 1.42

* Fri Apr 06 2007 Ilya Mashkin <oddity@altlinux.ru> 1.41-alt1
- New version 1.41

* Fri Feb 09 2007 Ilya Mashkin <oddity@altlinux.ru> 1.37-alt1
- New version 1.37

* Wed Dec 06 2006 Ilya Mashkin <oddity at altlinux.ru> 1.31-alt1
- New version 1.31 (bug fixes)
- Add man loadndisdriver.8

* Wed Nov 29 2006 Ilya Mashkin <oddity at altlinux.ru> 1.30-alt1
- New version 1.30

* Sat Nov 26 2006 Ilya Mashkin <oddity at altlinux.ru> 1.29-alt1
- New version 1.29

* Wed Nov 08 2006 Ilya Mashkin <oddity at altlinux.ru> 1.28-alt1
- New version 1.28

* Sat Oct 22 2006 Ilya Mashkin <oddity at altlinux.ru> 1.27-alt1
- New version 1.27

* Sat Oct 15 2006 Ilya Mashkin <oddity at altlinux.ru> 1.26-alt1
- New version 1.26

* Mon Oct 02 2006 Ilya Mashkin <oddity at altlinux.ru> 1.24-alt1
- New version 1.24

* Wed Aug 09 2006 Ilya Mashkin <oddity at altlinux.ru> 1.22-alt1
- New version 1.22

* Wed Jul 19 2006 Ilya Mashkin <oddity at altlinux.ru> 1.21-alt1
- New version 1.21

* Sat Jul 09 2006 Ilya Mashkin <oddity at altlinux.ru> 1.19-alt1
- New version 1.19

* Wed May 10 2006 Ilya Mashkin <oddity at altlinux.ru> 1.16-alt1
- New version 1.16

* Thu Apr 13 2006 Ilya Mashkin <oddity at altlinux.ru> 1.13-alt1
- New version 1.13

* Fri Apr 07 2006 Ilya Mashkin <oddity at altlinux.ru> 1.12-alt1
- New version 1.12

* Sat Mar 26 2006 Ilya Mashkin <oddity at altlinux.ru> 1.11-alt1
- New version 1.11

* Wed Mar 01 2006 Ilya Mashkin <oddity at altlinux.ru> 1.10-alt1
- New version 1.10

* Sat Feb 05 2006 Ilya Mashkin <oddity at altlinux.ru> 1.9-alt1
- New version 1.9

* Sat Jan 07 2006 Ilya Mashkin <oddity at altlinux.ru> 1.7-alt2
- replace kernel-source-ndiswrapper

* Fri Dec 09 2005 Ilya Mashkin <oddity at altlinux.ru> 1.7-alt1
- New version 1.7

* Sun Nov 08 2005 Ilya Mashkin <oddity at altlinux.ru> 1.5-alt1
- NMU:version 1.5

* Sun Oct 08 2005 Ilya Mashkin <oddity at altlinux.ru> 1.4-alt1
- 1.4, remove wrong deps, old patch

* Mon Jul 18 2005 Ivan Zakharyaschev <imz@altlinux.ru> 1.1-alt2
- add %_libdir/ndis/ -- place to store packaged Windows
  drivers (ndis-driver-* pkgs).

* Mon Jul 18 2005 Ivan Zakharyaschev <imz@altlinux.ru> 1.1-alt1
- initial build for ALT:
  + include Mdk's patch (spaces);
  + package the sources as kernel-source for the module.
