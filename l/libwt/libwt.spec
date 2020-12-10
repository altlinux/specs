%define oname wt

Name: libwt
Version: 4.4.0
Release: alt1
Summary: Wt (pronounced as witty) is a C++ library for developing web applications.
License: GPL
Group: Development/C++
Url: https://www.webtoolkit.eu

# Source-url: https://github.com/emweb/wt/archive/%version.tar.gz
Source: %oname-%version.tar

BuildPreReq: gcc-c++ cmake libsqlite3-devel zlib-devel libpcre-devel
BuildPreReq: libssl-devel libmariadb-devel

# Automatically added by buildreq on Mon Nov 26 2018
# optimized out: boost-devel boost-devel-headers cmake-modules fontconfig fontconfig-devel glib2-devel glibc-devel-static libGL-devel libX11-devel libcom_err-devel libfreetype-devel libkrb5-devel libpng-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libssl-devel libstdc++-devel libunixODBC-devel libunixODBC-devel-compat pkg-config python-base python-modules python3 python3-base zlib-devel
BuildRequires: boost-asio-devel boost-filesystem-devel boost-interprocess-devel boost-program_options-devel doxygen graphviz libharu-devel libpango-devel libqt4-devel libqt4-webkit-devel phonon-devel python3-dev

%description
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.

%package devel
Summary: Wt (pronounced as witty) is a C++ library for developing web applications.
Group: System/Libraries

%description devel
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.

%package dbo
Summary: Wt (pronounced as witty) is a C++ library for developing web applications.
Group: System/Libraries

%description dbo
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.

%package dbo-mysql
Summary: Wt (pronounced as witty) is a C++ library for developing web applications (dbo mysql).
Group: System/Libraries

%description dbo-mysql
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.

%package dbo-sqlite
Summary: Wt (pronounced as witty) is a C++ library for developing web applications (dbo sqlite)
Group: System/Libraries

%description dbo-sqlite
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.

%package dbo-mssql
Summary: Wt (pronounced as witty) is a C++ library for developing web applications (dbo mssql)
Group: System/Libraries

%description dbo-mssql
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.

%package http
Summary: Wt (pronounced as witty) is a C++ library for developing web applications (http).
Group: System/Libraries

%description http
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.


%package docs
Summary: Documentation for Wt (pronounced as witty) is a C++ library for developing web applications.
Group: Development/Documentation
BuildArch: noarch

%description docs
Wt (pronounced as witty) is a C++ library for developing web applications.

The API is widget-centric and uses well-tested patterns of desktop GUI development 
tailored to the web. 
To the developer, it offers abstraction of many web-specific implementation details, 
including client-server protocols (HTTP, Ajax, WebSockets), 
and frees the developer from tedious JavaScript manipulations of HTML and dealing 
with cross-browser issues. Instead, with Wt, 
you can focus on actual functionality with a rich set of feature-complete widgets.


%prep
%setup -q -n %oname-%version

%build

ADD_CFLAGS=`pkg-config --cflags pango`

%add_optflags -I%_includedir/pcre -fno-strict-aliasing ${ADD_CFLAGS}
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DPCRE_INCLUDE_DIR:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DPOCO_UNBUNDLED:BOOL=ON \
	-DWT_CPP_11_MODE=-std=c++0x \
	.

%make_build VERBOSE=1

%install
%makeinstall_std

%if %_lib == lib64
mkdir -p %buildroot/%_libdir
mv %buildroot/usr/lib/* %buildroot/%_libdir
%endif


%files
%doc Changelog LICENSE README*
%exclude %_libdir/lib*dbo*.so.*
%exclude %_libdir/lib*test*.so.*
%exclude %_libdir/lib*http*.so.*
%_libdir/lib*.so.*

%files dbo
%_libdir/libwtdbo.so.*

%files dbo-mysql
%_libdir/libwtdbomysql.so.*

%files dbo-sqlite
%_libdir/libwtdbosqlite*.so.*

%files dbo-mssql
%_libdir/libwtdbomssqlserver*.so.*

%files http
%_libdir/lib*http*.so.*

%files devel
%dir %_includedir/Wt/
%_includedir/Wt/*
%_libdir/lib*.so
%exclude %_libdir/lib*test*.so
%dir %_sysconfdir/wt/
%config(noreplace) %_sysconfdir/wt/wt_config.xml

#files docs

%changelog
* Thu Dec 10 2020 Pavel Vainerman <pv@altlinux.ru> 4.4.0-alt1
- new version (4.4.0) with rpmgs script

* Sat Aug 24 2019 Pavel Vainerman <pv@altlinux.ru> 4.1.0-alt1
- new version (4.1.0) with rpmgs script

* Mon Nov 26 2018 Pavel Vainerman <pv@altlinux.ru> 4.0.4-alt1
- new version (4.0.4) with rpmgs script

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.2-alt2
- NMU: rebuilt with boost-1.67.0.

* Sun Nov 26 2017 Pavel Vainerman <pv@altlinux.ru> 4.0.2-alt1
- new version (4.0.2) with rpmgs script

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.7-alt2
-NMU: rebuild with libharu

* Wed Jun 14 2017 Pavel Vainerman <pv@altlinux.ru> 3.3.7-alt1
- new version 3.3.7 (with rpmrb script)

* Thu Jan 05 2017 Pavel Vainerman <pv@altlinux.ru> 3.3.6-alt0.2
- fixed unment dependencies

* Thu Jan 05 2017 Pavel Vainerman <pv@altlinux.ru> 3.3.6-alt0.1
- new version 3.3.6 (with rpmrb script)

