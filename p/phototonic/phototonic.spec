Name: phototonic
Version: 2.1.10
Release: alt1

Summary: An image viewer and organizer
Group: Graphics
License: GPLv3
Url: https://github.com/oferkv/phototonic

#VCS: https://github.com/oferkv/phototonic.git
Source: %name-%version.tar.gz

# Automatically added by buildreq on Sun Oct 18 2015 (-bi)
# optimized out: elfutils libGL-devel libqt5-core libqt5-gui libqt5-widgets libstdc++-devel python-base python3 python3-base qt5-base-devel qt5-declarative-devel
BuildRequires: gcc-c++ libexiv2-devel qt5-multimedia-devel qt5-script-devel qt5-svg-devel

%description
Phototonic is an image viewer and organizer with the following features:
* Light weight with a smooth and clear user interface
* Does not depend on any desktop environment
* Supports several customized thumbnail layouts
* Load thumbnails and browse images recursively
* Dynamic thumbnails loading, enabling fast browsing of very large folders
* Filter thumbnails
* Image navigation and file management
* Slide show
* View random image
* Transformation: rotation, flipping, cropping, image mirroring
* Adjust image colors
* Keep transformations zoom and colors while browsing multiple images
* Extensive automatic and manual zoom options
* Supported image formats:
BMP, GIF, ICO, JPEG, MNG, PBM, PGM, PNG, PPM, SVG, SVGZ, TGA, TIFF, XBM, XPM
* Supports GIF animations
* Keyboard shortcuts and mouse behavior customization
* Load image files or folders from command line
* Open images with external applications

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# Install translations
mkdir -p %buildroot%_datadir/%name/translations
cp -r translations/*.qm %buildroot%_datadir/%name/translations

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/translations
%_iconsdir/hicolor/*x*/apps/%name.png
%doc README.md

%changelog
* Mon Jan 28 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.10-alt1
- 2.1.10

* Mon Oct 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- 2.1 (new url)

* Sun Nov 15 2015 Motsyo Gennadi <drool@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Sun Oct 18 2015 Motsyo Gennadi <drool@altlinux.ru> 1.6.26-alt1
- initial build for ALT Linux from Mageia srpm package
