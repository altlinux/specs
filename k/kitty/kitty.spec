%define _unpackaged_files_terminate_build 1
%def_with check

Name: kitty
Version: 0.24.4
Release: alt1

Summary: Cross-platform, fast, feature-rich, GPU based terminal
License: GPL-3.0
Group: Terminals
Url: https://sw.kovidgoyal.net/kitty/

Requires: %name-terminfo = %EVR

# VCS: https://github.com/kovidgoyal/kitty
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Patch1: alt-sphinx-use-classic-theme.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libxkbcommon-x11-devel

BuildRequires: wayland-protocols
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel

BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: libdbus-devel
BuildRequires: librsync-devel
BuildRequires: liblcms2-devel
BuildRequires: fontconfig-devel
BuildRequires: libharfbuzz-devel

BuildRequires: python3-module-sphinx-copybutton
BuildRequires: python3-module-sphinx-inline-tabs
BuildRequires: python3-module-sphinxext-opengraph
BuildRequires: python3-module-sphinx-sphinx-build-symlink

# For tic
BuildRequires: ncurses

%if_with check
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: fonts-ttf-gnu-freefont-mono
%endif

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
%patch0 -p1
%patch1 -p1

# Changing shebangs to python3
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python3|%__python3|g'  \
                                    -e 's|/usr/bin/env python|%__python3|g'   \
                                    -i "{}" \;
%ifarch %e2k
# ftbfs workaround with lcc 1.25.17:
# kitty/screen.c:1437,1463: pointless comparison of unsigned integer with zero
sed -i "s/-Werror//g" setup.py
%endif

%build
%python3_build_debug

%install
mkdir -p %buildroot%_prefix
python3 setup.py linux-package \
	--prefix=%buildroot%_prefix \
	--update-check-interval=0 \
	--debug

python3 __main__.py + complete setup bash | \
	install -Dm644 /dev/stdin %buildroot%_datadir/bash-completion/completions/kitty

python3 __main__.py + complete setup zsh | \
	install -Dm644 /dev/stdin  %buildroot%_datadir/zsh/site-functions/_kitty

python3 __main__.py + complete setup fish | \
	install -Dm644 /dev/stdin %buildroot%_datadir/fish/vendor_completions.d/kitty.fish

%check
python3 setup.py test --prefix=%buildroot%_prefix

%files
%_bindir/%name
%_datadir/doc/%name/
%_libexecdir/%name/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_man5dir/*
%_datadir/bash-completion/completions/kitty
%_datadir/zsh/site-functions/_kitty
%_datadir/fish/vendor_completions.d/kitty.fish

%files terminfo
%_datadir/terminfo/*/*

%changelog
* Thu Mar 03 2022 Egor Ignatov <egori@altlinux.org> 0.24.4-alt1
- new version 0.24.4

* Mon Feb 28 2022 Egor Ignatov <egori@altlinux.org> 0.24.3-alt1
- new version 0.24.3

* Wed Feb 16 2022 Egor Ignatov <egori@altlinux.org> 0.24.2-alt1
- new version 0.24.2

* Tue Sep 07 2021 Egor Ignatov <egori@altlinux.org> 0.23.1-alt1
- new version 0.23.1
- cleanup spec
- add bash, zsh and fish completions
- add alt-sphinx-use-classic-theme patch
- disable -Werror for e2k (@mike)

* Mon Jun 28 2021 Egor Ignatov <egori@altlinux.org> 0.21.2-alt1
- new version 0.21.2

* Mon Jun 21 2021 Egor Ignatov <egori@altlinux.org> 0.21.1-alt1
- Update sources to 0.21.1

* Tue May 11 2021 Egor Ignatov <egori@altlinux.org> 0.20.3-alt1
- Update sources to 0.20.3

* Thu Apr 29 2021 Egor Ignatov <egori@altlinux.org> 0.20.2-alt1
- Update sources to 0.20.2

* Tue Apr 27 2021 Egor Ignatov <egori@altlinux.org> 0.20.1-alt1
- Update sources to 0.20.1
- Cleanup spec

* Wed Mar 24 2021 Egor Ignatov <egori@altlinux.org> 0.19.3-alt2
- Fix: add debug sources to debuginfo

* Tue Feb 09 2021 Egor Ignatov <egori@altlinux.org> 0.19.3-alt1
- First build for ALT.
