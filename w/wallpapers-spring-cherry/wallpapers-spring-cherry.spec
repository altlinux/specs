%define photos_dir %_datadir/wallpapers
%define wname spring-cherry

Name: wallpapers-%wname
Version: 20090517
Release: alt2

Summary: Blooming spring cherry trees for screen backgrounds
Summary(ru_RU.UTF-8): Цветущие весенние вишни для обоев на рабочий стол
License: %ccbysa30
Group: Graphics

Source: %name-%version.tar
Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildArch: noarch
Provides: %name = %version-%release
Obsoletes: %name < %version-%release

BuildPreReq: rpm-build-licenses >= 1.0.1-alt1

%description
Photo images of blooming spring cherry trees for screen backgrounds.
Includes versions for standard and wide screens.

%description -l ru_RU.UTF-8
Фотографии цветущих весенних вишен для обоев на рабочий стол.
Включает версии как для стандартных, так и для широких экранов.

%package standard-screen
Summary: Blooming spring cherry trees for screen backgrounds
Summary(ru_RU.UTF-8): Цветущие весенние вишни для обоев на рабочий стол
License: %ccbysa30
Group: Graphics
Provides: %name-standard-screen = %version-%release
Obsoletes: %name-standard-screen < %version-%release

%description standard-screen
Photo images of blooming spring cherry trees for screen backgrounds.
Version for standard 4:3 screen.

%description standard-screen -l ru_RU.UTF-8
Фотографии цветущих весенних вишен для обоев на рабочий стол.
Версия для стандартного экрана 4:3.

%package widescreen
Summary: Blooming spring cherry trees for screen backgrounds
Summary(ru_RU.UTF-8): Цветущие весенние вишни для обоев на рабочий стол
License: %ccbysa30
Group: Graphics
Provides: %name-widescreen = %version-%release
Obsoletes: %name-widescreen < %version-%release

%description widescreen
Photo images of blooming spring cherry trees for screen backgrounds.
Version for wide 16:10 screen.

%description widescreen -l ru_RU.UTF-8
Фотографии цветущих весенних вишен для обоев на рабочий стол.
Версия для широкого экрана 16:10.

%prep
%setup

%build

%install
mkdir -p %buildroot/%photos_dir/%wname/{1600x1200,1920x1200}
install -m 0644 1600x1200/*.jpg %buildroot%photos_dir/%wname/1600x1200
install -m 0644 1920x1200/*.jpg %buildroot%photos_dir/%wname/1920x1200

%files standard-screen
%photos_dir/%wname/1600x1200/*.jpg

%files widescreen
%photos_dir/%wname/1920x1200/*.jpg

%changelog
* Thu May 21 2009 Paul Wolneykien <manowar@altlinux.ru> 20090517-alt2
- Initial build for ALT Linux.
