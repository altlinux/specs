# TODO: fix nuget to operate offline
%def_with prebuild

%define _dotnet_corerelease 6.0*

Name: powershell
Version: 7.3.1
Release: alt1

Summary: PowerShell for every system!

License: MIT
Url: https://github.com/PowerShell/PowerShell
Group: Development/Other

# Source-url: https://github.com/PowerShell/PowerShell/archive/v%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/PowerShell/PowerShell/releases/download/v%version/powershell-%version-linux-x64-fxdependent.tar.gz
Source1: %name-prebuild-%version.tar

Source2: %name.1
Source3: Microsoft.PowerShell.SDK.csproj.TypeCatalog.targets

ExclusiveArch: %_dotnet_archlist

BuildRequires(pre): rpm-macros-dotnet >= 6.0

AutoReq:yes,nonodejs,nonodejs_native,nomono,nomonolib,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

Requires: dotnet-6.0

BuildRequires: cmake gcc-c++
BuildRequires: dotnet-sdk-6.0


# >= 1.2.100035
Requires: libomi >= 1.2.0
Requires: libpsrp >= 1.4.4
Requires: libpsl-native
#BuildRequires: libpsrp
#BuildRequires: libpsl-native

#if_without prebuild
# local nuget cache
#BuildRequires: nuget-packages >= 20170602
#endif

BuildRequires: /proc

%description
PowerShell is a cross-platform (Windows, Linux, and macOS) automation and configuration tool/framework
that works well with your existing tools and is optimized for dealing with structured data
(e.g. JSON, CSV, XML, etc.), REST APIs, and object models. It includes a command-line shell,
an associated scripting language and a framework for processing cmdlets.

%prep
%setup -a1

%build
%if_without prebuild
#export NUGET_PACKAGES=$(pwd)/nuget
#export NUGET_FALLBACK_PACKAGES=$(pwd)/nuget-fallback

# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=powershell
export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=true
export DOTNET_CLI_TELEMETRY_OPTOUT=true
subst "s|git describe --abbrev=60 --long|echo %version-%release|" PowerShell.Common.props

## Restore
dotnet restore src/powershell-unix
dotnet restore src/ResGen
dotnet restore src/TypeCatalogGen

## Setup the build target to gather dependency information (see Start-TypeGen function in build.psm1)
cp %SOURCE3 src/Microsoft.PowerShell.SDK/obj/Microsoft.PowerShell.SDK.csproj.TypeCatalog.targets
dotnet msbuild src/Microsoft.PowerShell.SDK/Microsoft.PowerShell.SDK.csproj /t:_GetDependencies "/property:DesignTimeBuild=true;_DependencyFile=$(pwd)/src/TypeCatalogGen/powershell.inc" /nologo

## Generate 'powershell.version'
echo %version-%release >powershell.version

## create the telemetry flag file
touch "DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY"

## Generate resource binding C# files
pushd src/ResGen
dotnet run
popd

## Generate 'CorePsTypeCatalog.cs'
pushd src/TypeCatalogGen
dotnet run ../System.Management.Automation/CoreCLR/CorePsTypeCatalog.cs powershell.inc
popd

## Build powershell core
dotnet publish --configuration Linux "src/powershell-unix/" --output bin --runtime "%_dotnet_rid"

# TODO: generate man from assets/powershell.1.ronn
%endif

%install
%if_with prebuild
mkdir -p %buildroot%_libdir/%name/
cp -a %name-prebuild/* %buildroot%_libdir/%name/
rm -rfv %buildroot%_libdir/%name/runtimes/{linux-,win,osx,freebsd}*
rm -fv %buildroot%_libdir/%name/{libcrypto.so.1.0.0,libssl.so.1.0.0}
mkdir -p %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/
# hack to use latest runtime
#__subst "s|2.0.0-preview1-002111-00|%_dotnet_corerelease|g" %buildroot%_libdir/%name/powershell.runtimeconfig.json
#cp -f %_libdir/libpsl-native.so %buildroot%_libdir/%name/
rm -f %buildroot%_libdir/%name/DELETE_ME_TO_DISABLE_CONSOLEHOST_TELEMETRY

# replace binary pwsh
#mkdir -p %buildroot%_libdir/%name/
cat <<EOF >%buildroot%_libdir/%name/pwsh
#!/bin/sh
exec dotnet %_libdir/%name/pwsh.dll "\$@"
EOF

# replace binary Microsoft.PowerShell.GlobalTool.Shim
cat <<EOF >%buildroot%_libdir/%name/Microsoft.PowerShell.GlobalTool.Shim
#!/bin/sh
exec dotnet %_libdir/%name/Microsoft.PowerShell.GlobalTool.Shim.dll "\$@"
EOF

#chmod 0755 %buildroot%_libdir/%name/pwsh

# replace downloaded libs with system versions

ln -sf %_libdir/libmi.so %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/libmi.so
#ln -sf %_libdir/libpsrpclient.so %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/libpsrpclient.so
#ln -sf %_libdir/libpsl-native.so %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/libpsl-native.so
cp -a %_dotnet_coreapp/libSystem.IO.Ports.Native.so %buildroot%_libdir/%name/runtimes/%_dotnet_rid/native/libSystem.IO.Ports.Native.so

%else
#dotnet publish --configuration Linux src/powershell-unix/ --output %buildroot%_libdir/%name/ --runtime linux-x64
#dotnet publish --configuration Linux src/powershell-unix/ --output %buildroot%_libdir/%name/
# cp -a bin/* %buildroot%_libdir/%name/
%endif

mkdir -p %buildroot%_man1dir/
cp %SOURCE2 %buildroot%_man1dir/

mkdir -p %buildroot%_bindir/
ln -s %_libdir/%name/pwsh %buildroot%_bindir/pwsh
ln -s pwsh %buildroot%_bindir/%name

%files
%_bindir/%name
%_bindir/pwsh
%_libdir/%name/
%_man1dir/%name.*
%doc docs/*

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 7.3.1-alt1
- new version 7.3.1 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.6-alt1
- new version 7.2.6 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.5-alt1
- new version 7.2.5 (with rpmrb script)

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.2-alt1
- new version 7.2.2 (with rpmrb script)

* Sat Feb 12 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.1-alt1
- new version (7.2.1) with rpmgs script

* Sat Feb 20 2021 Vitaly Lipatov <lav@altlinux.ru> 7.1.2-alt1
- new version 7.1.2 (with rpmrb script)

* Sat Dec 28 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt8
- enable aarch64 build
- add disabled ctest for libpsl-native
- drop script coreclr version

* Tue Dec 17 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt7
- rebuild with .NET Core 3.1
- disable -Werror

* Wed Mar 20 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt6
- add require to the version from runtime config

* Thu Mar 07 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt5
- drop obsoleted libicu56 require (ALT bug 36210)
- add hack to use latest runtime (ALT bug 36198)

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt4
- always build libpsl-native.so

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt3
- add dotnet requires

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt2
- only pack prebuild binaries

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- initial release for ALT Sisyphus
