Name: libgflags
Summary: A commandline flags library that allows for distributed flags
Version: 2.1.1
Release: alt1
Group: System/Libraries
Url: http://code.google.com/p/gflags
License: BSD
Source: v%version.tar.gz
Patch: gflags-2.1.1-cmake.patch

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: gcc-c++ cmake

%description
The %name package contains a library that implements commandline flags
processing.  As such it's a replacement for getopt().  It has increased
flexibility, including built-in support for C++ types like string, and
the ability to define flags in the source file in which they're used.

%package devel
Summary: A commandline flags library that allows for distributed flags
Group: Development/C++
Requires: %name = %version

%description devel
The %name-devel package contains static and debug libraries and header
files for developing applications that use the %name package.

%prep
%setup -n gflags-%version
%patch
# bloody cmakers!
sed -i 's/set (LIBRARY_INSTALL_DIR lib)/set (LIBRARY_INSTALL_DIR %_lib)/' CMakeLists.txt

%build
%cmake -DBUILD_SHARED_LIBS=True -DBUILD_gflags_nothreads_LIB=False
%cmake_build

%install
%cmakeinstall_std

%files
%doc *.txt
%_libdir/*.so.*
%_bindir/gflags_completions.sh

%files devel
%doc doc/*
%_includedir/gflags
%_libdir/*.so
%_prefix/lib/cmake/*
##_libdir/pkgconfig/*.pc

%changelog
* Fri Aug 22 2014 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1
- Provide CMake devel instead of pkgconfig (upstream switched to cmake)
- Switch nothread build off (temporary?)

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Initial build from native spec

	* Thu Sep 10 2009 <opensource@google.com>
        - Change from '%configure' to something like it, but without -m32

	* Mon Apr 20 2009 <opensource@google.com>
	- Change build rule to use '%configure' rather than './configure'
	- Change install to use DESTDIR instead of prefix for make install.
	- Use wildcards for doc/ and lib/ directories
        - Use {_libdir}/{_includedir}/etc instead of {prefix}/lib, etc

	* Tue Dec 13 2006 <opensource@google.com>
	- First draft

