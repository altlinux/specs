Name:    bspwm
Version: 0.9.10
Release: alt1

Summary: A tiling window manager based on binary space partitioning
License: BSD-2-Clause
Group:   Graphical desktop/Other
Url:     https://github.com/baskerville/bspwm

Source:  %name-%version.tar

BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  xcb-util-wm-devel

%description
bspwm is a tiling window manager that represents windows as the leaves of a full binary tree.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/%name
%_bindir/bspc
%_docdir/%name/
%_man1dir/%name.1.*
%_man1dir/bspc.1.*
%_datadir/xsessions/%name.desktop

%_datadir/bash-completion/completions/bspc*
%_datadir/fish/vendor_completions.d/bspc*.fish
%_datadir/zsh/site-functions/_bspc*

%changelog
* Sun Jun 04 2023 Roman Alifanov <ximper@altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus

