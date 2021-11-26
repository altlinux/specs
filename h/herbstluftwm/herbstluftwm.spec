Name: herbstluftwm
Version: 0.9.0
Release: alt3

Summary: A manual tiling window manager
License: BSD-2-Clause
Group: Graphical desktop/Other
Url: https://herbstluftwm.org

# repacked https://herbstluftwm.org/tarballs/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.watch
Source2: %name.wmsession

Patch1: 0001-ALT-use-xvt-as-default-terminal.patch
Patch2: 0002-DEBIAN-reproducible.patch
Patch3: 0003-FC-herbstluftwm-gcc11.patch

BuildRequires(pre): cmake rpm-macros-cmake
BuildRequires: asciidoc asciidoc-a2x gcc-c++ glib2-devel libxslt-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel
Requires: /usr/bin/xvt
Requires: dmenu
Requires: dzen2
Requires: xrandr

%package examples
Summary: Example scripts for %name
Group: Graphical desktop/Other
Requires: %name
BuildArch: noarch

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.

%description examples
Sample bash scripts for herbstluftwm and herbstclient, which give the user
an idea of what is possible.

%prep
%setup
%autopatch -p2
# fix errors about improper shebangs due to /usr/bin/env
find . -type f -exec sed -i "s@#!/usr/bin/env bash@#!/bin/bash@" {} +

%build
export CPPFLAGS="%optflags"
export CFLAGS="%optflags"
%cmake
%cmake_build

%install
%cmakeinstall_std

install -D -m0644  %SOURCE2 %buildroot%_sysconfdir/X11/wmsession.d/17%name

# We use the normal doc convention for this instead.
# INSTALL is not shipped.
rm -f %buildroot%_datadir/doc/%name/{INSTALL,NEWS,LICENSE,BUGS}

%files
%doc BUGS LICENSE NEWS
%dir %_datadir/doc/%name/
%dir %_datadir/doc/%name/examples/
%_datadir/doc/%name/herbstclient.html
%_datadir/doc/%name/hlwm-doc.json
%_datadir/doc/%name/%name-tutorial.html
%_datadir/doc/%name/%name.html
%_datadir/doc/%name/examples/dmenu.sh

%dir %_sysconfdir/xdg/%name
%_sysconfdir/X11/wmsession.d/17%name
%_sysconfdir/xdg/%name/autostart
%_sysconfdir/xdg/%name/panel.sh
%_sysconfdir/xdg/%name/restartpanels.sh
%_sysconfdir/xdg/herbstluftwm/dmenu_run_hlwm

%_bindir/herbstclient
%_bindir/%name

%_man1dir/herbstclient.1*
%_man1dir/%name.1*
%_man7dir/%name-tutorial.7*

%_datadir/xsessions/herbstluftwm.desktop

#dir %_datadir/zsh
#dir %_datadir/zsh/site-functions
%_datadir/zsh/site-functions/_herbstclient

#dir %_datadir/bash-completion/
#dir %_datadir/bash-completion/completions/
%_datadir/bash-completion/completions/herbstclient

#dir %_datadir/fish
#dir %_datadir/fish/vendor_completions.d
%_datadir/fish/vendor_completions.d/herbstclient.fish

%files examples
%exclude %_datadir/doc/%name/examples/dmenu.sh
%_datadir/doc/%name/examples

%changelog
* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 0.9.0-alt3
- NMU: new completion policy

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.9.0-alt2
- NMU: fixed build

* Mon Nov 02 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Mon Jun 22 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.3-alt1
- Updated to 0.8.3.

* Sun May 03 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Tue Nov 05 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt2
- Fixed bash completion location.

* Fri Oct 18 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt1
- Initial build for ALT Sisyphus based on openSUSE spec file, but heavily
  reworked.
- Applied Debian patch for reproducibility.
- Fixed bash completion path.
- Changed to use /usr/bin/xvt as default X terminal instead of xterm.
