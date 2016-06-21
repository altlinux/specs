%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist  %_libdir/trikStudio/*.so* %_libdir/trikStudio/plugins/tools/kitPlugins/*.so %_libdir/trikStudio/plugins/tools/*.so %_libdir/trikStudio/plugins/editors/*.so
%define rev 91af0cec
Name: trikStudio
Version: 3.1.3
Release: alt5.%rev.1
Summary: Intuitive programming environment robots
Summary(ru_RU.UTF-8): Интуитивно-понятная среда программирования роботов
License: Apache License 2.0
Group: Education
Url: https://github.com/qreal/qreal/

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar.gz
Patch1: install.patch

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel libusb-devel libudev-devel libgmock-devel

Requires: %name-data = %version-%release
Conflicts: lib%name

%description
Intuitive programming environment allows you to program robots using a sequence
of pictures. With TRIK Studio programming is easy and fun.

TRIK Studio perfectly as universal for teaching programming, provided the
transition from the chart to the textual programming language that is planned to
implement the language of block diagrams. The environment is also implemented
programming robots Lego Mindsorms NXT 2.0 and EV3, but the possibility of such
robots are very limited in comparison with the TRIC .

%description -l ru_RU.UTF-8
Интуитивно-понятная среда программирования позволяет программировать роботов с
помощью последовательности картинок. С TRIK Studio программирование становится
простым и увлекательным.

TRIK Studio прекрасно подходит как универсальное ПО преподавания основ
программирования, предусмотрен переход от диаграмм к текстовым языкам
программирования, планируется реализация языка блок-схем. В среде также
реализовано программирование роботов Lego Mindsorms NXT 2.0 и EV3, но
возможности таких роботов сильно ограничены в сравнении с ТРИК.

%package data
Summary: Data files for %name
Group: Education
BuildArch: noarch

%description data
Data files for %name

%prep
%setup
%patch1
sed -e '2 a export LD_LIBRARY_PATH=%_libdir\/trikStudio\/' -i installer/platform/trikStudio.sh

%build
%qmake_qt5 -r CONFIG-=debug CONFIG+=release CONFIG+=no_rpath PREFIX=/usr qrealRobots.pro
#%%qmake_qt5 -r 'QMAKE_CXXFLAGS=-pipe -Wall -g -O2 -fPIC -DPIC -std=c++0x' CONFIG-=debug CONFIG+=no_rpath CONFIG+=release PREFIX=/usr qrealRobots.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
mv %buildroot%_libdir/*.so* %buildroot%_libdir/%name

%files
%_bindir/*
%_libdir/%name
%_sysconfdir/%name.config

%files data
%_datadir/%name
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*
%doc LICENSE NOTICE README.md

%changelog
* Tue Jun 21 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt5.91af0cec.1
- New snapshot
- Replaced library
- Packages libtrikStudio, libtrikStudio-devel united into a package trikStudio.

* Sat Mar 26 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt4.30210b3a.1
- Move config file from package trikStudio-data in package trikStudio
- Added conflict with libqscintilla2-qt4-devel.

* Wed Mar 23 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt3.30210b3a.1
- fix install.patch

* Wed Mar 23 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2.30210b3a.1
- new package libtrikStudio
- rename package trikStudio-devel to libtrikStudio-devel

* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1.30210b3a.1
- Fix altlinux-policy-shared-lib-contains-devel-so
- Exclude libqextserialport (it has in the repository)
- Diveded into 3 package

* Fri Mar 18 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt0.1.30210b3a
- Initial build for ALT Linux Sisyphus (Closes: 31733).
