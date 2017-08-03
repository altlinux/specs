Name: dirac
Version: 1.0.2
Release: alt2

Summary: Video Codec based on Wavelets
License: MPL/GPL/LGPL
Group: Video

Url: http://diracvideo.org
Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
Patch0: http://pkgs.fedoraproject.org/cgit/rpms/dirac.git/plain/dirac-1.0.2-backports.patch
Patch1: http://pkgs.fedoraproject.org/cgit/rpms/dirac.git/plain/0001-Fix-uninitialised-memory-read-that-causes-the-encode.patch
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: doxygen gcc-c++ graphviz libstdc++-devel tetex-core tetex-latex
BuildRequires: chrpath

%description
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n lib%name
Group: System/Libraries
Summary: Shared library of the Dirac Video codec

%description -n lib%name
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files of the Dirac Video codec
Requires: lib%name = %version-%release

%description -n lib%name-devel
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package utils
Group: Video
Summary: Example encoder and decoder for the Dirac video codec

%description utils
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%prep
%setup
%patch0 -p0
%patch1 -p1
find doc unit_tests util libdirac_encoder libdirac_byteio \
	-type f -name \* -exec chmod 644 {} \;
sed -i 's/-Werror//g' configure*

%build
#autoreconf
%configure \
	--disable-static \
%ifarch x86_64
	--enable-mmx=yes \
%endif
	#

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

%make_build

%install
%makeinstall_std

# FIXME: should not be there in the first place
chrpath -d %buildroot%_bindir/dirac*

%files utils
%doc README TODO AUTHORS
%_bindir/dirac*
%_bindir/BMPtoRGB
%_bindir/RGB*
%_bindir/UYVYtoRGB
%_bindir/YUV*
%_bindir/create_dirac_testfile.pl

%files -n lib%name
%_libdir/libdirac*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/libdirac*.so
%_datadir/doc/%name/
%_libdir/pkgconfig/dirac.pc

%changelog
* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.0.2-alt2
- applied fedora patches
- enable MMX on x86_64
- spec cleanup
- drop rpath

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0.2-alt1.1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.1
- Removed bad RPATH

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.10.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdirac
  * postun_ldconfig for libdirac
  * postclean-05-filetriggers for spec file

* Thu Jul 03 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.10.0-alt1
- 0.10.0 release.

* Fri Oct 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.0-alt1
- 0.8.0 release.

* Thu May 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7.0-alt1
- 0.7.0 release.

* Sat Feb 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.6.0-alt1
- 0.6.0 release.

* Wed Dec 21 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.5.4-alt1
- 0.5.4 release.
- initial build for ALTLinux.
- specfile is based on mandriva's.
