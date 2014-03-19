Name: libfreehand
Version: 0.0.0
Release: alt1
Summary: A library for import of Macromedia/Adobe FreeHand documents

Group: System/Libraries
License: MPLv2.0
Url: http://www.freedesktop.org/wiki/Software/libfreehand/
Source: http://dev-www.libreoffice.org/src/%name-%version.tar.xz

Patch0: 0001-coverity-fix-memory-leak.patch

# Automatically added by buildreq on Wed Mar 19 2014
# optimized out: gnu-config libstdc++-devel libwpd9-devel pkg-config xz
BuildRequires: doxygen gcc-c++ gperf libwpg-devel zlib-devel

%description
libfreehand is library providing ability to interpret and import
Macromedia/Adobe FreeHand documents into various applications.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

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
Summary: Tools to transform Macromedia/Adobe FreeHand documents into other formats
Group: Publishing

%description tools
Tools to transform Macromedia/Adobe FreeHand documents into other formats.
Currently supported: SVG, raw.

%prep
%setup

%patch0 -p1

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

%files
%doc AUTHORS COPYING
%_libdir/*.so.*

%files devel
%doc ChangeLog
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files doc
%doc COPYING
%doc docs/doxygen/html

%files tools
%_bindir/fh2raw
%_bindir/fh2svg

%changelog
* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.0-alt1
- Initial build from FC

* Mon Nov 04 2013 David Tardon <dtardon@redhat.com> - 0.0.0-3
- fix memory leak

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> 0.0.0-2
- add gperf to BuildRequires

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
