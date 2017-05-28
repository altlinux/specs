%def_with bootstrap

%define corerelease 2.0.0-preview1-002111-00
%define pre -preview1

Name: dotnet-coreclr
Version: 2.0.0
Release: alt1.preview1

Summary: .NET Core runtime, called CoreCLR, and the base library, called mscorlib

License: MIT
Url: https://github.com/dotnet/coreclr
Group: Development/Other

# Source-url: https://github.com/dotnet/coreclr/archive/v%version%pre.tar.gz
Source: %name-%version.tar

#Source1: init-tools.sh

ExclusiveArch: x86_64

#add_verify_elf_skiplist *.dbg

# TODO:
# verify-elf: WARNING: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/1.1.1/Linux.x64.Release/libcoreclr.so: eu-elflint failed
# the file containing the function 'CoreDllMain' might not be compiled with -fpic/-fPIC
# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/1.1.1/Linux.x64.Release/libcoreclr.so: TEXTREL entry found: 0x0000000000000000
#set_verify_elf_method relaxed

BuildRequires: clang = 3.8.0

BuildRequires: cmake llvm libstdc++-devel libunwind-devel liblttng-ust-devel liblwp-devel
#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel openssl-devel
BuildRequires: python-modules-xml

%if_with bootstrap
BuildRequires: dotnet-bootstrap
%else
BuildRequires: dotnet
%endif


Requires: dotnet-common >= %version

%description
This package contains the .NET Core runtime, called CoreCLR,
and the base library, called mscorlib.

It includes the garbage collector, JIT compiler,
base .NET data types and many low-level classes.

.NET Core is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

%prep
%setup

# make strange error if uncomment due isMSBuildOnNETCoreSupported initialized
#find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_libdir/dotnet/fake-os-release|g"

# TODO: CMake Error: CMake can not determine linker language for target: System.Globalization.Native
%__subst "s|__isMSBuildOnNETCoreSupported=0|__isMSBuildOnNETCoreSupported=1|" build.sh

# temp. disable lldb using
%__subst "s|add_subdirectory(src/ToolBox/SOS/lldbplugin)||" CMakeLists.txt

%build
DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap ./build.sh x64 release verbose skipnuget

%install
mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
cp -a bin/Product/Linux.x64.Release/* %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/

# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/2.0.0/createdump: RPATH contains illegal entry "/tmp/.private/lav/RPM/BUILD": /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac
rm -f %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/createdump

%files
%doc *.TXT THIRD-PARTY-NOTICES README.md CONTRIBUTING.md
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/*

%changelog
* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial release for ALT Sisyphus
