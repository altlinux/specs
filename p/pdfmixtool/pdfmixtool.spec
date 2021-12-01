Name: pdfmixtool
Version: 1.0.2
Release: alt1

License: GPLv3
Group: Office
Url: https://www.scarpetta.eu/pdfmixtool
Packager: Evgeny Chuck <koi at altlinux.org>

Source: %name-%version.tar
# Source-url: https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%version/pdfmixtool-v%version.tar.gz

# Automatically added by buildreq on Sun Jul 11 2021 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libp11-kit libqt5-core libqt5-gui libqt5-widgets libqt5-xml libsasl2-3 libstdc++-devel pkg-config python-base qt5-base-devel qt5-tools sh4

BuildRequires: cmake
BuildRequires: libqpdf-devel
BuildRequires: qt5-base-devel

BuildRequires: qt5-tools-devel
BuildRequires: qt5-svg-devel
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

%build
%cmake
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
* Sun Jul 11 2021 Evgeny Chuck <koi@altlinux.org> 1.0.2-alt1
- initial build for ALT Sisyphus
