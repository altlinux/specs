%define _unpackaged_files_terminate_build 1

Name: hamr
Version: 1.1.0
Release: alt1

Summary: Instant access to apps, calculations, clipboard history, and files
License: MIT
Group: Graphical desktop/Other
Url: https://hamr.run/
Vcs: https://github.com/Stewart86/hamr

Source: %name-%version.tar
Source1: vendor.tar
Source2: systemd_daemon_config.tar

%filter_from_requires /^niri$/d
%filter_from_requires /^hyprland$/d
%filter_from_requires /^swaybg$/d

Requires: hamr-daemon
Requires: hamr-gtk

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-python3

BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: libglycin-gtk4-devel
BuildRequires: libgtk4-layer-shell-devel

%description
Hamr learns from your usage patterns to surface what you need, when you
need it. Type a few characters to launch apps, calculate math, search 
files, access clipboard history, and more.

%package daemon
Summary: Socket server wrapping core
Group: System/Servers

%description daemon
%summary.

%package gtk
Summary: GTK4 native UI with layer shell
Group: Graphical desktop/Other

%description gtk
%summary.

%package tui
Summary: Terminal UI for headless use
Group: Other

%description tui
%summary.

%prep
%setup -a1 -a2
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[profile.release]
strip = false
opt-level = 3
debug = true
EOF

%build
%rust_build --all-features

%install
%rust_install hamr hamr-daemon hamr-gtk hamr-tui

mkdir -pv %buildroot%_datadir/hamr/plugins/
cp -rv plugins/ %buildroot%_datadir/hamr/plugins/

install -Dm 0644 systemd_daemon_config/hamr-daemon.service  %buildroot%_userunitdir/hamr-daemon.service
install -Dm 0644 systemd_daemon_config/hamr-gtk.service %buildroot%_userunitdir/hamr-gtk.service

%check
%rust_test --all-features

%files
%doc LICENSE
%_bindir/hamr
%_datadir/hamr

%files daemon
%_bindir/hamr-daemon
%_userunitdir/hamr-daemon.service

%files gtk
%_bindir/hamr-gtk
%_userunitdir/hamr-gtk.service

%files tui
%_bindir/hamr-tui

%changelog
* Wed May 20 2026 Dina Tagantseva <dinchik@altlinux.org> 1.1.0-alt1
- New version.

* Mon May 04 2026 Dina Tagantseva <dinchik@altlinux.org> 1.0.22-alt2
- Fixed requires (Closes: 58737)

* Tue Apr 07 2026 Dina Tagantseva <dinchik@altlinux.org> 1.0.22-alt1
- Initial build for Sisyphus
