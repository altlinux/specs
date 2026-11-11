%define _unpackaged_files_terminate_build 1

Name:    lovr
Version: 0.19.1
Release: alt1

Summary: Lua Virtual Reality Framework
License: MIT
Group:   Video
URL:     https://github.com/bjornbytes/lovr

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Patch: lovr-0.19.0-link-libm.patch
Patch1: lovr-0.19.0-phonon-thirdparty.patch
Patch2: lovr-0.19.1-joltc-jolt-5.6.patch
Patch3: lovr-0.19.1-system-jolt-cmake.patch
Patch4: lovr-0.19.1-system-glslang.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libX11-devel libXrandr-devel libXinerama-devel libXcursor-devel
BuildRequires: libglfw3-devel libluajit-devel glslang-devel zlib-devel libcurl-devel
BuildRequires: vulkan-headers libXau-devel libxcb-devel libvulkan-devel libXdmcp-devel
BuildRequires: openxr-devel libJolt-devel

ExclusiveArch: x86_64 aarch64

%description
A simple Lua framework for rapidly building VR experiences.

You can use LOVR to easily create VR experiences without much setup or programming
experience. The framework is tiny, fast, open source, and supports lots of
different platforms and devices.

%prep
%setup -a1
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%cmake -B build \
    -DLOVR_SYSTEM_LUA=On \
    -DLOVR_SYSTEM_GLFW=On \
    -DLOVR_SYSTEM_OPENXR=On \
    -DLOVR_USE_GLSLANG=On \
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
sed -i 's|^Exec=.*|Exec=lovr %%F|' %buildroot%_desktopdir/lovr.desktop
sed -i 's|^Icon=.*|Icon=lovr|' %buildroot%_desktopdir/lovr.desktop
printf 'MimeType=text/x-lua;application/zip;\n' >> %buildroot%_desktopdir/lovr.desktop
install -Dm644 etc/lovr.png %buildroot%_iconsdir/hicolor/256x256/apps/lovr.png
install -d %buildroot%_libdir/lovr/plugins
install -m644 build/plugins/lua-enet/enet.so %buildroot%_libdir/lovr/plugins/enet.so
install -m644 build/plugins/lovr-http/http.so %buildroot%_libdir/lovr/plugins/http.so

%files
%doc LICENSE README.md CHANGES.md
%_bindir/lovr
%_desktopdir/lovr.desktop
%_iconsdir/hicolor/256x256/apps/lovr.png
%_libdir/libjoltc.so
%_libdir/libmsdfgen.so
%_libdir/libphonon.so
%dir %_libdir/lovr
%dir %_libdir/lovr/plugins
%_libdir/lovr/plugins/enet.so
%_libdir/lovr/plugins/http.so

%changelog
* Wed Nov 11 2026 Sergey Palcheh <minergenon@altlinux.org> 0.19.1-alt1
- new version 0.19.1
- use system JoltPhysics 5.6 (libJolt-devel) instead of bundled Jolt 5.3.0;
  port joltc to Jolt 5.6 API (CharacterContact, CollisionEstimationResult)
- use system glslang (glslang-devel) for runtime GLSL shader compilation
- use system OpenXR loader (openxr-devel) instead of the bundled submodule

* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 0.19.0-alt2
- fixed debuginfo unmet dependency: removed post-build strip from bundled phonon

* Sun Jun 14 2026 Sergey Palcheh <minergenon@altlinux.org> 0.19.0-alt1
- Initial build for Sisyphus

