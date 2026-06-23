Name: vlither
Version: 2.5
Release: alt1

Summary: Desktop client for Slither.io rendered with Vulkan

License: GPL-3.0-or-later
Group: Games/Arcade
URL: https://github.com/for-loop9/vlither
# Source-url: https://github.com/for-loop9/vlither.git
Source: %name-%version.tar

# Downstream patches (kept separate so the bundled source stays pristine and
# the package remains updatable).
Patch1: 0001-use-system-glfw.patch
Patch2: 0002-native-wayland-support.patch
Patch3: 0003-default-server.patch
Patch4: 0004-vsync-on-by-default.patch
Patch5: 0005-snappier-input.patch
Patch6: 0006-fix-cxx-compound-literal.patch

# The premake project hardcodes x86_64 architecture
ExclusiveArch: x86_64

BuildRequires: premake5 make
BuildRequires: gcc-c++
BuildRequires: libvulkan-devel
# Use the system GLFW (3.4, built with both X11 and Wayland backends) instead of
# the bundled vanilla copy, so the client works on X11 and Wayland.
BuildRequires: libglfw3-devel
# Slang shader compiler (provides slangc); compiles app/res/shaders/src/*.slang
BuildRequires: /usr/bin/slangc

%description
Vlither is a desktop client for Slither.io which can run outside the
browser. It is written in C and uses Vulkan for rendering all graphics,
resulting in faster rendering. It links the system GLFW and bundles the
thermite rendering engine, cimgui/Dear ImGui, cglm, stb, mongoose and the
Vulkan Memory Allocator, all built from source.

%prep
%setup
%autopatch -p1

%build
export VULKAN_SDK=%_prefix

# Compile Slang shaders to SPIR-V (build.py command 2)
python3 build.py 2

# Generate gmake makefiles from project.lua
premake5 --file=project.lua gmake

# Build the release configuration
%make_build -C build/makefiles config=release_linux verbose=1

%install
# Application binary (the binary itself is named "app" upstream).
# ELF objects are not allowed under %_datadir, so install it into %_libexecdir.
install -Dm755 build/bin/linux_x86_64_release/app %buildroot%_libexecdir/%name/%name

# Runtime resources (shaders bin, textures, fonts) loaded via relative app/res/ path.
# The binary loads shaders from app/res/shaders/bin/*.spv, so preserve the bin/ level.
mkdir -p %buildroot%_datadir/%name/app/res/shaders
cp -a app/res/shaders/bin %buildroot%_datadir/%name/app/res/shaders/
cp -a app/res/textures %buildroot%_datadir/%name/app/res/
cp -a app/res/fonts %buildroot%_datadir/%name/app/res/

# Wrapper launcher: the binary loads resources via relative paths (app/res/...)
# and writes user.dat into the current directory, so run from a per-user data dir.
mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
datadir="${XDG_DATA_HOME:-$HOME/.local/share}/vlither"
mkdir -p "$datadir/app"
# Symlink read-only resources so the binary finds them via relative path
ln -snf %_datadir/%name/app/res "$datadir/app/res"
cd "$datadir" || exit 1
exec %_libexecdir/%name/%name "$@"
EOF
chmod 755 %buildroot%_bindir/%name

%files
%doc README.md LICENSE
%_bindir/%name
%_libexecdir/%name/
%_datadir/%name/

%changelog
* Fri Jun 19 2026 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- initial build for ALT Sisyphus (version 2.5)
- link against the system GLFW (X11 and Wayland) instead of the bundled copy
- install compiled shaders under app/res/shaders/bin/ so the client finds them
- default to VSync on and a reachable default server
- fix a non-portable C++ compound literal in bundled imgui (builds on p10/p11)

