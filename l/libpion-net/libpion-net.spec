%define		srcname pion-net

%add_optflags -DBOOST_NO_CXX11_RVALUE_REFERENCES=1

Name:		lib%srcname
Version:	5.0.7
Release:	alt1.git20141017.2
Summary:	Pion Network Library (pion-net) is a C++ development library for implementing lightweight HTTP interfaces.
License: 	Boost Software License v1.0
Group: 		System/Libraries
Url:		http://sourceforge.net/projects/pion/
Source0:	%srcname-%version.tar

BuildRequires: boost-devel boost-asio-devel boost-filesystem-devel boost-interprocess-devel boost-signals-devel bzlib-devel doxygen gcc-c++ libicu-devel libssl-devel zlib-devel

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

%build
%add_optflags -fpermissive -std=gnu++11
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
%make_build V=1

%make docs

%install
%makeinstall_std
rm -rf %buildroot{%_libdir/%srcname/*.la,%_libdir/%srcname/*.a,%_libdir/*.la}

install -d %buildroot%_sysconfdir/pion
cp -fR platform/build/config/* %buildroot%_sysconfdir/pion/

install -d %buildroot%_datadir/pion
cp -fR platform/ui %buildroot%_datadir/pion/

install -d %buildroot%_docdir/%srcname
cp -fR doc/html doc/*.pdf AUTHORS ChangeLog NEWS *.md TODO *.html \
	%buildroot%_docdir/%srcname

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
* Tue Aug 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.7-alt1.git20141017.2
- Rebuilt with boost 1.63.0.

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0.7-alt1.git20141017.1
- Rebuilt for gcc5 C++11 ABI.

* Thu May 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.7-alt1.git20141017
- Version 5.0.7

* Thu May 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt1.1.qa4
- Rebuilt with log4cplus 2.0.0

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 4.0.13-alt1.1.qa3.1
- rebuild with boost 1.57.0

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt1.1.qa3
- Rebuilt with log4cplus 1.2.0-rc1

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.13-alt1.1.qa2
- Rebuilt with log4cplus 1.1.2

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.0.13-alt1.1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

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
