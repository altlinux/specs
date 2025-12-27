Name: wprs
Version: 0.1.0
Release: alt1

Summary: Like xpra, but for Wayland

License: Apache-2.0
Group: System/X11
Url: https://github.com/wayland-transpositor/wprs

ExclusiveArch: x86_64

# Source-url: https://github.com/wayland-transpositor/wprs.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust rpm-build-python3
BuildRequires: rpm-build-rust /proc
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel
BuildRequires: libwayland-client-devel libwayland-server-devel

%description
wprs is a remote desktop application for Wayland. It works like xpra, but for
Wayland, and written in Rust. It implements rootless remote desktop access for
remote Wayland (and X11, via XWayland) applications.

The system consists of two main components:
- wprsd (server): A Wayland compositor on the remote machine that serializes application state
- wprsc (client): A local Wayland client that mirrors remote windows locally

%prep
%setup -a1 -n %name-%version

mkdir -p .cargo
cat <<EOF >> .cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export RUSTFLAGS="-C target-feature=+avx2"
%rust_build

%install
mkdir -p %buildroot%_bindir
install -m755 target/release/wprsd %buildroot%_bindir/
install -m755 target/release/wprsc %buildroot%_bindir/
install -m755 target/release/xwayland-xdg-shell %buildroot%_bindir/
install -m755 wprs %buildroot%_bindir/
mkdir -p %buildroot%_userunitdir
install -m644 wprsd.service %buildroot%_userunitdir/

%files
%_bindir/wprsd
%_bindir/wprsc
%_bindir/xwayland-xdg-shell
%_bindir/wprs
%_userunitdir/wprsd.service
%doc README.md LICENSE

%changelog
* Sat Dec 27 2025 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- Initial package for ALT Linux
