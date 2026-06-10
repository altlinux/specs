%define _libexecdir %_prefix/libexec
%define sover 6

%def_disable clang
# >= Qt 6.10.3
%def_without docs

Name: dtkmultimedia
Version: 6.0.4
Release: alt3

Summary: Deepin tool kit multimedia modules

License: Apache-2.0 and BSL-1.0 and GPL-2.0-or-later and LGPL-3.0-or-later
# src/ocr/ppocr/postprocess_op.cpp: Apache-2.0
# src/ocr/ppocr/postprocess_op.h: Apache-2.0
# src/ocr/ppocr/utility.cpp: Apache-2.0
# src/ocr/ppocr/utility.h: Apache-2.0
# src/ocr/ppocr/clipper.cpp: BSL-1.0
# src/ocr/ppocr/clipper.hpp: BSL-1.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkmultimedia
Vcs: https://github.com/linuxdeepin/dtkmultimedia

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
%if_enabled clang
BuildRequires(pre): rpm-macros-llvm-common
%endif
BuildRequires: cmake dqt6-base-devel dqt6-multimedia-devel dqt6-tools-devel dtk6-common-devel libdtk6core-devel libdtk6widget-devel libcups-devel glib2-devel libncnn-devel libopencv-devel libudev-devel libavcodec-devel libavformat-devel libswresample-devel libswscale-devel libffmpegthumbnailer-devel libavdevice-devel libusb-devel libportaudio2-devel libv4l-devel libmpv-devel gstreamer1.0-devel gst-plugins1.0-devel libXtst-devel
BuildRequires: libdqt6-openglwidgets libdqt6-concurrent
%if_with docs
BuildRequires: dqt6-base-doc doxygen
%endif
%if_enabled clang
BuildRequires: clang-devel lld-devel libomp%_llvm_version-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif

%description
Deepin tool kit multimedia modules.

%package -n libdtk6multimedia%sover
Summary: Libraries for %name
Group: System/Libraries
Requires: libdqt6-gui = %_dqt6_version

%description -n libdtk6multimedia%sover
Deepin tool kit core modules.
Libraries for %name.

%package -n libdtk6multimedia-devel
Summary: Development package for libdtk6multimedia
Group: Development/KDE and QT

%description -n libdtk6multimedia-devel
Header files and libraries for libdtk6multimedia.

%package -n libdtk6multimediawidgets%sover
Summary: Libraries for %name
Group: System/Libraries
Requires: libdqt6-gui = %_dqt6_version

%description -n libdtk6multimediawidgets%sover
Deepin tool kit core modules.
Libraries for %name.

%package -n libdtk6multimediawidgets-devel
Summary: Development package for libdtk6multimediawidgets
Group: Development/KDE and QT

%description -n libdtk6multimediawidgets-devel
Header files and libraries for libdtk6multimediawidgets.

%package -n libdtk6ocr%sover
Summary: Libraries for %name
Group: System/Libraries

%description -n libdtk6ocr%sover
Deepin tool kit core modules.
Libraries for %name.

%package -n libdtk6ocr-devel
Summary: Development package for libdtk6ocr
Group: Development/KDE and QT

%description -n libdtk6ocr-devel
Header files and libraries for libdtk6ocr.

%package -n libdtk6ocr-data
Summary: Data files for libdtk6ocr
Group: Graphics
BuildArch: noarch

%description -n libdtk6ocr-data
Data files for libdtk6ocr.

%if_with docs
%package -n libdtk6multimedia-doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch

%description -n libdtk6multimedia-doc
This package provides %name documantation.
%endif

%prep
%setup
%patch0 -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CPLUS_INCLUDE_PATH=%_includedir/opencv4:$CPLUS_INCLUDE_PATH
%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDTK_VERSION=%version \
  -DLIBRARY_INSTALL_DIR=%_lib \
%if_without docs
  -DBUILD_DOCS=OFF \
%endif
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules \
#

%install
%DQ6install

%files -n libdtk6multimedia%sover
%doc README.md LICENSES/*
%_libdir/libdtk6multimedia.so.%sover
%_libdir/libdtk6multimedia.so.%version

%files -n libdtk6multimedia-devel
%_libdir/libdtk6multimedia.so
%_includedir/dtk6multimedia/
%_libdir/cmake/dtk6multimedia/
%_libdir/pkgconfig/dtk6multimedia.pc
%_dqt6_mkspecsdir/modules/qt_lib_dtk6multimedia.pri

%files -n libdtk6multimediawidgets%sover
%doc README.md LICENSES/*
%_libdir/libdtk6multimediawidgets.so.%sover
%_libdir/libdtk6multimediawidgets.so.%version

%files -n libdtk6multimediawidgets-devel
%_libdir/libdtk6multimediawidgets.so
%_includedir/dtk6multimediawidgets/

%files -n libdtk6ocr%sover
%doc README.md LICENSES/*
%_libdir/libdtk6ocr.so.%sover
%_libdir/libdtk6ocr.so.%version

%files -n libdtk6ocr-data
%dir %_datadir/libdtk6ocr/
%_datadir/libdtk6ocr/dtkocrmodels/

%files -n libdtk6ocr-devel
%_libdir/libdtk6ocr.so
%_includedir/dtk6ocr/
%_libdir/cmake/dtk6ocr/
%_libdir/pkgconfig/dtk6ocr.pc
%_dqt6_mkspecsdir/modules/qt_lib_dtk6ocr.pri

%if_with docs
%files -n libdtk6multimedia-doc
%_datadir/doc/dqt6/dtk6multimedia.qch
%endif

%changelog
* Wed Jun 10 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt3
- Fixed build with Qt 6.10.3.

* Mon Dec 29 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt2
- Fixed build with ffmpeg 8.0.1.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt1
- New version 6.0.4.

* Tue Sep 16 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.2-alt2
- Fixed build with ncnn 20250916.

* Tue Jun 17 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.2-alt1
- New version 6.0.2.

* Tue Apr 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt2
- Moved mkspecs module to devel subpackage.

* Tue Apr 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt1
- Initial build for ALT Sisyphus.
