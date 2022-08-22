Name: fsearch
Version: 0.2.2
Release: alt1

Summary: A fast file search utility for Unix-like systems based on GTK+3
Summary(ru_RU.UTF-8): Утилита для быстрого поиска файлов на основе GTK+3

License: GPL-2.0-only
Group: File tools
Url: http://cboxdoerfer.github.io/fsearch

# Source-url: https://github.com/cboxdoerfer/fsearch/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: libpcre2-devel
BuildRequires: gettext-tools
BuildRequires: libpango-devel
BuildRequires: libcairo-devel
BuildRequires: libgtk+3-devel
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: libpcre-devel
BuildRequires: libicu-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires(pre): rpm-macros-meson

%description
FSearch is a fast file search utility, inspired by Everything Search Engine.
It's written in C and based on GTK3.

Functions:
Instant (as you type) results.
Support for wildcard symbols.
Regular expression support.
Filter support.
Include and exclude specific folders for indexing.
Ability to exclude certain files/folders from the index using wildcard
expressions.
Quick sort by file name, path, size or modification time.
Customizable interface.

%description -l ru_RU.UTF-8
FSearch - это быстрая утилита для поиска файлов, созданная на основе движка
"Everything". Она написана на C и использует графическую библиотеку GTK3.

Функции:
Мгновенные (по мере ввода) результаты.
Поддержка подстановочных символов.
Поддержка регулярных выражений.
Поддержка фильтров.
Включать и исключать определенные папки для индексации.
Возможность исключать из индекса определенные файлы/папки с помощью
подстановочных выражений.
Быстрая сортировка по имени файла, пути, размеру или времени модификации.
Настраиваемый интерфейс.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md NEWS
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_man1dir/%name.1.*
%_datadir/metainfo/*.xml

%changelog
* Mon Aug 22 2022 Evgeny Chuck <koi@altlinux.org> 0.2.2-alt1
- new version (0.2.2) with rpmgs script

* Thu Aug 18 2022 Evgeny Chuck <koi@altlinux.org> 0.2.1-alt1
- new version (0.2.1) with rpmgs script

* Tue Aug 16 2022 Evgeny Chuck <koi@altlinux.org> 0.2-alt1
- new version (0.2) with rpmgs script

* Sun Jul 10 2022 Evgeny Chuck <koi@altlinux.org> 0.1.4-alt1
- new version (0.1.4) with rpmgs script

* Thu Jun 23 2022 Evgeny Chuck <koi@altlinux.org> 0.1.3-alt1
- new version (0.1.3) with rpmgs script

* Mon Feb 28 2022 Evgeny Chuck <koi@altlinux.org> 0.1.2-alt1
- initial build for ALT Linux Sisyphus
