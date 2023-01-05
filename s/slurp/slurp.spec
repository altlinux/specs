Name:     slurp 
Version:  1.4.0
Release:  alt1

Summary:  Wayland region selector
License:  MIT
Group:    Graphics
Url:      https://github.com/emersion/slurp

ExcludeArch: i586 armh
Source:   %name-%version.tar

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires(pre): rpm-macros-meson

%description
Select a region in a Wayland compositor and print it to the standard output. Works well with grim.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/slurp
%_mandir/man1/*

%changelog
* Wed Dec 28 2022 Roman Alifanov <ximper@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
