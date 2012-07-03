Name: libmms
Version: 0.6.2
Release: alt1

Summary: mms stream protocol library

License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/libmms/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/libmms/%version/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Nov 08 2009
BuildRequires: glib2-devel

%description
libmms is a library implementing the mms streaming protocol.

%package devel
Summary: Libraries and includefiles for developing with libmms
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package provides the necessary development headers and libraries
to allow you to devel with libmms.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING.LIB ChangeLog NEWS README README.LICENSE
%_libdir/libmms.so.*

%files devel
%_includedir/libmms/
%_libdir/libmms.so
%_pkgconfigdir/libmms.pc

%changelog
* Wed Mar 09 2011 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Nov 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt2
- cleanup spec, change Url, update buildreqs

* Sun Nov 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- new version 0.5 (with rpmrb script)

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- fix headers packing

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version 0.4 (with rpmrb script)

* Mon Jun 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
