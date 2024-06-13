Name: loook
Version: 0.9.0
Release: alt1

Summary: Loook searches for text strings in ODF documents

License: GPLv2
Group: Text tools
Url: https://mechtilde.de/Loook/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://mechtilde.de/Loook/Downloads/loook-%version-sources.zip
Source: %name-%version.tar

BuildRequires: gettext-tools
BuildRequires: rpm-build-python3

Requires: python3
Requires: python3-modules-tkinter

BuildArch: noarch

%description
This program is a program written in Python that searches for strings
in files created by OpenOffice.org, Apache OpenOffice, LibreOffice or
StarOffice 6.0 or higher. This is especially true for all documents
that were created in the Open Document Format. In addition, it can now
also search in documents created by Microsoft Word, Excel or PowerPoint
from the 2007 version in an OOXML format.

%prep
%setup

%install
install -Dm 0755 %name.py %buildroot%_datadir/%name/%name.py
install -Dm 0644 man/%name.1 %buildroot/%_man1dir/%name.1

# symlink executable
mkdir -p %buildroot%_bindir/
ln -s %_datadir/%name/%name.py %buildroot%_bindir/%name

# install messages
for m in cs de en es fr it nl ; do
    msgfmt %name.${m}.po -o %name-%version.${m}.mo
    install -Dm 0644 %name-%version.${m}.mo %buildroot%_datadir/locale/${m}/LC_MESSAGES/%name.mo
done

%find_lang %name

install -Dm 0644 %name.png %buildroot/%_pixmapsdir/%name.png
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_man1dir/*

%changelog
* Thu Jun 13 2024 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version (0.9.0) (ALT bug 50291)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.7-alt1
- new version 0.6.7 (with rpmrb script)

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4-alt0.1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt0.1.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.6.4-alt0.1.1
- Rebuilt with python-2.5.

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt0.1
- initial build for ALT Linux Sisyphus

