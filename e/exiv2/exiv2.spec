%def_enable video
%def_enable webready
%def_disable check

Name: exiv2
Version: 0.26
Release: alt2

Summary: Command line tool to access EXIF data in image files
License: GPLv2+
Group: Graphics
Url: http://www.exiv2.org

#VCS: https://github.com/Exiv2/exiv2.git
Source: https://github.com/Exiv2/%name/archive/%name-%version.tar.gz
Patch: %name-0.23-alt-lfs.patch

# fc
## upstream patches (lookaside cache)
Patch6:  0006-1296-Fix-submitted.patch

# Security fixes
Patch10: exiv2-CVE-2017-17723.patch
Patch11: exiv2-wrong-brackets.patch
Patch12: exiv2-CVE-2017-11683.patch
Patch13: exiv2-CVE-2017-14860.patch
Patch14: exiv2-CVE-2017-14864-CVE-2017-14862-CVE-2017-14859.patch
Patch15: exiv2-CVE-2017-17725.patch
Patch16: exiv2-CVE-2017-17669.patch
Patch17: exiv2-additional-security-fixes.patch
Patch18: exiv2-CVE-2018-10958.patch
Patch19: exiv2-CVE-2018-10998.patch
Patch20: exiv2-CVE-2018-11531.patch
Patch21: exiv2-CVE-2018-12264-CVE-2018-12265.patch
Patch22: exiv2-CVE-2018-14046.patch
Patch23: exiv2-CVE-2018-5772.patch
Patch24: exiv2-CVE-2018-8976.patch
Patch25: exiv2-CVE-2018-8977.patch

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ libexpat-devel zlib-devel
BuildRequires: doxygen xsltproc graphviz
%{?_enable_webready:BuildRequires: libcurl-devel libssh-devel libgcrypt-devel}

%description
Exiv2 comprises of a C++ library and a command line utility to access
image metadata. Exiv2 supports full read and write access to the EXIF and
IPTC metadata, EXIF MakerNote support, extract and delete methods for
EXIF thumbnails, classes to access IFD and so on.

%package -n libexiv2
Summary: EXIF and IPTC metadata manipulation library
Group: Graphics

%description -n libexiv2
libexiv2 is a C++ library to access image metadata.

%package -n libexiv2-devel
Summary: Headers and links to compile against the exiv2 library
Group: Development/C
Requires: libexiv2 = %version-%release

%description -n libexiv2-devel
This package contains all files which one needs to compile programs using the
exiv2 library.

%prep
%setup -n %name-%version
%patch -b .lfs
%patch6 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1

%build
%make -C config -f config.make
# exiv2: embedded copy of exempi should be compiled with BanAllEntityUsage
# https://bugzilla.redhat.com/show_bug.cgi?id=888769
export CPPFLAGS="$CPPFLAGS -DBanAllEntityUsage=1"
%configure \
	--disable-static \
	--disable-rpath \
	%{subst_enable video} \
	%{subst_enable webready}
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std
%find_lang exiv2

%check
%make check

%files
%_bindir/%name
%_man1dir/*
%doc README doc/ChangeLog

%files -n libexiv2 -f exiv2.lang
%_libdir/lib%name.so.*

%files -n libexiv2-devel
%_libdir/lib%name.so
%_includedir/%name/
%_pkgconfigdir/%name.pc


%changelog
* Tue Aug 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt2
- applied set of fc/upstream patches (fixed CVE-2017-11683,
  CVE-2017-14859, CVE-2017-14860, CVE-2017-14862,
  CVE-2017-14864, CVE-2017-17669, CVE-2017-17723,
  CVE-2017-17725, CVE-2018-10958, CVE-2018-10998,
  CVE-2018-11531, CVE-2018-12264, CVE-2018-12265,
  CVE-2018-14046, CVE-2018-5772, CVE-2018-8976,
  CVE-2018-8977)

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- 0.26

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- 0.25
- explicitly enabled video files and WebReady support

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.24-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Dec 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

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

