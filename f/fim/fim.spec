Name: fim
Version: 0.2.2
Release: alt2

Summary: Free Image Manipulator
License: GPLv2
Group: Graphics

Url: http://www.nongnu.org/fim
Source0: %url/%name-%version.tar.bz2
Source1: fim.desktop
Patch0: fim-0.2.2-ru.patch
Patch1: fim-0.2.2-alt-gcc43.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Jul 02 2008
BuildRequires: gcc-c++ libgd2-devel libjpeg-devel libqt4-devel

%description
* If you have ever been asked, after a meeting or a party, to send photos
  to your friends from the event and you had to resize them all...
* If you have ever wanted to publish your images but you had to sign them
  firstly so nobody could borrow your work...
* If you ever had to convert a lot of images...

Then Free Image Manipulator has been made just for you!
You can resize many images (you only set their maximum size and images
are scalled automatically so that ratio is not changed)

* You can add text (you choose font, size, color of background and foreground,
  position, spacing, opacity of background and foreground)
* Despite the fact that images had different sizes, after resizing, added text
  will look on every image the same (all chosen options are relative)
* You are able to save or load images from one of the formats: jpeg, png, gif
  (every image in the set can be in different format, it doesn't matter)

%prep
%setup -n release
%patch0 -p1
%patch1 -p1

%build
cd src
%_libdir/qt4/bin/qmake
%make_build

%install
cd src
%make_install INSTALL_ROOT=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%post
%update_menus

%postun
%clean_menus

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/fonts/TTF/*.ttf
%_pixmapsdir/%name.png
%doc BUGS FEATURES LICENSE README

# TODO:
# - figure out whether plain Vera fonts will do
# - or package fonts separately and require them

%changelog
* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.2.2-alt2
- fixed build with gcc 4.3
- created desktop file

* Wed Jul 02 2008 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- built for ALT Linux
- added Russian translation

