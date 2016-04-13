Name: libetonyek
Version: 0.1.6
Release: alt1
Summary: A library for import of Apple Keynote presentations

Group: System/Libraries
License: MPLv2.0
Url: http://www.freedesktop.org/wiki/Software/libetonyek/
Source: %name-%version.tar.xz

BuildRequires: cppunit-devel

# Automatically added by buildreq on Mon Sep 21 2015
# optimized out: boost-devel-headers gnu-config libstdc++-devel pkg-config xz
BuildRequires: doxygen gcc-c++ libglm-devel librevenge-devel libxml2-devel mdds-devel zlib-devel
BuildRequires: liblangtag-devel mdds-devel

%description
libetonyek is library providing ability to interpret and import Apple
Keynote presentations into various applications. Only version 5 is
supported at the moment, although versions 2-4 should work.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Apple Keynote presentations into other formats
Group: Development/C++

%description tools
Tools to transform Apple Keynote presentations into other formats.
Currently supported: XHTML, raw, text.

%prep
%setup

%build
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
make install DESTDIR=%buildroot
rm -f %buildroot/%_libdir/*.la
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

%check
export LD_LIBRARY_PATH=%buildroot/%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check

%files
%doc AUTHORS COPYING FEATURES NEWS README
%_libdir/*.so.*

%files devel
%doc ChangeLog
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING
%doc docs/doxygen/html

%files tools
%_bindir/*

%changelog
* Wed Apr 13 2016 Fr. Br. George <george@altlinux.ru> 0.1.6-alt1
- Autobuild version bump to 0.1.6

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 0.1.3-alt1
- Autobuild version bump to 0.1.3

* Wed Jun 11 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Tue May 13 2014 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- Autobuild version bump to 0.0.4
- Drop patch

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Initial build from FC

* Fri Dec 06 2013 David Tardon <dtardon@redhat.com> - 0.0.3-1
- new release

* Wed Dec 04 2013 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new release

* Mon Nov 04 2013 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new release

* Wed Oct 30 2013 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
