%define theme_name faenza-blue
Name: icon-theme-%theme_name
Version: 0.2.1
Release: alt2
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

%package hd
Summary: SVG-icon for %name
Group:  Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %version-%release

%description hd
SVG-icon for %name

%prep
%setup -q -n %theme_name-%version

%build

%install
mkdir -p %buildroot%_iconsdir/Faenza-Blue
cp -R * %buildroot%_iconsdir/Faenza-Blue

#Remove dead link
find -L %buildroot%_iconsdir/Faenza-Blue -type l -delete
mkdir -p %buildroot%_docdir/%name
mv %buildroot%_iconsdir/Faenza-Blue/AUTHORS %buildroot%_docdir/%name
mv %buildroot%_iconsdir/Faenza-Blue/ChangeLog %buildroot%_docdir/%name
mv %buildroot%_iconsdir/Faenza-Blue/COPYING %buildroot%_docdir/%name

%files
%_iconsdir/Faenza-Blue
%exclude %_iconsdir/Faenza-Blue/*/96
%exclude %_iconsdir/Faenza-Blue/*/scalable
%_docdir/%name

%files hd
%_iconsdir/Faenza-Blue/*/96
%_iconsdir/Faenza-Blue/*/scalable

%changelog
* Fri Jan 19 2018 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt2
- Added icon for newmoon
- new subpackage icon-theme-faenza-blue-hd

* Sat Feb 11 2017 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- Initial build for ALT Linux Sisyphus.
