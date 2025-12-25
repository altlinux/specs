%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: ddrescueview
Version: 0.4.5
Release: alt1

Summary: graphical viewer for GNU ddrescue map files
License: GPL-3.0-or-later
Group: Archiving/Backup
URL: https://sourceforge.net/projects/ddrescueview/
Vcs: https://salsa.debian.org/pascal-team/ddrescueview

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: lazarus
BuildRequires: dos2unix
BuildRequires: qt5pas-devel

ExcludeArch: i586

%description
This small tool allows the user to graphically examine ddrescue's map files
in a user friendly GUI application. The Main window displays a block grid
with each block's color representing the block types it contains. Many people
know this type of view from defragmentation programs.

Features:

* Display ddrescue map in a colored block graphic
* Examine each block in the image, see a detailed list of
map entries contained
* To keep track of the rescue process, ddrescueview can automatically
re-read the mapfile
* Units can be displayed with decimal (KB, MB...) or
binary (KiB, MiB...) prefixes

%prep
%setup
dos2unix *.txt
%patch -p1
sed -i "s/Categories=.*/Categories=Utility;Archiving;FileTools;GTK;/" resources/linux/applications/ddrescueview.desktop

%build
lazbuild \
         --lazarusdir=%_libdir/lazarus \
         --bm="GNU/Linux Release" \
         --ws=qt5 \
         source/ddrescueview.lpi

%install
install -Dm 755 source/ddrescueview %buildroot%_bindir/%name
install -Dm 644 resources/linux/man/man1/ddrescueview.1 %buildroot%_man1dir/%{name}.1
cp -rv resources/linux/icons/ %buildroot%_datadir/
install -Dm 644 resources/linux/applications/%{name}.desktop %buildroot%_desktopdir/%{name}.desktop

%files
%doc readme.txt changelog.txt
%_bindir/ddrescueview
%_desktopdir/ddrescueview.desktop
%_iconsdir/hicolor/*/apps/ddrescueview.png
%_man1dir/ddrescueview.1.xz

%changelog
* Thu Dec 25 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.5-alt1
- Initial build for Sisyphus
