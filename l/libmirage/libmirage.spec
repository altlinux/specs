%add_optflags -fcommon

%define soversion 11

Name: libmirage
Version: 3.2.8
Release: alt1

Summary: A CD-ROM image access library
License: GPLv2+
Group: System/Libraries

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>

# http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
Source: %name-%version.tar

BuildPreReq: gobject-introspection-devel
BuildPreReq: libblkid-devel
BuildPreReq: libflac-devel
BuildPreReq: libmount-devel
BuildPreReq: libogg-devel
BuildPreReq: libopus-devel
BuildPreReq: libpcre-devel
BuildPreReq: libselinux-devel
BuildPreReq: libvorbis-devel

BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: glib-networking
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: libGConf
BuildRequires: liblzma-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: zlib-devel

%description
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

%package -n %name%soversion
Summary: A CD-ROM image access library
Group: System/Libraries
Requires: %name-plugins >= %version
Requires: %name-common >= %version
Provides: %name = %EVR
Obsoletes: %name <= 3.0.3-alt1

%description -n %name%soversion
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

%package plugins
Summary: CD-ROM image format plugins for %name
Group: System/Libraries
Conflicts: %{name}10

%description plugins
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

This package provides the image format plugins for %name.

%package common
Summary: Common files for %name
Group: System/Libraries
BuildArch: noarch

%description common
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

This package provides the common files for %name.

%package devel
Summary: A CD-ROM image access library
Group: Development/C
Requires: glib2-devel

%description devel
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

This package contains files needed to develop with libMirage.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

%files -n %name%soversion
%doc AUTHORS ChangeLog INSTALL NEWS README
%_libdir/libmirage.so.*

%files plugins
%_libdir/libmirage-3.2

%files common -f %name.lang
%_datadir/mime/packages/*.xml
%_datadir/gtk-doc/html/%name

%files devel
%_libdir/libmirage.so
%_libdir/girepository-1.0/Mirage-3.2.typelib
%_pkgconfigdir/%name.pc
%_includedir/%name-3.2
%_datadir/gir-1.0/*

%changelog
* Sat Aug 31 2024 Nazarov Denis <nenderus@altlinux.org> 3.2.8-alt1
- New version 3.2.8.

* Thu Feb 15 2024 Nazarov Denis <nenderus@altlinux.org> 3.2.7-alt1
- New version 3.2.7.

* Thu Jan 13 2022 Nazarov Denis <nenderus@altlinux.org> 3.2.6-alt1
- Version 3.2.6

* Sun Nov 14 2021 Nazarov Denis <nenderus@altlinux.org> 3.2.5-alt2
- Separate plugins and common packages

* Thu Nov 11 2021 Nazarov Denis <nenderus@altlinux.org> 3.2.5-alt1
- Version 3.2.5

* Fri Mar 19 2021 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt2.1
- Don't bzip sources to speedup rpmbuild -bp
- Update build requires

* Sun Dec 13 2020 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt2
- Build with -fcommon instead -fno-common by default

* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt1
- Version 3.2.4 (ALT #39133)

* Mon Jun 17 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.2-alt1
- Version 3.2.2

* Sat Jan 26 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt2
- Remove %ubt macro

* Fri Jul 27 2018 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1%ubt
- Version 3.2.0

* Thu Aug 03 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt2%ubt
- Add conflicts on libmirage10 (ALT #33724)

* Wed Aug 02 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt1%ubt
- Version 3.1.0

* Sat Oct 15 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.5-alt2
- Add provides/obsoletes on libmirage (ALT #32614)

* Thu Oct 13 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.5-alt1
- Version 3.0.5

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.4-alt1
- Version 3.0.4

* Sun Nov 30 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Fri Oct 10 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt0.M70T.1
- Build for branch t7

* Tue Oct 07 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Thu Aug 07 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt0.M70T.1
- Build for branch t7

* Wed Aug 06 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Sun Jul 20 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70P.1
- Build for branch p7

* Fri Jul 04 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70T.1
- Build for branch t7

* Thu Jul 03 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M70P.1
- Build for branch p7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M70T.1
- Build for branch t7

* Sat Sep 21 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2
- Fix post-install unowned files

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Tue Jan 24 2012 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt2
- Fix buildrequires

* Sun Sep 18 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jan 25 2011 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt2
- Fix shared-mime-info

* Thu Nov 11 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmirage
  * postun_ldconfig for libmirage
  * shared-mime-info for libmirage
  * postclean-05-filetriggers for spec file

* Fri Nov 14 2008 Nick S. Grechukh <gns@altlinux.org> 1.1.0-alt1
- first build for ALT Linux

* Sat Jun 28 2008 Rok Mandeljc <rok.mandeljc@email.si> - 1.1.0-1
- Updated to 1.1.0

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.
