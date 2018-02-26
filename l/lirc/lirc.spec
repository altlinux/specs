%define version 0.8.7
%define add_rel %nil
%def_disable static

Name: lirc
Version: 0.9.0
Release: alt1.1

Summary: The Linux Infrared Remote Control package
License: GPL
Group: System/Base
URL: http://www.lirc.org
Packager: Anton Farygin <rider@altlinux.ru>

Source: %name-%version%add_rel.tar.bz2
Source1: lircd
Source2: pathdown.sh
Source4: lircd.sysconfig
Source5: liblircclient0.pc
Patch1: %name-0.8.1-alt-configure.patch
Patch2: %name-0.8.0pre4-hiddev_fix.patch
Patch3: %name-alt-font-fix.patch
Patch6: %name-0.8.6-devpath.patch
Patch7: %name-0.8.6-fdiformat.patch

# Automatically added by buildreq on Fri Nov 27 2009
BuildRequires: imake libSM-devel libX11-devel libalsa-devel libftdi-devel

BuildPreReq: svgalib-devel

%description
LIRC is a package that allows you to decode and send infra-red signals
of many (but not all) commonly used remote controls.

%package -n liblirc
Summary: Client library for LIRC
Group: System/Libraries

%description -n liblirc
Libraries needed by programs, which uses LIRC

%package -n liblirc-devel
Summary: Development for LIRC
Group: Development/C
Requires: lib%name = %version-%release

%description -n liblirc-devel
Development library for LIRC

%package -n liblirc-devel-static
Summary: Development for LIRC
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n liblirc-devel-static
Static library for LIRC

%prep
%setup -q -n %name-%version%add_rel
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch6 -p2
%patch7 -p2

%build
%add_optflags -I%_includedir/libftdi
%autoreconf
%configure  %{subst_enable static} --localstatedir=%_var --with-x --with-major=61 \
	    --with-syslog --with-driver=userspace --with-port=0x3f8 --with-irq=4
NPROCS=1
%make_build
pushd contrib/hal
./gen-hal-fdi.pl
popd

%install
%makeinstall devdir=%buildroot/dev varrundir=%buildroot/%_runtimedir
mkdir -p %buildroot/%_runtimedir/%name
mkdir -p %buildroot%_initdir
mkdir -p %buildroot/dev
mkdir -p %buildroot%_datadir/hal/fdi/policy/10osvendor
install -p -m600 contrib/lircd.conf contrib/lircmd.conf %buildroot%_sysconfdir
pushd contrib/hal/
./gen-hal-fdi.pl
popd
install -p -m644 contrib/hal/20-ircontrol-lirc.fdi %buildroot%_datadir/hal/fdi/policy/10osvendor/
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/lircd
install -m755 %SOURCE1 %buildroot%_initdir
chmod +x %buildroot%_initdir/lircd
touch %buildroot/dev/lirc
%makeinstall -C $RPM_BUILD_DIR/%name-%version%add_rel/doc/man

mkdir -p %buildroot%_datadir/pkgconfig/
install -m644 %SOURCE5 %buildroot%_datadir/pkgconfig/

t=$(pwd)/kernel-source-%name-%version
rm -rf $t
mkdir -p $t/drivers/scripts
mkdir -p %buildroot%_usrsrc/kernel/sources
cp config.h $t/
cp -a drivers/{*.h,Makefile.kernel} $t/drivers/
cp %SOURCE2 $t/drivers/scripts/

%pre
/usr/sbin/groupadd -r -f %name &> /dev/null ||:

%post
%post_service lircd

%preun
%preun_service lircd

%files
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/*.conf
%_initdir/*
%_bindir/*
%attr(2711,root,%name) %_sbindir/lircd
%_sbindir/lircmd
%_datadir/hal/fdi/policy/10osvendor/*.fdi
%doc NEWS TODO remotes doc/lirc.css doc/irxevent.keys doc/html doc/images
%_man1dir/*.1*
%_man8dir/*.8*
%dir %_runtimedir/%name

%files -n liblirc
%_libdir/liblirc_client.so.*

%files -n liblirc-devel
%_libdir/liblirc_client.so
%_includedir/*
%_datadir/pkgconfig/*

%if_enabled static
%files -n liblirc-devel-static
%_libdir/liblirc_client.a
%endif #static

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Anton Farygin <rider@altlinux.ru> 0.9.0-alt1
- new version

* Tue Jul 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.7-alt2
- pkg-config from debain added

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1.qa2
- Rebuilt for debuginfo
- Added svgalib-devel into BuildPreReq
- Fixed checking of ftdi.h

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Sep 08 2010 Anton Farygin <rider@altlinux.ru> 0.8.7-alt1
- new version

* Mon Apr 12 2010 Anton Farygin <rider@altlinux.ru> 0.8.6-alt5
- Added driver for wb677 (Asrock ION330HT) receiver

* Thu Jan 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.6-alt4.2
- patched for 2.6.32 kernel compatibility

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt4.1
- Rebuilt with python 2.6

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt4
- removed modutils and hal requires
- fixed hal fdi (altbug #21732)

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt3
- fixed location of lirc daemon 
- use /dev/lirc0 as default lirc device

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt2
- added %_runtimedir/%name

* Tue Sep 15 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt1
- new version
- added mode2 to lirc package
- add patches from RH for standardized remote keycodes

* Sun Jun 21 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.5-alt1
- new version.
- add requires to hal (as provides .fdi).

* Sat Dec 27 2008 L.A. Kostis <lakostis@altlinux.ru> 0.8.4-alt1.a
- New version.
- .spec cleanup.
- remove obsoleted patches.

* Thu Mar 13 2008 L.A. Kostis <lakostis@altlinux.ru> 0.8.3-alt1.cvs20080313
- 2008-03-13 CVS snapshot.
- remove commandir driver (already included).
- fix init script priority (start lircd before dm).

* Sun Nov 04 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8.2-alt1
- 0.8.2.
- update commandir driver to 1.4.4 version.

* Sat May 19 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt2
- fix bogus font in xmode2 (ALT #9149).

* Sat Feb 17 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt1
- 0.8.1 version.
- remove obsoleted patches.
- update commandir driver to 1.4.2 version.
- update -alt-config patch.

* Wed May 10 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt4
- Some init.d script improvements (see #9454).

* Tue May 09 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt3.1
- Fixed typo in post (see #9534).

* Sat Apr 29 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt3
- Added sources:
  + commandir-1.4.1 - CommandIR Mini hardware driver.
- Added patches:
  + lirc-0.8.0-2-cmdir.patch - update cmdir patch from vendor.
  + commandir-1.4.1-cleanup.patch - update commandir kernel driver 
    for 2.6.16+ kernel.
- Add post/preun service.

* Mon Apr 03 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt2
- Added patches:
  + lirc-drivers-cvs-update.patch - sync drivers changes 
    for 2.6.16+ kernels.
  
* Tue Feb 14 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt1
- new version 0.8.0.
- update Makefile for kernel modules.

* Fri Jan 20 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt1.pre4
- 0.8.0pre4.
- spec cleanup.
- update buildreq.
- disable static builds by default.

* Thu Nov 27 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt4
- removed .la file

* Fri Oct 17 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt3
- fix in start up script (--lock-file option replace with --lockfile, #3177)

* Tue Sep 23 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt2
- kernel source makefile fix

* Fri Sep 19 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (from CVS)
- building kernel-source package

* Tue Oct 29 2002 Kachalov Anton <mouse@altlinux.ru> 0.6.6-alt1
- new version 0.6.6

* Mon Oct 28 2002 Kachalov Anton <mouse@altlinux.ru> 0.6.5-alt2
- remove smode2 from the package

* Tue Feb 26 2002 Kachalov Anton <mouse@altlinux.ru> alt1
- new version (0.6.5) build

* Mon Jan 21 2002 Kachalov Anton <mouse@altlinux.ru> alt3
- syncing with new dev package

* Fri Jan 11 2002 Kachalov Anton <mouse@altlinux.ru> alt2
- added group lirc
- configure with --localstatedir=/var
- startup script fix

* Wed Jan 09 2002 Kachalov Anton <mouse@altlinux.ru> alt1
- build for Sisyphus
