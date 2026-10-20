# TODO: build from sources
%define _unpackaged_files_terminate_build 1
%def_enable netstandart
%def_enable dotnet_host

%define _dotnet_major 8.0

%define _dotnet_coreversion 8.0.32
%define _dotnet_sdkversion 8.0.132

%define _dotnet_corerelease 8.0.32
#define _dotnet_sdkmanifestsrelease1 %nil
%define _dotnet_sdkmanifestsrelease 8.0.100
%define _dotnet_sdkrelease 8.0.132
%define _dotnet_corerelease1 8.0.32
%define _dotnet_templatesrelease %_dotnet_corerelease1
%define _dotnet_coreapprefrelease %_dotnet_corerelease
%define _dotnet_netstandartrelease 2.1.0



%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major

Name: dotnet-sdk-%_dotnet_major
Version: %_dotnet_sdkversion
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

BuildRequires: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkversion
#BuildRequires: dotnet-bootstrap-%_dotnet_major = %_dotnet_corerelease
#BuildRequires: dotnet-host >= %_dotnet_coreversion

BuildRequires: dotnet-apphost-pack-%_dotnet_major = %_dotnet_coreversion

# SDK unusable without dotnet CLI
Requires: dotnet-%_dotnet_major = %_dotnet_coreversion

Requires: dotnet-runtime-%_dotnet_major = %_dotnet_coreversion
Requires: dotnet-apphost-pack-%_dotnet_major = %_dotnet_coreversion
Requires: dotnet-aspnetcore-runtime-%_dotnet_major = %_dotnet_coreversion
Requires: dotnet-aspnetcore-targeting-pack-%_dotnet_major = %_dotnet_coreversion
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
Release: alt6
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
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 8.0.132-alt1
- .NET SDK 8.0.132
- security fixes:
  + CVE-2026-66822, GHSA-wxxw-5cvc-53j7: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-58280, GHSA-mc4q-93x5-f6hj: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-69651, GHSA-3rxq-g8rj-r2cf: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-96958, GHSA-r955-8q5j-3h83: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-96960, GHSA-7hqp-7c5m-4vq6: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-96959, GHSA-c399-9853-6jmj: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-84008, GHSA-846f-f764-76mx: .NET Denial of Service Vulnerability
  + CVE-2026-70174, GHSA-f749-vhgx-39h6: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-87697, GHSA-c27m-942f-rcfh: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-70035, GHSA-4j9v-h7pp-725h: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-83520, GHSA-4w5f-7jp2-w48g: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96229, GHSA-5qr9-xxm9-6cmq: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-96232, GHSA-f8qh-mqg4-9939: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-96234, GHSA-fq6x-pvr9-888r: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-70007, GHSA-pfwj-2f93-rf42: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96224, GHSA-xq57-crx4-g373: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96235, GHSA-g44w-h65v-4cw9: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-85363, GHSA-f63g-mx39-3r38: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96233, GHSA-87vj-4hqv-22p9: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-70175, GHSA-x3vp-85cm-q97r: ASP.NET Core Elevation of Privilege Vulnerability
  + CVE-2026-70196, GHSA-57xr-hfxx-jw5x: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-70179, GHSA-vrrp-6v32-2p8g: ASP.NET Core Elevation of Privilege Vulnerability
  + CVE-2026-70181, GHSA-w5qq-qrpp-rf4c: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-96238: .NET SDK Security Feature Bypass Vulnerability
  + CVE-2026-96237: .NET SDK Remote Code Execution Vulnerability
  + CVE-2026-70159, GHSA-334f-vvp4-7g6p: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-70186, GHSA-mf4x-w4gh-4656: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-105016, GHSA-5gjq-3f94-rcf7: fix Microsoft QUIC remote code execution vulnerability
  + CVE-2026-85790, GHSA-2mxg-prvg-9jfg: .NET Information Disclosure Vulnerability
  + CVE-2026-70162, GHSA-2fmv-rv2c-59x7: .NET Denial of Service Vulnerability
  + CVE-2026-70183, GHSA-494h-xx7x-5frh: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-88092, GHSA-rv87-ccxw-8ggf: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-70188, GHSA-fpq8-4vhr-rcxx: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-96230, GHSA-qjpx-jqm5-h2c4: ASP.NET Core Remote Code Execution Vulnerability
  + CVE-2026-92707: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-96222, GHSA-vrv5-2jg9-4mmr: .NET Spoofing Vulnerability
  + CVE-2026-96231, GHSA-2j93-m82w-73j2: .NET and Visual Studio Elevation of Privilege Vulnerability
  + CVE-2026-96225, GHSA-w6wh-p4g7-mpj2: .NET and Visual Studio Elevation of Privilege Vulnerability
  + CVE-2026-70197, GHSA-4mpw-cpwj-hxxj: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96236, GHSA-f4g7-52wc-p8x7: ASP.NET Core Denial of Service Vulnerability

* Fri Sep 25 2026 Vitaly Lipatov <lav@altlinux.ru> 8.0.131-alt1
- .NET SDK 8.0.131
- fixed CVEs:
 + CVE-2026-69439: .NET and Visual Studio Elevation of Privilege Vulnerability
 + CVE-2026-71328: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69522: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69304: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-58649: .NET Information Disclosure Vulnerability

* Sun Aug 30 2026 Vitaly Lipatov <lav@altlinux.ru> 8.0.130-alt1
- fixed CVEs:
 + CVE-2026-62898: .NET Information Disclosure Vulnerability
 + CVE-2026-62899: .NET Security Feature Bypass Vulnerability
 + CVE-2026-62900: .NET Information Disclosure Vulnerability
 + CVE-2026-62901: .NET Denial of Service Vulnerability
 + CVE-2026-62886: .NET Elevation of Privilege Vulnerability
 + CVE-2026-62871: .NET Elevation of Privilege Vulnerability
 + CVE-2026-70354: .NET Core Remote Code Execution Vulnerability
 + CVE-2026-62902: .NET Information Disclosure Vulnerability
 + CVE-2026-62897: .NET Remote Code Execution Vulnerability
 + CVE-2026-62909: .NET Elevation of Privilege Vulnerability
 + CVE-2026-50651: .NET Denial of Service Vulnerability
 + CVE-2026-50526: .NET Tampering Vulnerability
 + CVE-2026-50524: .NET Denial of Service Vulnerability
 + CVE-2026-50646: .NET Remote Code Execution Vulnerability
 + CVE-2026-50649: .NET Remote Code Execution Vulnerability
 + CVE-2026-50650: .NET Elevation of Privilege Vulnerability
 + CVE-2026-56158: .NET Remote Code Execution Vulnerability
 + CVE-2026-47302: .NET Denial of Service Vulnerability
 + CVE-2026-50648: .NET Denial of Service Vulnerability
 + CVE-2026-50527: .NET Denial of Service Vulnerability
 + CVE-2026-47304: .NET Security Feature Bypass Vulnerability
 + CVE-2026-50525: .NET Denial of Service Vulnerability
 + CVE-2026-57108: .NET Denial of Service Vulnerability
 + CVE-2026-50528: .NET Security Feature Bypass Vulnerability
 + CVE-2026-50659: .NET Spoofing Vulnerability
 + CVE-2026-47300: .NET Elevation of Privilege Vulnerability
 + CVE-2026-47303: .NET Elevation of Privilege Vulnerability
 + CVE-2026-45591: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-45491: .NET Elevation of Privilege Vulnerability
 + CVE-2026-45490: .NET Elevation of Privilege Vulnerability
 + CVE-2026-32177: .NET Denial of Service Vulnerability
 + CVE-2026-35433: .NET Elevation of Privilege Vulnerability
 + CVE-2026-32175: .NET Core Tampering Vulnerability
 + CVE-2026-42899: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-26171: .NET Denial of Service Vulnerability
 + CVE-2026-32203: .NET Denial of Service Vulnerability
 + CVE-2026-33116: .NET Denial of Service Vulnerability
 + CVE-2026-32178: .NET Spoofing Vulnerability

* Mon Apr 06 2026 Vitaly Lipatov <lav@altlinux.ru> 8.0.125-alt1
- .NET SDK 8.0.125

* Tue Oct 28 2025 Vitaly Lipatov <lav@altlinux.ru> 8.0.121-alt1
- .NET SDK 8.0.121 release
- fixed CVEs:
 + CVE-2025-26646: .NET and Visual Studio Spoofing Vulnerability
 + CVE-2025-30399: .NET Remote Code Execution Vulnerability

* Tue Mar 04 2025 Vitaly Lipatov <lav@altlinux.ru> 8.0.113-alt1
- .NET SDK 8.0.113 release

* Sat Dec 07 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.111-alt1
- .NET SDK 8.0.111 release

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
