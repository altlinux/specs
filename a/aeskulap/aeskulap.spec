%add_optflags %optflags_shared 

Name: aeskulap
Version: 0.2.2
Release: alt3.git2ac922d

Summary: Medial image viewer for DICOM images
License: GPL/LGPL
Group: Graphics

Url: http://aeskulap.nongnu.org
# Git https://github.com/jenslody/aeskulap
Source: %name-%version.tar

Requires: dcmtk, libdcmtk, GConf
BuildPreReq: gcc-c++, zlib-devel, libpng-devel, libtiff-devel
BuildPreReq: libxml2-devel, libwrap-devel, libssl-devel
BuildPreReq: libgtkmm2-devel, libglademm-devel, libgconfmm2-devel
BuildPreReq: perl-XML-Parser, gettext, intltool
BuildPreReq: libdcmtk-devel
BuildRequires: desktop-file-utils GConf

%description
Aeskulap is a medical image viewer. It is able to load a series of special
images stored in the DICOM format for review. It is able to query and fetch
DICOM images from archive nodes (also called PACS) over the network. The
goal of this project is to create a full open source replacement for
commercially available DICOM viewers. It is based on gtkmm, glademm, and
gconfmm and designed to run under Linux. Ports of these packages are
available for different platforms. It should be quite easy to port It to
any platform were these packages are available.

%prep
%setup

%build
%autoreconf
%configure

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=MedicalSoftware \
	--add-category=Viewer \
	%buildroot%_desktopdir/aeskulap.desktop

%files -f %name.lang
%_bindir/aeskulap
%_datadir/aeskulap/*
%_datadir/applications/aeskulap.desktop
%_datadir/appdata/*
%_libdir/aeskulap/*
%_iconsdir/*/*/*
%config %_sysconfdir/gconf/schemas/aeskulap.schemas
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYING.LIB NEWS README

%changelog
* Wed Nov 01 2017 Anton Farygin <rider@altlinux.ru> 0.2.2-alt3.git2ac922d
- build from new upstream git

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.2-alt2.1.qa3.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 03 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt2.1.qa3
- Fix build with new GConf

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt2.1.qa2
- Fixed build

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.2-alt2.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for aeskulap

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt2.1
- Blind rebuild without libyaml.

* Thu Feb 18 2010 Andrey Yurkovsky <anyr@altlinux.org> 0.2.2-alt2
- Portugese translation update
- dcmtk removed from source

* Sat Feb 06 2010 Andrey Yurkovsky <anyr@altlinux.org> 0.2.2-alt0.M51.1
- build for branch 5.1

* Wed Nov 11 2009 Andrey Yurkovsky <anyr@altlinux.org> 0.2.2-alt1
- initial build
