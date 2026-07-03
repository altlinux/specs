Name: schismtracker
Version: 20260524
Release: alt1

Summary: Schism Tracker is a free and open-source reimplementation of Impulse Tracker
License: GPLv2
Group: Sound

Url: https://schismtracker.org/
VCS: https://github.com/schismtracker/schismtracker
Packager: Alexei Mezin <alexvm@altlinux.org>

##Source0: xsnow-%version.tar.gz
Source: %name-%version.tar.gz

Summary(ru_RU.UTF8): Schism Tracker это свободная реализация программы Impulse Tracker

BuildRequires: libSDL-devel libSDL2-devel libavformat-devel libflac-devel zlib-devel libutf8proc-devel
BuildRequires: perl-Encode python3-module-setuptools

%description
Schism Tracker is a free and open-source reimplementation of Impulse Tracker, 
a program used to create high quality music without the requirements of specialized, 
expensive equipment.

Where Impulse Tracker was limited to i386-based systems running MS-DOS, 
Schism Tracker runs on almost any platform that SDL2 supports.

%description -l ru_RU.UTF8
Schism Tracker это свободная реализация программы Impulse Tracker, которая используется
для создания качественной музыки без привлечения специализированного и дорогого оборудования.

В отличие от оригинального Impulse Tracker, который работало только под MS-DOS, это
программа работает на всех платформах, которые поддерживаются библиотекой SDL2.


%prep
%setup

# fix Categories
##%__subst 's|Categories=Game;|Categories=Game;Amusement;|' data/xsnow.desktop.in

%build
%autoreconf
%configure --prefix=/usr --with-sdl2
%make

%install
%makeinstall_std

# remove installed icon
rm -f  %buildroot/usr/share/pixmaps/schism-icon-128.png

# manually install icons

# 48x48 pixmap requred by Policy, see https://www.altlinux.org/Icon_Paths_Policy
install -m 755 -d %buildroot/%_liconsdir/
install -m 644 icons/schism-icon-48.png %buildroot/%_liconsdir/%name.png

# install other icon sizes
install -m 755 -d %buildroot/%_iconsdir/hicolor/128x128/apps
install -m 644 icons/schism-icon-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/%name.png

install -m 755 -d %buildroot/%_iconsdir/hicolor/64x64/apps
install -m 644 icons/schism-icon-64.png %buildroot/%_iconsdir/hicolor/64x64/apps/%name.png

install -m 755 -d %buildroot/%_iconsdir/hicolor/96x96/apps
install -m 644 icons/schism-icon-96.png %buildroot/%_iconsdir/hicolor/96x96/apps/%name.png


# rename desktop file
rename schism %name %buildroot/%_desktopdir/schism.desktop

# fix icon name in desktop file
desktop-file-edit --set-icon=%name %buildroot/%_desktopdir/%name.desktop


%files
%doc README.md
%_bindir/*
%_man1dir/*
%_liconsdir/%name.*
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/*
 
%changelog
* Fri Jul 03 2026 Alexei Mezin <alexvm@altlinux.org> 20260524-alt1
- New version

* Sun Jan 04 2026 Alexei Mezin <alexvm@altlinux.org> 20251014-alt1
- Initial build

