%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-Languages
Version: 0.6
Release: alt3.git20140226
Summary: Abstract syntax tree and compilation framework
License: MIT / BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/Languages.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator llvm-devel-static
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel gcc-c++
BuildPreReq: gnustep-Etoile-SourceCodeKit-devel lemon

Requires: lib%name = %EVR
Requires: gnustep-back
Requires: gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-SourceCodeKit

%description
LanguageKit provides the abstract syntax tree and compilation framework
for Etoile Pragmatic Smalltalk and EScript.  LanguageKit is split into
three main components:

- The core LanguageKit framework provides the abstract syntax tree
  structure that front ends (such as Pragmatic Smalltalk) construct and
  manipulate.  It also contains an AST interpreter.
- The Runtime subframework provides a runtime library for code generated
  by LanguageKit.  This sits on top of the Objective-C runtime and
  provides extra features, such as non-local returns and small integers.
- The CodeGen framework uses LLVM to generate optimised native code from
  LanguageKit abstract syntax trees.

%package -n lib%name
Summary: Shared libraries of LanguageKit
Group: System/Libraries

%description -n lib%name
LanguageKit provides the abstract syntax tree and compilation framework
for Etoile Pragmatic Smalltalk and EScript.

This package contains shared libraries of LanguageKit.

%package -n lib%name-devel
Summary: Development files of LanguageKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR
Requires: gnustep-Etoile-EtoileFoundation-devel
Requires: gnustep-Etoile-SourceCodeKit-devel

%description -n lib%name-devel
LanguageKit provides the abstract syntax tree and compilation framework
for Etoile Pragmatic Smalltalk and EScript.

This package contains development files of LanguageKit.

%package docs
Summary: Documentation for LanguageKit
Group: Development/Documentation
BuildArch: noarch

%description docs
LanguageKit provides the abstract syntax tree and compilation framework
for Etoile Pragmatic Smalltalk and EScript.

This package contains documentation for LanguageKit.

%prep
%setup

mkdir -p /usr/src/GNUstep/Headers
ln -s $PWD/LanguageKit/Runtime \
	/usr/src/GNUstep/Headers/LanguageKitRuntime

cp %_libdir/GNUstep/Etoile/* $PWD/../
prepare_docgen
ln -s ../Developer $PWD/../

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll
export LD_LIBRARY_PATH=$LD_LIBRARY_PAYH:$PWD/LanguageKit/Runtime/LanguageKitRuntime.framework/Versions/Current

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	AUXILIARY_CPPFLAGS="-I$PWD"

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in LanguageKit LanguageKitCodeGen LanguageKitRuntime \
	SmalltalkSupport
do
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

install -d %buildroot%_docdir/GNUstep/Languages
cp -fRP LanguageKit/Documentation \
	%buildroot%_docdir/GNUstep/Languages/LanguageKit
cp -fRP LanguageKit/Runtime/Documentation \
	%buildroot%_docdir/GNUstep/Languages/LanguageKitRuntime
cp -fRP LanguageKit/CodeGen/Documentation \
	%buildroot%_docdir/GNUstep/Languages/LanguageKitCodeGen

cp LanguageKit/README README.LanguageKit
cp Compiler/README README.Compiler
cp Compiler/HACKING HACKING.Compiler
cp Smalltalk/README README.Smalltalk

install -d %buildroot%_man1dir
install -m644 Compiler/*.1 %buildroot%_man1dir/

%files
%doc README* HACKING*
%_bindir/*
%_man1dir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/LanguageKit.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/LanguageKitCodeGen.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/LanguageKitRuntime.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/SmalltalkSupport.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/LanguageKit.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/LanguageKitCodeGen.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/LanguageKitRuntime.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/SmalltalkSupport.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Fri Apr 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3.git20140226
- Rebuilt with llvm 3.4 (thnx glebfm@)

* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.git20140226
- Added documentation

* Wed Mar 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20140226
- Initial build for Sisyphus

