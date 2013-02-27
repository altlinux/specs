#set_verify_elf_method unresolved=strict

Name: gnustep-ProjectCenter
Version: 0.6.1
Release: alt1
Summary: GNUstep's Integrated Developement Environment (IDE)
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel musl-devel

Requires: lib%name = %EVR

%description
ProjectCenter is GNUstep's Integrated Developement Environment (IDE). It
is based in part on NeXT's original Project Builder application under
OPENSTEP4.2/Mach. It assists you in starting new projects and lets you
manage your project files using a intuitive and well ordered graphical
user interface.

Supporting the project types 'Application', 'Bundle', 'Library', 'Tool',
and 'Aggregate', ProjectCenter automatically creates the project
makefiles and aids you in the process of editing, project compilation,
package building and debugging. In the future, built-in CVS support will
be available, too.

ProjectCenter is a very useable application, but is still evolving.
Support is there for project creation and inspection as well as basic
Makefile generation. Using the 'Application' project type, you can
already create graphical applications using ProjectCenter and Gorm in
conjunction.

%package -n lib%name
Summary: Shared libraries of ProjectCenter
Group: System/Libraries

%description -n lib%name
ProjectCenter is GNUstep's Integrated Developement Environment (IDE). It
is based in part on NeXT's original Project Builder application under
OPENSTEP4.2/Mach. It assists you in starting new projects and lets you
manage your project files using a intuitive and well ordered graphical
user interface.

This package contains shared libraries of ProjectCenter.

%package -n lib%name-devel
Summary: Development files of ProjectCenter
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
ProjectCenter is GNUstep's Integrated Developement Environment (IDE). It
is based in part on NeXT's original Project Builder application under
OPENSTEP4.2/Mach. It assists you in starting new projects and lets you
manage your project files using a intuitive and well ordered graphical
user interface.

This package contains development files of ProjectCenter.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -I%_libdir/musl/include'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in ProjectCenter; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0.6.0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0.6.0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0.6.0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0.6.0/$i
done
popd

%files
%doc ChangeLog Documentation/*
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0.6.0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0.6.0/Headers

%changelog
* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

