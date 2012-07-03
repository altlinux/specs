Name: xorg-drv-wizardpen
Version: 0.8.1
Release: alt1

Summary: Genius WizardPen tablet driver for X.Org and XFree86
License: GPLv2
Group: System/X11
Url: https://launchpad.net/wizardpen
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source0: %name-%version.tar.gz

#Patch0: altlinux.patch

# Automatically added by buildreq on Tue Feb 10 2009
BuildRequires: gcc-c++ gcc-fortran rpm-macros-fillup xorg-inputproto-devel xorg-randrproto-devel xorg-sdk xorg-xproto-devel

%description
This is a X.Org and XFree86 4.x driver for the Genius WizardPen
and MousePen tablets. Other Genius USB tablets may be working too,
please report any experience with it, if you have one.

%define _udevlibdir /lib/udev/rules.d
%define _udevdir %_sysconfdir/udev/rules.d

%prep
%setup
#%patch0 -p1

%build
%autoreconf -fi
./configure \
    --with-xorg-module-dir=%buildroot%{_libdir}/X11/modules \
    --with-udev-rules-dir=%buildroot%{_udevlibdir} \
    --with-udev-settings-rules-dir=%buildroot%{_udevdir} \
    --with-xorg-conf-dir=%buildroot%{_sysconfdir}/X11/xorg.conf.d
%make_build

%install
%make_install install \
	bindir=%buildroot%_bindir \
	mandir=%buildroot%_mandir

%files
%_libdir/X11/modules/input/wizardpen_drv.so
%_bindir/wizardpen-calibrate
%_mandir/man4/wizardpen.4.gz
%_udevlibdir/*.rules
#%_udevdir/*.rules
%_sysconfdir/X11/xorg.conf.d/*.conf

%changelog
* Fri Nov 11 2011 Paul Wolneykien <manowar@altlinux.ru> 0.8.1-alt1
- Upgrade to the rev. 51 (v0.8.1) of lp:wizardpen.
- Do not use HAL (FDIs).
- Install the Wizardpen Xorg.conf part.
- Configure for G-Pen 560 for idVendor=0458, idProduct=5003.

* Sun Nov 07 2010 Paul Wolneykien <manowar@altlinux.ru> 0.8.0-alt1
- Synchronize the version number with upstream.

* Wed Jun 16 2010 Paul Wolneykien <manowar@altlinux.ru> 0.7.0-alt2
- Restore the FDI configuration for the Aiptek device.
- Install modules to the X11/modules/input directory.
- Do not install anything to the xorg.conf.d directory.

* Wed Jun 16 2010 Paul Wolneykien <manowar@altlinux.ru> 0.7.0-alt1
- Import new version from the (re)-activated Launchpad upstream

* Tue May 19 2009 Paul Wolneykien <manowar@altlinux.ru> 0.6.0.2-alt4
- Removes the hysteresis in the threshold-based button event handling.

* Thu May 04 2009 Paul Wolneykien <manowar@altlinux.ru> 0.6.0.2-alt3
- Threshold-based button event.

* Thu Apr 30 2009 Paul Wolneykien <manowar@altlinux.ru> 0.6.0.2-alt2
- Fix button event handler.
- FDI for Hal based Xorg autoconfiguration included.
- Fix of the wrong InitValuatorClassDeviceStruct() call.

* Wed Feb 11 2009 Paul Wolneykien <manowar@altlinux.ru> 0.6.0.2-alt1
- Initial build of the version 0.6.0.2 for ALT Linux.

* Tue Feb 10 2009 Paul Wolneykien <manowar@altlinux.ru> 0.5.0-alt1
- Initial build for ALT Linux.
