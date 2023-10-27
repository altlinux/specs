Name: xfishtank
Version: 3.2.1pre1
Release: alt2

Summary:  An aquarium for your screen, with fish swimming around on your desktop.
License: GPLv3+
Group: Toys

Url: https://www.ratrabbit.nl/ratrabbit/software/xfishtank/index.html
Source: %name-%version.tar.gz
Packager: Alexei Mezin <alexvm@altlinux.org>

Summary(ru_RU.UTF8):  Аквариум на вашем рабочем столе.

Patch0: rus_descr.patch

BuildRequires: libXpm-devel libXt-devel libgtk+3-devel libxml2-devel libdbus-devel gcc-c++ 
BuildRequires: ImageMagick-tools libXinerama-devel libxkbcommon-devel libXtst-devel desktop-file-utils


%description
Xfishtank is a modern clone of well-known vintage application called xfish. It shows fishes swimming over the desktop.

%description -l ru_RU.UTF8
Xfishtank это современная версия винтажного приложения xfish. Программа создает аквариум на рабочем столе.

%prep
%setup
%patch0 -p1


%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# create 48x48 pixmap and put icons according to the Policy, see https://www.altlinux.org/Icon_Paths_Policy
convert -resize 48x48 src/%name.png %name.png
install -m 755 -d %buildroot/%_liconsdir/
install -m 644 %name.png %buildroot/%_liconsdir/
# fix Category
desktop-file-install --dir %buildroot/%_desktopdir \
    --add-category=Amusement %buildroot/%_desktopdir/%name.desktop

%files
%doc README
%_gamesbindir/*
%_man1dir/*
%_liconsdir/%name.*
%_desktopdir/*
 
%changelog
* Fri Oct 27 2023 Michael Shigorin <mike@altlinux.org> 3.2.1pre1-alt2
- Re-added explicit BR: desktop-file-utils

* Wed Oct 25 2023 Alexei Mezin <alexvm@altlinux.org> 3.2.1pre1-alt1
- New version

* Sun Jan 16 2022 Michael Shigorin <mike@altlinux.org> 3.1.1-alt1.1
- Added explicit BR: desktop-file-utils (older libgio didn't pull it in)

* Sat Jan 15 2022 Alexei Mezin <alexvm@altlinux.org> 3.1.1-alt1
- New version

* Sun Dec 05 2021 Alexei Mezin <alexvm@altlinux.org> 3.0.0-alt2
- Fix packaging error
- Minor spec cleanup

* Sat Dec 04 2021 Alexei Mezin <alexvm@altlinux.org> 3.0.0-alt1
- Initial build
