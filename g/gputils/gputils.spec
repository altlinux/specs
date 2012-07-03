Name: gputils
Version: 0.13.7
Release: alt1

Summary: Development utilities for Microchip (TM) PIC (TM) microcontrollers

License: GPL
Group: Development/Other
Url: http://gputils.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/gputils/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Jan 17 2005
BuildRequires: flex hostinfo

%description
This is a collection of development tools for Microchip (TM) PIC (TM)
microcontrollers.

This is ALPHA software: there may be serious bugs in it, and it's
nowhere near complete.  gputils currently only implements a subset of
the features available with Microchip's tools.  See the documentation for
an up-to-date list of what gputils can do.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
#%_mandir/fr/man1/*
%_datadir/%name/
%doc AUTHORS ChangeLog NEWS README doc/gputils.pdf doc/gputils.ps

%changelog
* Sun May 03 2009 Vitaly Lipatov <lav@altlinux.ru> 0.13.7-alt1
- new version 0.13.7 (with rpmrb script) (fix bug #19884)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.13.6-alt1
- new version 0.13.6 (with rpmrb script)
- cleanup spec, enable SMP build

* Thu Sep 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.13.4-alt0.1
- new version 0.13.4 (with rpmrb script)

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.13.3-alt1
- new version

* Mon Jan 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- first build for ALT Linux Sisyphus

