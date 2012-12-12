%set_verify_elf_method unresolved=strict

Name: gnustep-projectcenter
Version: 0.6.1
Release: alt1.git20121122
Summary: GNUstep IDE, a part of the GNUstep project and is copyrighted by the FSF
License: GPLv2+ and GPLv3
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-projectcenter.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc

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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'

for i in Aggregate Application Bundle Framework Library ResourceSet \
	Tool ProjectCenter Build Misc
do
	rm -f $(find ./ -name $i -type f)
done
libProjectCenter=$PWD/Framework/ProjectCenter.framework/libProjectCenter.so

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS="$libProjectCenter"
 
%install
%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_SYSTEM_ROOT=%buildroot

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/ProjectCenter.framework/Versions/Current/$i ./
	ln -s %_libdir/$i \
		GNUstep/Frameworks/ProjectCenter.framework/Versions/Current/
done
popd

%files
%doc ChangeLog Documentation/*
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20121122
- Initial build for Sisyphus

