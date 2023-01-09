%def_enable    man
%def_enable    check

Name:          unpaper
Version:       7.0.0
Release:       alt1
Summary:       unpaper is a post-processing tool for scanned sheets of paper
Summary(ru_RU.UTF-8): программа для обработки страниц после сканирования
License:       GPL-2.0-only and 0BSD and Apache-2.0 and MIT
Group:         Publishing
Url:           http://www.flameeyes.eu/projects/unpaper
Vcs:           git@github.com:unpaper/unpaper.git
Packager:      Vitaly Lipatov <lav@altlinux.ru>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libavformat-devel
%{?_enable_man:BuildRequires: python3-module-sphinx}
%{?_enable_man:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%{?_enable_check:BuildRequires: pytest3}
%{?_enable_check:BuildRequires: python3-module-pytest}
%{?_enable_check:BuildRequires: python3-module-Pillow}

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously created
photocopies. The main purpose is to make scanned book pages better
readable on screen after conversion to PDF or DJVU. unpaper tries to
clean scanned images by removing dark edges that appeared through
scanning or copying on areas outside the actual page content.
The program also tries to detect disaligned centering and rotation
of pages and will automatically straighten each page by rotating it
to the correct angle.

%description -l ru_RU.UTF-8
unpaper — это программа для обработки страниц после сканирования,
особенно в тех случаях, когда была отсканирована фотокопия книги.
Основная её цель есть улучшить читаемость с экрана после преобразования
в форматы PDF и DJVU. Программа unpaper пытается убрать тёмное
окаймление, появляющуюся за пределами содержимого страницы
при сканировании или копировании. Программа также пытается определить
нарушения центровки страниц и их наклон и автоматически выпрямляет
страницы, поворачивая их на соответствующий угол.

%prep
%setup
%ifarch %e2k
sed -i "/-Werror=return-type/d" meson.build
%endif

%build
%meson
%meson_build

%install
%meson_install

%check
export LC_CTYPE=en_US.UTF-8
meson test -C %_target_platform \
   unpaper_tests.py
   
%files
%_bindir/%name
%_man1dir/%name.1.xz
%doc AUTHORS NEWS README.md


%changelog
* Tue Jan 03 2023 Pavel Skrylev <majioa@altlinux.org> 7.0.0-alt1
- ^ 6.1 -> 7.0.0

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt3
- rebuild with ffmpeg 4.0

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt2
- rebuild with ffmpeg

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt1
- new version 6.1 (with rpmrb script)

* Thu Apr 25 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- cleanup spec
- new version 0.4.2 (with rpmrb script)

* Sat May 26 2012 Malo Skryleve <malo@altlinux.org> 0.4-alt2
- Fixed some errors

* Fri May 25 2012 Malo Skryleve <malo@altlinux.org> 0.4-alt1
- updated to version 0.4, changed source host because of a new author

* Thu Jun 26 2008 Yury Aliaev <mutabor@altlinux.org> 0.3-alt1
- version 0.3

* Fri Jun 01 2007 Yury Aliaev <mutabor@altlinux.org> 0.2-alt1
- Initial build
