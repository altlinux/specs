%global apiversion 0.0
%define soname 0

%set_automake_version 1.16

Name: libzmf
Version: 0.0.2
Release: alt4
Summary: A library for import of Zoner document formats

Group: System/Libraries
License: %mpl
Url: http://wiki.documentfoundation.org/DLP/Libraries/libzmf
# Repacked http://dev-www.libreoffice.org/src/%name/%name-%version.tar.xz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildPreReq: help2man

# Automatically added by buildreq on Wed Feb 08 2017
# optimized out: gnu-config libstdc++-devel pkg-config python-base python-modules python3 zlib-devel
BuildRequires: boost-devel-headers doxygen gcc-c++ libicu-devel libpng-devel librevenge-devel python3-base
BuildRequires: zlib-devel

%{?!_without_check:%{?!_disable_check:BuildPreReq: cppunit-devel}}

%description
libzmf is library providing ability to interpret and import Zoner
document formats into various applications. Currently it only supports
Zoner Callisto/Draw v 4-5.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soname = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Development/Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch

%description common
%name common package.

%package -n %name%soname
Group: System/Libraries
Summary: %name library
Obsoletes: %name <= 0.0.2-alt3

%description -n %name%soname
%name library.

%package tools
Summary: Tools to transform Zoner documents into other formats
Group: Other
Requires: %name%soname = %EVR

%description tools
Tools to transform Zoner documents into other formats.
Currently supported: SVG, raw.

%prep
%setup

subst 's|.png|.svg|' docs/doxygen/Makefile.am

%build
%autoreconf
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-werror \
	%{?_without_check:--disable-tests} \
	%{?_disable_check:--disable-tests} \
	#

doxygen -u docs/doxygen/doxygen.cfg

%make_build

%install
%makeinstall_std
rm %buildroot/%_libdir/*.la
rm -r %buildroot/%_docdir/%name

# generate and install man pages
export LD_LIBRARY_PATH=%buildroot/%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in zmf2raw zmf2svg; do
    help2man -N -S '%name %version' -o ${tool}.1 %buildroot%_bindir/${tool}
done
mkdir -p %buildroot/%_mandir/man1
cp -p zmf2*.1 %buildroot/%_mandir/man1

%check
export LD_LIBRARY_PATH=%buildroot/%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files -n %name%soname
%_libdir/%name-%apiversion.so.%soname
%_libdir/%name-%apiversion.so.%{soname}.*

%files devel
%_includedir/%name-%apiversion
%_libdir/%name-%apiversion.so
%_libdir/pkgconfig/%name-%apiversion.pc

%files doc
%doc docs/doxygen/html

%files common
%doc COPYING AUTHORS NEWS ChangeLog

%files tools
%_bindir/zmf2raw
%_bindir/zmf2svg
%_mandir/man1/zmf2raw.1*
%_mandir/man1/zmf2svg.1*

%changelog
* Fri Jan 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.0.2-alt4
- Builded in accordance with SharedLibsPolicy.

* Sat Jan 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.0.2-alt3
- fixed FTBFS

* Sat Aug 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.0.2-alt2
- fixed FTBFS

* Sun Jul 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.0.2-alt1
- 0.0.1 -> 0.0.2
- fixed FTBFS

* Thu Feb 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.0.1-alt1
- Initial build.
