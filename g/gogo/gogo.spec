Name: gogo
Version: 3.13
Release: alt5

Summary: Fast MP3 encoder optimized for 3DNow! and SSE
Summary(ru_RU.UTF-8): улучшенный для 3DNow! и SSE кодировщик mp3
License: LGPL
Group: Sound
Url: http://homepage2.nifty.com/kei-i/
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar.bz2
Patch: %name-%version-alt1-fix-floating-point.patch

BuildRequires: nasm

ExclusiveArch: i586 i686

%description
GOGO is a mp3 encoder based on lame3.88beta and optimized
by PEN@MarineCat, Keiichi SAKAI, URURI, kei and shigeo.

GOGO makes use of MMX, 3D Now! Enhanced 3D Now!, SSE and SSE2
if your system supports these instructions.

%description -l ru_RU.UTF-8
Gogo есть кодировщик mp3 на основе LAME 3.9x, оптимизированный группою
разработчиков: Пен@морекот, Кеиши Сакаи, Уриру, Кеи и Шигео. Gogo будет
использовать инструкции MMX, 3D Now! Enhanced 3D Now!, SSE и SSE2,
если на вашея системе они поддерживаются.

%prep
%setup
%patch -p2

%build
%configure
cd linux
%make_build

%install
cd linux
mkdir -p %buildroot%_bindir
install -s gogo %buildroot%_bindir

%files
%doc COPYING history readme.html readme_e.html contrib/cdda2mp3/* contrib/aircheck/*
%_bindir/*

%changelog
* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 3.13-alt5
- Removed rpmwrap dependency from the spec

* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 3.13-alt4
- Fixed spec file

* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 3.13-alt3
- Set build arch only to i586 and i686

* Wed Mar 30 2011 Malo Skryleve <malo@altlinux.org> 3.13-alt2
- Added patch, and fixed spec file

* Wed Mar 16 2011 Malo Skryleve <malo@altlinux.org> 3.13-alt1
- initial build for ALT Linux Sisyphus

