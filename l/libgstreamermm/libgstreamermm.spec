%define major 1.8
%define oname gstreamermm
Name: libgstreamermm
Version: %major.0
Release: alt1

Summary: C++ wrapper for GStreamer library

Group: Video
License: LGPLv2+
Url: http://www.gtkmm.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.gnome.org/pub/GNOME/sources/%oname/%major/%oname-%version.tar

Patch1: 01-disable-tests.patch
Patch2: 02-do-not-compile-examples.patch
Patch3: 03-fix-build-with-gstreamer1.10.patch
Patch4: 04-fix-build-with-gstreamer1.12.patch
Patch5: 05-fix-build-with-gcc7.patch

# Automatically added by buildreq on Wed Oct 07 2009
BuildRequires: doxygen gcc-c++
BuildRequires: gst-plugins-bad1.0-devel gst-plugins1.0-devel libxml++2-devel mm-common

%add_optflags -fpermissive

%description
GStreamermm is a C++ wrapper library for the multimedia library
GStreamer (http://gstreamer.freedesktop.org).  It is designed to allow
C++ development of applications that work with multi-media.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the static libraries and header files needed for
developing gstreamermm applications.

%prep
%setup -n %oname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#patch5 -p1

%build
export MMDOCTOOLDIR=/usr/share/mm-common/doctool/
%autoreconf
%configure --enable-shared --disable-examples --disable-docs --disable-dependency-tracking \
    --disable-gl --disable-plugins-bad
%make_build

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -exec rm -f {} ';'
# Move documentation to gtk-doc directory
#mkdir -p %buildroot%_datadir/gtk-doc/html
#mv %buildroot%_docdir/%oname-0.10/reference/html %buildroot%_datadir/gtk-doc/html/%oname-0.10
# Removing code generation script stuff
rm -rf %buildroot%_libdir/gstreamermm-1.0/gen/

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*

%files devel
%doc %_docdir/gstreamermm-1.0/
%_includedir/gstreamermm-1.0/
%_libdir/gstreamermm-1.0/
%_datadir/devhelp/books/gstreamermm-1.0/
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Aug 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script) (ALT bug 32596)
- build with --disable-plugins-bad --disable-gl (do not compiled)

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.8-alt2.1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.8-alt2.1
- Fixed build with new glib2

* Mon Apr 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.8-alt2
- fix build

* Mon Jan 03 2011 Vitaly Lipatov <lav@altlinux.ru> 0.10.8-alt1
- new version 0.10.8 (with rpmrb script)

* Wed Oct 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.10.5-alt1
- new version (0.10.5) import in git

* Fri Jun 26 2009 Denis Leroy <denis@poolshark.org> - 0.10.2-1
- Update to upstream 0.10.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Denis Leroy <denis@poolshark.org> - 0.10.1-1
- Update to upstream 0.10.1
- No longer uses gstreamerbase include dir

* Sun Dec 28 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-2
- Rebuild for pkgconfig

* Fri Dec 26 2008 Denis Leroy <denis@poolshark.org> - 0.9.8-1
- Update to upstream 0.9.8
- Disabled parallel make

* Fri Oct 10 2008 Denis Leroy <denis@poolshark.org> - 0.9.7-1
- Update to upstream 0.9.7

* Wed Sep  3 2008 Denis Leroy <denis@poolshark.org> - 0.9.6-1
- Update to upstream 0.9.6

* Sat May 31 2008 Denis Leroy <denis@poolshark.org> - 0.9.5-1
- Update to upstream 0.9.5
- Fixed gstreamer plugin BuildRequires

* Fri Feb 22 2008 Denis Leroy <denis@poolshark.org> - 0.9.4-1
- Updated to upstream 0.9.4

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 0.9.2-1
- First draft

