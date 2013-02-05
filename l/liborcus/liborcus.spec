Name: liborcus
Version: 0.3.0
Release: alt1
Summary: Standalone file import filter library for spreadsheet documents

Group: System/Libraries
License: MIT
Url: http://gitorious.org/orcus
Source: http://kohei.us/files/orcus/src/%{name}_%version.tar.bz2
Patch: liborcus-alt-boost.patch

# Automatically added by buildreq on Mon Feb 04 2013
# optimized out: boost-devel boost-intrusive-devel gnu-config libstdc++-devel pkg-config
BuildRequires: boost-devel-headers boost-interprocess-devel boost-program_options-devel gcc-c++ zlib-devel

%description
%name is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tools for working with Orcus
Group: Publishing

%description tools
Tools for working with Orcus.

%prep
%setup -n %{name}_%version
%patch -p1

%build
# TODO spreadsheet-model requires ixion
%configure --disable-debug --disable-static --disable-werror --with-pic \
    --disable-spreadsheet-model --without-libzip
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build V=1

%install
make install DESTDIR=%buildroot
rm -f %buildroot/%_libdir/*.la

%files
%doc AUTHORS
%_libdir/%name-0.4.so.*

%files devel
%_includedir/%name-0.4
%_libdir/%name-0.4.so
%_libdir/pkgconfig/%name-0.4.pc

%files tools
%_bindir/orcus-xml-dump

%changelog
* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build from FC

* Sat Dec 08 2012 David Tardon <dtardon@redhat.com> - 0.3.0-2
- a pointless release bump

* Fri Dec 07 2012 David Tardon <dtardon@redhat.com> - 0.3.0-1
- new release

* Sun Sep 09 2012 David Tardon <dtardon@redhat.com> - 0.1.0-1
- initial import
