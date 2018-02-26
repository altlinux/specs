Name: libilbc1
Version: 0.0.2
Release: alt1

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
%configure --enable-sse2 --enable-doc --disable-static --disable-rpath
make

%install
%define docdir %_defaultdocdir/%name-%version
make install DESTDIR=%buildroot
mkdir -p %buildroot%_defaultdocdir/%name-%version/
cp -p COPYING INSTALL README AUTHORS gips_iLBClicense.pdf %buildroot%docdir/
cp -pr doc/api/html %buildroot%docdir/

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

%changelog
* Wed Dec 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.2-alt1
- 0.0.2 released

* Thu Apr  2 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1-alt1
- initial build for Sisyphus

* Thu Feb  7 2008 Steve Underwood <steveu@coppice.org> 0.0.1
- First pass
