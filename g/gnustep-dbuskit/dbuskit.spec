%set_verify_elf_method unresolved=strict

Name: gnustep-dbuskit
Version: 0.3.2
Release: alt1.git20121111
Summary: GNUstep interface to the DBUS data transport mechanism
License: LGPLv2.1+
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-dbuskit.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libdbus-devel /proc
BuildPreReq: clang3.1-devel clang3.1
BuildPreReq: texinfo texi2html texlive-latex-base

Requires: lib%name = %version-%release

%description
GNUstep interface to the DBUS data transport mechanism. This library
allows applications written in GNUstep to communicate directly with apps
which use DBUS.

Requires: lib%name

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

%build
export CC=gcc
%add_optflags -DHAVE_OBJC_RUNTIME_H
#export OBJCPP=gcc
%autoreconf
for i in $(find ./ -type f); do
	sed -i 's|[0-9a-z_]*alt-linux-cgg|gcc|g' $i
done
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
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/DBusKit.framework/Versions/Current/$i ./
	ln -s $i GNUstep/Frameworks/DBusKit.framework/Versions/Current/
done
popd

%makeinstall_std -C Documentation \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
     GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_infodir/*
%_docdir/GNUstep

%changelog
* Sun Dec 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20121111
- Initial build for Sisyphus

