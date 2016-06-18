#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: libyami
Summary: Yet Another Media Infrastructure
Version: 0.4.0
Release: alt1
License: Apache License 2.0
Group: System/Libraries
BuildRequires: libv4l-devel libGLES-devel
BuildRequires: gcc-c++ glibc-devel-static libEGL-devel libdrm-devel libva-devel
Url: https://github.com/01org/libyami/releases
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Patch1: %name-%version.patch

%package devel
Summary: %summary
Group: Development/C

%description devel
%summary


%description
Yet Another Media Infrastructure. it is core part of media codec with hardware acceleration, it is yummy to your video experience on Linux like platform.


%prep
%setup
%patch1 -p1
%autoreconf

%build
%configure \
  --enable-dmabuf \
  --enable-v4l2   \
  --enable-capi   \
  --enable-v4l2-ops \
  --enable-mpeg2dec \
  --enable-vp8dec   \
  --enable-vp9dec   \
  --enable-jpegdec  \
  --enable-h264dec  \
  --enable-h265dec  \
  --enable-vc1dec   \
  --enable-h264enc  \
  --enable-jpegenc  \
  --enable-vp8enc   \
  --enable-h265enc
%make

%install
%make_install DESTDIR=%buildroot INSTALL_PREFIX=%buildroot install

%files
%_libdir/libyami.so.*
%_libdir/libyami_v4l2.so.*

%files devel
%_libdir/libyami.so
%_libdir/libyami_v4l2.so
%_includedir/%name
%_pkgconfigdir/*.pc

%changelog
* Sat Jun 18 2016 Denis Smirnov <mithraen@altlinux.ru> 0.4.0-alt1
- first build for Sisyphus

