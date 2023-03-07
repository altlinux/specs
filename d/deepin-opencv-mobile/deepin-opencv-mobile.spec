%define llvm_ver 15
%define opencv_world_ver 4

%def_disable clang

Name: deepin-opencv-mobile
Version: 0
Release: alt1.git7ca8299

Summary: Deepin fork of opencv-mobile

License: Apache-2.0
Group: Engineering
Url: https://github.com/linuxdeepin/opencv-mobile

Source: %url/archive/%version/%name-%version.tar.gz

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): libopencv-devel
%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake

%description
%summary.

%package -n deepin-libopencv_world%{opencv_world_ver}
Summary: Library for opencv-mobile
Group: System/Libraries

%description -n deepin-libopencv_world%{opencv_world_ver}
The package provides development files for opencv-mobile.

%package -n deepin-libopencv_world-devel
Summary: Development package for %name
Group: Development/C++
Requires: libopencv-devel

%%description -n deepin-libopencv_world-devel
The package provides development files for %name.

%prep
%setup
#sed -i 's|"opencv2/core.hpp"|<%%_includedir/opencv4/opencv2/core.hpp>|' \
#  opencv-4.5.4/modules/world/include/opencv2/world.hpp

%build
#%%ifarch ppc64le
#%%add_optflags -mcpu=power9 -mvsx
#%%endif
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
export LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_lib/deepin \
  -DCMAKE_INSTALL_INCLUDEDIR=include/deepin \
  -DBUILD_ZLIB=OFF \
  -DBUILD_TIFF=OFF \
  -DBUILD_OPENJPEG=OFF \
  -DBUILD_JASPER=OFF \
  -DBUILD_JPEG=OFF \
  -DBUILD_PNG=OFF \
  -DBUILD_OPENEXR=OFF \
  -DBUILD_WEBP=OFF \
  -DBUILD_TBB=OFF \
  -DBUILD_IPP_IW=OFF \
  -DBUILD_ITT=OFF \
  -DWITH_AVFOUNDATION=OFF \
  -DWITH_CAP_IOS=OFF \
  -DWITH_CAROTENE=OFF \
  -DWITH_CPUFEATURES=OFF \
  -DWITH_EIGEN=OFF \
  -DWITH_FFMPEG=OFF \
  -DWITH_GSTREAMER=OFF \
  -DWITH_GTK=OFF \
  -DWITH_IPP=OFF \
  -DWITH_HALIDE=OFF \
  -DWITH_VULKAN=OFF \
  -DWITH_INF_ENGINE=OFF \
  -DWITH_NGRAPH=OFF \
  -DWITH_JASPER=OFF \
  -DWITH_OPENJPEG=OFF \
  -DWITH_JPEG=OFF \
  -DWITH_WEBP=OFF \
  -DWITH_OPENEXR=OFF \
  -DWITH_PNG=OFF \
  -DWITH_TIFF=OFF \
  -DWITH_OPENVX=OFF \
  -DWITH_GDCM=OFF \
  -DWITH_TBB=OFF \
  -DWITH_HPX=OFF \
  -DWITH_OPENMP=ON \
  -DWITH_PTHREADS_PF=OFF \
  -DWITH_V4L=OFF \
  -DWITH_CLP=OFF \
  -DWITH_OPENCL=OFF \
  -DWITH_OPENCL_SVM=OFF \
  -DWITH_ITT=OFF \
  -DWITH_PROTOBUF=OFF \
  -DWITH_IMGCODEC_HDR=OFF \
  -DWITH_IMGCODEC_SUNRASTER=OFF \
  -DWITH_IMGCODEC_PXM=OFF \
  -DWITH_IMGCODEC_PFM=OFF \
  -DWITH_QUIRC=OFF \
  -DWITH_ANDROID_MEDIANDK=OFF \
  -DWITH_TENGINE=OFF \
  -DWITH_ONNX=OFF \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_opencv_apps=OFF \
  -DBUILD_ANDROID_PROJECTS=OFF \
  -DBUILD_ANDROID_EXAMPLES=OFF \
  -DBUILD_DOCS=OFF \
  -DBUILD_EXAMPLES=OFF \
  -DBUILD_PACKAGE=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DBUILD_TESTS=OFF \
  -DBUILD_WITH_STATIC_CRT=OFF \
  -DBUILD_FAT_JAVA_LIB=OFF \
  -DBUILD_ANDROID_SERVICE=OFF \
  -DBUILD_JAVA=OFF \
  -DBUILD_OBJC=OFF \
  -DENABLE_PRECOMPILED_HEADERS=OFF \
  -DENABLE_FAST_MATH=OFF \
  -DCV_TRACE=OFF \
  -DBUILD_opencv_java=OFF \
  -DBUILD_opencv_gapi=OFF \
  -DBUILD_opencv_objc=OFF \
  -DBUILD_opencv_js=OFF \
  -DBUILD_opencv_ts=OFF \
  -DBUILD_opencv_python2=OFF \
  -DBUILD_opencv_python3=OFF \
  -DBUILD_opencv_dnn=OFF \
  -DBUILD_opencv_imgcodecs=OFF \
  -DBUILD_opencv_videoio=OFF \
  -DBUILD_opencv_calib3d=OFF \
  -DBUILD_opencv_flann=OFF \
  -DBUILD_opencv_objdetect=OFF \
  -DBUILD_opencv_stitching=OFF \
  -DBUILD_opencv_ml=OFF \
  -DBUILD_opencv_world=ON \
%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

# remove dublicated opencv files
#rm -rf %%buildroot%%_includedir/deepin/opencv4/
rm -rf %buildroot%_includedir/deepin/opencv4/opencv2/{core*,cvconfig.h,features2d*,highgui*,imgproc*,photo*,video*,opencv*}
rm -rf %buildroot%_datadir/opencv4/
rm -rf %buildroot%_libdir/deepin/cmake/opencv4/
rm -rf %buildroot%_bindir/*

# package docs for special builtin version of opencv
mkdir -p %buildroot%_docdir/deepin-opencv-4.5.4/
cp -a opencv-4.5.4/{COPYRIGHT,LICENSE,README.md,SECURITY.md} %buildroot%_docdir/deepin-opencv-4.5.4/
mv -f %buildroot%_datadir/licenses/opencv4/SoftFloat-COPYING.txt %buildroot%_docdir/deepin-opencv-4.5.4/

%files -n deepin-libopencv_world%{opencv_world_ver}
%doc LICENSE README.md
%doc %_docdir/deepin-opencv-4.5.4
%dir %_libdir/deepin/
%_libdir/deepin/libopencv_world.so.%{opencv_world_ver}*

%files -n deepin-libopencv_world-devel
%dir %_libdir/deepin/
%_libdir/deepin/libopencv_world.so
%dir %_includedir/deepin/
%dir %_includedir/deepin/opencv4/
%dir %_includedir/deepin/opencv4/opencv2/
%_includedir/deepin/opencv4/opencv2/world.hpp

%changelog
* Tue Mar 07 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git7ca8299
- Initial build for ALT Sisyphus (for deepin-ocr-plugin).
