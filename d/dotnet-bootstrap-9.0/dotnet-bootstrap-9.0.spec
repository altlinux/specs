%define _unpackaged_files_terminate_build 1

%define _dotnet_major 9.0
#%define preview %nil
%define _dotnet_coreversion 9.0.21
%define _dotnet_sdkversion 9.0.319

%define _dotnet_corerelease 9.0.21
%define _dotnet_corerelease1 9.0.21

#%define _dotnet_sdkmanifestsrelease0 8.0.100
#define _dotnet_sdkmanifestsrelease1 9.0.100
%define _dotnet_sdkmanifestsrelease 9.0.100
%define _dotnet_sdkrelease 9.0.319

%define _dotnet_templatesrelease %_dotnet_corerelease1
%define _dotnet_coreapprefrelease %_dotnet_corerelease
%define _dotnet_netstandartrelease 2.1.0

%define _dotnet_aspnetcorerelease %_dotnet_corerelease1
%define _dotnet_aspnetcoreapprefrelease %_dotnet_corerelease1


%define _dotnetdir %_libdir/%name

Name: dotnet-bootstrap-%_dotnet_major
Version: %_dotnet_sdkrelease
Release: alt1

Summary: .NET 9 SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# from https://github.com/dotnet/core/tree/master/release-notes/9.0


# x86_64
# Source-url: https://builds.dotnet.microsoft.com/dotnet/Sdk/%{_dotnet_sdkrelease}/dotnet-sdk-%{_dotnet_sdkrelease}-linux-x64.tar.gz
Source: %name-%version.tar

# aarch64
# Source2-url: https://builds.dotnet.microsoft.com/dotnet/Sdk/%{_dotnet_sdkrelease}/dotnet-sdk-%{_dotnet_sdkrelease}-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64 aarch64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no,lib,shell
AutoProv: no

BuildRequires(pre): rpm-macros-dotnet >= 6.0

# libraries the prebuilt binaries are linked with (by soname: package names differ between branches)
BuildRequires: liblttng-ust.so.0()(64bit)

# for System.Security.Cryptography.Native.OpenSsl.so (dlopen)
#Requires: libcrypto10 libssl10

# it is not linked directly (need the same version like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

Provides: dotnet-bootstrap-runtime-%_dotnet_major = %_dotnet_coreversion
Provides: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkversion

%filter_from_requires /^\/usr\/lib\/ld-linux-aarch64.*/d

%description
This package contains full .NET %_dotnet_major SDK binaries, needed for bootstrap build.

%prep
%setup
%ifarch aarch64
rm -rf packs/ host/ shared/
tar xfv %SOURCE2
%endif

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb (https://bugzilla.altlinux.org/show_bug.cgi?id=33411)
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|libsosplugin.so|libsos.so|g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

cd %buildroot%_libdir/%name

# See also https://bugzilla.altlinux.org/show_bug.cgi?id=37413
strip \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/lib*.so \
	shared/Microsoft.NETCore.App/%_dotnet_corerelease/createdump \
	sdk/%_dotnet_sdkrelease/AppHostTemplate/apphost \
	packs/Microsoft.NETCore.App.Host.%_dotnet_rid/%_dotnet_corerelease/runtimes/%_dotnet_rid/native/libnethost.so \
	packs/Microsoft.NETCore.App.Host.%_dotnet_rid/%_dotnet_corerelease/runtimes/%_dotnet_rid/native/apphost \
	host/fxr/%_dotnet_corerelease/libhostfxr.so \
	dotnet \
	#

%files
%dir %_dotnetdir/
%_dotnetdir/dotnet
%dir %_dotnetdir/templates/
%_dotnet_templates/
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Host.%_dotnet_rid/
%_dotnet_coreapphost/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Ref/
%_dotnet_coreappref/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnet_aspnetcoreappref/
%dir %_dotnetdir/packs/NETStandard.Library.Ref/
%_dotnet_netstandart/
%dir %_dotnetdir/host/
%dir %_dotnetdir/host/fxr/
%_dotnet_hostfxr/
%dir %_dotnetdir/sdk/
%_dotnet_sdk/
%dir %_dotnetdir/sdk-manifests/
%ifdef _dotnet_sdkmanifestsrelease1
%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease1/
%endif
%ifdef _dotnet_sdkmanifestsrelease0
%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease0/
%endif
%_dotnet_sdkmanifests/
%dir %_dotnetdir/shared/
%dir %_dotnetdir/shared/Microsoft.NETCore.App/
%_dotnet_coreapp/
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%_dotnet_aspnetcoreapp/
%_dotnetdir/LICENSE.txt
%_dotnetdir/ThirdPartyNotices.txt

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 9.0.319-alt1
- .NET SDK 9.0.319 and runtime 9.0.21
- security fixes:
  + CVE-2026-66822, GHSA-wxxw-5cvc-53j7: fix information disclosure.
  + CVE-2026-58280, GHSA-mc4q-93x5-f6hj: fix denial of service.
  + CVE-2026-69651, GHSA-3rxq-g8rj-r2cf: fix denial of service.
  + CVE-2026-96958, GHSA-r955-8q5j-3h83: fix denial of service.
  + CVE-2026-96960, GHSA-7hqp-7c5m-4vq6: fix denial of service.
  + CVE-2026-96959, GHSA-c399-9853-6jmj: fix denial of service.
  + CVE-2026-84008, GHSA-846f-f764-76mx: fix denial of service.
  + CVE-2026-70174, GHSA-f749-vhgx-39h6: fix remote code execution.
  + CVE-2026-87697, GHSA-c27m-942f-rcfh: fix remote code execution.
  + CVE-2026-70035, GHSA-4j9v-h7pp-725h: fix remote code execution.
  + CVE-2026-83520, GHSA-4w5f-7jp2-w48g: fix remote code execution.
  + CVE-2026-96229, GHSA-5qr9-xxm9-6cmq: fix information disclosure.
  + CVE-2026-96232, GHSA-f8qh-mqg4-9939: fix information disclosure.
  + CVE-2026-96234, GHSA-fq6x-pvr9-888r: fix information disclosure.
  + CVE-2026-70007, GHSA-pfwj-2f93-rf42: fix remote code execution.
  + CVE-2026-96224, GHSA-xq57-crx4-g373: fix remote code execution.
  + CVE-2026-96235, GHSA-g44w-h65v-4cw9: fix remote code execution.
  + CVE-2026-85363, GHSA-f63g-mx39-3r38: fix remote code execution.
  + CVE-2026-96233, GHSA-87vj-4hqv-22p9: fix denial of service.
  + CVE-2026-70175, GHSA-x3vp-85cm-q97r: fix elevation of privilege.
  + CVE-2026-70196, GHSA-57xr-hfxx-jw5x: fix denial of service.
  + CVE-2026-70179, GHSA-vrrp-6v32-2p8g: fix elevation of privilege.
  + CVE-2026-70181, GHSA-w5qq-qrpp-rf4c: fix denial of service.
  + CVE-2026-70161: fix elevation of privilege.
  + CVE-2026-70165: fix elevation of privilege.
  + CVE-2026-70190: fix elevation of privilege.
  + CVE-2026-96238: fix security feature bypass.
  + CVE-2026-96237: fix remote code execution.
  + CVE-2026-70159, GHSA-334f-vvp4-7g6p: fix denial of service.
  + CVE-2026-70186, GHSA-mf4x-w4gh-4656: fix denial of service.
  + CVE-2026-105016, GHSA-5gjq-3f94-rcf7: fix remote code execution.
  + CVE-2026-85790, GHSA-2mxg-prvg-9jfg: fix information disclosure.
  + CVE-2026-70162, GHSA-2fmv-rv2c-59x7: fix denial of service.
  + CVE-2026-70183, GHSA-494h-xx7x-5frh: fix security feature bypass.
  + CVE-2026-88092, GHSA-rv87-ccxw-8ggf: fix security feature bypass.
  + CVE-2026-70188, GHSA-fpq8-4vhr-rcxx: fix security feature bypass.
  + CVE-2026-96230, GHSA-qjpx-jqm5-h2c4: fix remote code execution.
  + CVE-2026-92707: fix denial of service.
  + CVE-2026-96231, GHSA-2j93-m82w-73j2: fix elevation of privilege.
  + CVE-2026-96225, GHSA-w6wh-p4g7-mpj2: fix elevation of privilege.
  + CVE-2026-70197, GHSA-4mpw-cpwj-hxxj: fix remote code execution.
  + CVE-2026-96236, GHSA-f4g7-52wc-p8x7: fix denial of service.
- BuildRequires by soname: liblttng-ust.so.0()(64bit).
- dropped unused BuildRequires: libunwind, libcurl, libkrb5.

* Sat Sep 26 2026 Vitaly Lipatov <lav@altlinux.ru> 9.0.318-alt1
- .NET SDK 9.0.318 and runtime 9.0.20
- fixed CVEs:
 + CVE-2026-69439: .NET and Visual Studio Elevation of Privilege Vulnerability
 + CVE-2026-71328: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69522: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69304: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-58649: .NET Information Disclosure Vulnerability
 + CVE-2026-69806: .NET Elevation of Privilege Vulnerability

* Mon Aug 31 2026 Vitaly Lipatov <lav@altlinux.ru> 9.0.317-alt1
- .NET SDK 9.0.317 and runtime 9.0.19
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

* Wed Oct 15 2025 Vitaly Lipatov <lav@altlinux.ru> 9.0.111-alt1
- The .NET 9.0.10 and .NET SDK 9.0.111 release
- fixed CVEs:
 + CVE-2025-24070: .NET Elevation of Privilege Vulnerability
 + CVE-2025-26682: .NET Denial of Service Vulnerability
 + CVE-2025-26646: .NET and Visual Studio Spoofing Vulnerability
 + CVE-2025-30399: .NET Remote Code Execution Vulnerability
 + CVE-2025-55248: .NET Information Disclosure Vulnerability
 + CVE-2025-55315: .NET Security Feature Bypass Vulnerability
 + CVE-2025-55247: .NET Denial of Service Vulnerability

* Tue Mar 04 2025 Vitaly Lipatov <lav@altlinux.ru> 9.0.103-alt1
- The .NET 9.0.2 and .NET SDK 9.0.103 release
- fixed CVEs:
 + CVE-2025-21171: .NET Remote Code Execution Vulnerability
 + CVE-2025-21172: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2025-21173: .NET Elevation of Privilege Vulnerability
 + CVE-2025-21176: .NET and Visual Studio Remote Code Execution Vulnerability

* Sat Dec 07 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.101-alt1
- The .NET 9.0.0 and .NET SDK 9.0.101 release
- use SDK version as package version

* Thu Sep 19 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.0.rc.1-alt1
- new version (9.0.0.rc.1) with rpmgs script

* Fri Apr 05 2024 Vitaly Lipatov <lav@altlinux.ru> 9.0.0.preview.2-alt1
- initial release for ALT Sisyphus
