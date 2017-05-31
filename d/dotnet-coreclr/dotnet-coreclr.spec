%def_without bootstrap

%define corerelease 2.0.0-preview1-002111-00
%define pre -preview1
%define shareddir %_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease

Name: dotnet-coreclr
Version: 2.0.0
Release: alt3.preview1

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

BuildRequires: clang

BuildRequires: cmake llvm libstdc++-devel libunwind-devel liblttng-ust-devel liblwp-devel
#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel openssl-devel
BuildRequires: python-modules-xml

%if_with bootstrap
BuildRequires: dotnet-bootstrap
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_libdir/dotnet
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
DOTNET_TOOL_DIR=%bootstrapdir ./build.sh x64 release verbose skipnuget

%install
mkdir -p %buildroot%shareddir/
# TODO: some publish use?
cp -a bin/Product/Linux.x64.Release/{System.Globalization.Native.so,libSystem.Globalization.Native.a,lib*.so,corerun,coreconsole,sosdocsunix.txt} %buildroot%shareddir/

# superpmi mcs
# https://github.com/dotnet/coreclr/tree/master/src/ToolBox/superpmi

# createdump
# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/2.0.0/createdump: RPATH contains illegal entry "/tmp/.private/lav/RPM/BUILD": /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac
# ldd: libmscordaccore.so => /tmp/.private/lav/RPM/BUILD/dotnet-coreclr-2.0.0/bin/obj/Linux.x64.Release/src/dlls/mscordac/libmscordaccore.so
#rm -f %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/createdump

%files
%doc *.TXT THIRD-PARTY-NOTICES README.md CONTRIBUTING.md
%shareddir/System.Globalization.Native.so
%shareddir/libSystem.Globalization.Native.a
%shareddir/lib*.so
%shareddir/corerun
%shareddir/coreconsole
%shareddir/sosdocsunix.txt

%changelog
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
