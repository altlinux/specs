Name: libvpb
Version: 4.2.58
Release: alt1

Summary: Voicetronix VPB interface library

License: LGPL
Group: System/Libraries
Url: http://www.voicetronix.com/downloads.htm

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define oname vpb-driver
Source: http://www.voicetronix.com/Downloads/vpb-driver-4.x/%oname-%version.tar
Patch: libvpb-4.2.42-alt-DSO.patch
Patch1: libvpb-4.2.42-alt-gcc4.7.patch
Patch2: libvpb-4.2.58-glibc2.27.patch

# Automatically added by buildreq on Fri Jan 16 2009
BuildRequires: gcc-c++ libpci-devel zlib-devel

%description
Voicetronix is one of the few Computer Telephony hardware vendors
with Open Source drivers. This is very important if you are developing
under an Open Source operating system such as Linux. One reason is that
Open Source operating systems like Linux are evolving very rapidly and
unfortunately closed source drivers usually only work with a very narrow
range of kernel versions. Another reason is that it guarantees the driver
will always be supported and bugs can be fixed if required.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%prep
%setup -n %oname-%version
#patch -p2
%patch1 -p2
%patch2 -p1

# disable build kernel module
%__subst "s|\$(srcdir)/vtcore.*||g" src/Makefile.in
%__subst "s|/sbin/ldconfig||g" src/libvpb/Makefile.in

%build
%configure --disable-static --enable-shared
%make_build

%install
%makeinstall_std
rm -rf %buildroot/etc/modprobe.d/blunt-axe.conf

%files
%doc README* COPYING
%_sbindir/vpbconf
%_sbindir/vpbscan
%_libdir/lib*.so.*
%_datadir/vpb-driver/

%files devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 4.2.58-alt1
- new version 4.2.58 (with rpmrb script)
- fix build with glibc 2.27 (pow10->exp10)

* Wed Oct 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.42-alt1.qa3
- Fixed build with gcc 4.7

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.42-alt1.qa2
- Fixed build

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 4.2.42-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Oct 14 2009 Vitaly Lipatov <lav@altlinux.ru> 4.2.42-alt1
- new version 4.2.42 (with rpmrb script)

* Thu Jan 15 2009 Vitaly Lipatov <lav@altlinux.ru> 4.2.38-alt1
- initial build for ALT Linux Sisyphus
