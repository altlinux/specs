%define MAJOR_VERSION     3
%define MINOR_VERSION     29
%define BUILD_NUMBER      88
%define PATCH_LEVEL       17
%define soversion %MAJOR_VERSION.%MINOR_VERSION
%define libname libv8
%def_without tests

Name:    v8-%MAJOR_VERSION.%MINOR_VERSION
Version: %MAJOR_VERSION.%MINOR_VERSION.%BUILD_NUMBER.%PATCH_LEVEL
Release: alt1

Summary: V8 is Google's open source JavaScript engine.
License: BSD
Group:   System/Libraries
Url:     http://code.google.com/p/v8

Source:  %name-%version.tar
BuildPreReq: gcc-c++ gyp
BuildRequires: python-modules-multiprocessing

Provides: %libname

%description
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used
in Google Chrome, the open source browser from Google. V8 implements ECMAScript
as specified in ECMA-262, 5rd edition.

%package -n lib%name
Summary: Google's JavaScript Engine
License: BSD
Group:   System/Libraries
Provides: %libname = %version
Provides: %libname = %MAJOR_VERSION.%MINOR_VERSION
Obsoletes: %libname = %MAJOR_VERSION.%MINOR_VERSION

%description -n lib%name
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used
in Google Chrome, the open source browser from Google. V8 implements ECMAScript
as specified in ECMA-262, 5rd edition.

%package -n lib%name-devel
Group:   Development/C++
Summary: Development headers and libraries for V8
Requires: lib%name = %version-%release
Provides: %libname-devel = %version
Provides: %libname-devel = %MAJOR_VERSION.%MINOR_VERSION
Conflicts: %libname-devel < %MAJOR_VERSION.%MINOR_VERSION

%description -n lib%name-devel
Development headers and libraries for V8.


%prep
%setup -q
sed -i 's|build/gyp/gyp|gyp|g' Makefile
#sed -i "s|'-Wno-unused-but-set-variable'||g" SConstruct

%build
GYPFLAGS='-Duse_system_icu=0' 
%make_build native \
	    mode=release \
	    library=shared \
	    snapshot=on \
	    i18nsupport=off \
	    soname_version=%{soversion} \
	    V=1 \
%ifarch armh
	    armfloatabi=hard
%endif


%install
mkdir -p %buildroot{%_libdir,%_bindir,%_includedir}
install -p -m755 out/native/d8 %buildroot%_bindir/
install -p -m644 out/native/lib.target/libv8.so.%soversion %buildroot%_libdir/
ln -s libv8.so.%soversion %buildroot%_libdir/libv8.so
install -p -m644 include/*.h %buildroot%_includedir/

%check
%if_with tests
# TODO: need depot_tools in PATH
LD_LIBRARY_PATH=out/Release/lib.target tools/run-tests.py \
		--no-presubmit \
		--outdir=out \
		--buildbot \
		--arch=native \
		--mode=Release \
		--progress=dots
%endif

%files -n lib%name
%doc AUTHORS ChangeLog LICENSE LICENSE.*
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_bindir/*

%changelog
* Fri Nov 21 2014 Andrey Cherepanov <cas@altlinux.org> 3.29.88.17-alt1
- Build for Sisyphus

