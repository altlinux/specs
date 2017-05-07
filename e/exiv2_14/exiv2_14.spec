%define soname 14

Name: exiv2_%soname
Version: 0.25
Release: alt1

Summary: Command line tool to access EXIF data in image files
License: GPLv2+
Group: Graphics

Url: http://www.exiv2.org
Source: %url/exiv2-%version.tar.gz

BuildRequires: gcc-c++ libexpat-devel zlib-devel
BuildRequires: doxygen xsltproc graphviz

%description
Exiv2 comprises of a C++ library and a command line utility to access image
metadata. Exiv2 supports full read and write access to the EXIF and IPTC
metadata, EXIF MakerNote support, extract and delete methods for EXIF
thumbnails, classes to access IFD and so on.

%package -n libexiv2_%soname
Summary: EXIF and IPTC metadata manipulation library
Group: Graphics

%description -n libexiv2_%soname
libexiv2 is a C++ library to access image metadata.

%prep
%setup -n exiv2-%version

%build
%make -C config -f config.make
%configure \
	--disable-static \
	--disable-rpath
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files -n libexiv2_%soname
%_libdir/libexiv2.so.*

%exclude %_bindir/exiv2
%exclude %_man1dir/*
%exclude %_libdir/libexiv2.so
%exclude %_includedir/*
%exclude %_pkgconfigdir/*
%exclude %_datadir/locale/*

%changelog
* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- compat library without -devel subpackage

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- compat library without -devel subpackage

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt2
- compat library without -devel subpackage

