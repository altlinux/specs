Name: gnustep-gworkspace
Version: 0.9.1
Release: alt1.git20121017
Summary: The GNUstep Workspace Manager of which the most visible part is the filebrowser
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gworkspace.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel /proc
BuildPreReq: libgnustep-objc2-devel libPDFKit-devel inotify-tools-devel
BuildPreReq: gnustep-systempreferences-devel libsqlite3-devel unzip
BuildPreReq: gnustep-gui-devel gnustep-gui

Requires: lib%name = %version-%release

%description
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

%package -n lib%name
Summary: Shared libraries of GWorkspace
Group: System/Libraries

%description -n lib%name
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

This package contains shared libraries of GWorkspace.

%package -n lib%name-devel
Summary: Development files of GWorkspace
Group: Development/Objective-C
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

This package contains development files of GWorkspace.

%package doc
Summary: Documentation for GWorkspace
Group: Documentation
BuildArch: noarch

%description doc
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

This package contains documentation for GWorkspace.

%prep
%setup

%build
export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
export CC=gcc

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-gwmetadata \
	--with-inotify \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lgnustep-gui -lobjc -lm'
 
libFSNode="$PWD/FSNode/FSNode.framework/libFSNode.so"
pushd Inspector
%make clean
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS="$libFSNode -lgnustep-base -lgnustep-gui -lobjc"
popd

%install
%makeinstall_std \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in MDKit Operation Inspector FSNode; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/?/$i ./
	ln -s %_libdir/$i GNUstep/Frameworks/$j.framework/Versions/?/
	done
done
popd

%files
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%doc Documentation/*

%changelog
* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20121017
- Initial build for Sisyphus

