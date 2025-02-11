%define _unpackaged_files_terminate_build 1
%define soname 0
%define targetdir out/Release
Summary: PDF rendering library
Name: pdfium
Version: 0.1
Release: alt1
License: Apache-2.0
Group: System/Base
Url: https://pdfium.googlesource.com/pdfium/
Source: %name-%version.tar
Source1: bundles_build.tar
Source2: third_party.tar
Source3: base.tar

ExcludeArch: %ix86 %arm ppc64le

BuildRequires: gn python3 llvm18.1 lld18.1 clang18.1 pkg-config libstdc++-devel
BuildRequires: pkg-config liblcms2-devel glib2-devel libjpeg-devel
BuildRequires: libopenjpeg2.0-devel ninja-build libgio-devel
BuildRequires: libfreetype-devel rpm-macros-ninja-build
BuildRequires: clang18.1-support gcc-c++
BuildRequires: /proc

Patch0: alt_use_system_libs.patch
Patch1: alt_fix_build_config.patch
Patch2: alt_add_sover.patch
Patch3: alt_dont_strip_static_lib_symbols.patch
Patch4: alt_fix_debug_info_pathes.patch
Patch5: alt_disable_rpath.patch
Patch7: alt-disable_arm_llvm_key.patch
Patch8: alt_force_build_pdfium_as_shared.patch
Patch9: alt-force_export_public_symbols.patch
#this is patch is needed to run the unit_tests without mounting /proc
#Patch6: alt_fix_testing_utils_pathes_lookup.patch

%description
PDF rendering library

%package -n lib%name%soname
Summary:PDF rendering library
Group: System/Libraries

%description -n lib%name%soname
PDF rendering library

%package -n lib%name-devel
Summary: Development files for the Pdfium library
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
Development files for the Pdfium library

%package -n %name-test
Summary: Unit tests for the Pdfium library
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n %name-test
Test CLI application for the Pdfium library

%prep
%setup -a0 -a1 -a2 -a3
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
#%%patch6
%patch7
%patch8
%patch9

mkdir -p %targetdir
cp .gear/args.gn %targetdir
sed -i 's|spec_soversion|%soname|g' \
build/toolchain/gcc_toolchain.gni
#sed -i "s|spec_test_resources_dir|$PWD/testing/resources|g" \
#testing/utils/path_service.cpp
gn gen %targetdir

%build
%ninja_build  -C %targetdir pdfium pdfium_all  --verbose
find ./public -name "*.h" | while read file; do
    sed -i 's|public|pdfium|g' "$file"
done

%install
pwd
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
mkdir -p %buildroot%_bindir
install -m 644 %targetdir/libpdfium.so.%soname  \
    %buildroot%_libdir
install -m 755 %targetdir/pdfium_test   \
    %buildroot%_bindir
install -d -m 755 pdfium  %buildroot%_includedir/pdfium
cp public/*.h  %buildroot%_includedir/pdfium
cp public/README  %buildroot%_includedir/pdfium
cp -R public/cpp  %buildroot%_includedir/pdfium
pushd  %buildroot%_libdir
ln -rs libpdfium.so.%soname libpdfium.so
popd

%check
export LD_LIBRARY_PATH=$PWD/%targetdir:$LD_LIBRARY_PATH
out/Release/pdfium_unittests

%files -n lib%name%soname
%_libdir/libpdfium.so.%soname

%files -n lib%name-devel
%_libdir/libpdfium.so
%_includedir/pdfium/*

%files -n %name-test
%_bindir/pdfium_test

%changelog
* Thu Jan 30 2025 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build

