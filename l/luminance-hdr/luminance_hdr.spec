%define _name luminance
Name: %_name-hdr
Version: 2.2.1
Release: alt1

Summary: A graphical tool for creating and processing HDR images
Group: Graphics
License: GPLv2+
Url: http://qtpfsgui.sourceforge.net/

Source: http://sourceforge.net/projects/qtpfsgui/files/%name-v%version.tar.gz
Source1: luminance-hdr_lang_ru.qm

Obsoletes: qtpfsgui
Provides: qtpfsgui = %version-%release

BuildRequires: cmake gcc-c++ libgomp-devel libqt4-devel phonon-devel
BuildRequires: openexr-devel libexiv2-devel libfftw3-devel
BuildRequires: libraw-devel-static libjpeg-devel libtiff-devel libgsl-devel

%description
Luminance HDR is a graphical user interface application that aims to
provide a workflow for HDR imaging.

%prep
%setup -n %name-v%version
# new russian translation
#cp %SOURCE1 i18n/lang_ru.qm
#rm -f i18n/lang_ru.ts

%build
%cmake
pushd BUILD
%make_build

%install
pushd BUILD
%makeinstall_std

%files
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS Changelog README TODO BUGS

%changelog
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

