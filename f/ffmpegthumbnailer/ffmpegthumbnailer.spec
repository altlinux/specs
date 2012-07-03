Name: ffmpegthumbnailer
Summary: Lightweight video thumbnailer that can be used by file managers
Version: 2.0.4
Release: alt1.4
License: GPLv2
Group: Graphics
Url: http://code.google.com/p/ffmpegthumbnailer/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: http://ffmpegthumbnailer.googlecode.com/files/%name-%version.tar.gz
Patch: %name-ffmpeg-0.7.1.patch
Patch1: %name-2.0.4-alt-gcc4.6.patch

BuildRequires: gcc-c++ libavformat-devel libjpeg-devel libpng-devel libswscale-devel

%description
Lightweight video thumbnailer that can be used by file managers.

This video thumbnailer can be used to create thumbnails for your
video files. The thumbnailer uses ffmpeg to decode frames from the
video files, so supported videoformats depend on the configuration
flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as
possible. The only dependencies are ffmpeg, libpng and libjpeg.

The project also includes a C/C++ library that can be used by
developers to generate thumbnails in their projects.

%package -n lib%name
Summary: Shared libraries for ffmpegthumbnailer
Group: System/Libraries
Obsoletes: lib%{name}3 < %version

%description -n lib%name
This package includes a shared libraries for ffmpegthumbnailer

%package -n lib%name-devel
Summary: Include Files and Libraries mandatory for Development
Group: Development/C++
Requires: libffmpegthumbnailer = %version-%release
Requires: libavutil-devel libavformat-devel libavcodec-devel libswscale-devel

%description -n lib%name-devel
This package includes C/C++ libraries that can be used by
developers to generate thumbnails in their projects

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog README
%_bindir/%name
%_man1dir/*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/lib%name
%_pkgconfigdir/*.pc

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.4
- Fixed build

* Mon Mar 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt1.3
- do not ignore rpm optflags

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.2
- Removed bad RPATH

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.1
- Rebuilt with ffmpeg 0.7.1

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt2
- Fixed build

* Wed Sep 09 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.4-alt1
- Version update and build for Sisyphus

* Mon Jun 01 2009 Motsyo Gennadi <drool@altlinux.ru> 1.5.2-alt1
- initial build for ALT Linux from OpenSuSE package
