Name:		qtqr
Version:	1.2
Release:	alt1
Summary:	GUI that makes easy creating and decoding the QR Codes
Summary(ru_RU.UTF8): Графическая оболочка для создания и распознавания QR-кодов
LIcense:	GPLv3
Group:		Graphics
Source:		qr-tools-%version.tar.gz
Source1:	qtqr_ru.ts
URL:		https://launchpad.net/qr-tools
BuildArch:	noarch

%setup_python_module qrtools

Requires:	qrencode

BuildRequires: libqt4-devel

# Automatically added by buildreq on Fri May 18 2012
# optimized out: fontconfig libgdk-pixbuf libqt4-core libqt4-devel libqt4-xml libwayland-client libwayland-server python-base
BuildRequires: ImageMagick-tools

%description
QtQR is a Qt based software that let's you generate QR Codes easily,
scan an image file for QR Codes and decode them or use your webcam to
scan a printed one.

%description -l ru_RU.UTF8
QtQR - графическая оболочка, позволяющая генерировать и распознавать
QR-коды, в том числе на изображенийях, полученных с веб-камеры.

%package -n %packagename
Group:		Development/Python
Summary:	Backend module for QtQR

%description -n %packagename
Python-qrtools is a backend ("library") for creating and decoding QR
Codes in python. Depends on qrenconde and zbar. You can use it in your
own projects

%description -n %packagename -l ru_RU.UTF8
Python-qrtools - модуль на языке программирования Python,
предоставляющий функции генерации и распознавания QR-кодов. Для
генерации используется qrenconde, для распознавания - zbar.

%prep
%setup -n qr-tools
for N in 16 24 32 48 128; do convert logo_a_la_faenza.svg $N.png; done

cat > %name.desktop <<@@@
[Desktop Entry]
Name=QtQR
Name[ru]=QtQR
GenericName=QR Code utility
GenericName[ru]=Работа с QR-кодами
Comment=QtQR is a Qt based software that let's you generate QR Codes easily, scan an image file for QR Codes and decode them or use your webcam to scan a printed one.
Comment[ru]=Графическая оболочка для создания и распознавания QR-кодов
Exec=qtqr
Icon=qtqr
Terminal=false
Type=Application
Categories=Graphics
@@@

cat > %name.sh <<@@@
#!/bin/sh
exec /usr/bin/python %_bindir/%name.py "\$@"
@@@

%build
# TODO check translation
lconvert-qt4 %SOURCE1 -o qtqr_ru.qm

%install
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D icon.png %buildroot%_pixmapsdir/%name.png
for N in 16 24 32 48 128; do
  install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done
install -D logo_a_la_faenza.svg buildroot%_iconsdir/hicolor/scalable/%name.svg
mkdir -p %buildroot%_datadir/qt4/translations
install %{name}_*.qm %buildroot%_datadir/qt4/translations/
install -D qrtools.py %buildroot%python_sitelibdir_noarch/%modulename.py
install -D %name.py %buildroot%_bindir/%name.py
install -D %name.sh %buildroot%_bindir/%name

%files
%doc samples
%_bindir/*
%_pixmapsdir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/qt4/translations/*

%files -n %packagename
%python_sitelibdir_noarch/%modulename.py


%changelog
* Fri May 18 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch
- Russian translation added

