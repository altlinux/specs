%global apiversion 0.0

Name: libstaroffice
Version: 0.0.5
Release: alt1
Summary: A library for import of binary StarOffice documents

Group: System/Libraries
License: %mpl|%lgpl2plus
Url: https://github.com/fosnola/libstaroffice/wiki
# Repacked https://github.com/fosnola/%name/releases/download/%version/%name-%version.tar.xz
Source: %name-%version.tar.xz

BuildRequires(pre): rpm-build-licenses
BuildPreReq: help2man

# Automatically added by buildreq on Wed Feb 08 2017
# optimized out: gnu-config libstdc++-devel pkg-config python-base python-modules python3
BuildRequires: doxygen gcc-c++ librevenge-devel python3-base zlib-devel

%description
%name is a library for import of binary StarOffice documents.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Group: Development/Documentation
Summary: Documentation of %name API
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Group: Development/Other
Summary: Tools to transform StarOffice documents into other formats
Requires: %name = %EVR

%description tools
Tools to transform StarOffice documents into other formats. Currently
supported: CSV, HTML, plain text, SVG, raw.

%prep
%setup

%build
%configure \
	--disable-static \
	--disable-werror \
	--disable-silent-rules \
	--enable-zip \
	--with-sharedptr=c++11 \
	#

sed -i \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool

%make_build

%install
%makeinstall_std
rm %buildroot/%_libdir/*.la
rm -r %buildroot/%_docdir/%name

# generate and install man pages
export LD_LIBRARY_PATH=%buildroot/%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in sd2raw sd2svg sd2text sdc2csv sdw2html; do
    help2man -N -S '%name %version' -o ${tool}.1 %buildroot%_bindir/${tool}
done
mkdir -p %buildroot/%_mandir/man1
cp -p sd2*.1 sd?2*.1 %buildroot/%_mandir/man1

%files
%doc CREDITS NEWS README COPYING.LGPL COPYING.MPL
%_libdir/%name-%apiversion.so.*

%files devel
%doc ChangeLog
%_includedir/%name-%apiversion
%_libdir/%name-%apiversion.so
%_libdir/pkgconfig/%name-%apiversion.pc

%files doc
%doc docs/doxygen/html COPYING.LGPL COPYING.MPL

%files tools
%_bindir/sdw2html
%_bindir/sd2raw
%_bindir/sd2svg
%_bindir/sd2text
%_bindir/sdc2csv
%_mandir/man1/sdw2html.1*
%_mandir/man1/sd2raw.1*
%_mandir/man1/sd2svg.1*
%_mandir/man1/sd2text.1*
%_mandir/man1/sdc2csv.1*

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.0.5-alt1
- Autobuild version bump to 0.0.5

* Thu Feb 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.0.2-alt1
- Initial build.
