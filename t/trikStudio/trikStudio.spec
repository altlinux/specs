%define rev 30210b3a
Name: trikStudio
Version: 3.1.3
Release: alt0.1.%rev
Summary: Intuitive programming environment robots
Summary(ru_RU.UTF-8): Интуитивно-понятная среда программирования роботов
License: Apache License 2.0
Group: Education
Url: https://github.com/qreal/qreal/
#branch alt-linux
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar.gz

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel libusb-devel libgmock-devel libudev-devel

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

%prep
%setup

%build
%qmake_qt5 -r CONFIG-=debug CONFIG+=release CONFIG+=no_rpath PREFIX=/usr qrealRobots.pro
#%%qmake_qt5 -r 'QMAKE_CXXFLAGS=-pipe -Wall -g -O2 -fPIC -DPIC -std=c++0x' CONFIG-=debug CONFIG+=no_rpath CONFIG+=release qrealRobots.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install 

%files
%_bindir/%name
%_sysconfdir/%name.conf
%_libdir/*.so*
%_libdir/%name
%_datadir/%name
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*
#doc COPYING README.md

%changelog
* Fri Mar 18 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt0.1.30210b3a
- Initial build for ALT Linux Sisyphus (Closes: 31733).
