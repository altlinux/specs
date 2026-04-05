%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: xclicker
Version: 1.5.1
Release: alt1

Summary: Fast gui autoclicker for x11 linux desktops
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/robiot/xclicker

Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xtst)

%description
XClicker is an open-source, easy to use, feature-rich, blazing fast
Autoclicker for linux desktops using x11.

%prep
%setup
sed -i "s/Categories=.*/Categories=Utility;Accessibility;/" assets/xclicker.desktop
sed -i "s|https://raw.githubusercontent.com/robiot/xclicker/master/img/||" README.md

%build
%meson
make release

%install
install -Dm 755 build/release/src/%name %buildroot%_bindir/%name
install -Dm 644 assets/%{name}.desktop %buildroot%_desktopdir/%{name}.desktop
install -Dm 644 assets/icon.png %buildroot%_iconsdir/hicolor/256x256/apps/%{name}.png

%files
%doc LICENSE README.md img/banner.png img/example.png
%_bindir/xclicker
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/256x256/apps/%{name}.png

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus
