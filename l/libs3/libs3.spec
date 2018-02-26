Summary: C Library and Tools for Amazon S3 Access
Name: libs3
Version: 2.0
Release: alt1
License: GPL
Group: Networking/Other
Url: http://sourceforge.net/projects/reallibs3
Packager: Denis Smirnov <mithraen@altlinux.ru>

Conflicts: libaff

Source: %name-%version.tar

Patch: %name-%version.patch

%define debug_package %nil

# Automatically added by buildreq on Sun Feb 14 2010 (-bb)
BuildRequires: libcurl-devel libxml2-devel

%description
This package includes the libs3 shared object library, needed to run
applications compiled against libs3, and additionally contains the s3
utility for accessing Amazon S3.

%package devel
Summary: Headers and documentation for libs3
Group: Development/C
Requires: %name = %version-%release

%description devel
This library provides an API for using Amazon's S3 service (see
http://s3.amazonaws.com).  Its design goals are:

 - To provide a simple and straightforward API for accessing all of S3's
   functionality
 - To not require the developer using libs3 to need to know anything about:
     - HTTP
     - XML
     - SSL
   In other words, this API is meant to stand on its own, without requiring
   any implicit knowledge of how S3 services are accessed using HTTP
   protocols.
 - To be usable from multithreaded code
 - To be usable by code which wants to process multiple S3 requests
   simultaneously from a single thread
 - To be usable in the simple, straightforward way using sequentialized
   blocking requests

%package devel-static
Summary: libs3 static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This library provides an API for using Amazon's S3 service (see
http://s3.amazonaws.com).  Its design goals are:

 - To provide a simple and straightforward API for accessing all of S3's
   functionality
 - To not require the developer using libs3 to need to know anything about:
     - HTTP
     - XML
     - SSL
   In other words, this API is meant to stand on its own, without requiring
   any implicit knowledge of how S3 services are accessed using HTTP
   protocols.
 - To be usable from multithreaded code
 - To be usable by code which wants to process multiple S3 requests
   simultaneously from a single thread
 - To be usable in the simple, straightforward way using sequentialized
   blocking requests

%prep
%setup -q
%patch -p1 
sed -i 's!\$(DESTDIR)/lib/!\${libdir}/!'g GNUmakefile

%build
BUILD=%buildroot/build make exported

%install
%makeinstall  DESTDIR=%buildroot/usr 

%files
%_bindir/s3
%_libdir/libs3.so.*

%files devel
%_includedir/libs3.h
%_libdir/libs3.so

%files devel-static
%_libdir/libs3.a

%changelog
* Mon Jun 18 2012 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt1
- 2.0

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt4
- rebuild

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt3
- add conflicts to libaff

* Sun Feb 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4-alt1
- first build for Sisyphus
