# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define major 7
%define libname libmysqlcppconn%major
%define develname libmysqlcppconn-devel

Summary: A MySQL database connector for C++
Name: mysql-connector-c++
Version: 1.1.9
Release: alt1
Group: System/Libraries
License: GPLv2
Url: http://dev.mysql.com/downloads/connector/cpp/
Source0: http://cdn.mysql.com/Downloads/Connector-C++/%name-%version.tar.gz
## patches from arch-linux
Patch0: mysql_cxx_linkage.patch
Patch1: mariadb_api.patch
Source44: import.info

# Automatically added by buildreq on Sat Feb 03 2018
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel python-base python-modules python3 python3-base
BuildRequires: boost-devel-headers cmake gcc-c++ libmysqlclient-devel python3-dev

%description
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

Using MySQL Connector/C++ instead of the MySQL C API (MySQL Client Library)
offers the following advantages for C++ users:

    * Convenience of pure C++ - no C function calls
    * Support of a well designed API - JDBC 4.0
    * Support of a commonly known and well documented API - JDBC 4.0
    * Support of the object oriented programming paradigma
    * Shorter development times

%package -n	%libname
Summary: The shared mysql-connector-cpp library
Group: System/Libraries
Provides: %name = %version-%release

%description -n	%libname
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

Using MySQL Connector/C++ instead of the MySQL C API (MySQL Client Library)
offers the following advantages for C++ users:

    * Convenience of pure C++ - no C function calls
    * Support of a well designed API - JDBC 4.0
    * Support of a commonly known and well documented API - JDBC 4.0
    * Support of the object oriented programming paradigma
    * Shorter development times

%package -n	%develname
Summary: Development library and header files for development with mysql-connector-cpp
Group: Development/C++
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n	%develname
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

Using MySQL Connector/C++ instead of the MySQL C API (MySQL Client Library)
offers the following advantages for C++ users:

    * Convenience of pure C++ - no C function calls
    * Support of a well designed API - JDBC 4.0
    * Support of a commonly known and well documented API - JDBC 4.0
    * Support of the object oriented programming paradigma
    * Shorter development times

%prep
%setup
%patch0 -p1 -b .linkage
%patch1 -p1 -b .mariadb
chmod -x examples/*.cpp examples/*.txt

# Save examples to keep directory clean (for doc)
mkdir _doc_examples
cp -pr examples _doc_examples

%build
%cmake \
		-DMYSQL_INCLUDE_DIR=%_includedir/mysql \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_LIBDIR=%_libdir \
		-DMYSQLCPPCONN_BUILD_EXAMPLES=OFF \
		-DMYSQL_LIB=%_libdir/libmysqlclient.so
%cmake_build

%install
cp BUILD/cppconn/config.h  cppconn/config.h

%makeinstall_std -C BUILD
rm -fr %buildroot%prefix/COPYING
rm -fr %buildroot%prefix/INSTALL
rm -fr %buildroot%prefix/README
rm -fr %buildroot%prefix/ANNOUNCEMENT
rm -fr %buildroot%prefix/Licenses_for_Third-Party_Components.txt
rm -f %buildroot%_libdir/libmysqlcppconn-static.a

%files -n %libname
%_libdir/*.so.*

%files -n %develname
%doc README COPYING examples
%dir %_includedir/cppconn
%_includedir/*.h
%_includedir/cppconn/*.h
%_libdir/*.so

%changelog
* Sat Feb 03 2018 Fr. Br. George <george@altlinux.ru> 1.1.9-alt1
- Autobuild version bump to 1.1.9
- Fix overloaded buildreq

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_1
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt2_2
- update by mgaimport

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt2_1
- devel bugfixes

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_1
- use mageia

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_1
- initial fc import

