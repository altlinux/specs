
%define rname libzip
Name: libzip1
Version: 0.9.3
Release: alt3
Summary: C library for reading, creating, and modifying zip archives

Group: System/Libraries
License: BSD
Url: http://www.nih.at/libzip/index.html

Source0: http://www.nih.at/libzip/%rname-%version.tar.bz2
Source1: libzip.map
Patch1: libzip-0.9-alt-versioning.patch

BuildRequires: gcc-c++ zlib-devel

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n libzip
Group: System/Libraries
Summary: C library for reading, creating, and modifying zip archives
%description -n libzip
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%prep
%setup -qn %rname-%version
install %SOURCE1 lib/libzip.map
%patch1 -p1

%autoreconf


%build
%configure \
    --disable-static \
    --enable-shared \
    --includedir=%_includedir/%rname

%make_build


%install
%make DESTDIR=%buildroot install


%files -n libzip
%doc AUTHORS NEWS README THANKS TODO
%_libdir/*.so.*

%changelog
* Mon Mar 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt3
- built only libzip

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt2
- rebuilt

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1
- new version

* Mon Dec 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt3
- remove ldconfig from %%post

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt2
- add versioning

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt1
- new version

* Mon Mar 24 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt1
- initial specfile
