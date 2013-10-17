Name: libgmock
Version: 1.7.0
Release: alt1
Summary: Google C++ Mocking Framework
Group: Development/C++
License: BSD
Url: http://code.google.com/p/googlemock/
Source: gmock-%version.zip

Provides: gmock
BuildRequires: gcc-c++ python-modules unzip libgtest-devel

%description
Google's framework for writing and using C++ mock classes on a variety
of platforms (Linux, Mac OS X, Windows, Windows CE, Symbian, etc).
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, it can help you derive better designs of your
system and write better tests.

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
%setup -n gmock-%version
# They're scared of maie install. Me not.
sed -i '/# Disables/,$d' Makefile.am
#Fix undefined symbol to libgtest
sed -i '/^lib_libgmock_la_SOURCES/a lib_libgmock_la_LIBADD = $(GTEST_LIBS)' Makefile.am
sed -i '/^lib_libgmock_main_la_LIBADD/s/= /= $(GTEST_LIBS) /g' Makefile.am

%build
# zip source sets GMT time as logal -- i.e. 3 hours in the future
find . | xargs touch

%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -D scripts/gmock-config %buildroot%_bindir/gmock-config

%check
%make LIBS="-lgmock -Llib/.libs" check

%files
%doc README CHANGES CONTRIBUTORS
%_libdir/*.so.*

%files devel
%_bindir/*-config
%_libdir/*.so
%_includedir/gmock

%files devel-static
%_libdir/*.a

%changelog
* Thu Oct 17 2013 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Autobuild version bump to 1.7.0

* Mon Jul 01 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.0-alt1
- Build for ALT

