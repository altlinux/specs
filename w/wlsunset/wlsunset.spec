Name: wlsunset
Version: 0.4.0
Release: alt1

Summary: Day/night gamma adjustments for Sway

License: MIT
Group: Other
Url: https://github.com/kennylevinsen/wlsunset

# Source-url: https://github.com/kennylevinsen/wlsunset/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)

%description
Day/night gamma adjustments for Sway and other Wayland compositors
supporting wlr-gamma-control-unstable-v1.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/wlsunset
%_man1dir/wlsunset.1.xz

%changelog
* Thu May 09 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.4.0-alt1
- initial build for ALT Sisyphus

