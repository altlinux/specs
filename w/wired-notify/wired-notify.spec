%define _unpackaged_files_terminate_build 1

Name: wired-notify
Version: 0.10.2
Release: alt1

Summary: Lightweight notification daemon with highly customizable layout blocks, written in Rust.
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/Toqozz/wired-notify
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libcairo-gobject-devel
BuildRequires: libdbus-devel
BuildRequires: pango-devel

%description
Wired is light and fully customizable notification daemon that provides you with powerful and extensible layout tools.

%prep
%setup
%patch0 -p1

%ifarch armh %ix86
sed -i '/idle_threshold/ s/u64/u32/' src/config.rs
%endif

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release %{?_smp_mflags} --all-targets --offline

%install
install -D -m755 target/release/wired -t %buildroot%_bindir/
install -D -m644 wired.service -t %buildroot/usr/lib/systemd/user/

%files
%doc README.md LICENSE readme_stuff
%_bindir/wired
/usr/lib/systemd/user/wired.service

%changelog
* Thu Nov 03 2022 Egor Ignatov <egori@altlinux.org> 0.10.2-alt1
- First build for ALT
