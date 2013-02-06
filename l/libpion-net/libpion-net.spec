%define		srcname pion-net

Name:		lib%srcname
Version:	4.0.13
Release:	alt1.1
Summary:	Pion Network Library (pion-net) is a C++ development library for implementing lightweight HTTP interfaces.
License: 	Boost Software License v1.0
Group: 		System/Libraries
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.pion.net/projects/pion-network-library
Source0:	http://www.pion.net/files/%srcname-%version.tar.bz2
Patch:		libpion-net-4.0.1-alt-fix-build-with-boost.patch
Patch1: libpion-net-4.0.13-alt-boost-1.52.0.patch
Patch2: libpion-net-4.0.13-alt-log4cplus.patch
Patch3: libpion-net-4.0.13-alt-install.patch
Patch4: libpion-net-4.0.13-alt-link.patch

# Automatically added by buildreq on Tue Sep 06 2011 (-bi)
# optimized out: boost-devel elfutils i586-glibc-core libcom_err-devel libgfortran-devel libkrb5-devel libstdc++-devel pkg-config python-base python-modules-compiler ruby
BuildRequires: boost-devel boost-asio-devel boost-filesystem-devel boost-interprocess-devel boost-signals-devel bzlib-devel doxygen gcc-c++ libicu-devel libssl-devel zlib-devel
# buildreqs updated manualy by iv@, as robot is insane a bit

BuildPreReq: python-modules python-devel
BuildPreReq: liblog4cplus-devel libxml2-devel graphviz

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
Requires: %srcname-data = %version-%release

%description -n %srcname-servers
%srcname servers

%package -n %srcname-data
Summary: Data files for %srcname
Group: System/Servers
BuildArch: noarch

%description -n %srcname-data
%srcname data

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
#patch -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build
%add_optflags -fpermissive
export CPPFLAGS="%optflags"
./autogen.sh
%configure \
	--enable-static \
	--with-plugins=%_libdir/%srcname \
	--with-log4cplus \
	--with-zlib \
	--with-bzlib \
	--with-openssl \
	--with-libxml \
	--with-python=%_bindir/python \
	--enable-doxygen-dot \
	--enable-doxygen-man
%make_build

%install
%make DESTDIR=%buildroot install
rm -rf %buildroot{%_libdir/%srcname/*.la,%_libdir/%srcname/*.a,%_libdir/*.la}

install -d %buildroot%_docdir/%srcname
install -p -m644 net/doc/*.pdf AUTHORS ChangeLog NEWS \
	%buildroot%_docdir/%srcname
pushd %buildroot%_datadir/pion/doc
mv * %buildroot%_docdir/%srcname/
popd

%files
%_libdir/*.so

%files docs
%_docdir/%srcname

%files -n %srcname-servers
%_bindir/*
%dir %_sysconfdir/pion
%dir %_sysconfdir/pion/pymodules
%dir %_sysconfdir/pion/vocabularies
%config(noreplace) %_sysconfdir/pion/*.xml
%config(noreplace) %_sysconfdir/pion/logconfig.txt
%config(noreplace) %_sysconfdir/pion/*/*
%config %_sysconfdir/pion/sslkey.pem


%files -n %srcname-data
%_datadir/pion

%files plugins
%_libdir/%srcname

%files devel
%_includedir/pion
%_pkgconfigdir/*

%files static
%_libdir/*.a

# TODO: yajl support (need 2.0.5 minimum)

%changelog
* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt1.1
- Rebuilt with log4cplus 1.1.1-rc3

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt1
- Version 4.0.13

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
