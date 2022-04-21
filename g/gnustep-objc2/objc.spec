# need because asm used
%set_verify_elf_method textrel=relaxed
%def_without opts
%def_with clang

%define oname objc2

Name: gnustep-%oname
Version: 2.1
Release: alt3
Summary: GNUstep Objective-C Runtime
License: BSD
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/libobjc2/trunk/
Source: lib%oname-%version.tar
Source1: robin-map.tar
Patch: objc2-fix-generate-eh_trampoline.s.patch

ExcludeArch: armh

BuildRequires(pre): rpm-macros-make
BuildRequires(pre): cmake
BuildRequires: libobjc-devel libstdc++-devel
%if_with clang
BuildRequires: clang-devel
BuildRequires: llvm-devel
%else
BuildRequires: gcc-objc gcc-c++
%endif

%description
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

%package -n lib%name
Summary: Shared libraries of GNUstep Objective-C Runtime
Group: System/Libraries

%description -n lib%name
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains shared libraries of GNUstep Objective-C Runtime.

%package -n lib%name-devel
Summary: Development files of GNUstep Objective-C Runtime
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains development files of GNUstep Objective-C Runtime.

%if_with opts
%package -n lib%name-opts
Summary: Shared libraries of GNUstep Runtime Optimisations
Group: System/Libraries

%description -n lib%name-opts
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains shared libraries of GNUstep Runtime Optimisations.

%package -n lib%name-opts-devel
Summary: Development files of GNUstep Runtime Optimisations
Group: Development/Objective-C
Requires: lib%name-opts = %version-%release

%description -n lib%name-opts-devel
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.

This package contains development files of GNUstep Runtime Optimisations.
%endif

%prep
%setup -n lib%oname-%version
%patch -p1
tar xf %SOURCE1
%if_without clang
# Remove Xclang unsupported by gcc
subst 's/ -Xclang//g' CMakeLists.txt Test/CMakeLists.txt
%endif
cp -fR objc objc2
#chmod +x build_opts.sh

%build
%define optflags_lto %nil
#./build_opts.sh
%add_optflags -I$PWD %optflags_shared -fpermissive
%add_optflags -D__STDC_LIMIT_MACROS -D__STDC_CONSTANT_MACROS
export CPPFLAGS="%optflags"
cmake \
	-DLIB_SUFFIX:STRING=%_libsuff \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_ASM_FLAGS:STRING="%optflags" \
%if_with clang
	-DCMAKE_ASM_COMPILER:FILEPATH='%_bindir/clang' \
	-DCMAKE_C_COMPILER:FILEPATH='%_bindir/clang' \
	-DCMAKE_CXX_COMPILER:FILEPATH='%_bindir/clang++' \
%else
	-DCMAKE_ASM_COMPILER:FILEPATH='%_bindir/cc' \
	-DCMAKE_C_COMPILER:FILEPATH='%_bindir/cc' \
	-DCMAKE_CXX_COMPILER:FILEPATH='%_bindir/g++' \
%endif
	-DLLVM_DIR:PATH='%_datadir/cmake/Modules' \
	-DCMAKE_STRIP:FILEPATH='/bin/true' \
	-DCPACK_STRIP_FILES:BOOL=OFF \
	-DCXX_RUNTIME:FILEPATH='-lpthread -lstdc++' \
	-DGNUSTEP_INSTALL_TYPE:STRING='NONE' \
	-DCMAKE_INSTALL_LIBDIR:STRING='%_lib' \
	-DINCLUDE_DIRECTORY:STRING=objc2 \
	-DLEGACY_COMPAT:BOOL=ON \
	-DLIBOBJC_NAME:STRING=objc2 \
%if_with clang
	-DLLVM_ON_UNIX:BOOL=ON \
%else
	-DLLVM_ON_UNIX:BOOL=OFF \
%endif
	-DLLVM_OPTS:BOOL=FALSE \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DTESTS:BOOL=OFF \
	.

%make_build_ext \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	PREFIX=%prefix \
	LIB_DIR=%_libdir \
	HEADER_DIR=%_includedir

%install
rm -f GNUmakefile
%makeinstall_std \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	install
#	PREFIX=%buildroot%prefix \
#	LIB_DIR=%buildroot%_libdir \
#	HEADER_DIR=%buildroot%_includedir \

sed -i 's|#include "visibility.h"|#include "objc2/visibility.h"|' \
	class.h
#install -p -m644 class.h visibility.h method_list.h ivar.h protocol.h \
#	selector.h sarray2.h category.h \
#	%buildroot%_includedir/objc2/

ln -s objc2 %buildroot%_includedir/objc

# see that headers in libdispath-devel
rm -v %buildroot%_includedir/{Block.h,Block_private.h}

%files -n lib%name
%doc ANNOUNCE* API README.md
%_libdir/*.so.*
%if_with opts
%exclude %_libdir/libGNUObjCRuntime.so.*
%endif

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%if_with opts
%exclude %_includedir/objc2/opts
%exclude %_libdir/libGNUObjCRuntime.so
%endif
%_pkgconfigdir/libobjc.pc

%if_with opts
%files -n lib%name-opts
%doc opts/README
%_libdir/libGNUObjCRuntime.so.*

%files -n lib%name-opts-devel
%_includedir/objc2/opts
%_libdir/libGNUObjCRuntime.so
%endif

%changelog
* Wed Apr 20 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt3
- spec: don't require gcc when clang build
- remove Block.h and Block_private.h headers (check libdispatch-devel)

* Fri Aug 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.1-alt2
- FTBFS: disable LTO.

* Thu Aug 27 2020 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- New version.
- Exclude armh from build architectures.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version.

* Sat Feb 09 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7.0-alt14.svn20140704
- Avoid build cycle with gnustep-make package.

* Tue Oct 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt13.svn20140704
- Fix build with gcc 7.0.
- Exclude aarch64 from supported platform.

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt12.svn20140704
- NMU: changed cmake modules location

* Mon Jan 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt11.svn20140704
- Build with gcc
- Do not package -opts subpackages

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt10.svn20140704
- New snapshot

* Fri Apr 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt10.svn20140227
- Rebuilt with llvm 3.4 (thnx glebfm@)

* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt9.svn20140227
- New snapshot

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt9.svn20140120
- Added symlink objc2 -> %_includedir/objc

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt8.svn20140120
- New snapshot

* Sun Jan 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt8.git20131223
- Added sarray2.h and category.h

* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt7.git20131223
- Added necessary headers

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt6.git20131223
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt6.git20130814
- New snapshot

* Thu Sep 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt6.git20130424
- Fixed build

* Mon Sep  02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt5.git20130424
- fix build with llvm 3.3
- build with clang (thnx glebfm@)

* Thu Aug 29 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7.0-alt5.git20130424
- fix build with llvm 3.3
- build with clang

* Thu Jun 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt4.git20130424
- New snapshot

* Mon Mar 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt4.git20130312
- Set CMAKE_BUILD_TYPE to Release (ALT #28693)

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.git20130312
- New snapshot

* Tue Mar 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.git20130130
- Rebuilt with clang 3.2

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt2.git20130130
- Back to previous snapshot

* Mon Mar 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20130301
- New snapshot
- Rebuilt with clang 3.2

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20130130
- Version 1.7.0

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt6.svn20130112
- Avoid use Method_t

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt5.svn20130112
- New snapshot

* Sun Dec 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt5.svn20121223
- New snapshot
- Built with llvm
- Added libGNUObjCRuntime.so

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt4.svn20121115
- Added synonym: lib%name-devel -> %name-devel

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt3.svn20121115
- Rebuilt with fixed gnustep-make

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.svn20121115
- Applied patch only for i586

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.svn20121115
- Initial build for Sisyphus

