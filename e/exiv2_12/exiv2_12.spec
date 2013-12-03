Name: exiv2_12
Version: 0.23
Release: alt2

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

%package -n libexiv2_12
Summary: EXIF and IPTC metadata manipulation library
Group: Graphics

%description -n libexiv2_12
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
%find_lang exiv2

%files -n libexiv2_12
%_libdir/libexiv2.so.*

%exclude %_bindir/exiv2
%exclude %_man1dir/*
%exclude %_libdir/libexiv2.so
%exclude %_includedir/*
%exclude %_pkgconfigdir/*
%exclude %_datadir/locale/*

%changelog
* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt2
- compat library without -devel subpackage

* Sun May 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23
- fixed interpackage dependencies
- enabled LFS support

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1.1
- Removed bad RPATH

* Thu Sep 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Wed Sep 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- 0.21.1

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20-alt2.1
- Rebuilt for debuginfo

* Sun Oct 31 2010 Victor Forsiuk <force@altlinux.org> 0.20-alt2
- Rebuilt for soname set-versions.

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 0.20-alt1
- 0.20

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- 0.19

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 0.18.2-alt1
- 0.18.2

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 0.17.1-alt2
- Remove obsolete ldconfig calls.

* Mon Jun 23 2008 Victor Forsyuk <force@altlinux.org> 0.17.1-alt1
- 0.17.1

* Mon Jun 09 2008 Victor Forsyuk <force@altlinux.org> 0.17-alt1
- 0.17

* Sat Mar 29 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Thu Dec 27 2007 Victor Forsyuk <force@altlinux.org> 0.12-alt3
- Library itself was included by mistake in both library and devel subpackages.
  Now we package in -devel only library symlink, as it should be. This in fact
  fixes ALT#13805.

* Mon Dec 24 2007 Victor Forsyuk <force@altlinux.org> 0.12-alt2
- Security fix: CVE-2007-6353.

* Mon Nov 27 2006 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- Initial build.

