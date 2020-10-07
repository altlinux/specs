%set_verify_elf_method unresolved=strict

Name: gnustep-dbuskit
Version: 0.3.2
Release: alt7.svn20140131.3
Summary: GNUstep interface to the DBUS data transport mechanism
License: LGPLv2.1+
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/dbuskit/trunk/
Source: %name-%version.tar
Patch1: gcc9-objc.patch
Patch2: link-libs.patch

BuildPreReq: gnustep-make-devel gnustep-base-devel
BuildPreReq: libdbus-devel /proc
BuildPreReq: texinfo texi2html

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
GNUstep interface to the DBUS data transport mechanism. This library
allows applications written in GNUstep to communicate directly with apps
which use DBUS.

%package -n lib%name
Summary: GNUstep interface to the DBUS Share data transport mechanism
Group: System/Libraries

%description -n lib%name
GNUstep interface to the DBUS data transport mechanism. This library
allows applications written in GNUstep to communicate directly with apps
which use DBUS.

This package contains shared libraris of GNUstep interface.

%package -n lib%name-devel
Summary: Shares libraries interface to the DBUS Share data transport mechanism
Group: System/Libraries
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
GNUstep interface to the DBUS data transport mechanism. This library
allows applications written in GNUstep to communicate directly with apps
which use DBUS.

This package contains develoment files GNUstep interface.

%package doc
Summary: Documentation of the interface to the DBUS Share data transport mechanism
Group: System/Libraries
BuildArch: noarch

%description doc
GNUstep interface to the DBUS data transport mechanism. This library
allows applications written in GNUstep to communicate directly with apps
which use DBUS.

This package cicu of GNUstep interface.

%prep
%setup
%patch1 -p1
%patch2 -p1
sed -i 's|@LIBDIR@|%_libdir|g' configure.ac

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

#add_optflags -DHAVE_OBJC_RUNTIME_H
#remove_optflags -frecord-gcc-switches
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-static=yes \
	--enable-static=no \
	--disable-libclang \
	--with-installation-domain=SYSTEM
# Override HAVE_LIBCLANG 1
subst 's/define HAVE_LIBCLANG.*/define HAVE_LIBCLANG 0/' Source/config.h

export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
export LD_LIBRARY_PATH=%_libdir/llvm
buildIt() {
	%make \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		CONFIG_SYSTEM_LIBS="-L$LD_LIBRARY_PATH -ldbus-1 $1" \
		nonstrict=yes
}

pushd Source
buildIt
popd
libDBusKit=$PWD/Source/DBusKit.framework/Versions/Current/libDBusKit.so
buildIt $libDBusKit
 
%make_build -C Documentation \
	messages=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std \
	messages=yes \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
lib=$(ls *.so.*.*)
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/DBusKit.framework/Versions/Current/$i ./
	ln -s %_libdir/$lib \
		GNUstep/Frameworks/DBusKit.framework/Versions/Current/$i
done
popd

%makeinstall_std -C Documentation \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files doc
%_infodir/*
%_docdir/GNUstep

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt7.svn20140131.3
- NMU: build without libgnustep-objc2-devel.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 0.3.2-alt7.svn20140131.2
- Rebuild with llvm6.0.
- BR cleanup.

* Mon Feb 05 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.2-alt7.svn20140131.1
- Rebuilt with llvm4.0.

* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt7.svn20140131
- New snapshot

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt7.git20140101
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt6.git20140101
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt5.git20140101
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt5.git20130710
- New snapshot

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt5.git20121111
- Moved headers into lib%name-devel

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt4.git20121111
- Rebuilt with llvm 3.2

* Wed Feb 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt3.git20121111
- Fixed links for libraries

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2.git20121111
- Rebuilt with libobjc2 instead of libobjc

* Sun Dec 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20121111
- Initial build for Sisyphus

