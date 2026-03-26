Name: xwayland-satellite
Version: 0.8.1
Release: alt2

Summary: Xwayland outside your Wayland
License: MPL-2.0
Group:   System/X11

URL: https://github.com/Supreeeme/xwayland-satellite
VCS: https://github.com/Supreeeme/xwayland-satellite.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-build-rust
BuildRequires: libxcbutil-cursor-devel
BuildRequires: clang21.1-devel
BuildRequires: xorg-xwayland-devel

Requires: xorg-xwayland

%description
xwayland-satellite grants rootless Xwayland integration to any Wayland compositor
implementing xdg_wm_base and viewporter. This is particularly useful for
compositors that (understandably) do not want to go through implementing support
for rootless Xwayland themselves.

%prep
%setup -a1
install -vpD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install
install -Dpm0644 xwayland-satellite.man %buildroot%_man1dir/xwayland-satellite.1

%files
%doc *.md LICENSE
%_bindir/xwayland-satellite
%_man1dir/xwayland-satellite.1.*

%changelog
* Thu Mar 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.1-alt2
- NMU: Fixed man-page packaging (ALT#58263).

* Tue Mar 03 2026 Ilya Sorochan <k0tran@altlinux.org> 0.8.1-alt1
- Update version.

* Wed Jan 14 2026 Ilya Sorochan <k0tran@altlinux.org> 0.8-alt1
- Update version.

* Wed Nov 12 2025 Ilya Sorochan <k0tran@altlinux.org> 0.7-alt1
- Initial build.
