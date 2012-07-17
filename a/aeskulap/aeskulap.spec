%add_optflags %optflags_shared 

Name: aeskulap
Version: 0.2.2
Release: alt2.1.qa2

Summary: Medial image viewer for DICOM images
License: GPL/LGPL
Group: Graphics

Url: http://aeskulap.nongnu.org

Packager: Andrey Yurkovsky <anyr@altlinux.org>
Source: %name-%version.tar.gz
Patch0: aeskulap-gcc4.patch
Patch1: aeskulap-dcmtk.patch
Patch2: aeskulap-i18n_pt.patch
Patch3: aeskulap-0.2.2-alt-DSO.patch

Requires: dcmtk, libdcmtk
BuildPreReq: gcc-c++, zlib-devel, libpng-devel, libtiff-devel
BuildPreReq: libxml2-devel, libwrap-devel, libssl-devel
BuildPreReq: libgtkmm2-devel, libglademm-devel, libgconfmm2-devel
BuildPreReq: perl-XML-Parser, gettext, intltool
BuildPreReq: libdcmtk-devel
BuildRequires: desktop-file-utils

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
rm -rf COPYING.DCMTK dcmtk
touch NEWS
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
%_libdir/aeskulap/*
%_liconsdir/*.*
%config %_sysconfdir/gconf/schemas/aeskulap.schemas
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYING.LIB NEWS README

%changelog
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
