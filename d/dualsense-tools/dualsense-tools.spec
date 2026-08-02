Name:    dualsense-tools
Version: 0.3.0
Release: alt1

Summary: Tools for the Sony Dualsense PS5 controller
License: MIT
Group:   System/Configuration/Hardware
URL:     https://github.com/Astrac/dualsense-tools

Source: %name-%version.tar
Source1: %name-development-%version.tar
Patch: add-desktop-file-and-icon.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libwayland-client-devel libalsa-devel libudev-devel

ExcludeArch: i586

%description
Dualsense Tools
This crate contains a set of tools that interface with the Sony Dualsense PS5
controller:

A low-level interface to read and decode HID reports from the controller.
An implementation of accelerometer-corrected-gyro tilt estimation.
A bevy plugin that exposes tilt estimates as a resource, including an example
to quickly visualize the estimates.
A virtual device application that creates a custom controller tailored
for 6-axis simulations (e.g. space games).

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install dualsense-6-axis

install -Dm 644 dualsense-6-axis/dualsense-6-axis.desktop \
    %buildroot%_datadir/applications/dualsense-6-axis.desktop

install -Dm 644 dualsense-6-axis/dualsense-6-axis.svg \
    %buildroot%_datadir/icons/hicolor/scalable/apps/dualsense-6-axis.svg

%files
%doc LICENSE README.md
%_bindir/dualsense-6-axis
%_datadir/applications/dualsense-6-axis.desktop
%_datadir/icons/hicolor/scalable/apps/dualsense-6-axis.svg

%changelog
* Sun Aug 02 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
