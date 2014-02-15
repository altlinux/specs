%set_verify_elf_method unresolved=strict

Name: gnustep-steptalk
Version: 0.10.0
Release: alt4.svn20140106
Summary: Scripting framework for creating scriptable servers or applications
License: LGPLv2.1+
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/steptalk/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc
BuildPreReq: libreadline-devel libncurses-devel

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

%package -n lib%name
Summary: Shared libraries of StepTalk
Group: System/Libraries

%description -n lib%name
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains shared libraries of StepTalk.

%package -n lib%name-devel
Summary: Development files of StepTalk
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains development files of StepTalk.

%package doc
Summary: Documentation for StepTalk
Group: Development/Documentation
BuildArch: noarch

%description doc
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains documentation for StepTalk.

%package stshell
Summary: Interactive tool for communicating with objects
Group: Development/Tools
Requires: %name = %EVR

%description stshell
StepTalk is a scripting framework for creating scriptable servers or
applications. StepTalk, when combined with the dynamism that the
Objective-C language provides, goes way beyond mere scripting.

This package contains StepTalk Shell, an interactive tool for
communicating with objects.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

buildIt() {
	%make_build \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		CONFIG_SYSTEM_LIBS="-lgnustep-base -lobjc2 -lm $1"
}

buildIt
rm -f $(find ./ -name Smalltalk -type f)
buildIt $PWD/Frameworks/StepTalk/StepTalk.framework/libStepTalk.so
 
mkdir -p /usr/src/GNUstep/Libraries
ln -s $PWD/Frameworks/StepTalk/StepTalk.framework/libStepTalk.so \
	/usr/src/GNUstep/Libraries/
TOPDIR=$PWD
%make_build -C Examples/Shell \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-I$TOPDIR/Frameworks" \
	CONFIG_SYSTEM_LIBS="-lgnustep-base -lobjc2 -lm"

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Examples/Shell GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/StepTalk.framework/Versions/0/$i ./
	for j in *.so.*.*; do
		ln -s %_libdir/$j GNUstep/Frameworks/StepTalk.framework/Versions/0/$i
	done
done
rm -f GNUstep/Frameworks/StepTalk.framework/Versions/0/StepTalk
ln -s %_libdir/$j GNUstep/Frameworks/StepTalk.framework/Versions/0/StepTalk
popd

%files
%doc ChangeLog NEWS README TODO WISH
%_bindir/*
%exclude %_bindir/stshell
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/StepTalk.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/StepTalk.framework//Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/StepTalk.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/StepTalk.framework//Headers

%files doc
%doc Documentation/*

%files stshell
%doc Examples/Shell/README Examples/Shell/*.txt
%_bindir/stshell

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt4.svn20140106
- Built with clang

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt3.svn20140106
- Added stshell

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.svn20140106
- New snapshot

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20131220
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20130630
- New snapshot

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20130302
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2.git20121202
- Rebuilt with libobjc2 instead of libobjc
- Don't require development packages for runtime packages

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20121202
- Initial build for Sisyphus

