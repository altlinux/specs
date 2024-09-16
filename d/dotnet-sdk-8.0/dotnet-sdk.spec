# TODO: build from sources
%define _unpackaged_files_terminate_build 1
%def_enable netstandart
%def_enable dotnet_host

%define _dotnet_major 8.0
%define _dotnet_corerelease 8.0.8
#define _dotnet_sdkmanifestsrelease1 %nil
%define _dotnet_sdkmanifestsrelease 8.0.100
%define _dotnet_sdkrelease 8.0.108
%define _dotnet_templatesrelease %_dotnet_corerelease
%define _dotnet_coreapprefrelease %_dotnet_corerelease
%define _dotnet_netstandartrelease 2.1.0
%define preview %nil
%define _dotnet_coreshortrelease 8.0.8%preview
%define _dotnet_sdkshortrelease 8.0.108%preview

%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major

Name: dotnet-sdk-%_dotnet_major
Version: 8.0.108%preview
Release: alt1

Summary: SDK for the .NET 8

License: MIT
URL: https://github.com/dotnet/sdk
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: aarch64 x86_64

BuildRequires: rpm-build-intro

# TODO
BuildRequires(pre): rpm-macros-dotnet

BuildRequires: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkshortrelease
#BuildRequires: dotnet-bootstrap-%_dotnet_major = %_dotnet_corerelease
#BuildRequires: dotnet-host >= %_dotnet_coreshortrelease

BuildRequires: dotnet-apphost-pack-%_dotnet_major = %_dotnet_coreshortrelease

# SDK unusable without dotnet CLI
Requires: dotnet-%_dotnet_major = %_dotnet_coreshortrelease

Requires: dotnet-runtime-%_dotnet_major = %_dotnet_coreshortrelease
Requires: dotnet-apphost-pack-%_dotnet_major = %_dotnet_coreshortrelease
Requires: dotnet-aspnetcore-runtime-%_dotnet_major = %_dotnet_coreshortrelease
Requires: dotnet-aspnetcore-targeting-pack-%_dotnet_major = %_dotnet_coreshortrelease
Requires: dotnet-targeting-pack-%_dotnet_major = %version-%release

Requires: netstandard-targeting-pack-2.1 = %_dotnet_netstandartrelease

Requires: dotnet-common

# https://bugzilla.altlinux.org/49566
Requires: ca-certificates-nuget.org

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%if_enabled dotnet_host
Provides: dotnet-sdk = %EVR
%endif


%description
SDK for the .NET runtime and libraries.

Just copying managed code now.

# Note: one for all versions
%package -n netstandard-targeting-pack-2.1
Version: %_dotnet_netstandartrelease
Release: alt2
Group: Development/Other
Summary: NETStandard.Library.Ref 2.1

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

Conflicts: %name <= %EVR

%description -n netstandard-targeting-pack-2.1
NETStandard.Library.Ref 2.1

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

%package -n dotnet-targeting-pack-%_dotnet_major
Summary: .NET 6 targeting pack
Group: Development/Other
AutoReq: no
AutoProv: no

%description -n dotnet-targeting-pack-%_dotnet_major
SDK for the .NET runtime and libraries.

%prep
%setup

%install
mkdir -p %buildroot%_dotnet_sdk/
cp -a %bootstrapdir/sdk/%_dotnet_sdkrelease/* %buildroot%_dotnet_sdk/

# dotnet --info get RID string from this .version, line 3
cp -a %bootstrapdir/sdk/%_dotnet_sdkrelease/.version %buildroot%_dotnet_sdk/
cp -a %bootstrapdir/sdk/%_dotnet_sdkrelease/.toolsetversion %buildroot%_dotnet_sdk/

# dotnet-targeting-pack
mkdir -p %buildroot%_dotnetdir/packs/
cp -a %bootstrapdir/packs/Microsoft.NETCore.App.Ref/ %buildroot%_dotnetdir/packs/
%if_enabled netstandart
cp -a %bootstrapdir/packs/NETStandard.Library.Ref/ %buildroot%_dotnetdir/packs/
%endif

mkdir -p %buildroot%_dotnetdir/templates/%_dotnet_templatesrelease/
cp -a %bootstrapdir/templates/%_dotnet_templatesrelease/* %buildroot%_dotnetdir/templates/%_dotnet_templatesrelease/

mkdir -p %buildroot%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease/
cp -a %bootstrapdir/sdk-manifests/%_dotnet_sdkmanifestsrelease/* %buildroot%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease/

%ifdef _dotnet_sdkmanifestsrelease1
mkdir -p %buildroot%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease1/
cp -a %bootstrapdir/sdk-manifests/%_dotnet_sdkmanifestsrelease1/* %buildroot%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease1/
%endif

# apphost used as executable, f.i. dotnet tool install --global paket will install it in $HOME/.dotnet/tools as paket
# rewrite one with our binary
rm -f %buildroot%_dotnet_sdk/AppHostTemplate/apphost
cp %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost %buildroot%_dotnet_sdk/AppHostTemplate/apphost

%files
%dir %_dotnetdir/sdk/
%_dotnet_sdk/

# TODO: standalone package
%dir %_dotnetdir/templates/
%dir %_dotnetdir/templates/%_dotnet_templatesrelease/
%_dotnetdir/templates/%_dotnet_templatesrelease/*.nupkg

%dir %_dotnetdir/sdk-manifests/
%_dotnet_sdkmanifests/
%ifdef _dotnet_sdkmanifestsrelease1
%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease1/
%endif

%files -n dotnet-targeting-pack-%_dotnet_major
%_dotnetdir/packs/Microsoft.NETCore.App.Ref/

%if_enabled netstandart
%files -n netstandard-targeting-pack-2.1
%dir %_dotnetdir/
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/NETStandard.Library.Ref/
%_dotnetdir/packs/NETStandard.Library.Ref/%_dotnet_netstandartrelease/
%endif

%changelog
* Mon Sep 16 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.108-alt1
- .NET SDK 8.0.108 release
- enable netstandard-targeting-pack-2.1 subpackage
- CVE-2024-38168: .NET Denial of Service Vulnerability
- CVE-2024-38167: .NET Information Disclosure Vulnerability
- CVE-2024-38095: .NET Denial of Service Vulnerability
- CVE-2024-35264: .NET Remote Code Execution Vulnerability

* Sat May 18 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.105-alt1
- .NET SDK 8.0.105 release

* Fri Apr 05 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.103-alt1
- .NET SDK 8.0.103 release

* Fri Mar 01 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.102-alt2
- add Requires: ca-certificates-nuget.org (ALT bug 49566)

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.102-alt1
- .NET SDK 8.0.102 release
- CVE-2023-36038: .NET Denial of Service Vulnerability
- CVE-2023-36049: .NET Elevation of Privilege Vulnerability
- CVE-2023-36558: .NET Security Feature Bypass Vulnerability
- CVE-2024-0056: Microsoft.Data.SqlClient and System.Data.SqlClient SQL Data provider Information Disclosure Vulnerability
- CVE-2024-0057: .NET Security Feature bypass Vulnerability
- CVE-2024-21319: .NET Denial of Service Vulnerability
- CVE-2024-21386: .NET Denial of Service Vulnerability
- CVE-2024-21404: .NET Denial of Service Vulnerability

* Mon Jan 08 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.100.rc.2.23502.2-alt1
- .NET SDK 8.0.100 RC2
- CVE-2023-44487: .NET Denial of Service Vulnerability
- CVE-2023-38171: .NET Denial of Service Vulnerability
- CVE-2023-36435: .NET Denial of Service Vulnerability
- CVE-2023-36792: .NET Remote Code Execution Vulnerability
- CVE-2023-36793: .NET Remote Code Execution Vulnerability
- CVE-2023-36794: .NET Remote Code Execution Vulnerability
- CVE-2023-36796: .NET Remote Code Execution Vulnerability
- CVE-2023-36799: .NET Denial of Service Vulnerability

* Fri Jul 28 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.100.preview.6.23330.14-alt1
- .NET SDK 8.0.0 preview 6

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.100.preview.1.23115.2-alt1
- .NET SDK 8.0.0 preview 1
- initial build for ALT Sisyphus
