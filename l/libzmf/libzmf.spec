%global apiversion 0.0

Name: libzmf
Version: 0.0.1
Release: alt1
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

%{?!_without_check:%{?!_disable_check:BuildPreReq: cppunit-devel}}

%description
libzmf is library providing ability to interpret and import Zoner
document formats into various applications. Currently it only supports
Zoner Callisto/Draw v 4-5.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Development/Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Zoner documents into other formats
Group: Other
Requires: %name = %EVR

%description tools
Tools to transform Zoner documents into other formats.
Currently supported: SVG, raw.

%prep
%setup

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-werror \
	%{?_without_check:--disable-tests} \
	%{?_disable_check:--disable-tests} \
	#

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

%files
%doc AUTHORS NEWS COPYING
%_libdir/%name-%apiversion.so.*

%files devel
%doc ChangeLog
%_includedir/%name-%apiversion
%_libdir/%name-%apiversion.so
%_libdir/pkgconfig/%name-%apiversion.pc

%files doc
%doc docs/doxygen/html COPYING

%files tools
%_bindir/zmf2raw
%_bindir/zmf2svg
%_mandir/man1/zmf2raw.1*
%_mandir/man1/zmf2svg.1*

%changelog
* Thu Feb 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.0.1-alt1
- Initial build.
