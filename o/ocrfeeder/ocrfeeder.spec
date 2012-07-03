Summary: OCRFeeder is a document layout analysis and optical character recognition system
Name: ocrfeeder
Version: 0.7.9
Release: alt3
License: GPLv3+
URL: http://live.gnome.org/OCRFeeder
Group: Graphics

%setup_python_module %name

BuildArch: noarch

Source: %name-%version.tar
Patch:	%name-%version-%release.patch

BuildRequires: python-devel

Requires: unpaper %packagename = %version

# Automatically added by buildreq on Thu Apr 12 2012
# optimized out: perl-Encode perl-XML-Parser pkg-config python-base python-devel python-module-distribute python-module-libxml2 python-module-pygobject python-module-pygtk python-modules python-modules-compiler python-modules-encodings
BuildRequires: glib2-devel gnome-common gnome-doc-utils intltool python-module-Reportlab python-module-enchant python-module-pygnome-extras python-module-pygoocanvas python-module-sane time

%description
OCRFeeder is a document layout analysis and optical character
recognition system. Given the images it will automatically outline its
contents, distinguish between what's graphics and text and perform OCR
over the latter. It generates multiple formats being its main one ODT.

%package -n %packagename
Summary: Supplemental module for %name, %summary
Group: Graphics
BuildArch: noarch

%description -n %packagename
Supplemental module for %name, %summary

%prep
%setup -q
%patch -p1

%build
./autogen.sh
%configure
%make

%install
%makeinstall_std

%find_lang ocrfeeder 

%files -f ocrfeeder.lang
%doc README TRANSLATORS NEWS
%_bindir/*
/usr/share/applications/ocrfeeder.desktop
/usr/share/gnome/help/ocrfeeder
%_man1dir/*
/usr/share/ocrfeeder

%files -n %packagename
%python_sitelibdir/ocrfeeder

%changelog
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

