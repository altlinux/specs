Name: ghostty
Version: 1.3.1
Release: alt1

Summary: Fast, feature-rich and cross-platform terminal emulator
License: MIT
Group: Terminals
URL: https://ghostty.org/
VCS: https://github.com/ghostty-org/ghostty

Requires: terminfo-ghostty = %EVR

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: deps-%version.tar

BuildRequires: /proc
BuildRequires: zig rpm-macros-zig
BuildRequires: blueprint-compiler
BuildRequires: fontconfig-devel
BuildRequires: glslang
BuildRequires: highway-devel
BuildRequires: libadwaita-devel
BuildRequires: libfreetype-devel
BuildRequires: libgtk4-devel
BuildRequires: libgtk4-layer-shell-devel
BuildRequires: libharfbuzz-devel
BuildRequires: liboniguruma-devel
BuildRequires: libpng-devel
BuildRequires: libsimdutf-devel
BuildRequires: libspirv-cross-devel
BuildRequires: libxml2-devel
BuildRequires: termutils-devel
BuildRequires: zlib-devel

%package -n libghostty
Summary: Ghostty shared library
Group: System/Libraries

%package -n libghostty-devel
Summary: Development part of ghostty
Group: Development/C

%package -n terminfo-ghostty
Summary: Ghostty terminfo
Group: Terminals

%define desc \
Ghostty is a terminal emulator that differentiates itself by being fast,\
feature-rich, and native. While there are many excellent terminal emulators\
available, they all force you to choose between speed, features, or native UIs.\
Ghostty provides all three.

%description %desc

%description -n libghostty %desc
This package provides Ghostty shared library.

%description -n libghostty-devel %desc
This package contains development part of Ghostty.

%description -n terminfo-ghostty %desc
This package contains terminfo entries for Ghostty.

%define _zig_system_integration %nil
%define _zig_optimize_mode ReleaseFast

%prep
%setup -a1

%build
%zig_build \
	-Demit-lib-vt \
	-Dsimd=true \
	-Dgtk-wayland=true \
	-Dstrip=false \
	-fsys=fontconfig \
	-fsys=freetype \
	-fsys=glslang \
	-fsys=gtk4-layer-shell \
	-fsys=harfbuzz \
	-fsys=highway \
	-fsys=libpng \
	-fsys=oniguruma \
	-fsys=simdutf \
	-fsys=spirv-cross \
	-fsys=zlib

%install
%zig_install
rm -v	%buildroot%_libdir/libghostty-vt.a \
	%buildroot%_datadir/pkgconfig/libghostty-vt-static.pc
%find_lang com.mitchellh.ghostty
%ifdef bootstrap
tar cf %SOURCE1 --exclude '*/rules' zig-pkg
%endif

%files -f com.mitchellh.ghostty.lang
%_bindir/ghostty
%_desktopdir/com.mitchellh.ghostty.desktop
%_datadir/bash-completion/completions/ghostty.bash
%_datadir/dbus-1/services/com.mitchellh.ghostty.service
%_datadir/fish/vendor_completions.d/ghostty.fish
%_datadir/ghostty
%_datadir/kio/servicemenus/com.mitchellh.ghostty.desktop
%_datadir/metainfo/*.xml
%_datadir/zsh/site-functions/_ghostty
#_datadir/nautilus-python
%_datadir/nvim/site/*/*.vim
%_datadir/vim/vimfiles/*/*.vim
%_iconsdir/*/*/*/*.*

%files -n libghostty
%_libdir/libghostty-vt.so.*

%files -n libghostty-devel
%_libdir/libghostty-vt.so
%_includedir/ghostty
%_datadir/pkgconfig/libghostty-vt.pc

%files -n terminfo-ghostty
%_datadir/terminfo/g/ghostty
%_datadir/terminfo/x/xterm-ghostty

%changelog
* Tue Sep 08 2026 Sergey Bolshakov <sbolshakov@altlinux.org >1.3.1-alt1
- v1.3.1-2523-gb0c421fcd
