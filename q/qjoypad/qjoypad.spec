Name: qjoypad
Version: 4.1.0
Release: alt4

Summary: A joystick-keyboard mapper
Summary(ru_RU.UTF-8): Программа для превращения событий джойстика в события клавиатуры
License: %gpl2only
Group: Games/Other
Url: http://downloads.sourceforge.net/qjoypad/qjoypad-4.1.0.tar.gz

Packager: Yuriy Al. Shirokov <yushi@altlinux.org>
Source0: %name-%version.tar
Source1: qjoypad.desktop
Patch0: %name-4.1.0-alt-configure-fixes.patch

Requires: libqt4-core
Requires(post,postun): desktop-file-utils

# Automatically added by buildreq on Wed Sep 15 2010
BuildRequires(pre): rpm-build-licenses, desktop-file-utils
BuildRequires: gcc-c++ libX11-devel libXtst-devel libqt4-devel ImageMagick-tools

%description
QJoyPad is a simple Linux/QT program that lets you use your gaming devices
where you want them: in your games! QJoyPad takes input from a gamepad or
joystick and translates it into key strokes or mouse actions, letting you
control any XWindow program with your game controller. QJoyPad also gives
you the advantage of multiple saved layouts so you can have a separate setting
for every game, or for every class of game!

%description -l ru_RU.UTF-8
QJoyPad -- это простая программа для Linux на Qt, которая позволит наконец
применить ваш джойстик по назначению -- для управления играми! QJoyPad превращает
нажатия на геймпад или джойстик в коды клавиатуры или движения мыши, так что
вы теперь можете управлять с помощью игрового контроллера любой программой для
X Window System. QJoyPad поддерживает несколько вариантов привязок, так что вы
можете хранить разные настройки для каждой игры или типа игр.

%prep
%setup
%patch0 -p1

%build
cd src
export PATH=$PATH:%_qt4dir/bin
./configure --prefix=%_prefix --install-dir=%buildroot
%make_build

%install
%makeinstall_std -C src
# Desktop file installation
%__install -D -m 644 %SOURCE1 $RPM_BUILD_ROOT%_desktopdir/%name.desktop
# Icons (tnx to drool@altlinux.ru)
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %buildroot/%_pixmapsdir/%name/gamepad4-64x64.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %buildroot/%_pixmapsdir/%name/gamepad4-64x64.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 %buildroot/%_pixmapsdir/%name/gamepad4-64x64.png %buildroot%_miconsdir/%name.png

%files
%doc README.txt
%exclude %_docdir
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Tue Sep 21 2010 Yuriy Al. Shirokov <yushi@altlinux.org> 4.1.0-alt4
- Spec error fixed.

* Tue Sep 21 2010 Yuriy Al. Shirokov <yushi@altlinux.org> 4.1.0-alt3
- System icons added.

* Sun Sep 19 2010 Yuriy Al. Shirokov <yushi@altlinux.org> 4.1.0-alt2
- Desktop file added; spec cleanup.

* Mon Sep 13 2010 Yuriy Al. Shirokov <yushi@altlinux.org> 4.1.0-alt1
- Packaged for ALT Linux
