Name: poco
Version: 1.7.2
Release: alt1
Summary: POrtable COmponents C++ Libraries
License: Boost Software License v1.0
Group: Development/C++
Url: http://pocoproject.org/

# https://github.com/pocoproject/poco.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake libsqlite3-devel zlib-devel libpcre-devel
BuildPreReq: libexpat-devel libssl-devel libmysqlclient-devel
BuildPreReq: libunixODBC-devel libiodbc-devel

%description
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

%package -n lib%name
Summary: POrtable COmponents C++ Libraries
Group: System/Libraries

%description -n lib%name
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

%package -n lib%name-devel
Summary: Development files of POrtable COmponents C++ Libraries
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

This package contains development files of POrtable COmponents C++
Libraries.

%package -n lib%name-devel-docs
Summary: Documentation for POrtable COmponents C++ Libraries
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

This package contains development documentation for POrtable COmponents
C++ Libraries.

%prep
%setup

%build
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
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
	.
%make_build VERBOSE=1


%install
%makeinstall_std

mkdir -p usr/%_lib
for i in %buildroot%_libdir/*.so*; do
	ln -s $i usr/%_lib/
done

export POCO_BASE=$PWD
%make -C CppParser DESTDIR=%buildroot LIBDIR=%_libdir LINKMODE=RELEASE
#make -C PocoDoc DESTDIR=%buildroot LIBDIR=%_libdir LINKMODE=RELEASE

cp -fR CppParser/include/Poco/CppParser %buildroot%_includedir/Poco/
cp -P usr/%_lib/libPocoCppParser.so* %buildroot%_libdir/

%files -n lib%name
%doc CHANGELOG CONTRIBUTORS libversion LICENSE NEWS README* VERSION
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

#files -n lib%name-devel-docs

%changelog
* Mon Mar 21 2016 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Mar 15 2016 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Mar 08 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Sep 30 2015 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- 1.6.1

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.git20140701
- Initial build for Sisyphus

