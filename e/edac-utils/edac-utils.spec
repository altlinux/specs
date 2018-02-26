Name: edac-utils
Version: 0.16
Release: alt2

Summary: Userspace helper for kernel EDAC drivers (ECC)
Group: System/Kernel and hardware
License: GPL
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Url: http://bluesmoke.sourceforge.net/

Source: edac-utils-0.16.tar
BuildRequires: libsysfs-devel

%description
EDAC is the current set of drivers in the Linux kernel that handle
detection of ECC errors from memory controllers for most chipsets
on i386 and x86_64 architectures. This userspace component consists
an init script which loads EDAC DIMM labels at system boot, and can
optionally be configured to load a specific EDAC driver if this is
not done automatically at system startup. The package also includes a
library and utility for reporting current error counts from the EDAC
sysfs files.

%package devel
Summary: Userspace helper for kernel EDAC drivers (ECC) (devel package)
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required to build
edac-based software.

%prep
%setup

%build
%configure --disable-static
%make

%install
mkdir -p "%buildroot"
DESTDIR="%buildroot" make install
# Create labels.d dir
mkdir -p %buildroot%_sysconfdir/edac/labels.d
mkdir -p %buildroot/%_initdir
mv %buildroot/etc/init.d/edac %buildroot/%_initdir

%files
%doc README NEWS ChangeLog DISCLAIMER
%_sbindir/edac-ctl
%_bindir/edac-util
%_mandir/*/*
%dir %attr(0755,root,root) %_sysconfdir/edac
%dir %attr(0755,root,root) %_sysconfdir/edac/labels.d
%config(noreplace) %_sysconfdir/edac/labels.db
%_initdir/edac
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/edac.h

%changelog
* Wed Jun 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.16-alt2
- post_service/preun_service removed

* Mon Jun 01 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.16-alt1
- initial

