Name: converseen
Version: 0.9.2
Release: alt2
Summary: Converseen is a free cross-platform batch image processor.
Summary(ru_RU.UTF-8): Converseen — свободная программа пакетного конвертирования изображений.
License: GPLv3
Group: Graphics
Url: http://converseen.fasterland.net/
BuildRequires: desktop-file-utils
# Automatically added by buildreq on Thu Aug 20 2015
# optimized out: cmake-modules fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-webkit-devel libstdc++-devel pkg-config
BuildRequires: ImageMagick-tools cmake gcc-c++ libImageMagick-devel phonon-devel qt4-designer
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-0.9.2.tar.bz2

%description
Converseen is a free cross-platform batch image processor for Windows and Linux
that allows you to convert, resize, rotate and flip an infinite number of
images with a mouse click.
Moreover, Converseen is able to transform an entire PDF file into a bunch
of images with the characteristics you prefer: you can choose one of the 100+
formats, you can set the size, resolution and the filename.

%description -l ru_RU.UTF-8
Converseen — свободная кроссплатформенная программа для Windows и Linux 
для пакетного конвертирования, изменения размера, поворота изображений в один
клик.
Кроме того, Converseen способен преобразовать вашу коллекцию изображений в PDF
файл с характеристиками, которые вы предпочитаете: вы можете выбрать один из
более чем 100 форматов, установить размер, разрешение и имя файла.

%prep
%setup -n %name-%version

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
%make_build

%install
%make_install DESTDIR=%buildroot install
desktop-file-validate %buildroot/%_desktopdir/%name.desktop

%files
%doc COPYING
%_bindir/%name
%_datadir/%name/*
%_datadir/kde4/services/ServiceMenus/converseen_import.desktop
%_datadir/pixmaps/%name.png
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml

%changelog
* Thu Aug 27 2015 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt2
- Fix encoding in description

* Thu Aug 20 2015 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux Sisyphus (Closes: 31215).
