Name: libe-book
Version: 0.0.3
Release: alt1
Summary: A library for reading and converting reflowable e-book formats
License: LGPL
Url: http://sourceforge.net/projects/libebook/
Group: System/Libraries
Source: %name-%version.tar.xz

BuildRequires: cppunit-devel

# Automatically added by buildreq on Tue Mar 18 2014
# optimized out: libcloog-isl4 libstdc++-devel pkg-config xz
BuildRequires: boost-devel-headers doxygen gcc-c++ gperf libicu-devel libwpd9-devel libxml2-devel zlib-devel

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
%autoreconf
%configure
%make_build

%install
%makeinstall

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
* Tue Mar 18 2014 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Autobuild version bump to 0.0.3

* Tue Mar 18 2014 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Initial build for ALT

