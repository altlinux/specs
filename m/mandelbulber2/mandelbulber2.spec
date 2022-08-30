%define manualpdf usr/share/doc/mandelbulber2/Mandelbulber_Manual.pdf

Name: mandelbulber2
Version: 2.28
Release: alt2

Summary: 3D fractal visualization tool
Summary(ru_RU.UTF-8): Инструмент 3D фрактальной визуализации

License: GPL-3.0-only
Group: Sciences/Mathematics
Url: https://mandelbulber.com

# Source-url: https://github.com/buddhi1980/mandelbulber2/releases/download/%version/mandelbulber2-%version.tar.gz
Source: %name-%version.tar

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libpng-devel
BuildRequires: libgsl-devel
BuildRequires: liblzo2-devel
BuildRequires: libgomp-devel
BuildRequires: libsndfile-devel
BuildRequires: ImageMagick

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
convert -size 16x16 qt/icons/mandelbulber.png %buildroot%_miconsdir/mandelbulber.png
convert -size 32x32 qt/icons/mandelbulber.png %buildroot%_niconsdir/mandelbulber.png
convert -size 48x48 qt/icons/mandelbulber.png %buildroot%_liconsdir/mandelbulber.png

%files
%doc NEWS README %manualpdf
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_liconsdir/mandelbulber.png
%_miconsdir/mandelbulber.png
%_niconsdir/mandelbulber.png

%changelog
* Tue Aug 30 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt2
- Fixed icon packaging as per policy

* Sat Aug 20 2022 Evgeny Chuck <koi@altlinux.org> 2.28-alt1
- new version (2.28) with rpmgs script
