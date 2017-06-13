Name: ffmpegthumbnailer
Summary: Lightweight video thumbnailer that can be used by file managers
Version: 2.2.0
Release: alt1

License: GPLv2
Group: Graphics
Url: http://code.google.com/p/ffmpegthumbnailer/

Source0: http://ffmpegthumbnailer.googlecode.com/files/%name-%version.tar.gz

BuildRequires: gcc-c++ libavformat-devel libjpeg-devel libpng-devel libswscale-devel cmake libswresample-devel libavfilter-devel libavresample-devel libpostproc-devel

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
Requires: libavutil-devel libavformat-devel libavcodec-devel libswscale-devel cmake

%description -n lib%name-devel
This package includes C/C++ libraries that can be used by
developers to generate thumbnails in their projects

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_GIO=ON -DENABLE_THUMBNAILER=ON
%cmake_build

%install
%make -C BUILD install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog README
%_bindir/%name
%_datadir/thumbnailers
%_man1dir/*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/lib%name
%_pkgconfigdir/*.pc

%changelog
* Tue Jun 13 2017 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.8-alt4.1
- rebuild with gcc5

* Fri Jan 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt4
- rebuilt with libav11

* Mon May 12 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt3
- rebuilt with libav10

* Sat Sep 21 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt2
- rebuilt with libav9

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.8-alt1
- new version

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.5
- Rebuilt with libpng15

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
