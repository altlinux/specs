Name: pdfmixtool
Version: 1.1.1
Release: alt2

License: LGPL-3.0-only
Group: Office
Url: https://www.scarpetta.eu/pdfmixtool

# Source-url: https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%version/pdfmixtool-v%version.tar.gz
Source: %name-%version.tar

Patch: %name-1.1-alt-desktop.patch

BuildRequires: cmake
BuildRequires: libqpdf-devel
BuildRequires: qt6-base-devel

BuildRequires: libnettle-devel
BuildRequires: zlib-devel
BuildRequires: libgnutls-devel
BuildRequires: libtasn1-devel
BuildRequires: libidn2-devel
BuildRequires: libp11-kit-devel

BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: libImageMagick-devel
BuildRequires(pre): rpm-macros-cmake

Summary: PDF Mix Tool is a simple PDF editing application
Summary(ru_RU.UTF-8): PDF Mix Tool - это простое приложение для редактирования PDF-файлов

%description
PDF Mix Tool can perform the following basic operations:
Combine two or more files, specifying a set of pages for each.
Rotate Pages.
Combine multiple pages into one (N-up).
In addition, it can also mix files, interleave their pages, create booklets,
add white pages to PDF file, remove pages from PDF file, extract pages from PDF
file, edit PDF document information.

%description -l ru_RU.UTF-8
PDF Mix Tool может выполнять следующие основные операции:
Объедините два или более файла, указав для каждого набор страниц.
Повернуть страницы.
Объединить несколько страниц в одну (N-up).
Кроме того, он также может смешивать файлы, чередовать их страницы, создавать
буклеты, добавлять белые страницы в файл PDF, удалять страницы из файла
PDF, извлекать страницы из файла PDF, редактировать информацию документа PDF.

%prep
%setup
%autopatch -p2

%build
%cmake -DQT_VERSION=6
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS.md CHANGELOG.md TRANSLATORS.md README.md LICENSE
%_bindir/%name
%_desktopdir/eu.scarpetta.PDFMixTool.desktop
%_iconsdir/hicolor/*/*/eu.scarpetta.PDFMixTool.*
%_datadir/metainfo/eu.scarpetta.PDFMixTool.appdata.xml

%changelog
* Tue Feb 28 2023 Evgeny Chuck <koi@altlinux.org> 1.1.1-alt2
- rebuilted on qt6

* Sat Sep 24 2022 Evgeny Chuck <koi@altlinux.org> 1.1.1-alt1
- new version (1.1.1) with rpmgs script

* Sat Sep 17 2022 Evgeny Chuck <koi@altlinux.org> 1.1-alt2
- Fixed desktop category

* Sat Jun 18 2022 Evgeny Chuck <koi@altlinux.org> 1.1-alt1
- new version (1.1) with rpmgs script

* Sun Feb 13 2022 Evgeny Chuck <koi@altlinux.org> 1.0.2-alt2
- fix License tag (GPLv3 -> LGPL-3.0-only)
- cleanup spec

* Sun Jul 11 2021 Evgeny Chuck <koi@altlinux.org> 1.0.2-alt1
- initial build for ALT Sisyphus
