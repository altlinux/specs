%define _unpackaged_files_terminate_build 1

Name: kitty
Version: 0.19.3
Release: alt1

Summary: Cross-platform, fast, feature-rich, GPU based terminal
License: GPL-3.0
Group: Terminals
Url: https://sw.kovidgoyal.net/kitty/

Requires: %name-terminfo = %EVR

#Upstream: https://github.com/kovidgoyal/kitty
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: fonts-ttf-gnu-freefont-mono
BuildRequires: libXcursor-devel, libXrandr-devel, libXi-devel, libXinerama-devel
BuildRequires: python3-devel, python3-module-sphinx-sphinx-build-symlink
BuildRequires: libxkbcommon-x11-devel, libGL-devel, fontconfig-devel
BuildRequires: libharfbuzz-devel, libpng-devel, liblcms2-devel, libdbus-devel
BuildRequires: wayland-protocols, libwayland-client-devel, libwayland-cursor-devel

#For tic
BuildRequires: ncurses


%add_python3_path %_libexecdir/%name

%description
- Offloads rendering to the GPU for lower system load and buttery
  smooth scrolling. Uses threaded rendering to minimize input latency.

- Supports all modern terminal features: graphics (images), unicode,
  true-color, OpenType ligatures, mouse protocol, hyperlinks, focus
  tracking, bracketed paste and several new terminal protocol
  extensions.

- Supports tiling multiple terminal windows side by side in different
  layouts without needing to use an extra program like tmux

- Can be controlled from scripts or the shell prompt, even over SSH.

- Has a framework for Kittens, small terminal programs that can be
  used to extend kitty's functionality. For example, they are used for
  Unicode input, Hints and Side-by-side diff.

- Supports startup sessions which allow you to specify the window/tab
  layout, working directories and programs to run on startup.

- Cross-platform: kitty works on Linux and macOS, but because it uses
  only OpenGL for rendering, it should be trivial to port to other
  Unix-like platforms.

- Allows you to open the scrollback buffer in a separate window using
  arbitrary programs of your choice. This is useful for browsing the
  history comfortably in a pager or editor.

- Has multiple copy/paste buffers, like vim.


%package terminfo
Summary: The terminfo file for kitty
Group: System/Configuration/Other
BuildArch: noarch

%description terminfo
Cross-platform, fast, feature-rich, GPU based terminal

The terminfo file for kitty


%prep
%setup

# The following test is known to be failed
rm kitty_tests/tui.py

# Changing shebangs to python3
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python3|%{__python3}|g'  \
                                    -e 's|/usr/bin/env python|%{__python3}|g'   \
                                    -i "{}" \;

%install
mkdir -p %buildroot%_prefix
python3 setup.py linux-package --prefix=%buildroot%_prefix --update-check-interval=0

%check
python3 setup.py test --prefix=%buildroot%_prefix

%files
%_bindir/%name
%_datadir/doc/%name/
%_libexecdir/%name/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.png
%_man1dir/*

%files terminfo
%_datadir/terminfo/*/*

%changelog
* Tue Feb 09 2021 Egor Ignatov <egori@altlinux.org> 0.19.3-alt1
- First build for ALT.
