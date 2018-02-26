Name: libtlalli
Version: 0.2.1
Release: alt3

Summary: Library for manipulating panoramic images
License: GPLv2+
Group: System/Libraries

URL: http://turingmachine.org/tlalli
Source: %url/distribution/libtlalli-%version.tar.gz

# Automatically added by buildreq on Mon Dec 29 2008
BuildRequires: flex libgsl-devel libjpeg-devel libpng-devel libtiff-devel

%description
libtlalli is a collection of utilities to stitch panoramas based upon the
Panorama Tools by Helmut Dersch.

Tlalli is not intended to be a replacement of panotools, it only replaces some
of its utilities (for instance, tlalli does not include a PToptimizer).

%package tools
Summary: Tools that use the %name library
Group: Graphics
Requires: %name = %version-%release

%description tools
TOptimizer, a command-line interface for control-point optimisation. panoinfo, a
tool for querying the library capabilities. Tmender, a replacement for
PTStitcher. Tblender, colour/brightness correction of overlapping photos.
Ttiff2psd, convert tiff files to a multilayer psd file. Tuncrop, convert
cropped/offset TIFF to flat TIFF.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the header files necessary for developing
programs which will manipulate panoramas using the %name library.

%prep
%setup

%build
%configure --disable-static
# fix rpath libtool issues
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std

%files
%_libdir/libtlalli.so.*

%files tools
%doc doc/*.txt
%_bindir/*

%files devel
%_includedir/tlalli
%_libdir/libtlalli.so

%changelog
* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 0.2.1-alt3
- Fix RPATH issue.

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt2
- Remove obsolete ldconfig calls.

* Mon Jul 16 2007 Victor Forsyuk <force@altlinux.org> 0.2.1-alt1
- Initial build.
