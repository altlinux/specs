Name: xwayland-satellite
Version: 0.7
Release: alt1

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

%files
%doc *.md LICENSE
%_bindir/xwayland-satellite

%changelog
* Wed Nov 12 2025 Ilya Sorochan <k0tran@altlinux.org> 0.7-alt1
- Initial build.
