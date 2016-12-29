%define _name luminance
Name: %_name-hdr
Version: 2.4.0
Release: alt5

Summary: A graphical tool for creating and processing HDR images
Group: Graphics
License: GPLv2+
Url: http://qtpfsgui.sourceforge.net/

Source: http://downloads.sourceforge.net/project/qtpfsgui/luminance/%version/%name-%version.tar.bz2
Source1: luminance-hdr_lang_ru.qm

Patch1: luminance-2.4.0-qt5-printsupport.patch

Obsoletes: qtpfsgui
Provides: qtpfsgui = %version-%release

BuildRequires: cmake gcc-c++ libgomp-devel
BuildRequires: boost-devel boost-program_options-devel
BuildRequires: qt5-base-devel qt5-tools-devel qt5-webkit-devel qt5-declarative-devel qt5-quick1-devel
BuildRequires: openexr-devel libexiv2-devel libfftw3-devel liblcms2-devel
BuildRequires: libraw-devel-static libjpeg-devel libtiff-devel libpng-devel
BuildRequires: libgsl-devel libgtest-devel zlib-devel
BuildRequires: libcfitsio-devel libccfits-devel

%description
Luminance HDR is a graphical user interface application that aims to
provide a workflow for HDR imaging.

%prep
%setup -n %name-%version
# new russian translation
#cp %SOURCE1 i18n/lang_ru.qm
#rm -f i18n/lang_ru.ts

%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%find_lang --with-qt --output=%name.lang lang qt

%files -f %name.lang
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/i18n
%_datadir/%name/help/
%_datadir/applications/*
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS Changelog README TODO BUGS

%changelog
* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt5
- rebuilt against libraw.so.16

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt4
- rebuilt against libraw.so.15

* Tue Jun 30 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt3
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Jan 31 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt2
- enabled FITS support

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt2
- rebuilt against libraw.so.10

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1
- built against libexiv2.so.13

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt2
- rebuilt against libexiv2.so.12

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sun Jan 22 2012 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt2
- rebuilt against libexiv2.so.11

* Sun Aug 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sun Oct 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Jun 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- rebuild against libexiv2-0.20
- updated russian translation
- obsoletes and provides qtpfsgui

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- first build for Sisyphus

