# undefine XXX__libtoolize
# %define unstable 1
%def_disable static

Name: pcsc-lite
Version: 1.7.4
Release: alt1

Group: System/Servers
Summary: Muscle PCSC Framework for Linux
License: %bsd
URL: http://pcsclite.alioth.debian.org/

Source0: pcsc-lite-%version.tar

Source1: pcscd.startup
Source2: pcsc-lite-pcscd.sysconfig

Conflicts: libpcsclite < %version-%release
Conflicts: libpcsclite > %version-%release

# Automatically added by buildreq on Thu Sep 10 2009
BuildRequires: flex tetex-latex

BuildRequires: rpm-build-licenses libudev-devel perl-podlators

%if_enabled static
BuildRequires: glibc-devel-static
%endif

%description
pcscd is the daemon program for PC/SC Lite. It is a resource 
manager that coorinates communications with Smart Card readers and Smart 
Cards that are connected to the system.
The purpose of PCSC Lite is to provide a Windows(R) SCard interface in a 
very small form factor for communicating to smartcards and readers.
PCSC Lite uses the same winscard api as used under Windows(R)

This package contains daemon program for PC/SC Lite

%package -n libpcsclite
Group: System/Libraries
Summary: Libraries for pcscd
#
%description -n libpcsclite
Libraries for pcscd. pcscd is the daemon program
for PC/SC Lite. It is a resource manager that coorinates
communications with Smart Card readers and Smart Cards
that are connected to the system. The purpose of PCSC Lite
is to provide a Windows(R) SCard interface in a very small
form factor for communicating to smartcards and readers.
PCSC Lite uses the same winscard api as used under Windows(R)

%package -n libpcsclite-devel
Group: Development/C
Summary: Haeders and other development files for libpcsclite
Requires: libpcsclite = %version-%release
#
%description -n libpcsclite-devel
Haeders and other development files for libpcsclite

%package -n libpcsclite-devel-static
Group: Development/C
Summary: Static libraries for libpcsclite
Requires: libpcsclite-devel = %version-%release
#
%description -n libpcsclite-devel-static
Static libraries for libpcsclite

%prep
%setup -q

%build
%autoreconf
%configure \
    %{subst_enable static} \
    --disable-libhal \
    --enable-debugatr \
    --enable-ipcdir=/var/run/pcscd \
    --enable-usbdropdir=%_libdir/pcsc/drivers \
    #

%make_build

# pdf
%make_build -C doc

%install
%makeinstall_std

mkdir -p %buildroot/%_initdir/
install -m 755 %SOURCE1 %buildroot/%_initdir/pcscd
mkdir -p %buildroot/%_sysconfdir/sysconfig
install -m 644 %SOURCE2 %buildroot/%_sysconfdir/sysconfig/pcscd

mkdir -p %buildroot%_sysconfdir/reader.conf.d
mkdir -p %buildroot/var/run/pcscd
mkdir -p %buildroot%_libdir/pcsc/drivers

%files
%doc AUTHORS COPYING DRIVERS HELP NEWS README SECURITY TODO doc/README.DAEMON
%dir %_sysconfdir/reader.conf.d/
%config(noreplace) %_sysconfdir/sysconfig/pcscd
%_initdir/pcscd
%_sbindir/pcscd
#%_bindir/make_hash_link.sh
%_man5dir/*
%_man8dir/*
%dir %_libdir/pcsc
%dir %_libdir/pcsc/drivers
%dir /var/run/pcscd

%files -n libpcsclite
%_libdir/libpcsclite.so.*

%files -n libpcsclite-devel
%doc ChangeLog
%_libdir/libpcsclite.so
%_includedir/PCSC/
%_libdir/pkgconfig/libpcsclite.pc

%if_enabled static
%files -n libpcsclite-devel-static
%_libdir/libpcsclite.a
%endif

%changelog
* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.4-alt1
- [1.7.4]

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 1.6.1-alt1
- [1.6.1]
  + Dropped update-reader.conf
- Disabled libhal, enabled libusb

* Thu Sep 10 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.5-alt1
- [1.5.5] (closes: #21489)
- Dropped testpcsc (test tool)
- IPC directory moved to /var/run/pcscd
- Packaged driver directory

* Tue Apr 28 2009 Andriy Stepanov <stanv@altlinux.ru> 1.5.2-alt1
- New version

* Thu Jan 17 2008 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt3
- fix initscript daemon startup options (#14023)

* Mon Oct 01 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt2
- add description to initscript

* Wed Sep 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4.4-alt1
- new version

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3.1-alt1
- new version

* Tue Feb 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt2
- fix default /etc/sysconfig/pcscd

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.2.0-alt1
- new version

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt5
- add patches from PLD

* Mon Dec 01 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt4
- remove *.la

* Mon Sep 29 2003 Sergey V Turchin <zerg at altlinux dot org> 1.1.1-alt3
- move config to %_sysconfdir
- fix build requires
- WITHOUT_RC_COMPAT=1 in initscript

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.1-alt2
- fix requires

* Tue Oct 22 2002 Sergey V Turchin <zerg@altlinux.ru> 1.1.1-alt1
- initial spec

