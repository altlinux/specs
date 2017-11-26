# FIXME:
%define _dotnet_sdkrelease 2.0.3

# TODO: build from sources
Name: dotnet-sdk
Version: 2.0.3
Release: alt1

Summary: SDK for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: rpm-build-intro

BuildRequires(pre): rpm-macros-dotnet >= %version

BuildRequires: dotnet-bootstrap-sdk = %_dotnet_sdkrelease

Requires: dotnet-common >= %version

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%description
SDK for the .NET Core runtime and libraries.

Just copying binary now.

%prep
%setup

%install
mkdir -p %buildroot%_dotnet_sdk/
cp -a %_libdir/dotnet-bootstrap/sdk/%_dotnet_sdkrelease/* %buildroot%_dotnet_sdk/
# dotnet --info get RID string from this .version, line 3
cp -a %_libdir/dotnet-bootstrap/sdk/%_dotnet_sdkrelease/.version %buildroot%_dotnet_sdk/

mkdir -p %buildroot%_cachedir/dotnet/NuGetFallbackFolder/
ln -sr %buildroot%_cachedir/dotnet/NuGetFallbackFolder %buildroot%_libdir/dotnet/sdk/NuGetFallbackFolder

%pre
%groupadd dotnet || :

%files
%dir %_libdir/dotnet/sdk/
%_dotnet_sdk/
%_libdir/dotnet/sdk/NuGetFallbackFolder/
%dir %_cachedir/dotnet/
%attr(2775,root,dotnet) %dir %_cachedir/dotnet/NuGetFallbackFolder/

%changelog
* Sun Nov 26 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- .NET Core SDK 2.0.3 Release

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core SDK 2.0.0 Release
- add /var/cache/dotnet/NuGetFallbackFolder for packages common cache

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- use dotnet-bootstrap-sdk buildreq

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- fix requires, provides
- add missed .version

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
