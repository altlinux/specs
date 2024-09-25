%define _unpackaged_files_terminate_build 1
%def_with check

Name: kitty
Version: 0.36.3
Release: alt1

Summary: Cross-platform, fast, feature-rich, GPU based terminal
License: GPL-3.0
Group: Terminals
VCS: https://github.com/kovidgoyal/kitty
Url: https://sw.kovidgoyal.net/kitty/

Requires: %name-kitten = %EVR
Requires: %name-terminfo = %EVR
Requires: %name-shell-integration = %EVR

Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: SymbolsNerdFontMono-Regular.ttf
Patch0: %name-%version-alt.patch

# 0.27.0: unmet /usr/pkg/bin/tic
%add_findreq_skiplist %_libexecdir/kitty/shell-integration/ssh/bootstrap-utils.sh

# play sound
Requires: libcanberra
# panel kitten
Requires: libstartup-notification
# icat kitten
Requires: ImageMagick-tools

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-golang

BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libxkbcommon-x11-devel

BuildRequires: wayland-protocols
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel

BuildRequires: simde-devel
BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: libssl-devel
BuildRequires: libdbus-devel
BuildRequires: liblcms2-devel
BuildRequires: libxxhash-devel
BuildRequires: fontconfig-devel
BuildRequires: libharfbuzz-devel

BuildRequires: python3-dev
BuildRequires: python3-module-sphinx-copybutton
BuildRequires: python3-module-sphinx-inline-tabs
BuildRequires: python3-module-sphinxext-opengraph
BuildRequires: python3-module-sphinx-sphinx-build-symlink

# tic for xterm-kitty terminfo
BuildRequires: ncurses

# + install -Dm644 /dev/stdin .../usr/share/bash-completion/completions/kitty
BuildRequires: /proc

%if_with check
# 0.35.1: test_zsh_integration fails, disable by not installing zsh
#BuildRequires: zsh
BuildRequires: bash
BuildRequires: fish
BuildRequires: /dev/pts
BuildRequires: fonts-ttf-gnu-freefont-mono
%endif

%add_python3_path %_libexecdir/kitty

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
%summary.

%package shell-integration
Summary: Shell-integration files for kitty
Group: System/Configuration/Other
BuildArch: noarch

%description shell-integration
%summary.

%package kitten
Summary: Standalone kitten executable
Group: System/Configuration/Other

%description kitten
Statically compiled, standalone executable, kitten (written in Go) that
can be used on all UNIX-like servers for remote control (kitten @), viewing
images (kitten icat), manipulating the clipboard (kitten clipboard), etc.

%prep
%setup -a 1
%patch0 -p1

install -Dm644 %SOURCE2 -t ./fonts

# Changing shebangs to python3
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python3|%__python3|g'  \
                                    -e 's|/usr/bin/env python|%__python3|g'   \
                                    -i "{}" \;

# Our gcc enables "_FORTIFY_SOURCE=3" by default, remove defenition
# form setup.py to avoid error "_FORTIFY_SOURCE" redefined
sed -i -e "s/-D_FORTIFY_SOURCE=2//" setup.py

%build
%add_optflags -Wno-switch
export CFLAGS="${CFLAGS:-%optflags}"
export CGO_ENABLED=0
python3 setup.py linux-package \
    --verbose \
    --update-check-interval=0 \
    %nil

%install
mkdir -pv %buildroot
cp -r ./linux-package %buildroot%_prefix

%buildroot%_bindir/kitten __complete__ setup bash | \
    install -Dm644 /dev/stdin %buildroot%_datadir/bash-completion/completions/kitty

%buildroot%_bindir/kitten __complete__ setup zsh | \
    install -Dm644 /dev/stdin  %buildroot%_datadir/zsh/site-functions/_kitty

%buildroot%_bindir/kitten __complete__ setup fish | \
    install -Dm644 /dev/stdin %buildroot%_datadir/fish/vendor_completions.d/kitty.fish

%buildroot%_bindir/kitty \
    +runpy 'from kitty.config import *; print(commented_out_default_config())' \
    | install -Dm644 /dev/stdin %buildroot%_datadir/kitty/kitty.conf.default


%check
%ifarch ppc64le
# test_elliptic_curve_data_exchange fails on ppc64le due to 64k memlock limit in the
# chroot environmet which is not enough for 64k pagesize system
rm kitty_tests/crypto.py

# test_transfer_receive and test_transfer_send fail on ppc64le:
# "Error: inappropriate ioctl for device"
rm kitty_tests/file_transmission.py
%endif

PYTHONPATH="$PWD" linux-package/bin/kitty +launch ./test.py


%files
%_bindir/kitty
%_libexecdir/kitty/
%_datadir/kitty/
%exclude %_libexecdir/kitty/shell-integration
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_man5dir/*
%_datadir/bash-completion/completions/kitty
%_datadir/zsh/site-functions/_kitty
%_datadir/fish/vendor_completions.d/kitty.fish

%files terminfo
%_datadir/terminfo/*/*

%files shell-integration
%_libexecdir/kitty/shell-integration

%files kitten
%_bindir/kitten

%changelog
* Wed Sep 25 2024 Egor Ignatov <egori@altlinux.org> 0.36.3-alt1
- new version 0.36.3

* Mon Sep 09 2024 Egor Ignatov <egori@altlinux.org> 0.36.2-alt1
- new version 0.36.2

* Tue Aug 27 2024 Egor Ignatov <egori@altlinux.org> 0.36.1-alt1
- new version 0.36.1

* Thu Aug 22 2024 Egor Ignatov <egori@altlinux.org> 0.36.0-alt1
- new version 0.36.0

* Mon Jun 24 2024 Egor Ignatov <egori@altlinux.org> 0.35.2-alt1
- new version 0.35.2

* Fri May 31 2024 Egor Ignatov <egori@altlinux.org> 0.35.1-alt1
- new version 0.35.1

* Sun Apr 21 2024 Egor Ignatov <egori@altlinux.org> 0.34.1-alt1
- new version 0.34.1

* Wed Apr 17 2024 Egor Ignatov <egori@altlinux.org> 0.34.0-alt1
- new version 0.34.0

* Tue Mar 26 2024 Egor Ignatov <egori@altlinux.org> 0.33.1-alt1
- new version 0.33.1

* Mon Mar 11 2024 Egor Ignatov <egori@altlinux.org> 0.32.2-alt2
- enable shell-integration tests
- fix build with gcc 10

* Wed Feb 14 2024 Egor Ignatov <egori@altlinux.org> 0.32.2-alt1
- new version 0.32.2

* Sat Jan 27 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.32.1-alt2
- NMU: fixed FTBFS on LoongArch

* Fri Jan 26 2024 Egor Ignatov <egori@altlinux.org> 0.32.1-alt1
- new version 0.32.1

* Mon Jan 22 2024 Egor Ignatov <egori@altlinux.org> 0.32.0-alt2
- package default config file

* Mon Jan 22 2024 Egor Ignatov <egori@altlinux.org> 0.32.0-alt1
- new version 0.32.0

* Wed Nov 08 2023 Egor Ignatov <egori@altlinux.org> 0.31.0-alt1
- new version 0.31.0

* Thu Oct 05 2023 Egor Ignatov <egori@altlinux.org> 0.30.1-alt1
- new version 0.30.1

* Tue Sep 26 2023 Egor Ignatov <egori@altlinux.org> 0.30.0-alt1
- new version 0.30.0
- move kitten to it's own sub-package

* Thu Jul 27 2023 Egor Ignatov <egori@altlinux.org> 0.29.2-alt1
- new version 0.29.2

* Mon Jul 17 2023 Egor Ignatov <egori@altlinux.org> 0.29.1-alt1
- new version 0.29.1

* Mon Jul 10 2023 Egor Ignatov <egori@altlinux.org> 0.29.0-alt1
- new version 0.29.0

* Tue Jul 04 2023 Egor Ignatov <egori@altlinux.org> 0.28.1-alt3
- FTBFS: fix build with new wayland-protocols

* Fri Apr 28 2023 Egor Ignatov <egori@altlinux.org> 0.28.1-alt2
- FTBFS: fix build with new gcc defaults

* Fri Apr 21 2023 Egor Ignatov <egori@altlinux.org> 0.28.1-alt1
- new version 0.28.1

* Sat Apr 15 2023 Egor Ignatov <egori@altlinux.org> 0.28.0-alt1
- new version 0.28.0

* Fri Mar 10 2023 Egor Ignatov <egori@altlinux.org> 0.27.1-alt1
- new version 0.27.1

* Mon Mar 06 2023 Egor Ignatov <egori@altlinux.org> 0.27.0-alt2
- fix FTBFS: build without docs
- clean up spec

* Tue Jan 31 2023 Egor Ignatov <egori@altlinux.org> 0.27.0-alt1
- new version 0.27.0

* Mon Nov 07 2022 Egor Ignatov <egori@altlinux.org> 0.26.5-alt1
- new version 0.26.5

* Tue Oct 18 2022 Egor Ignatov <egori@altlinux.org> 0.26.4-alt1
- new version 0.26.4

* Thu Sep 22 2022 Egor Ignatov <egori@altlinux.org> 0.26.3-alt1
- new version 0.26.3

* Wed Sep 07 2022 Michael Shigorin <mike@altlinux.org> 0.26.2-alt2
- NMU: fix build on e2k and --without check

* Mon Sep 05 2022 Egor Ignatov <egori@altlinux.org> 0.26.2-alt1
- new version 0.26.2

* Wed Aug 31 2022 Egor Ignatov <egori@altlinux.org> 0.26.1-alt1
- new version 0.26.1

* Thu Aug 04 2022 Egor Ignatov <egori@altlinux.org> 0.25.2-alt2
- spec: Release build with debug info

* Tue Jun 07 2022 Egor Ignatov <egori@altlinux.org> 0.25.2-alt1
- new version 0.25.2

* Thu May 26 2022 Egor Ignatov <egori@altlinux.org> 0.25.1-alt1
- new version 0.25.1

* Thu Apr 28 2022 Egor Ignatov <egori@altlinux.org> 0.25.0-alt3
- add libstartup-notification dependency (closes: #42606)
- add ImageMagick-tools dependency (closes: #42607)
- add libcanberra dependency

* Wed Apr 13 2022 Egor Ignatov <egori@altlinux.org> 0.25.0-alt2
- spec: move shell-integration to another package as upstream suggests

* Mon Apr 11 2022 Egor Ignatov <egori@altlinux.org> 0.25.0-alt1
- new version 0.25.0

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
