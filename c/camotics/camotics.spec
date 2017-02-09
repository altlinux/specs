Name: camotics
Version: 1.1.0
Release: alt1

Summary: Open-Source Simulation and Computer Aided Machining - A 3-axis CNC GCode simulator

License: GPLv2+ and LGPL2.1
Group: Engineering
Url: https://github.com/CauldronDevelopmentLLC/CAMotics

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ scons boost-filesystem-devel boost-program_options-devel boost-interprocess-devel libcairo-devel libqt4-devel bzlib-devel libsqlite3-devel libexpat-devel libv8-3.15-devel libevent-devel python-module-simplejson libssl-devel libre2-devel zlib-devel
BuildRequires: ImageMagick-tools desktop-file-utils
Requires: %name-data = %version-%release

%description
CAMotics is an Open-Source software which can simulate 3-axis NC machining. It
is a fast, flexible and user friendly simulation software for the DIY and
Open-Source community. CAMotics works on Linux, OS-X and Windows.

At home manufacturing is one of the next big technology revolutions. Much like
the PC was 30 years ago. There have been major advances in desktop 3D printing
yet uptake of desktop CNCs has lagged depsite the availability of cheap CNC
machines. One of the major reasons for this is a lack of Open-Source simulation
and CAM software. CAM and NC machine simulation present some very difficult
programming problems, as is evidenced by 30 years of academic papers on these
topics. Whereas, 3D printing simulation and tool path generation are much
easier. Such software is essential to using a CNC.

Being able to simulate is a critical part of creating CNC tool paths.
Programming a CNC with out a simulator is cutting with out measuring; it s both
dangerous and expensive. With CAMotics you can preview the results of your
cutting operation before you fire up your machine. This will save you time and
money and open up a world of creative possibilities by allowing you to rapidly
visualize and improve upon designs with out wasting material or breaking tools.

%package data
Summary: Data files for %name
Group: Engineering
Buildarch: noarch

%description data
Data files for %name

%prep
%setup

%build
export QT4DIR=%_includedir/qt4
%make_build

%install
scons install install_prefix=%buildroot%prefix

#Install missing data files
mkdir -p %buildroot%_datadir/%name
cp -r tpl_lib %buildroot%_datadir/%name

#Install examples
mkdir -p %buildroot%_docdir/%name
cp -r examples %buildroot%_docdir/%name

#Install and fixing desktop files
install -pD -m644 CAMotics.desktop %buildroot%_desktopdir/CAMotics.desktop
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-key=Encoding \
        --set-icon=camotics \
        --remove-category=Science \
        --add-category=Science \
        --add-category=Engineering \
        %buildroot%_desktopdir/CAMotics.desktop

#Convert and install images files
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
	convert images/camotics.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/camotics.png
done

%files
%_bindir/*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%_desktopdir/CAMotics.desktop

%files data
%_docdir/%name
%_datadir/%name

%changelog
* Wed Feb 08 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- New version 1.1.0

* Sun Jan 29 2017 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1.20170106.1
- Initial build for ALT Linux Sisyphus (Closes: 33041).
