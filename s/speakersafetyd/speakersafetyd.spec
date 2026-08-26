%define _unpackaged_files_terminate_build 1

Name: speakersafetyd
Version: 2.0.1
Release: alt1
Summary: Rust speaker safety daemon for Asahi Linux
License: MIT
Group: System/Kernel and hardware
Url: https://github.com/asahilinux/speakersafetyd
VCS: https://github.com/asahilinux/speakersafetyd.git

ExclusiveArch: aarch64

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: clang-devel
BuildRequires: pkgconfig(alsa)

%description
speakersafetyd is a userspace daemon written in Rust that implements an analogue
of the Texas Instruments Smart Amp speaker protection model.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%makeinstall_std \
    DESTDIR=%buildroot \
    UNITDIR=%_unitdir \
    UDEVDIR=%_udevrulesdir \
    SHAREDIR=%_datadir

%files
%doc README.md
%_bindir/%name
%_unitdir/%name.service
%_datadir/%name
%_udevrulesdir/*

%changelog
* Tue Aug 25 2026 Vasiliy Doylov <neko@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
