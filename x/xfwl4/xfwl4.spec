Name: xfwl4
Version: 4.21.0
Release: alt1

Summary: Xfce's Wayland Compositor
License: GPL-3.0-or-later
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

Url: https://docs.xfce.org/xfce/xfwl4/start
Vcs: https://gitlab.xfce.org/xfce/xfwl4.git
Source0: %name-%version.tar
Source1: vendor-%version.tar
Patch: %name-%version-%release.patch
ExcludeArch: i586

BuildRequires(pre): meson rpm-macros-meson
BuildRequires: rust-cargo rustc
BuildRequires: xfce-wayland-protocols
BuildRequires: libxfce4ui-gtk3-devel >= 4.21.4
BuildRequires: libxfconf-devel >= 4.21.2
BuildRequires: libdisplay-info-devel >= 0.3.0
BuildRequires: libdrm-devel >= 2.4.0
BuildRequires: libgbm-devel >= 25.0.0
BuildRequires: libinput-devel >= 1.28.0
BuildRequires: libpixman-devel >= 0.44.0
BuildRequires: libseat1-devel >= 0.9.0
BuildRequires: libudev-devel >= 1:257
BuildRequires: libxkbcommon-devel >= 0.8.0
BuildRequires: jq
BuildRequires: xfce-wayland-protocols
BuildRequires: wayland-protocols
BuildRequires: wlr-protocols

Requires: xfce4-common

%define _unpackaged_files_terminate_build 1

%description
Xfwl4 will be Xfce's Wayland compositor.
It is currently heavily under development. While many xfwm4 (and other
desktop environment) features are implemented, some things are not
implemented yet.

%prep
%setup
tar xf %SOURCE1
%patch -p1
# Use system package for xfce-wayland-protocols
rmdir resources/xfce-wayland-protocols/
PROTOCOLS_DIR="$(pkg-config --variable=pkgdatadir xfce-wayland-protocols)"
ln -sr "$PROTOCOLS_DIR" resources/xfce-wayland-protocols

# Use system wayland packages instead of vendored sources
replace_crate_with_system()
{
	local package_name="$1"; shift
	local crate_name="$1"; shift
	local protos_dir="$1"; shift
	local system_protos_dir=

	rm -rf vendor/"$crate_name"/"$protos_dir"
	system_protos_dir="$(pkg-config --variable=pkgdatadir "$package_name")"
	[ -d "$system_protos_dir" ] || exit 1
	ln -sr "$system_protos_dir" vendor/"$crate_name"/"$protos_dir"

	jq -r ".files | keys[] | select(startswith(\"$protos_dir/\"))" \
			vendor/"$crate_name"/.cargo-checksum.json | while read fpath; do
		sed -r -i "s;,?\"$fpath\":[[:blank:]]*\"[^\"]*\";;" vendor/"$crate_name"/.cargo-checksum.json
	done
}

replace_crate_with_system wayland-protocols wayland-protocols protocols
replace_crate_with_system wlr-protocols wayland-protocols-wlr wlr-protocols

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=2", "-Cdebuginfo=1"]

[profile.release]
strip = false

[source."git+https://github.com/smithay/smithay?rev=4645e03d6bd9377aa368de20e91d69951450392d"]
git = "https://github.com/smithay/smithay"
rev = "4645e03d6bd9377aa368de20e91d69951450392d"
replace-with = "vendored-sources"
EOF

%build
%meson \
	--buildtype=release \
	-Degl=true \
	-Dxwayland=true \
	-Duse-system-gettext=true \
	-Ddebug-rendering=false

%meson_build -v

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/wayland-sessions/%name.desktop
%dir %_datadir/xfce4/%name/
%config %_datadir/xfce4/%name/defaults

%changelog
* Mon Jun 29 2026 Mikhail Efremov <sem@altlinux.org> 4.21.0-alt1
- Initial build.

