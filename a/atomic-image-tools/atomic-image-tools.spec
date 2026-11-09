# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/atomic-image-tools

%define _unpackaged_files_terminate_build 1

Name: atomic-image-tools
Version: 0.1.0
Release: alt1

Summary: Some tools for ALT Atomic builder image
License: GPL-3.0-or-later
Group: Other
URL: https://altlinux.space/alt-atomic/atomic-image-tools
VCS: https://altlinux.space/alt-atomic/atomic-image-tools.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(libxml-2.0)

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libexecdir/get-os-metainfo

%changelog
* Tue Nov 10 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1.0-alt1
- Initial build.
