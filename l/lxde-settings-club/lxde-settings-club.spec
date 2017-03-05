%define theme_name club
%define theme_virt_dir lxde
%define theme_fullname lxde-settings-%theme_name
Name: %theme_fullname
Version: 0.1
Release: alt1
Packager: LXDE Development Team <lxde at packages.altlinux.org>
BuildArch: noarch

Summary: Provides LXDE configuration
License: GPLv3
Group: Graphical desktop/Other
Url: https://altlinux.org
BuildArch: noarch

Source: %name-%version.tar
Provides: lxde-settings
Requires: icon-theme-faenza-blue gtk3-theme-clearlooks-phenix
Requires: fonts-ttf-google-droid-sans-mono fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif

%description
ALT Linux Active User Club theme for LXDE.

This package contains configuration for LXDE.

%prep
%setup

%build

%install
mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme_fullname << __EOF__
%_datadir/%theme_virt_dir %_datadir/%theme_fullname 1
__EOF__

mv skel %buildroot%_sysconfdir/skel

mkdir -p %buildroot%_datadir/%theme_fullname
cp -r * %buildroot%_datadir/%theme_fullname

%files
%_sysconfdir/alternatives/packages.d/%theme_fullname
%_datadir/%theme_fullname
%_sysconfdir/skel/.config/*

%changelog
* Sun Mar 05 2017 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus.
