Name: icon-theme-qogir
Version: 20190407
Release: alt1
Summary: Qogir icon theme

Group: Graphical desktop/GNOME
License: GPL3
Url: https://github.com/vinceliuice/Qogir-theme

Source: %name-%version.tar.gz

BuildArch: noarch
Packager: Leontiy Volodin <lvol@altlinux.org>

BuildRequires: gtk-update-icon-cache

%description
A flat colorful design icon theme for Qogir theme

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/icons/Qogir
mkdir -p %buildroot%_datadir/icons/Qogir-dark
./Install -d %buildroot%_datadir/icons
rm -rf %buildroot%_datadir/icons/Qogir*/scalable/apps/gtk-missing-image.svg

%files
%doc AUTHORS COPYING README.md
%_datadir/icons/Qogir*

%changelog
* Thu Apr 11 2019 Leontiy Volodin <lvol@altlinux.org> 20190407-alt1
- Initial build for ALT Sysiphus

