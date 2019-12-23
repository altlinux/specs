Name:		qtqr
Version:	2.0
Release:	alt1
Summary:	GUI that makes easy creating and decoding the QR Codes
Summary(ru_RU.UTF8): Графическая оболочка для создания и распознавания QR-кодов
LIcense:	GPLv3
Group:		Graphics
Source:		qr-tools-%version.tar
Source1:	qtqr.desktop
Patch1:		01_setup_script.patch
Patch2:		02_no_crash_on_bad_input.patch

URL:		https://launchpad.net/qr-tools
BuildArch:	noarch

Requires:	qrencode

# Automatically added by buildreq on Mon Dec 23 2019
# optimized out: fontconfig libqt5-core libqt5-xml python-modules python2-base python3 python3-base sh4
BuildRequires: ImageMagick-tools python3-dev qt5-tools

%description
QtQR is a Qt based software that let's you generate QR Codes easily,
scan an image file for QR Codes and decode them or use your webcam to
scan a printed one.

%description -l ru_RU.UTF8
QtQR - графическая оболочка, позволяющая генерировать и распознавать
QR-коды, в том числе на изображенийях, полученных с веб-камеры.

%package -n python3-module-qrtools
Group:		Development/Python3
Summary:	Backend module for QtQR
Requires: python3(PIL)

%description -n python3-module-qrtools
Python-qrtools is a backend ("library") for creating and decoding QR
Codes in python. Depends on qrenconde and zbar. You can use it in your
own projects

%description -n python3-module-qrtools -l ru_RU.UTF8
Python-qrtools - модуль на языке программирования Python,
предоставляющий функции генерации и распознавания QR-кодов. Для
генерации используется qrenconde, для распознавания - zbar.

%prep
%setup -n qr-tools-%version
%patch1 -p1
%patch2 -p1
cp %SOURCE1 .

for N in 16 24 32 48 128; do convert logo_a_la_faenza.svg -resize ${N}x${N} $N.png; done

%build
%python3_build
for n in *.ts; do lrelease-qt5 -nounfinished $n -qm ${n%%.ts}.qm; done

%install
%python3_install
install -m755 -D qtqr.py %buildroot%_bindir/qtqr
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D icon.png %buildroot%_pixmapsdir/%name.png
for N in 16 24 32 48 128; do
  install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done
install -D logo_a_la_faenza.svg buildroot%_iconsdir/hicolor/scalable/%name.svg

mkdir -p %buildroot%_datadir/qt5/translations
install *.qm %buildroot%_datadir/qt5/translations/

%files
%doc samples
%_bindir/*
%_pixmapsdir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/qt5/translations/*

%files -n python3-module-qrtools
%python3_sitelibdir_noarch/qrtools*
%python3_sitelibdir_noarch/__pycache__/*.py*


%changelog
* Mon Dec 23 2019 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Switch to Pyton3
- Switch tp Qt5

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 1.2-alt3
- Correct icons size

* Mon Dec 22 2014 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Fix translation
- Fix new PIL import syntax

* Fri May 18 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch
- Russian translation added

