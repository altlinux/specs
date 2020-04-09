%def_enable snapshot
%define ver_major 0.8
%define xdg_name org.gnome.OCRFeeder

Name: ocrfeeder
Version: %ver_major.3
Release: alt1

Summary: OCRFeeder is a document layout analysis and optical character recognition system
Group: Graphics
License: GPL-3.0-or-later 
Url: https://wiki.gnome.org/Apps/OCRFeeder

BuildArch: noarch

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: python3-module-%name = %EVR
Requires: unpaper
# works best with Russian
Requires: tesseract tesseract-langpack-en tesseract-langpack-ru
#Requires: gocr
#Requires: ocrad
#Requires: cuneiform


BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: intltool yelp-tools
BuildRequires: python3-devel python3-module-pygobject3-devel
BuildRequires: libgtk+3-gir libgoocanvas2-gir
BuildRequires: python3-module-enchant python3-module-Pillow
BuildRequires: python3-module-Reportlab python3-module-odf
BuildRequires: python3-module-sane

%description
OCRFeeder is a document layout analysis and optical character
recognition system. Given the images it will automatically outline its
contents, distinguish between what's graphics and text and perform OCR
over the latter. It generates multiple formats being its main one ODT.

%package -n python3-module-%name
Summary: Supplemental module for OCRFeeder
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
%summary

This package provides supplemental module for %name.

%prep
%setup

%build
%autoreconf
%configure PYTHON=%__python3
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f ocrfeeder.lang
%_bindir/%name
%_bindir/%name-cli
%_desktopdir/%xdg_name.desktop
%_datadir/%name
%_man1dir/%name.1.*
%_man1dir/%name-cli.1.*
%_iconsdir/hicolor/*/*/%xdg_name.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS README TRANSLATORS NEWS

%files -n python3-module-%name
%python3_sitelibdir/ocrfeeder

%changelog
* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- updated to 0.8.3-8-g38c995d (ported to Python3 & PyGI)
- required tesseract as default engine

* Thu May 23 2013 Fr. Br. George <george@altlinux.ru> 0.7.9-alt4
- Fix buildreq

* Sat Apr 28 2012 Fr. Br. George <george@altlinux.ru> 0.7.9-alt3
- Unpaper black filter threshold customization
- Window size autoadjustment tune

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 0.7.9-alt2
- Auto-adjust window size for reasonable block count

* Thu Apr 12 2012 Fr. Br. George <george@altlinux.ru> 0.7.9-alt1
- Version up
- Multilang patches applied
- Python module separated
- Russian translation

* Wed Dec 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.6-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.6-alt1
- first build for sisyphus

