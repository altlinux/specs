
%def_disable experimental

Name: libe-book
Version: 0.1.3
Release: alt1
Summary: A library for reading and converting reflowable e-book formats
License: LGPL
Url: http://sourceforge.net/projects/libebook/
Group: System/Libraries
Source: %name-%version.tar.xz

BuildRequires: gcc-c++ liblangtag-devel
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(cppunit)

%if_enabled experimental
BuildRequires: pkgconfig(libcss) >= 0.3.0 pkgconfig(libparserutils) pkgconfig(libwapcaplet)
BuildRequires: pkgconfig(libhubbub) >= 0.3.0
BuildRequires: pkgconfig(libmspack)
%endif

BuildRequires: doxygen
BuildRequires: gperf

%description
libe-book is a library and a set of tools for reading and converting
various non-HTML reflowable e-book formats.

Currently supported are:
- eReader .pdb
- FictionBook v. 2 (including zipped files)
- PalmDoc Ebook
- Plucker .pdb
- QiOO (mobile format, for java-enabled cellphones)
- TCR (simple compressed text format)
- TealDoc
- zTXT
- ZVR (simple compressed text format)

%package devel
Group: Development/C++
Summary: Development environment for %name, %summary
%description devel
%summary

%package tools
Group: Text tools
Summary: Tools for reading and converting reflowable e-book formats
%description tools
libe-book is a library and a set of tools for reading and converting
various non-HTML reflowable e-book formats.

Currently supported are:
- eReader .pdb
- FictionBook v. 2 (including zipped files)
- PalmDoc Ebook
- Plucker .pdb
- QiOO (mobile format, for java-enabled cellphones)
- TCR (simple compressed text format)
- TealDoc
- zTXT
- ZVR (simple compressed text format)

%prep
%setup

%build
%add_optflags -DBOOST_SYSTEM_NO_DEPRECATED -DBOOST_ERROR_CODE_HEADER_ONLY
%autoreconf
%configure --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files tools
%_bindir/*

%files devel
%doc README
%doc %_defaultdocdir/%name
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.1.3-alt1
- Autobuild version bump to 0.1.3

* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt4
- Fixed build with new boost.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt3
- Revert previous update and disable deprecated symbols instead

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.2-alt2
- Fixed build with new toolchain

* Thu Feb 25 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1.1
- rebuild against libicu*.so.56

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.1.2-alt1
- Autobuild version bump to 0.1.2

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Tue Mar 18 2014 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Autobuild version bump to 0.0.3

* Tue Mar 18 2014 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Initial build for ALT

