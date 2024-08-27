Name: icon-theme-alt
Version: 1.0
Release: alt0.beta3
Summary: ALT icon theme

License: GPL-3.0
Group: Graphics
URL: https://altlinux.org

Source: %name-%version.tar

BuildArch: noarch

%description
ALT Icon theme based on Qogir icon theme.

%prep
%setup
# Remove symlinks to empty directories
rm -f  ALT/animations/24@{2,3}x ALT/emotes/24@{2,3}x

%install
mkdir -p %buildroot%_iconsdir
cp -a ALT %buildroot%_iconsdir

%files
%_iconsdir/ALT

%changelog
* Tue Aug 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.beta3
- Initial build in Sisyphus.
