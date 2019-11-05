Name: herbstluftwm
Version: 0.7.2
Release: alt2

Summary: A manual tiling window manager
License: BSD-2-Clause
Group: Graphical desktop/Other
Url: https://herbstluftwm.org

# repacked https://herbstluftwm.org/tarballs/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.watch
Source2: %name.wmsession

Patch1: 0001-SUSE-examples-remove-executable-bits.patch
Patch2: 0002-DEBIAN-reproducible.patch
Patch3: 0003-ALT-bash-completion-path.patch
Patch4: 0004-ALT-use-xvt-as-default-terminal.patch

BuildRequires: asciidoc asciidoc-a2x gcc-c++ glib2-devel libxslt-devel libX11-devel libXext-devel
Requires: /usr/bin/xvt
Requires: dzen2
Requires: dmenu

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
%make_build

%install
%makeinstall_std \
	PREFIX="%prefix"

install -D -m0644  %SOURCE2 %buildroot%_sysconfdir/X11/wmsession.d/17%name

# We use the normal doc convention for this instead.
# INSTALL is not shipped.
rm -f %buildroot%_datadir/doc/%name/{INSTALL,NEWS,LICENSE,BUGS}

%files
%doc BUGS LICENSE NEWS
%dir %_datadir/doc/%name/
%_datadir/doc/%name/herbstclient.html
%_datadir/doc/%name/%name-tutorial.html
%_datadir/doc/%name/%name.html

%dir %_sysconfdir/xdg/%name
%_sysconfdir/X11/wmsession.d/17%name
%_sysconfdir/xdg/%name/autostart
%_sysconfdir/xdg/%name/panel.sh
%_sysconfdir/xdg/%name/restartpanels.sh

%_bindir/herbstclient
%_bindir/%name
%_bindir/dmenu_run_hlwm

%_man1dir/herbstclient.1*
%_man1dir/%name.1*
%_man7dir/%name-tutorial.7*

%_datadir/xsessions/herbstluftwm.desktop

%dir %_datadir/zsh
%dir %_datadir/zsh/functions
%dir %_datadir/zsh/functions/Completion
%dir %_datadir/zsh/functions/Completion/X
%_datadir/zsh/functions/Completion/X/_herbstclient

%dir %_datadir/bash-completion/
%dir %_datadir/bash-completion/completions/
%_datadir/bash-completion/completions/herbstclient-completion

%dir %_datadir/fish
%dir %_datadir/fish/vendor_completions.d
%_datadir/fish/vendor_completions.d/herbstclient.fish

%files examples
%_datadir/doc/%name/examples

%changelog
* Tue Nov 05 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt2
- Fixed bash completion location.

* Fri Oct 18 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.2-alt1
- Initial build for ALT Sisyphus based on openSUSE spec file, but heavily
  reworked.
- Applied Debian patch for reproducibility.
- Fixed bash completion path.
- Changed to use /usr/bin/xvt as default X terminal instead of xterm.
