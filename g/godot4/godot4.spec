%define _unpackaged_files_terminate_build 1
%def_with standard
%def_without mono
%def_without mono_assemblies
# see architecture_aliases in platform_methods.py
%define arch_alias %_arch
%ifarch aarch64
%define arch_alias arm64
%endif

Name: godot4
Version: 4.5.1
Release: alt1

Summary: Libre game engine
License: MIT
Group: Development/Tools
Url: https://godotengine.org
VCS: https://github.com/godotengine/godot.git
ExclusiveArch: aarch64 x86_64 %e2k

Source: godot-%version.tar
Patch0: godot4-4.3-alpine-fix-glslang.patch
Patch2: godot4-4.3-alt-dynamic-link-xatlas.patch
Patch4: godot4-4.5-alt-unbundle-clipper2.patch

Provides: godot = %version
Requires: libEGL
Requires: libpulseaudio
Requires: libxkbcommon

BuildRequires: embree-devel
BuildRequires: gcc-c++
BuildRequires: glslang-devel
BuildRequires: libClipper2-devel
BuildRequires: libSDL3-devel
BuildRequires: libalsa-devel
BuildRequires: libbrotli-devel
BuildRequires: libbullet3-devel
BuildRequires: libenet-devel
BuildRequires: libfreetype-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libgraphite2-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libicu-devel
BuildRequires: libjpeg-devel
BuildRequires: libmbedtls-3.6-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libogg-devel
BuildRequires: libpcre2-devel
BuildRequires: libpng-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsquish-devel
BuildRequires: libstdc++-devel
BuildRequires: libtheora-devel
BuildRequires: libudev-devel
BuildRequires: libvorbis-devel
BuildRequires: libwebp-devel
BuildRequires: libxatlas-devel
BuildRequires: libzstd-devel
BuildRequires: openxr-devel
BuildRequires: scons
BuildRequires: wayland-devel
BuildRequires: zlib-devel
%if_with mono
BuildRequires: dotnet-sdk-8.0
BuildRequires: /proc
%endif

%description
Godot Engine is a feature-packed, cross-platform game engine to create 2D and 3D
games from a unified interface. It provides a comprehensive set of common tools,
so that users can focus on making games without having to reinvent the wheel.

%if_with mono
%package mono
Summary: Libre game engine (Mono version)
Group: Development/Tools

Provides: godot-mono = %version

%description mono
%summary.
%endif

%package common
Summary: Common files for Godot game engine
Group: Development/Tools

%description common
%summary.

%package runner
Summary: Shared binary to play games developed with the Godot engine
Group: Games/Other

%description runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

%prep
%setup
%autopatch -p1

pushd thirdparty
rm -rf \
  brotli \
  clipper2 \
  enet \
  embree \
  freetype \
  glslang \
  graphite \
  harfbuzz \
  icu4c \
  libjpeg-turbo \
  libogg \
  libpng \
  libtheora \
  libvorbis \
  libvpx \
  libwebp \
  mbedtls \
  miniupnpc \
  openxr \
  pcre2 \
  sdl \
  squish \
  xatlas \
  zlib \
  zstd \
  #
popd

%build
export BUILD_NAME="%release"
%define disable_builtin() %{expand:builtin_%{1}=no}

%define disable_builtins \\\
  %{disable_builtin brotli} \\\
  %{disable_builtin certs} \\\
  %{disable_builtin clipper2} \\\
  %{disable_builtin embree} \\\
  %{disable_builtin enet} \\\
  %{disable_builtin freetype} \\\
  %{disable_builtin glslang} \\\
  %{disable_builtin graphite} \\\
  %{disable_builtin harfbuzz} \\\
  %{disable_builtin icu4c} \\\
  %{disable_builtin libjpeg_turbo} \\\
  %{disable_builtin libogg} \\\
  %{disable_builtin libpng} \\\
  %{disable_builtin libtheora} \\\
  %{disable_builtin libvorbis} \\\
  %{disable_builtin libwebp} \\\
  %{disable_builtin mbedtls} \\\
  %{disable_builtin miniupnpc} \\\
  %{disable_builtin openxr} \\\
  %{disable_builtin pcre2} \\\
  %{disable_builtin sdl} \\\
  %{disable_builtin squish} \\\
  %{disable_builtin xatlas} \\\
  %{disable_builtin zlib} \\\
  %{disable_builtin zstd} \\\
%nil

%define scons_options \\\
  arch=%_arch \\\
  %disable_builtins \\\
  disable_exceptions=false \\\
  engine_update_check=no \\\
  -j %__nprocs \\\
  platform=linuxbsd \\\
  production=yes \\\
  pulseaudio=yes \\\
  system_certs_path=%_datadir/ca-certificates/ca-bundle.crt \\\
  tools=yes \\\
  use_llvm=no \\\
  use_static_cpp=no \\\
  verbose=yes \\\
%nil

%if_with standard
scons \
  %scons_options \
  target=editor \
  #

scons \
  %scons_options \
  target=template_release \
  #
%endif

%if_with mono
# mono
scons \
  %scons_options \
  target=editor \
  module_mono_enabled=yes \
  #

%if_with mono_assemblies
# mono_assemblies
bin/godot.linuxbsd.editor.%arch_alias.mono \
  --generate-mono-glue modules/mono/glue \
  --headless \
  --verbose \
  #

modules/mono/build_scripts/build_assemblies.py \
  --godot-output-dir=./bin \
  --godot-platform=linuxbsd \
  --push-nupkgs-local ~/godotnupkg \
  #
# mono_assemblies
%endif
# mono
%endif

%install
%if_with standard
install -Dm 755 bin/godot.linuxbsd.editor.%arch_alias \
  -t %buildroot%_libdir/godot

install -d %buildroot%_bindir
install -m755 bin/godot.linuxbsd.editor.%arch_alias \
  %buildroot%_bindir/godot4
install -m755 bin/godot.linuxbsd.template_release.%arch_alias \
  %buildroot%_bindir/godot4-runner

install -Dm 644 misc/dist/linux/org.godotengine.Godot.desktop \
  %buildroot%_desktopdir/org.godotengine.Godot4.desktop
sed -i \
  -e '/Exec/ s/godot/godot4/' \
  -e '/Name/ s/Godot Engine/Godot 4 Engine/' \
  %buildroot%_desktopdir/org.godotengine.Godot4.desktop

install -Dm 644 misc/dist/linux/org.godotengine.Godot.appdata.xml \
  -t %buildroot%_datadir/metainfo

install -Dm 644 misc/dist/linux/godot.6 \
  -t %buildroot%_man6dir
%endif

%if_with mono
# mono
install -d %buildroot%_bindir
ln -s \
  ../..%_libdir/godot-mono/godot.linuxbsd.editor.%arch_alias.mono \
  %buildroot%_bindir/godot4-mono \
  #
  install -d %buildroot%_libdir/godot-mono
install -m 755 bin/godot.linuxbsd.editor.%arch_alias.mono \
  -t %buildroot%_libdir/godot-mono

install -Dm 644 misc/dist/linux/org.godotengine.Godot.desktop \
  %buildroot%_desktopdir/org.godotengine.Godot4-mono.desktop
sed -i \
  -e '/Exec/ s/godot/godot4-mono/' \
  -e '/Name/ s/Godot Engine/Godot 4 Engine Mono/' \
  %buildroot%_desktopdir/org.godotengine.Godot4-mono.desktop

install -Dm 644 misc/dist/linux/org.godotengine.Godot.appdata.xml \
  %buildroot%_datadir/metainfo/org.godotengine.Godot-mono.appdata.xml

install -Dm 644 misc/dist/linux/godot.6 \
  %buildroot%_man6dir/godot-mono.6
%if_with mono_assemblies
install -d %buildroot%_libdir/godot-mono
cp -r bin/GodotSharp -t %buildroot%_libdir/godot-mono
%endif
# mono
%endif

install -Dm 644 icon.png \
  %buildroot%_iconsdir/hicolor/256x256/apps/godot4.png
install -Dm 644 icon.svg \
  %buildroot%_iconsdir/hicolor/scalable/apps/godot4.svg

%if_with standard
%files
%_bindir/godot4
%_datadir/metainfo/org.godotengine.Godot.appdata.xml
%_desktopdir/org.godotengine.Godot4.desktop
%_libdir/godot/godot.linuxbsd.editor.%arch_alias
%_man6dir/godot.6.xz
%endif

%files common
%_iconsdir/hicolor/256x256/apps/godot4.png
%_iconsdir/hicolor/scalable/apps/godot4.svg

%if_with standard
%files runner
%_bindir/godot4-runner
%endif

%if_with mono
# mono
%files mono
%_bindir/godot4-mono
%_datadir/metainfo/org.godotengine.Godot-mono.appdata.xml
%_desktopdir/org.godotengine.Godot4-mono.desktop
%_libdir/godot-mono/godot.linuxbsd.editor.%arch_alias.mono
%_man6dir/godot-mono.6.xz
%if_with mono_assemblies
# mono_assemblies
%_libdir/godot-mono/GodotSharp/Api/Debug/GodotPlugins.*
%_libdir/godot-mono/GodotSharp/Api/Debug/GodotSharp.*
%_libdir/godot-mono/GodotSharp/Api/Debug/GodotSharpEditor.*
%_libdir/godot-mono/GodotSharp/Api/Release/GodotPlugins.*
%_libdir/godot-mono/GodotSharp/Api/Release/GodotSharp.*
%_libdir/godot-mono/GodotSharp/Api/Release/GodotSharpEditor.*
%_libdir/godot-mono/GodotSharp/Tools/GodotTools.*
%_libdir/godot-mono/GodotSharp/Tools/JetBrains.Lifetimes.dll
%_libdir/godot-mono/GodotSharp/Tools/JetBrains.RdFramework.dll
%_libdir/godot-mono/GodotSharp/Tools/JetBrains.Rider.PathLocator.dll
%_libdir/godot-mono/GodotSharp/Tools/Microsoft.Build.Locator.dll
%_libdir/godot-mono/GodotSharp/Tools/Newtonsoft.Json.dll
%_libdir/godot-mono/GodotSharp/Tools/NuGet.Frameworks.dll
%_libdir/godot-mono/GodotSharp/Tools/nupkgs/Godot.NET.Sdk.*.nupkg
%_libdir/godot-mono/GodotSharp/Tools/nupkgs/Godot.SourceGenerators.*.nupkg
%_libdir/godot-mono/GodotSharp/Tools/nupkgs/GodotSharp.*
%_libdir/godot-mono/GodotSharp/Tools/nupkgs/GodotSharpEditor.*
# mono_assemblies
%endif
# mono
%endif

%changelog
* Fri Oct 24 2025 Constantin Sunzow <protvin@altlinux.org> 4.5.1-alt1
- New version.

* Tue Sep 23 2025 Constantin Sunzow <protvin@altlinux.org> 4.5-alt1
- Fix Mono build (depends on network and required non-free binaries).
- Introduce godot-runner.
- New version.

* Tue Dec 24 2024 Constantin Sunzow <protvin@altlinux.org> 4.3-alt1
- Initial build.
