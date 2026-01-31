%define oname PhotoFilmStrip

%def_with check

Name: photofilmstrip
Version: 4.2.1
Release: alt1

Summary: PhotoFilmStrip creates movies out of your pictures
Summary(ru_RU.UTF-8): PhotoFilmStrip создает фильмы из фотографий

License: GPL-2.0
Group: Video
URL: https://www.photofilmstrip.org
VCS: https://github.com/PhotoFilmStrip/PFS

Packager: Alexander Kovalev <alexvk@altlinux.org>

Source: %name-%version.tar
# fix russian translation
Source1: ru.po
Source2: %name.desktop

Requires: libges-gir
Requires: python3-module-%name = %EVR

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: libges-gir
BuildRequires: python3-module-wx
%endif

%description
PhotoFilmStrip creates movies out of your pictures in just 3 steps.
First select your photos, customize the motion path and render the video.
There are several output possibilities for VCD, SVCD, DVD up to FULL-HD.

%description -l ru_RU.UTF-8
PhotoFilmStrip создает фильмы из фотографий всего за 3 шага.
Выберите фотографии, настройте траекторию движения и сделайте видео.
Есть несколько возможностей вывода видео: от VCD, SVCD, DVD до Full-HD.

%package -n python3-module-%name
Summary: Python module for %oname
Summary(ru_RU.UTF-8): Python-модуль для %oname
Group: Development/Python3
BuildArch: noarch
Conflicts: %name < %EVR

%description -n python3-module-%name
PhotoFilmStrip creates movies out of your pictures in just 3 steps.
First select your photos, customize the motion path and render the video.
There are several output possibilities for VCD, SVCD, DVD up to FULL-HD.

This package contains Python module for %oname.

%description -n python3-module-%name -l ru_RU.UTF-8
PhotoFilmStrip создает фильмы из фотографий всего за 3 шага.
Выберите фотографии, настройте траекторию движения и сделайте видео.
Есть несколько возможностей вывода видео: от VCD, SVCD, DVD до Full-HD.

Этот пакет содержит Python-модуль для %oname.

%prep
%setup
cp -a %SOURCE1 po
cp -a %SOURCE2 data

%build
%pyproject_build

%make -C docs/help man

%install
%pyproject_install

mkdir -p %buildroot%_man1dir
install -m0644 docs/help/_build/man/%name.1 %buildroot%_man1dir
# remove the sphinx-build leftovers
rm -rv %buildroot%_docdir/%name/html/objects.inv

%find_lang %oname

%check
%pyproject_run_pytest

%files -f %oname.lang
%doc README LICENSE COPYING
%_bindir/%name
%_bindir/%name-cli
%_datadir/%name
%_datadir/pixmaps/%name.xpm
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_docdir/%name
%_man1dir/*

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Fri Jan 30 2026 Alexander Kovalev <alexvk@altlinux.org> 4.2.1-alt1
- Initial build for ALT.
- Updated russian translation.
