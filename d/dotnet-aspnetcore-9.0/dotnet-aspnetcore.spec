%define _unpackaged_files_terminate_build 1

%define _dotnet_major 9.0
#%define preview %nil
%define _dotnet_coreversion 9.0.21
%define _dotnet_corerelease 9.0.21
%define _dotnet_corerelease1 9.0.21
%define _dotnet_aspnetcorerelease %_dotnet_corerelease1
%define _dotnet_aspnetcoreapprefrelease %_dotnet_corerelease1

# FIXME: build from sources
%def_with bootstrap

Name: dotnet-aspnetcore-%_dotnet_major
Version: %_dotnet_coreversion
Release: alt1

Summary: ASP.NET is a cross-platform .NET framework for building modern cloud-based web application

License: MIT
Url: https://github.com/dotnet/aspnetcore
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: aarch64 x86_64

BuildRequires(pre): rpm-macros-dotnet
# TODO = %version

%if_with bootstrap
BuildRequires: dotnet-bootstrap-runtime-%_dotnet_major = %_dotnet_coreversion
#= %version
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common = %version

# BuildRequires: libuv

#%remove_optflags -frecord-gcc-switches
#BuildRequires: clang llvm cmake libstdc++-devel

#BuildRequires: libcurl-devel libssl-devel zlib-devel libkrb5-devel

%description
ASP.NET is an open-source and cross-platform framework
for building modern cloud based internet connected applications,
such as web apps, IoT apps and mobile backends.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

Just copied managed binaries now.

%package -n dotnet-aspnetcore-runtime-%_dotnet_major
Summary: ASP.NET 9 runtime
Group: Development/Other
#AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoReq: no
AutoProv: no

Requires: dotnet-runtime-%_dotnet_major = %version

%description -n dotnet-aspnetcore-runtime-%_dotnet_major
The ASP.NET runtime contains everything needed to run .NET Core
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET Core applications.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
Summary: ASP.NET 9 targeting pack
Group: Development/Other
#AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoReq: no
AutoProv: no

#Requires: dotnet-targeting-pack-%_dotnet_major

%description -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
The ASP.NET runtime contains everything needed to run .NET Core
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET Core applications.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%prep
%setup

%install
mkdir -p %buildroot%_dotnet_aspnetcoreapp

%if_with bootstrap
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_aspnetcorerelease/.version %buildroot%_dotnet_aspnetcoreapp
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_aspnetcorerelease/*.dll %buildroot%_dotnet_aspnetcoreapp
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_aspnetcorerelease/*.json %buildroot%_dotnet_aspnetcoreapp

mkdir -p %buildroot%_dotnet_aspnetcoreappref/
cp -a %bootstrapdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_aspnetcoreapprefrelease/* %buildroot%_dotnet_aspnetcoreappref/
%endif


%files -n dotnet-aspnetcore-runtime-%_dotnet_major
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%dir %_dotnet_aspnetcoreapp/
%_dotnet_aspnetcoreapp/.version
%_dotnet_aspnetcoreapp/Microsoft.AspNetCore.App.deps.json
%_dotnet_aspnetcoreapp/Microsoft.AspNetCore.App.runtimeconfig.json
%_dotnet_aspnetcoreapp/*.dll

%files -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnet_aspnetcoreappref/

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 9.0.21-alt1
- ASP.NET Core 9.0.21
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
  + CVE-2026-70161: .NET SDK Elevation of Privilege Vulnerability
  + CVE-2026-70165: .NET SDK Elevation of Privilege Vulnerability
  + CVE-2026-70190: .NET SDK Elevation of Privilege Vulnerability
  + CVE-2026-96238: .NET SDK Security Feature Bypass Vulnerability
  + CVE-2026-96237: .NET SDK Remote Code Execution Vulnerability
  + CVE-2026-70159, GHSA-334f-vvp4-7g6p: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-70186, GHSA-mf4x-w4gh-4656: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-105016, GHSA-5gjq-3f94-rcf7: microsoft QUIC Remote Code Execution Vulnerability
  + CVE-2026-85790, GHSA-2mxg-prvg-9jfg: .NET Information Disclosure Vulnerability
  + CVE-2026-70162, GHSA-2fmv-rv2c-59x7: .NET Denial of Service Vulnerability
  + CVE-2026-70183, GHSA-494h-xx7x-5frh: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-88092, GHSA-rv87-ccxw-8ggf: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-70188, GHSA-fpq8-4vhr-rcxx: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-96230, GHSA-qjpx-jqm5-h2c4: ASP.NET Core Remote Code Execution Vulnerability
  + CVE-2026-92707: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-96231, GHSA-2j93-m82w-73j2: .NET and Visual Studio Elevation of Privilege Vulnerability
  + CVE-2026-96225, GHSA-w6wh-p4g7-mpj2: .NET and Visual Studio Elevation of Privilege Vulnerability
  + CVE-2026-70197, GHSA-4mpw-cpwj-hxxj: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96236, GHSA-f4g7-52wc-p8x7: ASP.NET Core Denial of Service Vulnerability

* Sat Sep 26 2026 Vitaly Lipatov <lav@altlinux.ru> 9.0.20-alt1
- ASP.NET Core 9.0.20
- fixed CVEs:
 + CVE-2026-69439: .NET and Visual Studio Elevation of Privilege Vulnerability
 + CVE-2026-71328: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69522: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69304: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-58649: .NET Information Disclosure Vulnerability
 + CVE-2026-69806: .NET Elevation of Privilege Vulnerability

* Tue Sep 01 2026 Vitaly Lipatov <lav@altlinux.ru> 9.0.19-alt1
- ASP.NET Core 9.0.19
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
 + CVE-2026-26130: .NET Denial of Service Vulnerability
 + CVE-2026-26127: .NET Denial of Service Vulnerability
 + CVE-2026-21218: .NET Security Feature Bypass Vulnerability
 + CVE-2025-55248: .NET Information Disclosure Vulnerability
 + CVE-2025-21171: .NET Remote Code Execution Vulnerability
 + CVE-2025-21172: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2025-21173: .NET Elevation of Privilege Vulnerability
 + CVE-2025-21176: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2025-24070: .NET Elevation of Privilege Vulnerability
 + CVE-2025-26682: .NET Denial of Service Vulnerability
 + CVE-2025-55315: .NET Security Feature Bypass Vulnerability

* Wed Oct 15 2025 Vitaly Lipatov <lav@altlinux.ru> 9.0.10-alt1
- ASP.NET 9.0.10 release
- fixed CVEs:
 + CVE-2025-24070: .NET Elevation of Privilege Vulnerability
 + CVE-2025-26682: .NET Denial of Service Vulnerability
 + CVE-2025-55315: .NET Security Feature Bypass Vulnerability


* Tue Mar 04 2025 Vitaly Lipatov <lav@altlinux.ru> 9.0.2-alt1
- ASP.NET 9.0.2 release

* Sun Dec 08 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.0.rel-alt1
- ASP.NET 9.0.0 release

* Sun Oct 06 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.0.rc.1-alt1
- ASP.NET 9.0.0 rc 1

* Sat Apr 06 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.0.preview.2-alt1
- ASP.NET 9.0.0 preview 2
- initial release for ALT Sisyphus
