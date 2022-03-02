Name: fsearch
Version: 0.1.2
Release: alt1

Summary: A fast file search utility for Unix-like systems based on GTK+3
Summary(ru_RU.UTF-8): Утилита для быстрого поиска файлов на основе GTK+3

License: GPL-2.0-only
Group: File tools
Url: http://cboxdoerfer.github.io/fsearch

# Source-url: https://github.com/cboxdoerfer/fsearch/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
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

%description
FSearch is a fast file search utility, inspired by Everything Search Engine.
It's written in C and based on GTK3.

%description -l ru_RU.UTF-8
FSearch - это быстрая утилита для поиска файлов, созданная на основе движка 
"Everything". Она написана на C и использует графическую библиотеку GTK3.

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
* Mon Feb 28 2022 Evgeny Chuck <koi@altlinux.org> 0.1.2-alt1
- initial build for ALT Linux Sisyphus
