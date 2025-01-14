%define _unpackaged_files_terminate_build 1

Name:    lios
Version: 20241022
Release: alt1

Summary: Linux-intelligent-ocr-solution
License: GPL-3.0
Group:   Graphics
VCS:     https://github.com/zendalona/lios
Url:            http://sourceforge.net/projects/lios/

Requires: python3-module-Pillow
Requires: python3-module-sane
Requires: python3-module-speechd
Requires: tesseract
Requires: ImageMagick
Requires: cuneiform
Requires: espeak
Requires: poppler
Requires: python3-module-enchant
Requires: aspell-en
Requires: aspell-ru
Requires: gst-plugins-base1.0
Requires: gstreamer1.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Lios is a free and open source software for converting print in to text using either scanner, camera, or screenshot, It can also produce text out of scanned images from other sources such as Pdf, Image or Folder containing Images. Program is given total accessibility for visually impaired.  Lios is written in python3, and we release it under GPL-3 license.

%package -n python3-module-%name
Summary: python3 module for %name
Group:          Development/Python3

%description -n python3-module-%name
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

chmod 755 %buildroot%_bindir/%name

%files
%doc *.md NEWS COPYING
%_bindir/%name
%_datadir/applications/Lios-ocr-screenshot.desktop
%_datadir/applications/Lios.desktop
%_datadir/%name/icons/*.png
%_datadir/%name/*.text
%_datadir/%name/%name.png
%_datadir/locale/fr/LC_MESSAGES/lios.mo
%_datadir/locale/it/LC_MESSAGES/lios.mo
%_datadir/pixmaps/lios.xpm
%_docdir/%name/copyright
%_man1dir/%name.1.xz

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-2.5.dist-info

%changelog
* Sat Dec 28 2024 Artem Semenov <savoptik@altlinux.org> 20241022-alt1
- Initial build for Sisyphus (ALT bug: 52269)
