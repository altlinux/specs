Name: libvdpau-va-gl
Version: 0.4.2
Release: alt1
Summary: VDPAU driver with OpenGL/VAAPI back-end
License: MIT
URL: https://github.com/i-rinat/libvdpau-va-gl
Group: System/Libraries

Source0: %name-%version.tar

BuildRequires: cmake gcc-c++ libva-devel python3

%description
%summary

%prep
%setup -q

%build
%define lib_suffix %nil
%if "%_lib" == "lib64"
%define lib_suffix 64
%endif
mkdir -p %_target_platform
pushd %_target_platform
cmake .. \
        -DCMAKE_INSTALL_PREFIX=%prefix \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_CXX_FLAGS_RELEASE='%optflags' \
        -DLIB_SUFFIX=%lib_suffix
popd
%make_build -C %_target_platform

%install
%make -C %_target_platform DESTDIR=%buildroot install

%files
%doc README.md LICENSE
%_libdir/vdpau/libvdpau_va_gl.so*

%changelog
* Tue Mar 17 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- initial release

