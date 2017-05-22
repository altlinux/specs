%define pre -preview1

Name: dotnet
Version: 2.0.0
Release: alt0.preview1

Summary: Installer packages for the .NET Core runtime and libraries

License: MIT
Url: https://github.com/dotnet/core-setup
Group: Development/Other

# Source-url: %url/archive/v%version%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: clang = 3.8.0

BuildRequires: cmake llvm libstdc++-devel

BuildRequires: dotnet-common >= %version

Requires: dotnet-common >= %version
Requires: dotnet-coreclr >= %version
Requires: dotnet-corefx >= %version
Requires: dotnet-sdk >= %version

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
DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap sh -x ./build.sh --arch x64 --hostver %version%pre --apphostver %version%pre --fxrver %version%pre --policyver %version%pre --commithash 0

%install
mkdir -p %buildroot%_libdir/dotnet/
install -m755 src/corehost/cli/exe/dotnet/dotnet %buildroot%_libdir/dotnet/

mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/
install -m755 src/corehost/cli/dll/libhostpolicy.so %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/
install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/%version%pre/
install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_libdir/dotnet/host/fxr/%version%pre/

mkdir -p %buildroot%_bindir/
ln -sr %buildroot%_libdir/dotnet/dotnet %buildroot%_bindir/dotnet

%files
%doc THIRD-PARTY-NOTICES README.md CONTRIBUTING.md LICENSE
%_bindir/dotnet
%_libdir/dotnet/dotnet

%_libdir/dotnet/host/fxr/%version%pre/libhostfxr.so

%_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/libhostpolicy.so
%_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/libhostfxr.so

%changelog
* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
