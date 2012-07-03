%define		srcname pion-net

Name:		lib%srcname
Version:	4.0.1
Release:	alt3.2
Summary:	Pion Network Library (pion-net) is a C++ development library for implementing lightweight HTTP interfaces.
License: 	Boost Software License v1.0
Group: 		System/Libraries
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.pion.net/projects/pion-network-library
Source0:	http://www.pion.net/files/%srcname-%version.tar.bz2
Patch:		libpion-net-4.0.1-alt-fix-build-with-boost.patch

# Automatically added by buildreq on Tue Sep 06 2011 (-bi)
# optimized out: boost-devel elfutils i586-glibc-core libcom_err-devel libgfortran-devel libkrb5-devel libstdc++-devel pkg-config python-base python-modules-compiler ruby
BuildRequires: boost-devel boost-asio-devel boost-filesystem-devel boost-interprocess-devel boost-signals-devel bzlib-devel doxygen gcc-c++ libicu-devel libssl-devel zlib-devel
# buildreqs updated manualy by iv@, as robot is insane a bit

BuildPreReq: python-modules

%description
Pion Network Library (pion-net) is a C++ development library for
implementing lightweight HTTP interfaces.
There are a wide variety of open source HTTP servers available,
from fast and lightweight servers such as lighttpd, to full-featured
platforms like Apache HTTPD. The motivation of pion-net is not to
implement yet another web server, but to provide HTTP(S) functionality
to new or existing C++ applications. If you're looking for a full-featured
server application, we suggest that you use one of the projects above.
If you're working on a Boost C++ application and would just like to
use HTTP to provide a simple user interface or interact with run-time
data, then pion-net is a much cleaner and simpler solution.

%package devel
Summary: Header files for %srcname library
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files for %srcname library

%package plugins
Summary: %srcname plugins
Group: System/Libraries

%description plugins
%srcname plugins

%package -n %srcname-servers
Summary: %srcname servers
Group: System/Servers

%description -n %srcname-servers
%srcname servers

%package static
Summary: Static %srcname library
Group: Development/C++
Requires: %name-devel = %version-%release

%description static
Static %srcname library.

%package docs
Summary: %srcname documentation
Group: Documentation
BuildArch: noarch

%description docs
%srcname documnetation.

%prep
%setup -n %srcname-%version
%patch -p2

%build
%configure --with-plugins=%_libdir/%srcname
%make_build CXXFLAGS+=-DBOOST_FILESYSTEM_VERSION=2 CFLAGS+=-DBOOST_FILESYSTEM_VERSION=2

%install
%make DESTDIR=%buildroot install
rm -rf %buildroot{%_libdir/%srcname/*.la,%_libdir/%srcname/*.a,%_libdir/*.la}

%files
%_libdir/*.so

%files docs
%doc net/doc/html AUTHORS ChangeLog README

%files -n %srcname-servers
%_bindir/*

%files plugins
%_libdir/%srcname

%files devel
%_includedir/pion
%_pkgconfigdir/*

%files static
%_libdir/*.a

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3.2
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3.1
- Rebuilt with Boost 1.48.0

* Tue Sep 06 2011 Ivan A. Melnikov <iv@altlinux.org> 4.0.1-alt3
- fixed build requirements.

* Mon Jul 25 2011 Ivan A. Melnikov <iv@altlinux.org> 4.0.1-alt2
- added patch to fix build with boost >= 1.47.0;
- rebuild with new boost.

* Fri Mar 11 2011 Motsyo Gennadi <drool@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux
