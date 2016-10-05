%define MAJOR_VERSION     5
%define MINOR_VERSION     1
%define BUILD_NUMBER      281
%define PATCH_LEVEL       75
%define soversion %MAJOR_VERSION.%MINOR_VERSION
%define libname libv8
%def_without tests

Name:    v8-nodejs
Version: %MAJOR_VERSION.%MINOR_VERSION.%BUILD_NUMBER.%PATCH_LEVEL
Release: alt1

Summary: V8 is Google's open source JavaScript engine (build for NodeJS)
License: BSD
Group:   System/Libraries
Url:     http://code.google.com/p/v8

Source:  %name-%version.tar
Source1: gyp.tar
Source2: icu.tar
Source3: buildtools.tar
Source4: gtest.tar
Source5: gmock.tar
Source6: swarming_client.tar
Source7: trace_event.tar
Source8: test262_data.tar

Patch1:  v8-alt-fix-isolate-on-ia32.patch

BuildPreReq: gcc-c++ gyp
BuildRequires: python-modules-multiprocessing
BuildRequires: python-modules-logging

Provides: %libname

%description
V8 is Google's open source JavaScript engine. V8 is written in C++ and
is used in Google Chrome, the open source browser from Google. V8
implements ECMAScript as specified in ECMA-262, 5rd edition.

%package -n lib%name
Summary: Google's JavaScript Engine
License: BSD
Group:   System/Libraries
Provides: %libname = %version
Provides: %libname = %MAJOR_VERSION.%MINOR_VERSION

%description -n lib%name
V8 is Google's open source JavaScript engine. V8 is written in C++ and
is used in Google Chrome, the open source browser from Google. V8
implements ECMAScript as specified in ECMA-262, 5rd edition.

%package -n lib%name-devel
Group:   Development/C++
Summary: Development headers and libraries for V8
Requires: lib%name = %version-%release
Provides: %libname-devel = %version
Provides: %libname-devel = %MAJOR_VERSION.%MINOR_VERSION
Conflicts: %libname-devel < %MAJOR_VERSION.%MINOR_VERSION
Conflicts: libv8-chromium-devel

%description -n lib%name-devel
Development headers and libraries for V8.

%prep
%setup -q
tar xf %SOURCE1
tar xf %SOURCE2
tar xf %SOURCE3
tar xf %SOURCE4
tar xf %SOURCE5
tar xf %SOURCE6
tar xf %SOURCE7
tar xf %SOURCE8
sed -i 's|build/gyp/gyp|gyp|g' Makefile
%patch1 -p1

%build
build/gyp_v8 \
	-Duse_system_icu=0 \
	-Dclang=0 \
	-Dhost_clang=0 \
	-Dcomponent=shared_library \
	-Dv8_use_snapshot=true \
	-Dv8_use_external_startup_data=1 \
	-Dv8_enable_i18n_support=0 \
	-Dwerror='' \
	-Dsoname_version=%{soversion}

%make_build -C out \
	BUILDTYPE=Release \
	V=1 \
%ifarch armh
	armfloatabi=hard
%endif

%install
mkdir -p %buildroot{%_libdir/v8,%_bindir,%_includedir}
install -p -m644 out/Release/lib.target/libv8.so.%soversion %buildroot%_libdir/
ln -s libv8.so.%soversion %buildroot%_libdir/libv8.so
install -p -m644 include/*.h %buildroot%_includedir/

%check
%if_with tests
# need depot_tools in PATH
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

%changelog
* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 5.1.281.75-alt1
- Initial build  to Sisyphus (ALT #32573)
