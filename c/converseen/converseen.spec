Name: converseen
Version: 0.9.11.1
Release: alt1
Summary: Converseen is a free cross-platform batch image processor
Summary(ru_RU.UTF-8): Converseen — свободная программа пакетного конвертирования изображений
License: GPLv3
Group: Graphics
Url: http://converseen.fasterland.net/
BuildRequires(pre): rpm-macros-cmake
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ImageMagick-tools
BuildRequires: libImageMagick-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-phonon-devel
BuildRequires: qt5-designer
BuildRequires: qt5-tools-devel

Source: %name-%version.tar

Requires: ImageMagick-tools

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
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %buildroot/%_desktopdir/net.fasterland.converseen.desktop

%files
%doc COPYING
%_bindir/%name
%_datadir/%name
%_datadir/kservices5/ServiceMenus/converseen_import.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/net.fasterland.converseen.desktop
%_datadir/metainfo/%name.appdata.xml

%changelog
* Mon Aug 14 2023 Anton Midyukov <antohami@altlinux.org> 0.9.11.1-alt1
- New version 0.9.11.1.

* Thu Jul 21 2022 Anton Midyukov <antohami@altlinux.org> 0.9.9.6-alt1
- new version 0.9.9.6

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 0.9.9.0-alt1
- new version 0.9.9.0

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 0.9.8.1-alt1
- new version 0.9.8.1

* Tue Nov 19 2019 Anton Midyukov <antohami@altlinux.org> 0.9.8.0-alt1
- new version 0.9.8.0

* Sun Aug 18 2019 Anton Midyukov <antohami@altlinux.org> 0.9.7.2-alt2
- Add missing Requires: ImageMagick-tools

* Mon Nov 26 2018 Anton Midyukov <antohami@altlinux.org> 0.9.7.2-alt1
- new version 0.9.7.2

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 0.9.6.2-alt3
- Rebuilt for libImageMagick.

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 0.9.6.2-alt2
- Rebuilt for libImageMagick

* Wed May 31 2017 Anton Midyukov <antohami@altlinux.org> 0.9.6.2-alt1
- new version 0.9.6.2

* Sat Dec 17 2016 Anton Midyukov <antohami@altlinux.org> 0.9.5.2-alt1
- new version 0.9.5.2

* Thu Sep 01 2016 Anton Midyukov <antohami@altlinux.org> 0.9.5-alt1
- New version 0.9.5
- Remove converseen_fix_desktop-file.patch.

* Sun Apr 03 2016 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt3
- Added loop to change the size of the icon
- Added converseen_fix_desktop-file.patch.

* Thu Aug 27 2015 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt2
- Fix encoding in description.

* Thu Aug 20 2015 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux Sisyphus (Closes: 31215).
