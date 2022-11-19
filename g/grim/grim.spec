Name:     grim
Version:  1.4.0
Release:  alt1

Summary:  Grab images from a Wayland compositor
License:  MIT
Group:    Graphics
Url:      https://github.com/emersion/grim

ExcludeArch: i586 armh
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
* Sat Nov 19 2022 Roman Alifanov <ximper@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
