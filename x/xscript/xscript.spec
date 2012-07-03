%define ugname _xscript
Summary: XScript is xml-based application server written in C++.
Name: xscript
Version: 5.63
Release: alt24.5
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://xscript.opensource.yandex.net
Source: %name.tar.bz2
Source2: %name-daemon.init
Patch: %name-configure.in.patch
Patch1: %name-context.h.patch
Patch2: %name-file_logger.h.patch
Patch3: %name-thread_pool.cpp.patch
Patch4: %name-component.h.patch
Patch5: %name-5.63-alt-DSO.patch

# Automatically added by buildreq on Sun Jan 11 2009
BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: boost-filesystem-devel boost-python-devel 
BuildRequires: gcc-c++ glibc-devel-static libcurl-devel libfcgi-devel liblua5-devel libxslt-devel

BuildPreReq: libssl-devel

%package common
Summary: %name common
Group: System/Servers

%package daemon
Summary: %name daemon
Group: System/Servers
Requires: %name-common = %version-%release

%package standart
Summary: %name modules
Group: System/Servers
Requires: %name-common = %version-%release


%package -n lib%name
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release

%package -n lib%name-devel
Summary: %name library development files
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: %name static library
Group: Development/C
Requires: lib%name-devel = %version-%release

%package -n lib%name-offline
Summary: %name offline library
Group: System/Libraries

%package -n lib%name-offline-devel
Summary: %name offline library development files
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-offline-devel-static
Summary: %name offline static library
Group: Development/C
Requires: lib%name-devel = %version-%release

%package -n python-module-%name
Summary: %name python module
Group: Development/Python

%package -n %name-utility
Summary: %name utulity
Group: System/Servers
Requires: %name-common = %version-%release

%description
XScript is xml-based application server written in C++.

%description common
Common %name files

%description daemon
Binary that runs as factcgi-daemon.

%description standart
Standard modules such as logger, thread pool and various blocks.

%description -n lib%name
%name library

%description -n lib%name-devel
%name library development files

%description -n lib%name-devel-static
%name static library

%description -n lib%name-offline
%name offline library

%description -n lib%name-offline-devel
%name offline library development files

%description -n lib%name-offline-devel-static
%name offline static library

%description -n python-module-%name
%name python module

%description -n %name-utility
XScript offline processor.
%name utility

%prep
%setup -q -n %name
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p2

%build
# touch config.rpath
%__subst 's|-lboost_thread|-lboost_thread-mt|g' configure.in
find . -name "Makefile.am" -exec %__subst 's|-lboost_thread|-lboost_thread-mt|g' {} \;
cp %_datadir/gettext/intl/config.rpath config.rpath

ACLOCAL_OPTIONS="-I config" ./autogen.sh
%add_optflags -DBOOST_FILESYSTEM_VERSION=2
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--enable-cppunit \
	--enable-maintainer-mode

%make_build

%install
%makeinstall_std

mkdir -p %buildroot/%_var/run/%name
mkdir -p %buildroot/%_var/log/%name
mkdir -p %buildroot/%_var/cache/%name
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_initdir
mkdir -p %buildroot/%_sysconfdir/cron.d

install -m755 %SOURCE2 %buildroot/%_initdir/%name
install -m755 extra/%{name}start.sh %buildroot/%_sbindir
install extra/xscript-cache-clean %buildroot/%_sysconfdir/cron.d
install -m755 extra/xscriptcacheclean.sh %buildroot/%_bindir

%pre
# Create user and groups
%_sbindir/groupadd -r -f %ugname 2>/dev/null ||:
%_sbindir/useradd -g %ugname -c '%name WWW server' -d '/dev/null' -s '/dev/null' \
	-G %webserver_group,%ugname -r %ugname 2>/dev/null || :

%files common
%dir %_sysconfdir/%name

%files daemon
%doc debian/changelog
%config(noreplace) %_sysconfdir/%name/%name-ulimits.conf
%_initdir/%name
%_bindir/%name-bin
%_sbindir/%{name}start.sh
%attr(2775,root,%ugname) %dir %_var/run/%name
%attr(2775,root,%ugname) %dir %_var/log/%name

%files standart
%_sysconfdir/cron.d/*
%_bindir/xscriptcacheclean.sh
%dir %_libdir/%name
%_libdir/%name/*.so*
%attr(2775,root,%ugname) %dir %_var/cache/%name

%files -n lib%name
%_sysconfdir/%name/%name.conf.example
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name
%_includedir/%name/*.h

%files -n lib%name-devel-static
%_libdir/lib%name.a

%files -n lib%name-offline
%_libdir/lib%name-offline.so.*
%dir %_libdir/%name

%files -n lib%name-offline-devel
%_libdir/lib%name-offline.so
%dir %_includedir/%name-utility
%_includedir/%name-utility/*.h

%files -n lib%name-offline-devel-static
%_libdir/lib%name-offline.a

%files -n python-module-%name
%python_sitelibdir/*.so*

%files -n %name-utility
%config(noreplace) %_sysconfdir/%name/offline.conf
%_bindir/%name-proc
%dir %_datadir/%name-proc
%_datadir/%name-proc/*.xsl

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.5
- Rebuilt

* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.4
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.3
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.2
- Rebuilt with Boost 1.48.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.63-alt24.1.3.1
- Rebuild with Python-2.7

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.1.2
- Rebuilt with Boost 1.46.1
- Added libssl-devel into BuildPreReq

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 5.63-alt24.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.63-alt24.1
- Rebuilt with python 2.6

* Mon Jul 06 2009 Boris Savelev <boris@altlinux.org> 5.63-alt24
- new version
- rebuild with new boost

* Tue May 12 2009 Boris Savelev <boris@altlinux.org> 5.61-alt13
- new version

* Sat Mar 14 2009 Boris Savelev <boris@altlinux.org> 5.55-alt12
- new version
- build with autogen.sh

* Tue Feb 24 2009 Boris Savelev <boris@altlinux.org> 5.54-alt1
- fix numeration
- new version
- add changelog into doc
- split packages
- add python bindings

* Fri Feb 13 2009 Boris Savelev <boris@altlinux.org> 0.1-alt2.svn745
- fix virtual user creation

* Fri Feb 13 2009 Boris Savelev <boris@altlinux.org> 0.1-alt1.svn745
- initial build for Sisyphus

