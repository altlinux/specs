#### TODO : hack! drop it when update to 3.x!
%set_gcc_version 4.9
BuildRequires: gcc4.9
### END hack ###

%def_disable static

Name: owfs
Version: 3.2p1
Release: alt1.1

Summary: 1-Wire Virtual File System
License: GPL
Group: System/Kernel and hardware

Url: http://sourceforge.net/projects/owfs
Source: %name-%version.tar.gz
#Patch: owfs-2.9-alt-gcc5.patch
Patch0: owfs-tcl-req.patch
Patch1: owfs-initscript.patch

BuildRequires: chrpath
BuildRequires: service

# Automatically added by buildreq on Tue Jul 25 2017
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcloog-isl4 libusb-devel perl perl-Encode perl-devel pkg-config python-base python-modules python-modules-compiler python-modules-email python3 python3-base ruby-stdlibs swig-data
BuildRequires: glibc-devel-static groff-base libftdi1-devel libfuse-devel mt-st python-devel python-module-google python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-locale selinux-policy swig

%description
OWFS is a userspace virtual filesystem providing access to 1-Wire
networks.

%package -n lib%name
Summary: Core library providing base functions to other OWFS modules
Group: System/Kernel and hardware

%description -n lib%name
lib%name is a core library providing base functions to other OWFS modules.

%package -n lib%name-devel
Summary: Development OWFS library files
Group: System/Kernel and hardware
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development OWFS library files.

%package -n lib%name-capi
Summary: C-API to develop third-part applications which access 1-Wire networks
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-capi
lib%name-capi library on top of libow providing an easy API to develop
third-part applications to access to 1-Wire networks.

%package -n lib%name-capi-devel
Summary: Development files for C-API library
Group: Development/C
Requires: lib%name-capi = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-capi-devel
Development files for C-API library.

%package -n libownet
Summary: C-API to develop third-part applications which access 1-Wire networks
Group: Development/C

%description -n libownet
libownet library provids an easy API to develop third-part
applications to access to 1-Wire networks. It doesn't depend on
owlib, and only supports remote-server connections. This library
doesn't include any 1-wire adapter support, except server
connections.

%package -n libownet-devel
Summary: Development files for libownet library
Group: Development/C
Requires: libownet = %version-%release

%description -n libownet-devel
Development files for libownet library.

%package fs
Summary: Virtual filesystem on top of lib%name providing access to 1-Wire networks
Group: System/Kernel and hardware
Requires: lib%name = %version-%release
Requires: service

%description fs
%name-fs is a virtual filesystem on top of lib%name providing access
to 1-Wire networks.

%package httpd
Summary: HTTP daemon providing access to 1-Wire networks
Group: Networking/WWW
Requires: lib%name = %version-%release
Requires: service

%description httpd
%name-httpd is a HTTP daemon on top of %name providing access to
1-Wire networks.

%package ftpd
Summary: FTP daemon providing access to 1-Wire networks
Group: Networking/File transfer
Requires: lib%name = %version-%release
Requires: service

%description ftpd
%name-ftpd is a FTP daemon on top of %name providing access to 1-Wire
networks.

%package server
Summary: Backend server (daemon) for 1-wire control
Group: System/Kernel and hardware
Requires: lib%name = %version-%release
Requires: service

%description server
%name-server is the backend component of the OWFS 1-wire bus control system.
owserver arbitrates access to the bus from multiple client processes.
The physical bus is usually connected to a serial or USB port, and
other processes connect to owserver over network sockets (tcp port).
Communication can be local or over a network.

%package tap
Summary: Packet sniffer for the owserver protocol
Group: Networking/Other

%description tap
%name-tap is a packet sniffer for the owserver protocol

%package mon
Summary: Statistics and settings monitor for owserver
Group: Monitoring

%description mon
%name-mon is a graphical monitor of owserver's status

%package perl
Summary: Perl interface for the 1-wire filesystem
Group: Development/Perl
Requires: lib%name = %version-%release

%description perl
%name-perl is a Perl interface for the 1-wire filesystem

%package -n python-module-%name
Summary: python interface for the 1-wire filesystem
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
python-module-%name is a Python interface for the 1-wire filesystem

%package shell
Summary: light weight shell access to owserver and the 1-wire filesystem
Group: Shells

%description shell
%name-shell is 4 small programs to easily access owserver (and thus
the 1-wire system) from shell scripts. owdir, owread, owwrite and
owpresent.

%package man
Summary: man pages for all the OWFS programs 1-wire devices
Group: Documentation

%description man
%name-man installs man pages for all the OWFS progams (owfs, owhtttpd,
owserver, owftpd, owshell, owperl, owtcl) and also all the supported
1-wire devices.

%prep
%setup
#patch -p2
%patch0 -p1
%patch1 -p1
sed -i- 's/) Makefile.PL/& INSTALLDIRS=vendor/' module/*/perl5/Makefile.am

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--with-systemdsystemunitdir=%_unitdir \
	--enable-usb \
	--enable-cache \
	--enable-mt \
	--enable-owfs \
	--enable-owhttpd \
	--enable-owcapi \
	--enable-ownetlib \
	--enable-owftpd \
	--enable-owserver \
	--enable-owtap \
	--enable-owmon \
	--enable-owperl \
	--enable-owpython \
	--disable-owphp \
	--disable-owtcl

%make_build

%install
make install DESTDIR=%buildroot

install -d -m 755 %buildroot%_includedir/owfs
mv -f %buildroot%_includedir/*.h %buildroot%_includedir/owfs

install -D -m 644 src/rpm/owfs.conf %buildroot/etc/sysconfig/owfs
install -D -m 755 src/rpm/owfs.init %buildroot%_initdir/owfs
install -d -m 755 %buildroot%_sbindir
mv -f %buildroot%_bindir/owfs %buildroot%_sbindir

install -D -m 644 src/rpm/owhttpd.conf %buildroot/etc/sysconfig/owhttpd
install -D -m 755 src/rpm/owhttpd.init %buildroot%_initdir/owhttpd
install -d -m 755 %buildroot%_sbindir
mv -f %buildroot%_bindir/owhttpd %buildroot%_sbindir

install -D -m 644 src/rpm/owftpd.conf %buildroot/etc/sysconfig/owftpd
install -D -m 755 src/rpm/owftpd.init %buildroot%_initdir/owftpd
install -d -m 755 %buildroot%_sbindir
mv -f %buildroot%_bindir/owftpd %buildroot%_sbindir

install -D -m 644 src/rpm/owserver.conf %buildroot/etc/sysconfig/owserver
install -D -m 755 src/rpm/owserver.init %buildroot%_initdir/owserver
install -d -m 755 %buildroot%_sbindir
mv -f %buildroot%_bindir/owserver %buildroot%_sbindir

chrpath -d %buildroot%perl_vendor_archlib/auto/OW/OW.so

# Remove tcl man files, till we build owfs without tcl support
%__rm -f %buildroot%_mandir/mann/*

# Clean up unused parts in man dirs
%__rm -f %buildroot%_man1dir/*.1so.*
%__rm -f %buildroot%_man3dir/*.3so.*
%__rm -f %buildroot%_man5dir/*.5so.*

%post fs
%post_service owfs

%preun fs
%preun_service owfs

%post httpd
%post_service owhttpd

%preun httpd
%preun_service owhttpd

%post ftpd
%post_service owftpd

%preun ftpd
%preun_service owftpd

%post server
%post_service owserver

%preun server
%preun_service owserver

%files -n lib%name
%_libdir/libow-*.so*

%files -n lib%name-devel
%doc README NEWS ChangeLog AUTHORS
%_includedir/owfs/owfs_config.h
%_libdir/libow.so

%files -n lib%name-capi
%_libdir/libowcapi-*.so.*

%files -n lib%name-capi-devel
%_includedir/owfs/owcapi.h
%_libdir/libowcapi.so

%files -n libownet
%_libdir/libownet-*.so*

%files -n libownet-devel
%_includedir/owfs/ownetapi.h
%_libdir/libownet.so

%files fs
%_unitdir/owfs.service
%_initdir/owfs

%config(noreplace) %_sysconfdir/sysconfig/owfs
%_sbindir/owfs

%files httpd
%_unitdir/owhttpd.service
%_initdir/owhttpd
%config(noreplace) %_sysconfdir/sysconfig/owhttpd
%_sbindir/owhttpd

%files shell
%_bindir/owdir
%_bindir/owread
%_bindir/owwrite
%_bindir/owpresent
#_bindir/owside
%_bindir/owget
%_bindir/owexist
%_bindir/owusbprobe

%files man
%_man1dir/*.1.*
%_man3dir/*.3.*
%_man5dir/*.5*
#_mandir/mann/*.n.*

%files ftpd
%_unitdir/owftpd.service
%_initdir/owftpd
%config(noreplace) %_sysconfdir/sysconfig/owftpd
%_sbindir/owftpd

%files server
%_unitdir/owserver.service
%_unitdir/owserver.socket
%_initdir/owserver
%config(noreplace) %_sysconfdir/sysconfig/owserver
%_sbindir/owserver
%_bindir/owexternal

%files tap
%_bindir/owtap

%files mon
%_bindir/owmon

%files perl
%perl_vendor_privlib/OW*
%perl_vendor_archlib/OW*
%perl_vendor_autolib/OW

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.2p1-alt1.1
- rebuild with new perl 5.26.1

* Mon Jul 24 2017 Grigory Milev <week@altlinux.ru> 3.2p1-alt1
- New version released
- Init.d scripts fixed
- Added systemd scripts

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.9p5-alt2.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.9p5-alt2.1
- rebuild with new perl 5.22.0

* Wed Nov 18 2015 Igor Vlasenko <viy@altlinux.ru> 2.9p5-alt2
- fixed build

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.9p5-alt1.1
- rebuild with new perl 5.20.1

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9p5-alt1
- Version 2.9p5

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.8p8-alt4
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.8p8-alt3
- rebuilt for perl-5.16

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8p8-alt2.2
- Removed bad RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.8p8-alt2.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 2.8p8-alt2
- rebuilt for perl-5.14

* Fri May 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8p8-alt1
- Version 2.8p8 (ALT #25286)

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7p16-alt1.3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.7p16-alt1.2
- Rebuilt with perl 5.12

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7p16-alt1.1
- Rebuilt with python 2.6

* Mon Feb 23 2009 Denis Klimov <zver@altlinux.org> 2.7p16-alt1
- new version
- change python subpackage module name to python-module-owfs

* Fri Nov 14 2008 Denis Klimov <zver@altlinux.ru> 2.7p8-alt1
- new version
- remove needless call postun_ldconfig macros
- add owget and owside program
- use one -f argument for files section of python subpackage
- fixing path to installed files in PYTHON_INSTALLED_FILES by sed

* Mon Apr 28 2008 Denis Klimov <zver@altlinux.ru> 2.7p4-alt2
- fix build for x86_64 arch. Now python subpackage feel with -f option

* Wed Apr 16 2008 Denis Klimov <zver@altlinux.ru> 2.7p4-alt1
- build for ALT Linux. Spec was rewrite from upstream file.

