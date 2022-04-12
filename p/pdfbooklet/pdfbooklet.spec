Name:    pdfbooklet
Version: 3.1.2
Release: alt1

Summary: Creates booklets from Pdf files, and much more
License: GPL-3.0+
Group:   Other
URL:	 https://sourceforge.net/projects/pdfbooklet/
Vcs:     https://github.com/Averell7/PdfBooklet

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Requires: python3-module-pygobject3
Requires: libpoppler-gir

BuildArch: noarch

Source:  %name-%version.tar

%description
PdfBooklet is a Python Gtk application which allows to make books or booklets
from existing pdf files. It can also adjust margins, rotate, scale, merge files
or extract pages.

%prep
%setup

%build
%python3_build

%install
%python3_install
%find_lang %name
%find_lang pdfshuffler
cat pdfshuffler.lang >> %name.lang
rm -f %buildroot%_datadir/locale/*/LC_MESSAGES/*.po

%files -f %name.lang
%doc *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/%name.png

%changelog
* Sat Apr 09 2022 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus
