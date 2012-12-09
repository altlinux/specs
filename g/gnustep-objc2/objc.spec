# need because asm used
%set_verify_elf_method textrel=relaxed

%define oname objc2

Name: gnustep-%oname
Version: 1.6.1
Release: alt2.svn20121115
Summary: GNUstep Objective-C Runtime
License: BSD
Group: Development/Objective-C
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/libobjc2/trunk/
Source: %name-%version.tar
Patch: gnustep-objc2-1.6.1-alt-i586.patch

BuildRequires(pre): rpm-macros-make
BuildPreReq: gnustep-make gnustep-make-devel gcc-objc gcc-c++
#BuildPreReq: cmake llvm-devel clang-devel

%description
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.  The modern ABI adds the following features:

%package -n lib%name
Summary: Shared libraries of GNUstep Objective-C Runtime
Group: System/Libraries

%description -n lib%name
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.  The modern ABI adds the following features:

This package contains shared libraries of GNUstep Objective-C Runtime.

%package -n lib%name-devel
Summary: Development files of GNUstep Objective-C Runtime
Group: Development/Objective-C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep Objective-C runtime is designed as a drop-in replacement for
the GCC runtime.  It supports both a legacy and a modern ABI, allowing
code compiled with old versions of GCC to be supported without requiring
recompilation.  The modern ABI adds the following features:

This package contains development files of GNUstep Objective-C Runtime.

%prep
%setup

%ifnarch x86_64
%patch -p1
%endif

cp -fR objc objc2
chmod +x build_opts.sh

%build
./build_opts.sh

%add_optflags -I$PWD %optflags_shared
export CPPFLAGS="%optflags"
%make_build_ext \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	PREFIX=%prefix \
	LIB_DIR=%_libdir \
	HEADER_DIR=%_includedir

%install
%make_install \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	PREFIX=%buildroot%prefix \
	LIB_DIR=%buildroot%_libdir \
	HEADER_DIR=%buildroot%_includedir \
	install

mv %buildroot%_includedir/objc %buildroot%_includedir/objc2

%files -n lib%name
%doc ANNOUNCE* API README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.svn20121115
- Applied patch only for i586

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.svn20121115
- Initial build for Sisyphus

