Name: libdmtx
Version: 0.7.2
Release: alt2
Summary: Library for working with Data Matrix 2D bar-codes

Group: System/Libraries
License: LGPLv2+
Url: http://www.libdmtx.org/
Source0: http://downloads.sourceforge.net/%name/%name-%version.tar.bz2
Patch0:	libdmtx-0.7.2-ruby.patch

## required for tests
BuildRequires: libSDL_image-devel libpng-devel

# Automatically added by buildreq on Thu May 12 2011
# optimized out: fontconfig libGL-devel libGLU-devel libSDL-devel pkg-config python-base python-modules ruby ruby-stdlibs zlib-devel
BuildRequires: libImageMagick-devel libruby-devel php5-devel python-devel

%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes on Linux, Unix, OS X, Windows, and mobile devices. At its core
libdmtx is a shared library, allowing C/C++ programs to use its capabilities
without restrictions or overhead.

The included utility programs, dmtxread and dmtxwrite, provide the official
interface to libdmtx from the command line, and also serve as a good reference
for programmers who wish to write their own programs that interact with
libdmtx. All of the software in the libdmtx package is distributed under
the LGPLv2 and can be used freely under these terms.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package utils
Summary: Utilities for reading and writing Data Matrix barcodes
Group: Graphics
Requires: %name = %version-%release

%description utils
The included utility programs, dmtxread and dmtxwrite, provide the
official interface to %name from the command line, and also serve as
a good reference for programmers who wish to write their own programs
that interact with %name.

# language bindings
%package -n     php-libdmtx
Summary: PHP bindings for %name
Group: System/Libraries
License: GPLv2+
Requires: %name = %version-%release

%description -n php-libdmtx
The php-%name package contains bindings for using %name from PHP.

%package -n     python-module-dmtx
Summary: Python bindings for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n python-module-dmtx
The python-%name package contains bindings for using %name from Python.

%package -n     ruby-libdmtx
Summary: Ruby bindings for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n ruby-libdmtx
The ruby-%name package contains bindings for using %name from Ruby.

%package -n vala-libdmtx
Summary: Vala bindings for %name
Group: System/Libraries
Requires: %name = %version-%release
Buildarch: noarch

%description -n vala-libdmtx
The vala-%name package contains bindings for using %name from Vala.

%prep
%setup

# fix permissions
chmod a-x wrapper/{php,python}/README
%patch0 -p0

%build
%configure --disable-static --enable-php --enable-python --enable-ruby --enable-vala
#  --enable-java           enable Java bindings
#    --enable-net            enable .NET bindings

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' wrapper/php/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' wrapper/php/libtool

sed -i 's@setup.py install@setup.py install --skip-build --root=$(DESTDIR)@' wrapper/python/Makefile

sed -i 's@^\(RUBY[A-Z]*DIR.*\)site@\1vendor@' wrapper/ruby/Makefile

for d in php python ruby; do echo "check:" >> wrapper/$d/Makefile; done

%make_build CFLAGS="-I`pwd` -fPIC" LDFLAGS=-L`pwd`/.libs LOCAL_LIBS="-L`pwd`/.libs -ldmtx"

%install
%make install DESTDIR=%buildroot INSTALL_ROOT=%buildroot

%check
make check
pushd test
for t in simple unit
do
    ./${t}_test/${t}_test
done
popd

%files
%doc AUTHORS COPYING.LESSER ChangeLog KNOWNBUG NEWS README README.linux TODO
%_libdir/%name.so.*

%files devel
%doc
%_includedir/*
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_mandir/man3/%name.3*

%files utils
%_bindir/dmtx*
%_mandir/man1/dmtx*.1*

%files -n php-libdmtx
%doc COPYING wrapper/php/README
%_libdir/php/*/*/*.so

%files -n python-module-dmtx
%doc wrapper/python/README
%python_sitelibdir/*

%files -n ruby-libdmtx
%doc wrapper/ruby/README
%ruby_sitearchdir/*.so

%files -n vala-libdmtx
%doc wrapper/vala/README
%_datadir/vala/vapi/libdmtx.vapi

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.7.2-alt2
- Rebuild with new libImageMagick

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Fr. Br. George <george@altlinux.ru> 0.7.2-alt1
- Initial build from FC

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Dan Horák <dan[at]danny.cz> 0.7.2-3
- updated license for the php subpackage
- run few tests

* Sat May 29 2010 Dan Horák <dan[at]danny.cz> 0.7.2-2
- added language bindigs

* Wed Feb  3 2010 Dan Horák <dan[at]danny.cz> 0.7.2-1
- initial Fedora version
