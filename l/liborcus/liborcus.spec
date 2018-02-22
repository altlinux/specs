Name: liborcus
Version: 0.13.2
Release: alt1
Summary: Standalone file import filter library for spreadsheet documents

Group: System/Libraries
License: MIT
Url: http://gitorious.org/orcus
Source: archive.tar.gz

%define libver 0.13

# Automatically added by buildreq on Thu Jul 25 2013
# optimized out: boost-devel boost-intrusive-devel libstdc++-devel pkg-config
BuildRequires: boost-devel-headers boost-interprocess-devel boost-program_options-devel gcc-c++ zlib-devel boost-filesystem-devel mdds-devel

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
%setup

%build
sed -i 's|liborcus_@ORCUS_API_VERSION@_la_LIBADD = |& ../parser/liborcus-parser-@ORCUS_API_VERSION@.la|' src/liborcus/Makefile.am
sed -i 's/liborcus_parser_.*_la_LIBADD = /& $(BOOST_SYSTEM_LIB) /' src/parser/Makefile.am

%autoreconf

# TODO spreadsheet-model requires ixion
%configure \
	--disable-debug \
	--disable-static \
	--disable-werror \
	--with-pic \
	--with-boost \
	--with-boost-system \
	--disable-python \
	--disable-spreadsheet-model \
	#

sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool

%make_build V=1

%install
make install DESTDIR=%buildroot
rm -f %buildroot/%_libdir/*.la
ln -s %name-%libver.pc %buildroot%_pkgconfigdir/%name.pc

%files
%doc AUTHORS
%_libdir/%name-*%libver.so.*

%files devel
%_includedir/%name-%libver
%_libdir/%name-*%libver.so
%_libdir/pkgconfig/%{name}*.pc

%files tools
%_bindir/orcus-*

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.13.2-alt1
- Autobuild version bump to 0.13.2

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 0.13.0-alt1
- Autobuild version bump to 0.13.0

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 0.12.1-alt2
- Rebuild with new boost

* Mon Oct 17 2016 Fr. Br. George <george@altlinux.ru> 0.12.1-alt1
- Autobuild version bump to 0.12.1

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.11.2-alt1
- Autobuild version bump to 0.11.2

* Thu Mar 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Mon Sep 21 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.2-alt1
- Updated to 0.9.2.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.7.0-alt2.1
- rebuild with boost 1.57.0

* Sat Jun 07 2014 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt2
- build to sisyphus

* Thu Feb 20 2014 Fr. Br. George <george@altlinux.ru> 0.7.0-alt1
- Autobuild version bump to 0.7.0
- Fix build (introduce chrpath hack)

* Thu Jul 25 2013 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Autobuild version bump to 0.5.1
- Fix underlinkage

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.0-alt1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build from FC

* Sat Dec 08 2012 David Tardon <dtardon@redhat.com> - 0.3.0-2
- a pointless release bump

* Fri Dec 07 2012 David Tardon <dtardon@redhat.com> - 0.3.0-1
- new release

* Sun Sep 09 2012 David Tardon <dtardon@redhat.com> - 0.1.0-1
- initial import
