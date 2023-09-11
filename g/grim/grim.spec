Name:     grim
Version:  1.4.1
Release:  alt1

Summary:  Grab images from a Wayland compositor
License:  MIT
Group:    Graphics
Url:      https://git.sr.ht/~emersion/grim

ExcludeArch: i586 armh

# Source-url: https://git.sr.ht/~emersion/grim/archive/v%version.tar.gz
Source:   %name-%version.tar

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires(pre): rpm-macros-meson
%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/grim
%_mandir/man?/grim*

%changelog
* Sun Sep 10 2023 Roman Alifanov <ximper@altlinux.org> 1.4.1-alt1
- new version (1.4.1) with rpmgs script
- changed upstream url
- move to tarball

* Sat Nov 19 2022 Roman Alifanov <ximper@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
