%define _unpackaged_files_terminate_build 1

%define _dotnet_major 3.1
%define _dotnet_corerelease 3.1.32

%define _dotnet_asppackrelease 3.1.10
%define _dotnet_aspnetcore_app %_dotnetdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/

# FIXME: build from sources
%def_with bootstrap
%define pre %nil

Name: dotnet-aspnetcore-%_dotnet_major
Version: 3.1.32
Release: alt1

Summary: ASP.NET Core is a cross-platform .NET framework for building modern cloud-based web application

License: MIT
Url: https://github.com/dotnet/aspnetcore
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

BuildRequires(pre): rpm-macros-dotnet
# = %version

%if_with bootstrap
#BuildRequires: dotnet-bootstrap-runtime-%_dotnet_major
BuildRequires: dotnet-bootstrap-%_dotnet_major = %version
#= %version
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common

Conflicts: dotnet-aspnetcore <= 3.1.6-alt1

%description
ASP.NET Core is an open-source and cross-platform framework
for building modern cloud based internet connected applications,
such as web apps, IoT apps and mobile backends.

ASP.NET Core apps can run on .NET Core or on the full .NET Framework.
It was architected to provide an optimized development framework
for apps that are deployed to the cloud or run on-premises.
It consists of modular components with minimal overhead,
so you retain flexibility while constructing your solutions.

Just copied managed binaries now.

%prep
%setup

%install
mkdir -p %buildroot%_dotnet_aspnetcore_app

%if_with bootstrap
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/.version %buildroot%_dotnet_aspnetcore_app
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_aspnetcore_app
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_corerelease/*.json %buildroot%_dotnet_aspnetcore_app

# TODO: subpackage targeting-packs
mkdir -p %buildroot%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/
cp -a %bootstrapdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/* %buildroot%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/
%endif

%files
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%dir %_dotnet_aspnetcore_app/
%_dotnet_aspnetcore_app/.version
%_dotnet_aspnetcore_app/Microsoft.AspNetCore.App.deps.json
%_dotnet_aspnetcore_app/Microsoft.AspNetCore.App.runtimeconfig.json

%_dotnet_aspnetcore_app/*.dll

%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_asppackrelease/

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 3.1.32-alt1
- ASP.NET Core 3.1.32
- CVE-2022-38013: .NET Denial of Service Vulnerability

* Sun Oct 16 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.26-alt1
- ASP.NET Core 3.1.26

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.23-alt1
- ASP.NET Core 3.1.23

* Sat Feb 12 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.22-alt1
- .NET Core 3.1.22 - December 14, 2021
- CVE-2021-43877: ASP.NET Core Elevation of privilege Vulnerability
- CVE-2021-34532: ASP.NET Core Information Disclosure Vulnerability

* Thu Jul 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.16-alt1
- ASP.NET Core 3.1.16
- CVE-2021-31957: ASP.NET Denial of Service Vulnerability

* Sat Feb 20 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.12-alt2
- cleanup spec, add Conflicts: dotnet-aspnetcore

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.12-alt1
- ASP.NET Core 3.1.12
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Sat Aug 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- ASP.NET Core 3.1.6

* Tue Dec 17 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- ASP.NET Core 3.1.0

* Wed May 22 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- initial release for ALT Sisyphus (just copy managed code)
