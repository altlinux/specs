%define manualpdf usr/share/doc/mandelbulber2/Mandelbulber_Manual.pdf

Name: mandelbulber2
Version: 2.29
Release: alt1

Summary: 3D fractal visualization tool
Summary(ru_RU.UTF-8): Инструмент 3D фрактальной визуализации

License: GPL-3.0-only
Group: Sciences/Mathematics
Url: https://mandelbulber.com

# Source-url: https://github.com/buddhi1980/mandelbulber2/releases/download/%version/mandelbulber2-%version.tar.gz
Source: %name-%version.tar

# russian language files
Source1: ru.tar

Patch1: %name-2.28-alt-add_language_ru.patch
Patch2: %name-2.28-alt-desktop.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libpng-devel
BuildRequires: libgsl-devel
BuildRequires: liblzo2-devel
BuildRequires: libgomp-devel
BuildRequires: libsndfile-devel
BuildRequires: /usr/bin/convert

BuildRequires(pre): rpm-macros-qt5

%description
Mandelbulber2 is an easy-to-use, user-friendly yet experimental application
for visualizing 3D Mandelbrot fractals. Mandelbulber2 provides a wide range of
effects such as: Complex 3D shading: hard shadows, background occlusion,
ambient overlay, fog, depth of field. Also includes a video editor and
keyframe animation of all floating point options.

%description -l ru_RU.UTF-8
Mandelbulber2 — это простое в использовании, удобное, но экспериментальное
приложение для визуализации трехмерных фракталов Мандельброта. Mandelbulber2
предоставляет широкий спектр эффектов, таких как: Комплексное трехмерное
затенение: жесткие тени, окклюзия фона, окружающее наложение, туман, глубина
резкости. Также включает видеоредактор и анимацию ключевых кадров всех
параметров с плавающей запятой.

%prep
%setup
%autopatch -p2

# Correct doc directory name
sed -i "s|doc/%name|doc/%name-%version|g" src/system.cpp

%build
pushd makefiles
%qmake_qt5 mandelbulber.pro
%make_build
popd

%install
mkdir -p %buildroot%_datadir/%name
cp -a usr/share/%name/* %buildroot%_datadir/%name
install -D -m 755 makefiles/%name %buildroot%_bindir/%name
install -D -m 644 %name.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 qt/icons/mandelbulber.png %buildroot%_miconsdir/mandelbulber.png
convert -resize 32x32 qt/icons/mandelbulber.png %buildroot%_niconsdir/mandelbulber.png
convert -resize 48x48 qt/icons/mandelbulber.png %buildroot%_liconsdir/mandelbulber.png

tar -xf %SOURCE1 -C %buildroot%_datadir/%name/language/ --strip-components=1
lconvert-qt5 %buildroot%_datadir/%name/language/ru.ts -o %buildroot%_datadir/%name/language/ru.qm
lconvert-qt5 %buildroot%_datadir/%name/language/formula_ru.ts -o %buildroot%_datadir/%name/language/formula_ru.qm

%files
%doc NEWS README %manualpdf
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_liconsdir/mandelbulber.png
%_miconsdir/mandelbulber.png
%_niconsdir/mandelbulber.png

%changelog
* Wed Apr 19 2023 Evgeny Chuck <koi@altlinux.org> 2.29-alt1
- new version (2.29) with rpmgs script

* Sat Sep 17 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt5
- Fixed desktop category

* Sun Sep 04 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt4
- Russian translation fix

* Wed Aug 31 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt3
- Added Russian localization

* Tue Aug 30 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt2
- Fixed icon packaging as per policy

* Sat Aug 20 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt1
- new version (2.28) with rpmgs script
