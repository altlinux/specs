Name: xfce-wayland-protocols
Version: 0.1.0
Release: alt2.g7dec3b0

Summary: Wayland protocols that are private to the Xfce desktop environment
License: MIT
Group: Development/Other
Url: https://gitlab.xfce.org/xfce/xfce-wayland-protocolss

Vcs: https://gitlab.xfce.org/xfce/xfce-wayland-protocols.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): meson rpm-macros-meson

%define _unpackaged_files_terminate_build 1

%description
Wayland protocols that are private to the Xfce
desktop environment and its compositor, xfwl4.  Regular applications
should not use or depend on these protocols, as use is intended only for
communication between Xfce components and the compositor.

These protocols may change without notice, and may not adhere to
customary backward-compatibility rules and conventions that Wayland
protocols usually follow.

%prep
%setup
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%_datadir/pkgconfig/*.pc
%_datadir/xfce4/%name/

%changelog
* Tue Jun 23 2026 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2.g7dec3b0
- Packaged xfce-input-device-list-private-v1.xml.
- Updated to g7dec3b0.

* Mon Jun 22 2026 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.g6748e9f
- Initial build.
