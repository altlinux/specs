Name: libilbc1
Version: 0.0.2
Release: alt3

Summary: iLBC is a library for the iLBC low bit rate speech codec.
License: Global IP Sound iLBC Public License, v2.0
Group: System/Libraries
Url: http://www.soft-switch.org/downloads/voipcodecs

Source: %name-%version-%release.tar

BuildRequires: doxygen

%description
iLBC is a library for the iLBC low bit rate speech codec.
%name is based on rfc3951 reference sources, but slightly
differs in API.

%package devel
Summary: iLBC development files
Group: Development/C
Requires: %name = %version-%release
Conflicts: libilbc-devel

%description devel
iLBC is a library for the iLBC low bit rate speech codec.
%name is based on rfc3951 reference sources, but slightly
differs in API.
This package provides iLBC development files.

%prep
%setup

%build
%autoreconf
%configure --enable-doc --disable-static --disable-rpath \
%ifarch %ix86 x86_64
	--enable-sse2
%else
	--disable-sse2
%endif
make

%install
%define docdir %_defaultdocdir/%name-%version
make install DESTDIR=%buildroot
mkdir -p %buildroot%_defaultdocdir/%name-%version/
cp -p COPYING INSTALL README AUTHORS gips_iLBClicense.pdf %buildroot%docdir/
cp -pr doc/api/html %buildroot%docdir/
mkdir -p %buildroot%_libdir/pkgconfig
cat > %buildroot%_libdir/pkgconfig/ilbc.pc << EOF
Name: ilbc
Description: iLBC codec for voice communication
Version: 0.0.2
Libs: -lilbc
Libs.private: -lm
Cflags: -I/usr/include/ilbc
EOF


%files
%dir %docdir
%docdir/[A-Z]*
%_libdir/libilbc.so.*

%files devel
%docdir/html
%docdir/gips_iLBClicense.pdf
%_includedir/ilbc.h
%_includedir/ilbc
%_libdir/libilbc.so
%_libdir/pkgconfig/*.pc

%changelog
* Tue Mar 01 2016 Anton Farygin <rider@altlinux.ru> 0.0.2-alt3
- add pkgconfig support

* Mon Apr 22 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.2-alt2
- fixed build on arm

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.2-alt1
- 0.0.2 released

* Thu Apr  2 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1-alt1
- initial build for Sisyphus

* Thu Feb  7 2008 Steve Underwood <steveu@coppice.org> 0.0.1
- First pass
