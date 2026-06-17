%define _unpackaged_files_terminate_build 1
%define jolt_version 5.3.0

Name:    lovr
Version: 0.19.0
Release: alt2

Summary: Lua Virtual Reality Framework
License: MIT
Group:   Video
URL:     https://github.com/bjornbytes/lovr

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Source2: JoltPhysics-%jolt_version.tar.gz
Patch: lovr-0.19.0-link-libm.patch
Patch1: lovr-0.19.0-phonon-thirdparty.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libX11-devel libXrandr-devel libXinerama-devel libXcursor-devel
BuildRequires: libglfw3-devel libluajit-devel glslang-devel zlib-devel libcurl-devel
BuildRequires: vulkan-headers libXau-devel libxcb-devel libvulkan-devel libXdmcp-devel

ExclusiveArch: x86_64

%description
A simple Lua framework for rapidly building VR experiences.

You can use LOVR to easily create VR experiences without much setup or programming
experience. The framework is tiny, fast, open source, and supports lots of
different platforms and devices.

%prep
%setup -a1
tar -xzf %SOURCE2
%patch -p1
%patch1 -p1

%build
%cmake -B build  \
    -DLOVR_SYSTEM_LUA=On \
    -DLOVR_SYSTEM_GLFW=On \
    -DLOVR_SYSTEM_OPENXR=Off \
    -DDYNAMIC_LOADER=OFF \
    -DLOVR_USE_GLSLANG=Off \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DCMAKE_BUILD_TYPE=Release \
    -Wno-dev

%make -C build

%install
install -Dm755 build/bin/lovr %buildroot%_bindir/lovr
install -Dm644 build/bin/libphonon.so %buildroot%_libdir/libphonon.so
install -Dm644 build/bin/libjoltc.so %buildroot%_libdir/libjoltc.so
install -Dm644 build/bin/libmsdfgen.so %buildroot%_libdir/libmsdfgen.so
install -Dm644 etc/lovr.desktop %buildroot%_desktopdir/lovr.desktop
sed -i 's|^Exec=.*|Exec=lovr %F|' %buildroot%_desktopdir/lovr.desktop
sed -i 's|^Icon=.*|Icon=lovr|' %buildroot%_desktopdir/lovr.desktop
printf 'MimeType=text/x-lua;application/zip;\n' >> %buildroot%_desktopdir/lovr.desktop
install -Dm644 etc/logo.svg %buildroot%_iconsdir/hicolor/scalable/apps/lovr.svg
install -d %buildroot%_libdir/lovr/plugins
install -m644 build/bin/enet.so %buildroot%_libdir/lovr/plugins/enet.so
install -m644 build/bin/http.so %buildroot%_libdir/lovr/plugins/http.so

%files
%doc LICENSE README.md CHANGES.md
%_bindir/lovr
%_desktopdir/lovr.desktop
%_iconsdir/hicolor/scalable/apps/lovr.svg
%_libdir/libjoltc.so
%_libdir/libmsdfgen.so
%_libdir/libphonon.so
%dir %_libdir/lovr
%dir %_libdir/lovr/plugins
%_libdir/lovr/plugins/enet.so
%_libdir/lovr/plugins/http.so

%changelog
* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 0.19.0-alt2
- fixed debuginfo unmet dependency: removed post-build strip from bundled phonon

* Sun Jun 14 2026 Sergey Palcheh <minergenon@altlinux.org> 0.19.0-alt1
- Initial build for Sisyphus

