Name: libgflags
Summary: A commandline flags library that allows for distributed flags
Version: 2.0
Release: alt1
Group: System/Libraries
Url: http://code.google.com/p/gflags
License: BSD
Source: gflags-%version.tar.gz

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: gcc-c++

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

%build
%configure
%make_build

%install
%makeinstall

%files
%_defaultdocdir/gflags*
%_libdir/*.so.*
%_bindir/gflags_completions.sh

%files devel
%_includedir/gflags
%_includedir/google
%_libdir/*.a
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
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

