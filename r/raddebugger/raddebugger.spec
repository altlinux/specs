Name: raddebugger
Version: 0.9.29
Release: alt1

Summary: A native, user-mode, multi-process, graphical debugger

License: MIT
Group: Development/Tools
URL: https://github.com/EpicGames/raddebugger
# Source-url: https://github.com/EpicGames/raddebugger/archive/refs/tags/v%version-alpha/raddebugger-%version-alpha.tar.gz
Source: %name-%version.tar
Source1: raddbg.desktop

Patch: fix-build-outside-git.patch

ExclusiveArch: x86_64

BuildRequires: gcc-c++ clang llvm llvm-devel
BuildRequires: libfreetype-devel
BuildRequires: libX11-devel libXext-devel libXfixes-devel libXrandr-devel
BuildRequires: libGL-devel libEGL-devel
BuildRequires: desktop-file-utils

%description
The RAD Debugger is a native, user-mode, multi-process, graphical debugger.
It currently supports local-machine x64 debugging on Windows and Linux.
It also includes the RAD Linker (radlink) - a performance linker for generating
x64 PE/COFF binaries, and the RAD Binary utility (radbin) for working with
debug information formats.

%prep
%setup
%patch -p1

%build
export CC=clang AR=llvm-ar
./build.sh clang release raddbg radbin radlink

%install
install -D -m 0755 build/raddbg %buildroot%_bindir/raddbg
install -D -m 0755 build/radbin %buildroot%_bindir/radbin
install -D -m 0755 build/radlink %buildroot%_bindir/radlink
install -D -m 0644 data/logo.png %buildroot%_iconsdir/hicolor/256x256/apps/raddbg.png
install -D -m 0644 %SOURCE1 %buildroot%_desktopdir/raddbg.desktop
install -D -m 0644 LICENSE %buildroot%_docdir/%name/LICENSE
install -D -m 0644 README.md %buildroot%_docdir/%name/README.md
test -f build/raddbg_readme.md && install -D -m 0644 build/raddbg_readme.md %buildroot%_docdir/%name/raddbg_readme.md || true

%files
%_bindir/raddbg
%_bindir/radbin
%_bindir/radlink
%_desktopdir/raddbg.desktop
%_iconsdir/hicolor/256x256/apps/raddbg.png
%doc %_docdir/%name/

%changelog
* Sat Oct 10 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.29-alt1
- Initial build for ALT Linux (v0.9.29-alpha)
- Add desktop file and icon
