%define _unpackaged_files_terminate_build 1

%def_without bootstrap

%define pre %nil

Name: dotnet-coreclr
Version: 2.1.6
Release: alt3

Summary: .NET Core runtime, called CoreCLR, and the base library, called mscorlib

License: MIT
Url: https://github.com/dotnet/coreclr
Group: Development/Other

# Source-url: https://github.com/dotnet/coreclr/archive/v%version%pre.tar.gz
Source: %name-%version.tar
Patch1: 0001-Add-support-for-building-under-glibc-2.26-13785.patch
Patch2: 0001-fix-build-with-clang6.0.patch
Patch3: dotnet-coreclr-alt-not-supported.patch
#Source1: init-tools.sh

ExclusiveArch: x86_64

#add_verify_elf_skiplist *.dbg

# TODO:
# verify-elf: WARNING: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/1.1.1/Linux.x64.Release/libcoreclr.so: eu-elflint failed
# the file containing the function 'CoreDllMain' might not be compiled with -fpic/-fPIC
# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/1.1.1/Linux.x64.Release/libcoreclr.so: TEXTREL entry found: 0x0000000000000000
#set_verify_elf_method relaxed

BuildRequires(pre): rpm-macros-dotnet = %version

BuildRequires: /proc

BuildRequires: clang llvm

BuildRequires: cmake libstdc++-devel libunwind-devel liblttng-ust-devel liblwp-devel
#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel libssl-devel
BuildRequires: python-modules-xml

# it is not linked directly (the same like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

%if_with bootstrap
BuildRequires: dotnet-bootstrap = %version
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common = %version

%description
This package contains the .NET Core runtime, called CoreCLR,
and the base library, called mscorlib.

It includes the garbage collector, JIT compiler,
base .NET data types and many low-level classes.

.NET Core is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

%prep
%setup
#patch1 -p1
#patch2 -p1
%patch3 -p2

# make strange error if uncomment due isMSBuildOnNETCoreSupported initialized
find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_libdir/dotnet/fake-os-release|g"

# TODO: CMake Error: CMake can not determine linker language for target: System.Globalization.Native
#__subst "s|__isMSBuildOnNETCoreSupported=0|__isMSBuildOnNETCoreSupported=1|" build.sh

%build
DOTNET_TOOL_DIR=%bootstrapdir sh -x ./build.sh x64 release verbose skipnuget ignorewarnings skiprestoreoptdata cmakeargs -DENABLE_LLDBPLUGIN=0

# FIXME: possible hack
cat <<EOF >.version
%version-%release
%_dotnet_corerelease
EOF

%install
mkdir -p %buildroot%_dotnet_shared/
# TODO: some publish use?
cp -a bin/Product/Linux.x64.Release/{System.Globalization.Native.so,lib*.so,corerun,coreconsole,createdump,sosdocsunix.txt} %buildroot%_dotnet_shared/

install -D -m644 .version %buildroot%_dotnet_shared/.version

# superpmi mcs
# https://github.com/dotnet/coreclr/tree/master/src/ToolBox/superpmi

# createdump
# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/2.0.0/createdump: RPATH contains illegal entry "/tmp/.private/lav/RPM/BUILD": /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac
# ldd: libmscordaccore.so => /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac/libmscordaccore.so
#rm -f %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%_dotnet_corerelease/createdump

%triggerpostun -- %name <= %version
# remove obsoleted empty dirs (see discussion at https://github.com/dotnet/sdk/issues/2772)
rmdir %_dotnetdir/shared/Microsoft.NETCore.App/* 2>/dev/null || :

%files
%doc CODE_OWNERS.TXT LICENSE.TXT PATENTS.TXT THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md
%dir %_dotnet_shared/
%_dotnet_shared/.version
%_dotnet_shared/System.Globalization.Native.so
%_dotnet_shared/lib*.so
%_dotnet_shared/corerun
%_dotnet_shared/createdump
%_dotnet_shared/coreconsole
%_dotnet_shared/sosdocsunix.txt

%changelog
* Wed Dec 26 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt3
- drop obsoleted empty dir from shared/Microsoft.NETCore.App/

* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- move versioned dirs to the appropriate packages

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5) (based on changes by lav@)

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version (2.1.4) with rpmgs script

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- .NET Core 2.1.3 LTS

* Sun May 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt2
- rebuild with llvm 6.0
- set libicu60 require

* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786
- backport patch: Add support for building under glibc 2.26

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core 2.0.0 Release

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- .NET Core 2.0.0 Preview 2 (2.0.0-preview2-25407-01)
- pack missed createdump

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview1
- strict packing

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial release for ALT Sisyphus
