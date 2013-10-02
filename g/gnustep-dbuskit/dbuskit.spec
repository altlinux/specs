%set_verify_elf_method unresolved=strict

Name: gnustep-dbuskit
Version: 0.3.2
Release: alt5.git20130710
Summary: GNUstep interface to the DBUS data transport mechanism
License: LGPLv2.1+
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-dbuskit.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libdbus-devel /proc
BuildPreReq: clang-devel clang
BuildPreReq: texinfo texi2html texlive-latex-base

Requires: lib%name = %version-%release

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

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

sed -i 's|@LIBDIR@|%_libdir|g' configure.ac

%build
export CC=gcc
%add_optflags -DHAVE_OBJC_RUNTIME_H
#export OBJCPP=gcc
%autoreconf
for i in $(find ./ -type f); do
	sed -i 's|[0-9a-z_]*alt-linux-gcc|clang|g' $i
done
export LD_LIBRARY_PATH=%_libdir/llvm
%configure \
	--libexecdir=%_libdir \
	--enable-static=yes \
	--enable-static=no \
	--enable-libclang=yes \
	--with-installation-domain=SYSTEM

export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
export LD_LIBRARY_PATH=%_libdir/llvm
buildIt() {
	%make \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		AUXILIARY_CPPFLAGS='-O2' \
		CONFIG_SYSTEM_LIBS="-L$LD_LIBRARY_PATH -lclang -ldbus-1 $1"
}

pushd Source
buildIt
popd
libDBusKit=$PWD/Source/DBusKit.framework/Versions/Current/libDBusKit.so
buildIt $libDBusKit
 
%make_build -C Documentation \
	messages=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%install
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
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
     GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

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

