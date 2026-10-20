%define _unpackaged_files_terminate_build 1
# Upstream sets no SONAME and promises no stable ABI, so ALT keeps its own
# library version MAJOR.MINOR.PATCH (file libpdfium.so.%%abiversion,
# SONAME libpdfium.so.%%soname = MAJOR). On every update compare the public
# API/ABI (public/*.h, exported FPDF*/FORM_*/FSDK* symbols) with the previous
# build and bump:
#   MAJOR - incompatible ABI change (removed symbol, changed signature or
#           struct layout): new SONAME, package lib%%name<MAJOR> with
#           Obsoletes per Shared Libs Policy, rebuild/check consumers
#           (naps2 dlopen()s libpdfium.so.0);
#   MINOR - only new functions/fields added compatibly (reset PATCH to 0),
#           or changes limited to functions marked "Experimental API" in
#           public/*.h (8076: FPDFCatalog_SetLanguage takes FPDF_WIDESTRING);
#   PATCH - no public API/ABI change.
%define soname 0
%define abiversion 0.2.1
%define targetdir out/Release
%define llvm_ver 21.1
%define clang_major 21
Summary: PDF rendering library
Name: pdfium
# chromium/NNNN branch of pdfium
Version: 8076
Release: alt1
License: Apache-2.0
Group: System/Base
Url: https://pdfium.googlesource.com/pdfium/
Source: %name-%version.tar
Source1: bundles_build.tar
Source2: third_party.tar
Source3: base.tar
Source4: buildtools.tar

ExcludeArch: %ix86 %arm ppc64le

BuildRequires: gn python3 llvm%llvm_ver clang%llvm_ver clang%llvm_ver-support
BuildRequires: pkg-config libstdc++-devel gcc-c++
BuildRequires: liblcms2-devel glib2-devel libjpeg-devel libpng-devel
BuildRequires: libopenjpeg2.0-devel ninja-build libgio-devel
BuildRequires: libfreetype-devel libharfbuzz-devel rpm-macros-ninja-build
BuildRequires: /proc

Patch1: alt_fix_build_config.patch
Patch2: alt_add_sover.patch
Patch3: alt_dont_strip_static_lib_symbols.patch
Patch4: alt_fix_debug_info_pathes.patch
Patch5: alt_disable_rpath.patch
Patch8: alt_force_build_pdfium_as_shared.patch
Patch9: alt-force_export_public_symbols.patch
Patch10: alt_clang21_compat.patch
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
%setup -a0 -a1 -a2 -a3 -a4
%patch1
%patch2
%patch3
%patch4
%patch5
#%%patch6
%patch8
%patch9
%patch10

mkdir -p %targetdir
sed -e 's|@LLVM_VERSION@|%llvm_ver|; s|@CLANG_MAJOR@|%clang_major|' \
    .gear/args.gn > %targetdir/args.gn
sed -i 's|spec_soversion|%soname|g; s|spec_abiversion|%abiversion|g' \
build/toolchain/gcc_toolchain.gni
#sed -i "s|spec_test_resources_dir|$PWD/testing/resources|g" \
#testing/utils/path_service.cpp
gn gen --script-executable=%__python3 %targetdir

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
install -m 644 %targetdir/libpdfium.so.%abiversion  \
    %buildroot%_libdir
install -m 755 %targetdir/pdfium_test   \
    %buildroot%_bindir
install -d -m 755 pdfium  %buildroot%_includedir/pdfium
cp public/*.h  %buildroot%_includedir/pdfium
cp public/README  %buildroot%_includedir/pdfium
cp -R public/cpp  %buildroot%_includedir/pdfium
pushd  %buildroot%_libdir
ln -s libpdfium.so.%abiversion libpdfium.so.%soname
ln -s libpdfium.so.%soname libpdfium.so
popd

%check
ln -sf libpdfium.so.%abiversion %targetdir/libpdfium.so.%soname
export LD_LIBRARY_PATH=$PWD/%targetdir:$LD_LIBRARY_PATH
# fails with libstdc++ (expects libc++ std::set behaviour)
out/Release/pdfium_unittests --gtest_filter=-RetainPtr.SetContains

%files -n lib%name%soname
%_libdir/libpdfium.so.%soname
%_libdir/libpdfium.so.%abiversion

%files -n lib%name-devel
%_libdir/libpdfium.so
%_includedir/pdfium/*

%files -n %name-test
%_bindir/pdfium_test

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 8076-alt1
- NMU: update to chromium/8076 branch (needed by python3-module-pypdfium2 5.x).
- Build with system clang 21, system harfbuzz, without PartitionAlloc
  (libpdfium no longer exports malloc/free).
- Build with LLVM 21, add BuildRequires libharfbuzz-devel and libpng-devel.
- Add own library ABI version 0.2.1 (libpdfium.so.0.2.1, SONAME
  libpdfium.so.0 kept: new functions added, only the experimental
  FPDFCatalog_SetLanguage changed; MAJOR.MINOR.PATCH rule in spec).

* Thu Jan 30 2025 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build

