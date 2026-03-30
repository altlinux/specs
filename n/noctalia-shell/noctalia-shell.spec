Name: noctalia-shell
Version: 4.7.1
Release: alt1

Summary: A sleek and minimal desktop shell thoughtfully crafted for Wayland
License: MIT
Group:   Graphical desktop/Other

URL: https://docs.noctalia.dev
VCS: https://github.com/noctalia-dev/noctalia-shell.git

Source0: %name-%version.tar
Source1: README-quickstart.md

BuildArch: noarch

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-python3

# https://docs.noctalia.dev/getting-started/installation/#dependencies-explained
Requires: noctalia-qs
Requires: brightnessctl
Requires: ImageMagick-tools
Requires: python3
Requires: git
Requires: power-profiles-daemon
Requires: xdg-desktop-portal

%add_findreq_skiplist %_xdgconfigdir/quickshell/noctalia-shell/Scripts/dev/*

# False positive
%filter_from_requires /swaymsg/d
%filter_from_requires /hyprland/d
%filter_from_requires /kitty/d
%filter_from_requires /labwc-base/d
%filter_from_requires /mangowc/d
# Scripts/python/src/theming/lib
%filter_from_requires /python3(lib)/d
%filter_from_requires /python3(lib.scheme)/d

%description
A beautiful, minimal desktop shell for Wayland that actually gets out of your
way. Built on Quickshell with a warm lavender aesthetic that you can easily
customize to match your vibe.

%prep
%setup
install -Dm644 %SOURCE1 .

%install
install -dm755 %buildroot%_xdgconfigdir/quickshell/noctalia-shell
cp -r ./*      %buildroot%_xdgconfigdir/quickshell/noctalia-shell

%files
%doc README.md LICENSE README-quickstart.md
%_xdgconfigdir/quickshell/noctalia-shell

%changelog
* Mon Mar 30 2026 Ilya Sorochan <k0tran@altlinux.org> 4.7.1-alt1
- Update version.
- Switch from quickshell to noctalia-qs.
- Rewise requires.

* Sun Jan 18 2026 Ilya Sorochan <k0tran@altlinux.org> 4.1.1-alt1
- Update version.

* Tue Nov 18 2025 Ilya Sorochan <k0tran@altlinux.org> 3.1.1-alt1
- Initial build.
