%define _unpackaged_files_terminate_build 1
%def_without mono
# see architecture_aliases in platform_methods.py
%define arch_alias %_arch
%ifarch aarch64
%define arch_alias arm64
%endif

Name: godot4
Version: 4.3
Release: alt1

Summary: Multi-platform 2D and 3D game engine
License: MIT
Group: Development/Tools
Url: https://godotengine.org
VCS: https://github.com/godotengine/godot.git
ExclusiveArch: aarch64 x86_64 %e2k

Source: godot-%version.tar
Patch0: godot4-4.3-alpine-fix-glslang.patch
Patch1: godot4-4.3-alpine-fix-miniupnpc.patch
Patch2: godot4-4.3-alt-dynamic-link-xatlas.patch
Patch3: godot4-4.3-alt-fix-desktop.patch

Provides: godot = %version
Requires: libEGL
Requires: libpulseaudio
Requires: libxkbcommon

BuildRequires: embree-devel
BuildRequires: gcc-c++
BuildRequires: glslang-devel
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
BuildRequires: libmbedtls-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libogg-devel
BuildRequires: libpcre2-devel
BuildRequires: libpng-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsquish-devel
BuildRequires: libstdc++-devel
BuildRequires: libtheora-devel
BuildRequires: libudev-devel
BuildRequires: libvolk-devel
BuildRequires: libvorbis-devel
BuildRequires: libwebp-devel
BuildRequires: libxatlas-devel
BuildRequires: libzstd-devel
BuildRequires: openxr-devel
BuildRequires: scons
BuildRequires: wayland-devel
BuildRequires: zlib-devel
%if_with mono
BuildRequires: dotnet-sdk-9.0
%endif

%description
%summary.

%if_with mono
%package mono
Summary: Multi-platform 2D and 3D game engine (Mono version)
Group: Development/Tools

Provides: godot-mono = %version

%description mono
%summary.
%endif

%prep
%setup
%autopatch -p1

%build
%define disable_builtin() %{expand:builtin_%{1}=no}

%define disable_builtins \\\
  %{disable_builtin brotli} \\\
  %{disable_builtin certs} \\\
  %{disable_builtin embree} \\\
  %{disable_builtin enet} \\\
  %{disable_builtin freetype} \\\
  %{disable_builtin glslang} \\\
  %{disable_builtin graphite} \\\
  %{disable_builtin harfbuzz} \\\
  %{disable_builtin icu4c} \\\
  %{disable_builtin libogg} \\\
  %{disable_builtin libpng} \\\
  %{disable_builtin libtheora} \\\
  %{disable_builtin libvorbis} \\\
  %{disable_builtin libwebp} \\\
  %{disable_builtin mbedtls} \\\
  %{disable_builtin miniupnpc} \\\
  %{disable_builtin openxr} \\\
  %{disable_builtin pcre2} \\\
  %{disable_builtin pcre2_with_jit} \\\
  %{disable_builtin squish} \\\
  %{disable_builtin xatlas} \\\
  %{disable_builtin zlib} \\\
  %{disable_builtin zstd} \\\
%nil

%define scons_options \\\
  arch=%_arch \\\
  cflags="$CFLAGS -fPIC -Wl,-z,relro,-z,now -w -O2" \\\
  colored=yes \\\
  cxxflags="$CXXFLAGS -fPIC -Wl,-z,relro,-z,now -w -O2" \\\
  %disable_builtins \\\
  disable_exceptions=false \\\
  engine_update_check=no \\\
  error=no \\\
  execinfo=no \\\
  -j %__nprocs \\\
  platform=linuxbsd \\\
  production=yes \\\
  pulseaudio=yes \\\
  system_certs_path=/usr/share/ca-certificates/ca-bundle.crt \\\
  target=editor \\\
  tools=yes \\\
  use_llvm=no \\\
  use_static_cpp=no \\\
  verbose=yes \\\
%nil

scons \
  %scons_options \
  %nil

%if_with mono
scons \
  %scons_options \
  module_mono_enabled=yes \
  mono_glue=no \
  %nil

bin/godot.linuxbsd.editor.%arch_alias.mono \
  --generate-mono-glue modules/mono/glue \
  --headless \
  %nil
modules/mono/build_scripts/build_assemblies.py \
  --godot-output-dir=./bin \
  --godot-platform=linuxbsd \
  %nil
%endif

%install
install -Dm 755 bin/godot.linuxbsd.editor.%arch_alias \
  %buildroot%_bindir/godot4
%if_with mono
install -Dm 755 bin/godot.linuxbsd.editor.%arch_alias.mono \
  %buildroot%_bindir/godot4-mono
%endif

install -Dm 644 icon.png \
  %buildroot%_iconsdir/hicolor/256x256/apps/godot4.png
install -Dm 644 icon.svg \
  %buildroot%_iconsdir/hicolor/scalable/apps/godot4.svg
install -Dm 644 misc/dist/linux/org.godotengine.Godot.desktop \
  -t %buildroot%_desktopdir
install -Dm 644 misc/dist/linux/org.godotengine.Godot.appdata.xml \
  -t %buildroot%_datadir/metainfo
install -Dm 644 misc/dist/linux/godot.6 -t %buildroot%_man6dir

%files
%_bindir/godot4
%_datadir/metainfo/org.godotengine.Godot.appdata.xml
%_desktopdir/org.godotengine.Godot.desktop
%_iconsdir/hicolor/256x256/apps/godot4.png
%_iconsdir/hicolor/scalable/apps/godot4.svg
%_man6dir/godot.6.xz

%if_with mono
%files mono
%_bindir/godot4-mono
%_datadir/metainfo/org.godotengine.Godot.appdata.xml
%_desktopdir/org.godotengine.Godot.desktop
%_iconsdir/hicolor/256x256/apps/godot4.png
%_iconsdir/hicolor/scalable/apps/godot4.svg
%endif

%changelog
* Tue Dec 24 2024 Constantin Sunzow <protvin@altlinux.org> 4.3-alt1
- Initial build.
