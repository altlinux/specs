%define theme rose-pine
%define themename %theme-hyprcursor

Name: hyprcursor-theme-%theme
Version: 0.3.2
Release: alt1
License: GPL-3.0

Summary: BreezeX RosePine for Hyprcursor

Group: Graphical desktop/Other

Url: https://github.com/ndom91/rose-pine-hyprcursor

BuildArch: noarch
Source: %name-%version.tar

%description
This is a Rose Pine remix of the original BreezeX cursor theme.
Then repackaged again for use with Hyprland's new Hyprcursor format.

%prep
%setup

%install
install -d %buildroot%_iconsdir/%themename
cp -r hyprcursors %buildroot%_iconsdir/%themename
cp manifest.hl %buildroot%_iconsdir/%themename

%files
%doc README.md LICENSE
%_iconsdir/%themename/

%changelog
* Sat Aug 03 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.2-alt1
- Initial build
