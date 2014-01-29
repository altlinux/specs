%set_verify_elf_method unresolved=strict

Name: gnustep-Backbone
Version: 0.1.0
Release: alt3.git20140115
Summary: Backbone is an attempt (our attempt) at creating a Really Good Desktop
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/backbone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.savannah.nongnu.org/backbone.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-gorm-devel

Requires: lib%name = %EVR
Requires: gnustep-back

Conflicts: gnustep-terminal
Conflicts: gnustep-TextEdit

%description
Backbone is an attempt (our attempt) at creating a Really Good Desktop.
The metric we use for "Really Good" is our own. In short, to us, Really
Good means to carry on the NeXTSTEP(R) and OPENSTEP(R) spirit.

%package -n lib%name
Summary: Shared libraries of Backbone
Group: System/Libraries

%description -n lib%name
Backbone is an attempt (our attempt) at creating a Really Good Desktop.
The metric we use for "Really Good" is our own. In short, to us, Really
Good means to carry on the NeXTSTEP(R) and OPENSTEP(R) spirit.

This package contains shared libraries of Backbone.

%package -n lib%name-devel
Summary: Development files of Backbone
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Backbone is an attempt (our attempt) at creating a Really Good Desktop.
The metric we use for "Really Good" is our own. In short, to us, Really
Good means to carry on the NeXTSTEP(R) and OPENSTEP(R) spirit.

This package contains development files of Backbone.

%prep
%setup

%build
cd System

./bootstrap
%configure

%install
cd System
export INSTALL_DIR=%buildroot%_libdir/GNUstep

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -DHAVE_CONFIG_H' \
	CONFIG_SYSTEM_LIBS='-lutil -lgnustep-gui -lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
install -d %buildroot%_libdir/GNUstep/Colors

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	ADDITIONAL_INSTALL_DIRS=%buildroot%_libdir/GNUstep \

pushd %buildroot%_libdir
for j in BBAppKit PrefsModule; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

%files
%doc AUTHORS
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/BBAppKit.framework/Versions/2014A/Headers
%exclude %_libdir/GNUstep/Frameworks/PrefsModule.framework/Versions/1.2.0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/BBAppKit.framework/Versions/2014A/Headers
%_libdir/GNUstep/Frameworks/PrefsModule.framework/Versions/1.2.0/Headers

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3.git20140115
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.git20140115
- Added explicit conflict with gnustep-terminal and gnustep-TextEdit

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140115
- Initial build for Sisyphus

