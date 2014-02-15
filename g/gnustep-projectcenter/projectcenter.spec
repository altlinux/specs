%set_verify_elf_method unresolved=strict

Name: gnustep-projectcenter
Version: 0.6.1
Release: alt5.svn20140117
Summary: GNUstep IDE, a part of the GNUstep project and is copyrighted by the FSF
License: GPLv2+ and GPLv3
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/apps/projectcenter/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
Project Center is the GNUstep equivalent to Project Builder (later
Xcode). This application is used to create and manage projects built
using GNUstep.

%package -n lib%name
Summary: Shared libraries of GNUstep Project Center
Group: System/Libraries

%description -n lib%name
Project Center is the GNUstep equivalent to Project Builder (later
Xcode). This application is used to create and manage projects built
using GNUstep.

This package contains shared libraries of GNUstep Project Center.

%package -n lib%name-devel
Summary: Development files of GNUstep Project Center
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
Project Center is the GNUstep equivalent to Project Builder (later
Xcode). This application is used to create and manage projects built
using GNUstep.

This package contains development files of GNUstep Project Center.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_SYSTEM_ROOT=%buildroot

pushd %buildroot%_libdir
rm -f GNUstep/Frameworks/ProjectCenter.framework/Versions/0.6.0/ProjectCenter
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/ProjectCenter.framework/Versions/0.6.0/$i ./
	for j in *.so.*.*; do
		ln -s %_libdir/$j \
			GNUstep/Frameworks/ProjectCenter.framework/Versions/0.6.0/$i
	done
done
ln -s %_libdir/$j \
	GNUstep/Frameworks/ProjectCenter.framework/Versions/0.6.0/ProjectCenter
popd

install -Dp -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog Documentation/*
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/ProjectCenter.framework/Versions/0.6.0/Headers
%exclude %_libdir/GNUstep/Frameworks/ProjectCenter.framework//Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/ProjectCenter.framework/Versions/0.6.0/Headers
%_libdir/GNUstep/Frameworks/ProjectCenter.framework//Headers

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt5.svn20140117
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.svn20140117
- New snapshot

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.git20131217
- New snapshot

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.git20130225
- New snapshot

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.git20121122
- Added menu file (thnx kostyalamer@)

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.git20121122
- Rebuilt with libobjc2 instead of libobjc
- Don't require development packages for runtime packages

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2.git20121122
- Added synonym: lib%name-devel -> %name-devel

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20121122
- Initial build for Sisyphus

