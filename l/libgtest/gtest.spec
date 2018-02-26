Name: libgtest
Version: 1.6.0
Release: alt1
Summary: Google's framework for writing C++ tests
Group: Development/C++
License: BSD
Url: http://code.google.com/p/googletest/
Source: gtest-%version.zip

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: gcc-c++ python-modules unzip

%description
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package devel
Group: Development/C++
Summary: Development environment for %name
Requires: %name = %version

%description devel
Development environment for %name

%package devel-static
Group: Development/C++
Summary: Static development environment for %name

%description devel-static
Static development environment for %name

%prep
%setup -n gtest-%version
# They're scared of maie install. Me not.
sed -i '/# Disables/,$d' Makefile.am

%build
# zip source sets GMT time as logal -- i.e. 3 hours in the future
find . | xargs touch
# Maybe we can also fix this by changing the autoconf macro that selects the
# pthread flags...
export LDFLAGS="-lpthread"
%autoreconf
%configure
%make_build

%install
%makeinstall
install -D scripts/gtest-config %buildroot%_bindir/gtest-config

%check
%make LIBS="-lgtest -Llib/.libs" check

%files
%doc README CHANGES CONTRIBUTORS
%_libdir/*.so.*

%files devel
%doc samples
%_bindir/*-config
%_libdir/*.so
%_includedir/gtest
%_datadir/aclocal/gtest.m4

%files devel-static
%_libdir/*.a

%changelog
* Tue Jul 05 2011 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Autobuild version bump to 1.6.0
- Rename spec and directory to confirm project name
- Resurrect make install killed by upstream

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Initial build from scratch

