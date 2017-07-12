%def_without bootstrap
%define corerelease 2.0.0-preview2-25407-01
%define pre -preview2

Name: dotnet
Version: 2.0.0
Release: alt2.preview2

Summary: Installer packages for the .NET Core runtime and libraries

License: MIT
Url: https://github.com/dotnet/core-setup
Group: Development/Other

# Source-url: %url/archive/v%version%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: clang

BuildRequires: cmake llvm libstdc++-devel

BuildRequires: dotnet-common >= %version

Requires: dotnet-common >= %version
Requires: dotnet-coreclr >= %version
Requires: dotnet-corefx >= %version
#Requires: dotnet-sdk >= %version

%if_with bootstrap
BuildRequires: dotnet-bootstrap
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_libdir/dotnet
%endif


%description
This repo contains the code to build the .NET Core runtime,
libraries and shared host (dotnet) installers for all supported platforms.
It does not contain the actual sources to .NET Core runtime;
this source is split across the dotnet/coreclr repo (runtime)
and dotnet/corefx repo (libraries).

%prep
%setup

find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_libdir/dotnet/fake-os-release|g"

%build
#DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap ./build.sh x64 release verbose
cd src/corehost
DOTNET_TOOL_DIR=%bootstrapdir sh -x ./build.sh --arch x64 --hostver %corerelease --apphostver %corerelease --fxrver %corerelease --policyver %corerelease --commithash 0

%install
mkdir -p %buildroot%_libdir/dotnet/
install -m755 src/corehost/cli/exe/dotnet/dotnet %buildroot%_libdir/dotnet/

mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
install -m755 src/corehost/cli/dll/libhostpolicy.so %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/%corerelease/
install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_libdir/dotnet/host/fxr/%corerelease/

mkdir -p %buildroot%_bindir/
ln -sr %buildroot%_libdir/dotnet/dotnet %buildroot%_bindir/dotnet

%files
%doc THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md LICENSE.TXT
%_bindir/dotnet
%_libdir/dotnet/dotnet

%_libdir/dotnet/host/fxr/%corerelease/libhostfxr.so

%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/libhostpolicy.so
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/libhostfxr.so

%changelog
* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packaging

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
