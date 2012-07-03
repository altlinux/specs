%define MOUNT_DIR /media

Name: libgpod4
Version: 0.8.2
Release: alt1.3

Summary: iPod access library
Group: Sound
License: %lgpl3plus
URL: http://www.gtkpod.org/libgpod

Source: %name-%version.tar

Provides: libgpod = %version-%release
Obsoletes: libgpod < 0.7

BuildRequires: gcc-c++ gtk-doc intltool
BuildRequires: glib2-devel libgio-devel libsqlite3-devel libplist-devel
BuildRequires: libsgutils-devel libusb-devel zlib-devel libimobiledevice-devel
BuildRequires: libtag-devel libxml2-devel libgdk-pixbuf-devel
BuildRequires: python-module-pygobject-devel python-module-mutagen swig
BuildRequires: rpm-build-licenses
BuildRequires: mono-devel libgtk-sharp2-devel

%description
libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

%package -n libgpod-devel
Summary: Development files for libgpod
Group: Development/C
Requires: %name = %version-%release

%description -n libgpod-devel
Files needed to develop applications that use libgpod,
an iPod access library.

%package -n libgpod-devel-doc
Summary: Development documentation for libgpod
Group: Development/C
BuildArch: noarch

%description -n libgpod-devel-doc
API documentation in gtk-doc format for libgpod,
an iPod access library.

%package -n python-module-gpod
Summary: Python bindings for libgpod
Group: Development/Python
Requires: %name = %version-%release
Obsoletes: python-modules-gpod < %version-%release
Provides: python-modules-gpod = %version-%release

%description -n python-module-gpod
Python bindings for libgpod, an iPod access library.

%package -n libgpod-sharp
Summary: C#/.NET library to access iPod content
Group: Development/Other
Requires: %name = %version-%release

%description -n libgpod-sharp
C#/.NET library to access iPod content.  Provides bindings to the libgpod
library.


%package -n libgpod-sharp-devel
Summary: Development files for libgpod-sharp
Group: Development/Other
Requires: libgpod-sharp = %version-%release

%description -n libgpod-sharp-devel
C#/.NET library to access iPod content.  Provides bindings to the libgpod
library.

This package contains the files required to develop programs that will use
libgpod-sharp.

%prep
%setup

# remove execute perms on the python examples as they'll be installed in %%doc
chmod -x bindings/python/examples/*.py

%build
%autoreconf
%configure \
	--disable-static \
	--enable-gtk-doc \
	--enable-pygobject \
	--without-hal \
	--enable-udev \
	--with-libimobiledevice \
	--with-temp_mount_dir="%MOUNT_DIR" \
	--enable-more-warnings=no

%make_build
pushd bindings/python
make README
popd

%install
%makeinstall_std

# remove Makefiles from the python examples dir
rm -rf bindings/python/examples/Makefile*

rm -f %buildroot%python_sitelibdir/gpod/*.la

%find_lang libgpod

%files -f libgpod.lang
%_bindir/*
%_libdir/*.so.*
/lib/udev/rules.d/*
/lib/udev/*-set-info

%files -n libgpod-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/libgpod-1.0.pc

%files -n libgpod-devel-doc
%_datadir/gtk-doc/html/*

%files -n python-module-gpod
%doc COPYING bindings/python/README bindings/python/examples
%python_sitelibdir/gpod

%files -n libgpod-sharp
%_libdir/libgpod

%files -n libgpod-sharp-devel
%_pkgconfigdir/libgpod-sharp.pc

%changelog
* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.3
- Rebuilt with libplist-1.8

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.2
- Removed -Werror compiler flag

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1.1
- Rebuild with Python-2.7

* Fri Aug 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt3
- rebuild with new libimobiledevice

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Rebuilt for debuginfo

* Mon Jan 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- update buildreq
- cleanup spec
- build with udev and without hal
- add python examples to %%doc
- add sharp and sharp-devel subpackage
- fix libgpod-devel - move libgpod-sharp.pc to sharp-devel

* Fri Sep 24 2010 Andriy Stepanov <stanv@altlinux.ru> 0.7.94-alt1
- New version

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.93-alt4
- Fixed packaging of python-module-gpod

* Sat Apr 10 2010 Andriy Stepanov <stanv@altlinux.ru> 0.7.93-alt3
- Pack missing files

* Sat Apr 10 2010 Andriy Stepanov <stanv@altlinux.ru> 0.7.93-alt2
- Update BuildRequires

* Sat Apr 10 2010 Andriy Stepanov <stanv@altlinux.ru> 0.7.93-alt1
- Update to new version.

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.1
- Rebuilt with python 2.6

* Mon Aug 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.2-alt1
- Update to 0.7.2

* Wed Apr 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt7
- Provide right package

* Wed Apr 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt6
- Rename package: SharedLibsPolicy

* Mon Apr 06 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt5
- 0.7.0-alt5

* Tue Mar 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt2
- renamed python-modules-gpod to python-module-gpod (shrek@)

* Wed Jan 21 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt1
- 0.7.0
- Updated BuildRequires

* Wed Jan 21 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.0-alt3
- Gearify

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt2
- fixed build with gcc4.3

* Sun Nov 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Feb 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- 0.4.2
- added libgpod-0.4.2-alt-gpod-link.patch

* Sun Sep 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.0-alt1
- Release 0.4.0
- Added libgpod-devel-doc package
- Added python-modules-gpod package

* Fri Mar 17 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.2-alt1
- Initial release for Sisyphus
