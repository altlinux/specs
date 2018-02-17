%define theme_name lxdesktop
%define theme_virt_dir lxde
%define theme_fullname lxde-settings-%theme_name
Name: %theme_fullname
Version: 0.3
Release: alt2
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
Requires: qasmixer
Requires: screenshot-tool
Requires: xdg-user-dirs-gtk

%description
Theme for LXDE, based on a branding-altlinux-lxdesktop-settings
and lxde-settings-upstream.

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
mv X11 %buildroot%_sysconfdir/X11
chmod 755 %buildroot%_sysconfdir/X11/profile.d/*.sh

mkdir -p %buildroot%_datadir/%theme_fullname
cp -r * %buildroot%_datadir/%theme_fullname

%files
%_sysconfdir/alternatives/packages.d/%theme_fullname
%_datadir/%theme_fullname
%_sysconfdir/skel/.config/*
%_sysconfdir/X11/profile.d/*.sh

%changelog
* Sat Feb 17 2018 Anton Midyukov <antohami@altlinux.org> 0.3-alt2
- Replacement screngrab to screenshot-tool

* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- version 0.3

* Sun Jan 14 2018 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- version 0.2

* Fri Aug 25 2017 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus.
