%define _unpackaged_files_terminate_build 1

Name: falcond-gui
Version: 1.0.0
Release: alt1

Summary: A GTK4/LibAdwaita application to control and monitor the Falcond gaming optimization daemon

License: MIT
Group: System/Kernel and hardware
Url: https://git.pika-os.com/general-packages/falcond-gui

# Source-url: https://git.pika-os.com/general-packages/falcond-gui/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: /proc

Requires: falcond

%description
falcond-gui provides a user-friendly graphical interface for managing falcond. It allows users to view the status of the daemon and customize its behavior.

%prep
%setup -a1
mkdir -p .cargo

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
cd %name
%rust_build

%install
cd %name
%rust_install

install -Dpm 0644 res/%name.desktop %buildroot%_desktopdir/%name.desktop
install -dm 0755 %buildroot%_iconsdir/hicolor/512x512/apps
install -pm 0644 res/falcond.png %buildroot%_iconsdir/hicolor/512x512/apps/falcond.png

%files
%doc README.md
%doc LICENSE.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/512x512/apps/falcond.png


%changelog
* Mon Jan 05 2026 Boris Yumankulov <boria138@altlinux.org> 1.0.0-alt1
- initial build for ALT Sisyphus

