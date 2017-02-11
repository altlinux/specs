%define theme_name faenza-blue
Name: icon-theme-%theme_name
Version: 0.2.1
Release: alt1
Summary: Faenza blue icon theme

Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://www.gnome-look.org/p/1157713

Source: https://dl.opendesktop.org/api/files/download/id/1476645816/%theme_name-%version.tar.xz

BuildArch: noarch
Packager: Anton Midyukov <antohami@altlinux.org>

%description
This icon theme for Gnome provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and Gnome menu items.

%prep
%setup -q -n %theme_name-%version

%build

%install
mkdir -p %buildroot%_iconsdir/Faenza-Blue
cp -R * %buildroot%_iconsdir/Faenza-Blue

#Remove dead link
find -L %buildroot%_iconsdir/Faenza-Blue -type l -delete
#rm -fR %buildroot%_iconsdir/Faenza-Blue/{AUTHORS ChangeLog COPYING}

%files
%_iconsdir/Faenza-Blue
%doc AUTHORS ChangeLog COPYING

%changelog
* Sat Feb 11 2017 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- Initial build for ALT Linux Sisyphus.
