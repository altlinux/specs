Name: libepubgen
Version: 0.1.0
Release: alt1
Summary: An EPUB generator library
Group: Development/C++

License: MPLv2.0
Url: https://sourceforge.net/projects/libepubgen/
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.xz

BuildRequires: cppunit-devel libxml2-devel
# Automatically added by buildreq on Mon Feb 19 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libstdc++-devel pkg-config python-base xz
BuildRequires: boost-devel-headers doxygen gcc-c++ librevenge-devel

%description
%name is a library for generating EPUB documents. It is directly
pluggable into import filters based on librevenge.

%package devel
Summary: Development files for %name
Requires: %name%{?_isa} = %version-%release
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
BuildArch: noarch
Group: Development/C++

%description doc
The %name-doc package contains documentation files for %name.

%prep
%setup

%build
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
make install DESTDIR=%buildroot INSTALL='install -p'
rm -rf %buildroot/%_docdir/%name

%check
LD_LIBRARY_PATH=%buildroot%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} make check

%files
%doc AUTHORS README NEWS
%_libdir/%{name}*.so.*

%files devel
%doc ChangeLog
%_includedir/%{name}*
%_libdir/%{name}*.so
%_libdir/pkgconfig/%{name}*

%files doc
%doc docs/doxygen/html

%changelog
* Mon Feb 19 2018 Fr. Br. George <george@altlinux.ru> 0.1.0-alt1
- Initial build from FC
