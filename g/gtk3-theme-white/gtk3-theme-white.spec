%define  themename White

Name:    gtk3-theme-white
Version: 3.18
Release: alt1

Summary: White theme is a simple theme built to mimic OS x Yosemite and El Capitan clean interface

License: GPLv3+
Group:   Graphical desktop/GNOME
Url:     http://gnome-look.org/content/show.php/White?content=173840

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   173840-White-Feb2016.tar.gz

BuildArch: noarch

%description
White theme is a simple theme built to mimic OS x Yosemite and El
Capitan clean interface.

%install
mkdir -p %buildroot%_datadir/themes
tar xf %SOURCE0 -C %buildroot%_datadir/themes

%files
%_datadir/themes/%themename

%changelog
* Mon Apr 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.18-alt1
- Initial build in Sisyphus
