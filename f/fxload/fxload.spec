Name: fxload
Version: 2002_04_11
Release: alt2

Summary: fxload
License: GPL
Group: Development/Other
Url: http://sourceforge.net/project/showfiles.php?group_id=17679

Packager: Alexander Gvozdev <gab@altlinux.ru>

Source0: %name-%version.tar.gz
Patch0: ezusb.c.patch
Patch1: ezusb.h.patch
Patch2: Makefile-fix.patch

BuildRequires: gcc-c++ flex libusb-devel 

%description
This program is conveniently able to download firmware into FX and FX2
EZ-USB devices, as well as the original AnchorChips EZ-USB.  It is
intended to be invoked by hotplug scripts when the unprogrammed device
appears on the bus.

%set_verify_elf_method textrel=relaxed, unresolved=relaxed

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build

%install
%make DESTDIR=%buildroot install
install -pD -m644 %_builddir/%name-%version/README.txt         %buildroot%_docdir/%name/INSTALL.txt
install -pD -m644 %_builddir/%name-%version/COPYING         %buildroot%_docdir/%name/COPYING

%files -n %name
/sbin/fxload
%_man8dir/*
%_datadir/usb/a3load.hex
%doc %_docdir/%name/*

%changelog
* Sun Mar 30 2008 Alexander Gvozdev <gab@altlinux.ru> 2002_04_11-alt2
- Compiling error fix on i586
* Wed Feb 28 2007 Alexander Gvozdev <gab@altlinux.ru> 2002_04_11-alt1
- Initial build
