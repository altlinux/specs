Name: kde5-plasma-theme-scratchy
Version: 20230916
Release: alt1
Summary: Dark theme, based on the catppuccin macchiato color palette
License: MIT
Group: Graphical desktop/KDE
Url: https://store.kde.org/p/1898344
Vcs: https://gitlab.com/jomada/Scratchy
Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/kf5/{aurorae/themes,plasma/desktoptheme}
cp -r aurorae/Scratchy %buildroot%_datadir/kf5/aurorae/themes
cp -r color-schemes %buildroot%_datadir/kf5
cp -r konsole %buildroot%_datadir/kf5
cp -r look-and-feel %buildroot%_datadir/kf5/plasma
cp -r plasma/Scratchy %buildroot%_datadir/kf5/plasma/desktoptheme

%files
%_datadir/kf5/aurorae/themes/Scratchy
%_datadir/kf5/color-schemes/Scratchy.colors
%_datadir/kf5/color-schemes/ScratchyLightly.colors
%_datadir/kf5/konsole/Scratchy.colorscheme
%_datadir/kf5/plasma/look-and-feel/Scratchy
%_datadir/kf5/plasma/desktoptheme/Scratchy

%changelog
* Sun Jan 21 2024 Alexander Makeenkov <amakeenk@altlinux.org> 20230916-alt1
- Initial build for ALT.

