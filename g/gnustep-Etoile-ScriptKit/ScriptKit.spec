%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-ScriptKit
Version: 0.1
Release: alt1.git20101123
Summary: Very lightweight cross-app scripting framework
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/ScriptKit.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-Etoile-Languages-devel
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-Languages

%description
ScriptKit is a very lightweight cross-app scripting framework built on
top of Distributed Objects. It simply exports a dictionary containing a
set of named objects for scripting with Objective-C or any languages
based on the LanguageKit such as Pragmatic Smalltalk.

%package -n lib%name
Summary: Shared libraries of ScriptKit
Group: System/Libraries

%description -n lib%name
ScriptKit is a very lightweight cross-app scripting framework built on
top of Distributed Objects. It simply exports a dictionary containing a
set of named objects for scripting with Objective-C or any languages
based on the LanguageKit such as Pragmatic Smalltalk.

This package contains shared libraries of ScriptKit.

%package -n lib%name-devel
Summary: Development files of ScriptKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
ScriptKit is a very lightweight cross-app scripting framework built on
top of Distributed Objects. It simply exports a dictionary containing a
set of named objects for scripting with Objective-C or any languages
based on the LanguageKit such as Pragmatic Smalltalk.

This package contains development files of ScriptKit.

%package docs
Summary: Documentation for ScriptKit
Group: Development/Documentation
BuildArch: noarch

%description docs
ScriptKit is a very lightweight cross-app scripting framework built on
top of Distributed Objects. It simply exports a dictionary containing a
set of named objects for scripting with Objective-C or any languages
based on the LanguageKit such as Pragmatic Smalltalk.

This package contains documentation for ScriptKit.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=ScriptKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=ScriptKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in ScriptKit; do
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

install -d %buildroot%_docdir/GNUstep/ScriptKit
cp -fRP Documentation/* %buildroot%_docdir/GNUstep/ScriptKit/

%files
%doc NEWS README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/ScriptKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/ScriptKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/ScriptKit.framework/Headers
%_libdir/GNUstep/Frameworks/ScriptKit.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20101123
- Initial build for Sisyphus

