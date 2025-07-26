Name:     grim
Version:  1.5.0
Release:  alt1

Summary:  Grab images from a Wayland compositor
License:  MIT
Group:    Graphics
Url:      https://gitlab.freedesktop.org/emersion/grim

ExcludeArch: i586 armh

# Source-url: https://gitlab.freedesktop.org/emersion/grim/-/archive/v%version/grim-v%version.tar.gz
Source:   %name-%version.tar

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(bash-completion)
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
%meson \
    -Dfish-completions=true \
    -Dbash-completions=true
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/grim
%_mandir/man?/grim*
%_datadir/bash-completion/completions/*.bash
%_datadir/fish/vendor_completions.d/*.fish

%changelog
* Sun Jul 27 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- changed upstream url
- pack fish and bash completions

* Sun Sep 10 2023 Roman Alifanov <ximper@altlinux.org> 1.4.1-alt1
- new version (1.4.1) with rpmgs script
- changed upstream url
- move to tarball

* Sat Nov 19 2022 Roman Alifanov <ximper@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
