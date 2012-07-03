Name: libvpb
Version: 4.2.42
Release: alt1.qa2

Summary: Voicetronix VPB interface library

License: LGPL
Group: System/Libraries
Url: http://www.voicetronix.com/downloads.htm

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define oname vpb-driver
Source: http://www.voicetronix.com/Downloads/vpb-driver-4.x/%oname-%version.tar.bz2
Patch: libvpb-4.2.42-alt-DSO.patch

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
%setup -q -n %oname-%version
%patch -p2
# disable build kernel module
%__subst "s|\$(srcdir)/vtcore.*||g" src/Makefile.in
%__subst "s|/sbin/ldconfig||g" src/libvpb/Makefile.in

%build
%configure --disable-static --enable-shared
%make_build

%install
%makeinstall_std

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
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.42-alt1.qa2
- Fixed build

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 4.2.42-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Oct 14 2009 Vitaly Lipatov <lav@altlinux.ru> 4.2.42-alt1
- new version 4.2.42 (with rpmrb script)

* Thu Jan 15 2009 Vitaly Lipatov <lav@altlinux.ru> 4.2.38-alt1
- initial build for ALT Linux Sisyphus
