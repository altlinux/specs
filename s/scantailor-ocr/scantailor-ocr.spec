Name: scantailor-ocr
Version: 1.0.9
Release: alt1

Summary: Scanned pages to compact searchable PDF (ScanTailor with OCR)

License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/2ndmax/scantailor-ocr

# Source-url: https://github.com/2ndmax/scantailor-ocr/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# ALT keeps the Tesseract language data in /usr/share/tesseract/tessdata
Patch: scantailor-ocr-1.0.9-alt-tessdata-dir.patch

BuildRequires: rpm-build-cmake ctest gcc-c++
BuildRequires: boost-devel-headers boost-intrusive-devel boost-devel
BuildRequires: zlib-devel libjpeg-devel libtiff-devel libpng-devel libopenjpeg2.0-devel openjpeg-tools2.0
BuildRequires: tesseract-devel libleptonica-devel
BuildRequires: qt6-base-devel qt6-tools-devel qt6-svg-devel

Requires: tesseract-langpack-en

%description
ScanTailor OCR is a fork of ScanTailor Advanced for post-processing of
scanned pages: page splitting, deskewing, content selection, margins,
dewarping and binarization. It exports the result directly to a compact
PDF (JBIG2 for black and white pages, layered pages for mixed ones) and
adds an invisible text layer using Tesseract OCR, so the PDF is searchable.

It can be installed next to the scantailor package.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
export QT_QPA_PLATFORM=offscreen
%ctest

%files
%_bindir/%name
%dir %_datadir/%name/
%_datadir/%name/translations/
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name-project.xml
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- initial build for Sisyphus
