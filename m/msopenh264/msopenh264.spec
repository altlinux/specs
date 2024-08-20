Name:    msopenh264
Version: 5.2.0
Release: alt1.git041b07a

Summary: MsOpenH264 is an H.264 encoder/decoder plugin for mediastreamer2 based on the openh264 library
License: GPL-2.0
Group: System/Libraries
URL: https://gitlab.linphone.org/BC/public/msopenh264

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libortp-devel
BuildRequires: libbctoolbox-devel
BuildRequires: libmediastreamer2-devel
BuildRequires: libopenh264-devel
# Mediastreamer2_PLUGINS_DIR
BuildRequires: mediastreamer2

%description
MsOpenH264 is an H.264 encoder/decoder plugin for mediastreamer2 based on the
openh264 library.

%prep
%setup

%build
export CMAKE_PREFIX_PATH=%_datadir/bctoolbox/cmake:$CMAKE_PREFIX_PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -Wno-dev \
  -DBUILD_SHARED_LIBS=TRUE
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc COPYING README.md
%dir %_libdir/mediastreamer/
%dir %_libdir/mediastreamer/plugins/
%_libdir/mediastreamer/plugins/libmsopenh264.so

%changelog
* Mon Aug 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.2.0-alt1.git041b07a
- Initial build for Sisyphus.
