%def_disable static
%define _customdocdir %_docdir/%name-%version

Name: openct
Version: 0.6.20
Release: alt3

Group: System/Servers
Summary: OpenCT Library for Smart Card Readers
License: LGPL
Url: http://www.opensc-project.org/

Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch1: %name-0.12.2-alt-automake-1.11.4.patch

Source10: openct.startup

# Automatically added by buildreq on Thu Sep 10 2009
BuildRequires: doxygen libltdl7-devel libpcsclite-devel libusb-compat-devel xsltproc

%if_enabled static
BuildRequires: libpcsclite-devel-static libusb-devel-static
%endif

%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
OpenCT implements drivers for several smart card readers.
It comes as driver in ifdhandler format for PC/SC-Lite, as CT-API
driver, or as a small and lean middleware, so applications can use
it with minimal overhead.  OpenCT also has a primitive mechanism
to export smart card readers to remote machines via tcp/ip.

%package -n lib%name
Group: System/Libraries
Summary: Library for accessing Smartcards

%description -n lib%name
These are the shared libraries for the smartcard terminal middleware
OpenCT.
If you want to compile applications using this library, you also need
the %name-devel package.

%package -n lib%name-devel
Requires: lib%name = %version
Group: System/Libraries
Summary: Supplementary files for developing %name applications
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files and documentation for %name.

%package -n lib%name-devel-static
Requires: lib%name = %version
Group: System/Libraries
Summary: Supplementary files for developing %name applications
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
static libraries for %name.

%package -n pcsc-lite-openct
License: BSD 3-Clause; LGPL v2.1 or later
Group: System/Libraries
Requires: pcsc-lite
Summary: PC/SC IFD Handler for OpenCT Smart Card Drivers

Provides: pcsc-openct = %version-%release
Obsoletes: pcsc-openct < %version-%release

%description -n pcsc-lite-openct
PC/SC Connector for OpenCT. It allows to use any of OpenCT Smart Card
drivers with the PCSC-Lite daemon from the pcsc-lite package.

OpenCT is a set of library and tools to talk to smart card readers.
OpenCT is used by the OpenSC Smart Card library.

%prep
%setup
%patch1 -p2

%build
%autoreconf
%add_optflags %optflags_shared
%configure \
        %{subst_enable static} \
        %{subst_enable debug} \
        --enable-pcsc \
        --with-bundle=%ifddir \
        --with-ifddir=%ifddir \
        --localstatedir=%_var \
        --disable-doc \
        --enable-api-doc \
        --enable-usb \
        --enable-pcsc \
        --docdir=%_docdir/%name-%version \
        --with-udev=/lib/udev
%make_build

%check
%make_build -k check

%install
%make install DESTDIR=%buildroot

##
# Create local state dir:
#
install -d %buildroot%_var/run/openct

##
# Install init script:
#
install -d %buildroot%_initdir
install -m 755 %SOURCE10 %buildroot%_initdir/%name

mkdir -p %buildroot/lib/udev/rules.d/
install -p etc/openct.udev %buildroot/lib/udev/rules.d/60-openct.rules

##
# HAL stuff
#
#mkdir -p %buildroot%_datadir/hal/fdi/{information,policy}/20thirdparty
#install -p etc/openct.fdi %buildroot%_datadir/hal/fdi/information/20thirdparty/10-usb-openct.fdi
#install -p etc/openct-policy.fdi %buildroot%_datadir/hal/fdi/policy/20thirdparty/10-usb-openct.fdi

#mkdir -p %buildroot%_usr/libexec/hal
#install -p -m755 etc/openct.hald %buildroot%_usr/libexec/hal/hald-addon-openct

%post
%post_service %name

%preun
%preun_service %name

%files
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/NEWS
%doc TODO
%exclude %_docdir/%name-%version/api
%_man1dir/*.*
%_bindir/*
%_sbindir/*
%config(noreplace) %_sysconfdir/openct.conf
#%_datadir/hal/fdi/information/20thirdparty/10-usb-openct.fdi
#%_datadir/hal/fdi/policy/20thirdparty/10-usb-openct.fdi
#%_usr/libexec/hal/hald-addon-openct
%_initdir/%name
# copy documentation from %_builddir
%dir %_var/run/openct
/lib/udev/openct_pcmcia
/lib/udev/openct_serial
/lib/udev/openct_usb
/lib/udev/rules.d/60-openct.rules

%files -n lib%name
%_libdir/libopenctapi.so
%_libdir/libopenct.so.*

%files -n lib%name-devel
%dir %_docdir/%name-%version
%doc %_docdir/%name-%version/api
%_libdir/libopenct.so
%_libdir/pkgconfig/libopenct.pc
%dir %_includedir/%name
%_includedir/%name/*.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n pcsc-lite-openct
%_libdir/openct-ifd.so
%ifddir/openct-ifd.bundle

%changelog
* Fri Apr 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.20-alt3
- Repair build with automake >= 1.11.4

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.20-alt2
- Remove HAL support
- Add udev rules/scripts

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 0.6.20-alt1
- [0.6.20]

* Thu Sep 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.17-alt1
- [0.6.17]
- spec cleanup
- HAL FDI moved to 20thirdparty subdirs
- Use upstream-provided HAL FDI's
- libopenctapi.so moved to libopenct package (closes: #21488)

* Sun Apr 26 2009 Andriy Stepanov <stanv@altlinux.ru> 0.6.15-alt4
- Take upstream SVN repository as base for git.alt

* Wed Apr 22 2009 Andriy Stepanov <stanv@altlinux.ru> 0.6.15-alt2
- Cleanup

* Tue Sep 02 2008 Andriy Stepanov <stanv@altlinux.ru> 0.6.15-alt1
- Up to new upstream version

* Tue Oct 30 2007 Andriy Stepanov <stanv@altlinux.ru> 0.6.14-alt3
- Apply patch from ruToken.

* Tue Oct 30 2007 Andriy Stepanov <stanv@altlinux.ru> 0.6.14-alt2
- Apply patch from ruToken.

* Thu Aug 02 2007 Andriy Stepanov <stanv@altlinux.ru> 0.6.12-alt1
- Switch to new version. Add patch for www.rutoken.ru devices. Add HAL support.

* Tue Dec 26 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.11-alt1
- new version

* Tue Sep 26 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.9-alt1
- new version

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.6.8-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5.0-alt2
- rebuild

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5.0-alt1
- new version

* Thu Nov 27 2003 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt2
- remove *.la

* Mon Nov 24 2003 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- build for ALT

* Fri Nov 14 2003 Florin <florin@mandrakesoft.com> 0.1.0-2mdk
- rebuild

* Wed Nov 12 2003 Florin <florin@mandrakesoft.com> 0.1.0-1mdk
- first mdk release
