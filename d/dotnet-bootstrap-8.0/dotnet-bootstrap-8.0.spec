%define _unpackaged_files_terminate_build 1

%define _dotnet_major 8.0
%define _dotnet_corerelease 8.0.8
#define _dotnet_sdkmanifestsrelease1 %nil
%define _dotnet_sdkmanifestsrelease 8.0.100
%define _dotnet_sdkrelease 8.0.108
%define _dotnet_aspnetcorerelease %_dotnet_corerelease
%define _dotnet_templatesrelease %_dotnet_corerelease
%define _dotnet_coreapprefrelease %_dotnet_corerelease
%define _dotnet_aspnetcoreapprefrelease %_dotnet_corerelease
%define _dotnet_netstandartrelease 2.1.0
%define preview %nil
%define _dotnet_coreshortrelease %_dotnet_corerelease%preview
%define _dotnet_sdkshortrelease %_dotnet_sdkrelease%preview

%define _dotnetdir %_libdir/%name

Name: dotnet-bootstrap-%_dotnet_major
Version: 8.0.8
Release: alt1

Summary: .NET 8 SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# from https://github.com/dotnet/core/tree/master/release-notes/8.0

# x86_64
# Source-url: https://raw.githubusercontent.com/dotnet/core/main/release-notes/%_dotnet_major/%{_dotnet_corerelease}/%{_dotnet_sdkrelease}.md dotnet-sdk-%{_dotnet_sdkrelease}-linux-x64.tar.gz
Source: %name-%version.tar

# aarch64
# Source2-url: https://raw.githubusercontent.com/dotnet/core/main/release-notes/%_dotnet_major/%{_dotnet_corerelease}/%{_dotnet_sdkrelease}.md dotnet-sdk-%{_dotnet_sdkrelease}-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64 aarch64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no,lib,shell
AutoProv: no

BuildRequires(pre): rpm-macros-dotnet >= 6.0

BuildRequires: libunwind >= 1.1
BuildRequires: liblttng-ust >= 2.8.0
BuildRequires: libcurl
BuildRequires: libkrb5

# for System.Security.Cryptography.Native.OpenSsl.so
# but already required by libkrb5
#Requires: libcrypto10 libssl10

# it is not linked directly (need the same version like in libicu-devel)
# there are icu detection in a version range
Requires: libicu

Provides: dotnet-bootstrap-runtime-%_dotnet_major = %_dotnet_coreshortrelease
Provides: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkshortrelease

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
%_dotnet_sdkmanifests/
%dir %_dotnetdir/shared/
%dir %_dotnetdir/shared/Microsoft.NETCore.App/
%_dotnet_coreapp/
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%_dotnet_aspnetcoreapp/
%_dotnetdir/LICENSE.txt
%_dotnetdir/ThirdPartyNotices.txt

%changelog
* Sun Sep 15 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.8-alt1
- The .NET 8.0.8 and .NET SDK 8.0.108 release
- CVE-2024-38168: .NET Denial of Service Vulnerability
- CVE-2024-38167: .NET Information Disclosure Vulnerability

* Sun Sep 15 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.7-alt1
- The .NET 8.0.7 and .NET SDK 8.0.107 release
- CVE-2024-38095: .NET Denial of Service Vulnerability
- CVE-2024-35264: .NET Remote Code Execution Vulnerability
- CVE-2024-30105: .NET Denial of Service Vulnerability

* Sun Sep 15 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.6-alt1
- The .NET 8.0.6 and .NET SDK 8.0.106 release

* Sat May 18 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.5-alt1
- The .NET 8.0.5 and .NET SDK 8.0.105 release
- CVE-2024-21409: .NET Elevation of Privilege Vulnerability
- CVE-2024-30046: .NET Denial of Service Vulnerability
- CVE-2024-30045: .NET Remote Code Execution Vulnerability

* Fri Apr 05 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.3-alt1
- The .NET 8.0.3 and .NET SDK 8.0.103 release
- CVE-2024-21392: .NET Denial of Service Vulnerability
- CVE-2024-26190: Microsoft QUIC Denial of Service Vulnerability

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.2-alt1
- The .NET 8.0.2 and .NET SDK 8.0.2 release
- CVE-2023-36038: .NET Denial of Service Vulnerability
- CVE-2023-36049: .NET Elevation of Privilege Vulnerability
- CVE-2023-36558: .NET Security Feature Bypass Vulnerability
- CVE-2024-0056: Microsoft.Data.SqlClient and System.Data.SqlClient SQL Data provider Information Disclosure Vulnerability
- CVE-2024-0057: .NET Security Feature bypass Vulnerability
- CVE-2024-21319: .NET Denial of Service Vulnerability
- CVE-2024-21386: .NET Denial of Service Vulnerability
- CVE-2024-21404: .NET Denial of Service Vulnerability

* Mon Jan 08 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.rc.2.23502.2-alt1
- The .NET 8.0 and .NET SDK 8.0.0 RC2

* Fri Jul 28 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.preview.6.23330.14-alt1
- The .NET 8.0 and .NET SDK 8.0.0 preview 6

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.preview.1.23115.2-alt1
- The .NET 8.0 and .NET SDK 8.0.0 preview 1
- initial release for ALT Sisyphus
