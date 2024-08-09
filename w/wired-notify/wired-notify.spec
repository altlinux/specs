%define _unpackaged_files_terminate_build 1

Name: wired-notify
Version: 0.10.6
Release: alt1

Summary: Lightweight notification daemon with highly customizable layout blocks
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/Toqozz/wired-notify
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Patch1: cty-nix-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libcairo-gobject-devel
BuildRequires: libdbus-devel
BuildRequires: pango-devel
BuildRequires: cargo-vendor-checksum diffstat

%description
Wired is light and fully customizable notification daemon that
provides you with powerful and extensible layout tools.

%prep
%setup
%patch0 -p1
%patch1 -p1

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

diffstat -p1 -l %PATCH1 | sed -re 's@vendor/@@' | xargs -r cargo-vendor-checksum -f

%build
cargo build --release %{?_smp_mflags} --all-targets --offline

%install
install -D -m755 target/release/wired -t %buildroot%_bindir/
install -D -m644 wired.service -t %buildroot%_user_unitdir

%files
%doc README.md LICENSE readme_stuff
%_bindir/wired
%_user_unitdir/wired.service

%changelog
* Fri Aug 09 2024 Egor Ignatov <egori@altlinux.org> 0.10.6-alt1
- new version 0.10.6

* Tue Jan 30 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.4-alt2
- NMU: fixed FTBFS on LoongArch (trivial patch for cty and nix crates)

* Tue Jan 23 2024 Egor Ignatov <egori@altlinux.org> 0.10.4-alt1
- new version 0.10.4

* Thu Nov 03 2022 Egor Ignatov <egori@altlinux.org> 0.10.2-alt1
- First build for ALT
