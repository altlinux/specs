%ifarch x86_64
%define targt linux-x86-64
%else
%define targt linux-x86-32
%endif
Name: avbin
Version: 8
Release: alt1.svn20090206.5
Summary: Thin wrapper around FFmpeg

Group: Video
License: GPL/LGPL
URL: http://code.google.com/p/avbin/
# http://avbin.googlecode.com/svn/trunk
Source: %name-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: libavcodec-devel libavformat-devel libavutil-devel libswscale-devel doxygen

%description
AVbin is a thin wrapper around FFmpeg, providing binary compatibility
for applications and languages that need it.

AVbin allows programs that require dynamic linkage to use FFmpeg. It
does this by providing

  * an accurate version number within the shared library, allowing
    applications to select the appropriate data structures and functions
    to use at runtime, and
  * a simplified interface with an unchanging ABI to the most common
    decoding functionality within FFmpeg.

%package -n lib%name
Summary: Shared library of AVbin, thin wrapper around FFmpeg
Group: System/Libraries

%description -n lib%name
AVbin is a thin wrapper around FFmpeg, providing binary compatibility
for applications and languages that need it.

AVbin allows programs that require dynamic linkage to use FFmpeg. It
does this by providing

  * an accurate version number within the shared library, allowing
    applications to select the appropriate data structures and functions
    to use at runtime, and
  * a simplified interface with an unchanging ABI to the most common
    decoding functionality within FFmpeg.

%package -n lib%name-devel
Summary: Development files of AVbin, thin wrapper around FFmpeg
Group: Development/C
Requires: lib%name = %version-%release
Requires: libavcodec-devel libavformat-devel libavutil-devel libswscale-devel

%description -n lib%name-devel
AVbin is a thin wrapper around FFmpeg, providing binary compatibility
for applications and languages that need it.

This package contains development files of AVbin.

%package -n lib%name-devel-doc
Summary: Development documentation for AVbin, thin wrapper around FFmpeg
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
AVbin is a thin wrapper around FFmpeg, providing binary compatibility
for applications and languages that need it.

This package contains development documentation for AVbin.

%package example
Summary: Example for AVbin, thin wrapper around FFmpeg
Group: Development/Documentation
Requires: lib%name

%description example
AVbin is a thin wrapper around FFmpeg, providing binary compatibility
for applications and languages that need it.

This package contains example for AVbin.

%prep
%setup

%build
./build.sh %targt
ln -s lib%name.so.%version dist/%targt/lib%name.so

pushd example
%make this LIBDIR=$PWD/../dist/%targt
popd

doxygen
rm -f doc/man/man3/deprecated.3

%install
install -d %buildroot%_libdir
cp -P dist/%targt/lib%name.so* %buildroot%_libdir/
chmod -x %buildroot%_libdir/*

install -d %buildroot%_includedir
install -p -m644 include/* %buildroot%_includedir

install -d %buildroot%_docdir/lib%name-devel
install -d %buildroot%_man3dir
install -m644 doc/html/* %buildroot%_docdir/lib%name-devel
install -m644 doc/man/man3/* %buildroot%_man3dir

install -d %buildroot%_bindir
install -m755 example/avbin_dump %buildroot%_bindir

%files -n lib%name
%doc COPYING* CHANGELOG
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel
%_man3dir/*

%files example
%doc example/*.c
%_bindir/*

%changelog
* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 8-alt1.svn20090206.5
- artificial deps on ffmpeg removed

* Sat Aug 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8-alt1.svn20090206.4
- Fixed calls of avcodec_decode_audio* and avcodec_decode_video*
  (thnx sbolshakov@)

* Sat Aug 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8-alt1.svn20090206.3
- Rebuilt with updated ffmpeg (thnx sbolshakov@)

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8-alt1.svn20090206.2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8-alt1.svn20090206.1
- Rebuilt for soname set-versions

* Fri Oct 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8-alt1.svn20090206
- Initial build for Sisyphus

