Name: libmirage
Version: 2.0.0
Release: alt1

Summary: A CD-ROM image access library
License: GPLv2+
Group: System/Libraries

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: %name-%version.tar.bz2

BuildRequires: bzlib-devel cmake glib-networking gobject-introspection-devel gtk-doc glibc-core libGConf liblzma-devel libsndfile-devel time zlib-devel

%description
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

%package devel
Summary: A CD-ROM image access library
Group: Development/C
Requires: %name = %version-%release
Requires: glib2-devel

%description devel
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

This package contains files needed to develop with libMirage.

%prep
%setup -q

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
         -DCMAKE_INSTALL_PREFIX=%prefix \
         -DCMAKE_C_FLAGS:STRING='%optflags' \
         
popd

%make_build -C %_target_platform

%install
%make -C %_target_platform DESTDIR=%buildroot install
find %buildroot%_libdir -name *.la -or -name \*.a | xargs rm -f

%files
%_defattr
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/libmirage.so.*
%_libdir/libmirage-2.0/*.so
%_datadir/mime/packages/*.xml

%files devel
%_defattr
%_libdir/libmirage.so
%_libdir/girepository-1.0/*
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/gir-1.0/*
%doc %_datadir/gtk-doc/html/*

%changelog
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
