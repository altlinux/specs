Name: icon-theme-qogir
Version: 20230223
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

rm -f

%build

%install
mkdir -p %buildroot%_datadir/icons/Qogir
mkdir -p %buildroot%_datadir/icons/Qogir-dark
./install.sh -d %buildroot%_datadir/icons

rm -rf %buildroot%_datadir/icons/Qogir*/scalable/apps/gtk-missing-image.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/view-financial-account-asset.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/help-contents.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/kstars_xplanet.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/l2h.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/new-command-alarm.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/dblatex.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/headphones.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/viewhtml.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/kdenlive-show-audio.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/kdenlive-hide-audio.svg
rm -rf %buildroot%_datadir/icons/Qogir*/24/actions/player-volume-muted.svg

%files
%doc AUTHORS COPYING README.md
%_datadir/icons/Qogir*

%changelog
* Sun Mar 12 2023 Artyom Bystrov <arbars@altlinux.org> 20230223-alt1
- update to new version

* Thu Apr 11 2019 Leontiy Volodin <lvol@altlinux.org> 20190407-alt1
- Initial build for ALT Sysiphus

