%set_verify_elf_method unresolved=strict

Name: gnustep-Paje
Version: 1.98
Release: alt3.1
Summary: Paje is an interactive and scalable trace-based visualization tool
License: GPLv2 / LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://www-id.imag.fr/Logiciels/paje/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: ghostscript-utils texlive-base-bin texlive-publishers

Requires: lib%name = %EVR
Requires: gnustep-back

%description
Paje is an interactive and scalable trace-based visualization tool which
can be used for a large variety of visualizations including performance
monitoring of parallel applications, monitoring the execution of
processors in a large scale PC cluster or representing the behavior of
distributed applications.

Users of Paje can tailor the visualization to their needs, without
having to know any insight nor to modify any component of Paje. This can
be done by defining the type hierarchy of objects to be visualized as
well as how these objects should be visualized. This feature allows the
use of Paje for a wide variety of visualizations such as the use of
resources by applications in a large-size cluster or the behavior of
distributed Java applications.

%package -n lib%name
Summary: Shared libraries of Paje
Group: System/Libraries

%description -n lib%name
Paje is an interactive and scalable trace-based visualization tool which
can be used for a large variety of visualizations including performance
monitoring of parallel applications, monitoring the execution of
processors in a large scale PC cluster or representing the behavior of
distributed applications.

Users of Paje can tailor the visualization to their needs, without
having to know any insight nor to modify any component of Paje. This can
be done by defining the type hierarchy of objects to be visualized as
well as how these objects should be visualized. This feature allows the
use of Paje for a wide variety of visualizations such as the use of
resources by applications in a large-size cluster or the behavior of
distributed Java applications.

This package contains shared libraries of Paje.

%package -n lib%name-devel
Summary: Development files of Paje
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Paje is an interactive and scalable trace-based visualization tool which
can be used for a large variety of visualizations including performance
monitoring of parallel applications, monitoring the execution of
processors in a large scale PC cluster or representing the behavior of
distributed applications.

Users of Paje can tailor the visualization to their needs, without
having to know any insight nor to modify any component of Paje. This can
be done by defining the type hierarchy of objects to be visualized as
well as how these objects should be visualized. This feature allows the
use of Paje for a wide variety of visualizations such as the use of
resources by applications in a large-size cluster or the behavior of
distributed Java applications.

This package contains development files of Paje.

%package docs
Summary: Documentation for Paje
Group: Documentation
BuildArch: noarch

%description docs
Paje is an interactive and scalable trace-based visualization tool which
can be used for a large variety of visualizations including performance
monitoring of parallel applications, monitoring the execution of
processors in a large scale PC cluster or representing the behavior of
distributed applications.

Users of Paje can tailor the visualization to their needs, without
having to know any insight nor to modify any component of Paje. This can
be done by defining the type hierarchy of objects to be visualized as
well as how these objects should be visualized. This feature allows the
use of Paje for a wide variety of visualizations such as the use of
resources by applications in a large-size cluster or the behavior of
distributed Java applications.

This package contains documentation for Paje.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes

%make_build -C Documentation/UserManual
%make_build -C Documentation/lang-paje
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in General; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/0/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/0/$i
			rm GNUstep/Frameworks/$j.framework/Versions/0/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/0/$j
		done
	done
done
popd

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc NEWS README* TODO
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/General.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/General.framework/Versions/0/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/General.framework/Headers
%_libdir/GNUstep/Frameworks/General.framework/Versions/0/Headers

%files docs
%doc Documentation/UserManual/*.ps Documentation/lang-paje/*.ps

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.98-alt3.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.98-alt3
- Built with clang
- Added menu file (thnx kostyalamer@)

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.98-alt2
- Added Requires: gnustep-back

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.98-alt1
- Initial build for Sisyphus

