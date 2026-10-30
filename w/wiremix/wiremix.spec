Name:    wiremix
Version: 0.11.0
Release: alt1

Summary: Simple TUI audio mixer for PipeWire
License: Apache-2.0 OR MIT
Group:   Sound
URL:     https://github.com/tsowell/wiremix
VCS:     https://github.com/tsowell/wiremix

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: clang-devel
BuildRequires: pkgconfig(libpipewire-0.3)

%description
wiremix is a simple TUI audio mixer for PipeWire. You can use it to adjust
volumes, route audio between devices and applications, and configure audio
device settings like input/output ports and profiles.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install
install -Dm644 %name.desktop \
    %buildroot%_desktopdir/%name.desktop

%check
%rust_test

%files
%doc LICENSE-APACHE LICENSE-MIT README.md CHANGELOG.md
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Oct 28 2026 Evgeniy Serov <scala@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.
