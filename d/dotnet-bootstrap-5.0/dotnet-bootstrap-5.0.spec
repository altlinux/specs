%define _unpackaged_files_terminate_build 1

%define major 5.0
%define sdkversion 5.0.408
%define coreversion 5.0.17
%define apprefversion 5.0.0
%define netstandartversion 2.1.0

Name: dotnet-bootstrap-5.0
Version: 5.0.17
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# from https://github.com/dotnet/core/blob/master/release-notes/5.0

# Source-url: https://download.visualstudio.microsoft.com/download/pr/904da7d0-ff02-49db-bd6b-5ea615cbdfc5/966690e36643662dcc65e3ca2423041e/dotnet-sdk-5.0.408-linux-x64.tar.gz
Source: %name-%version.tar

# Source2-url: https://download.visualstudio.microsoft.com/download/pr/d4b71fac-a2fd-4516-ac58-100fb09d796a/e79d6c2a8040b59bf49c0d167ae70a7b/dotnet-sdk-5.0.408-linux-arm64.tar.gz
Source2: %name-aarch64-%version.tar

ExclusiveArch: x86_64 aarch64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no,lib,shell
AutoProv: no

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

# LTS provides
Provides: dotnet-bootstrap-runtime = %coreversion
Provides: dotnet-bootstrap-sdk = %sdkversion

Provides: dotnet-bootstrap-runtime-%major = %coreversion
Provides: dotnet-bootstrap-sdk-%major = %sdkversion

%description
This package contains full .NET 5.0 SDK binaries, needed for bootstrap build.

https://github.com/dotnet/core/blob/master/release-notes/5.0/%version/%version.md

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
	shared/Microsoft.NETCore.App/%coreversion/libmscordbi.so \
	shared/Microsoft.NETCore.App/%coreversion/libmscordaccore.so \
	shared/Microsoft.NETCore.App/%coreversion/libhostpolicy.so \
	shared/Microsoft.NETCore.App/%coreversion/libdbgshim.so \
	shared/Microsoft.NETCore.App/%coreversion/libcoreclrtraceptprovider.so \
	shared/Microsoft.NETCore.App/%coreversion/libcoreclr.so \
	shared/Microsoft.NETCore.App/%coreversion/libclrjit.so \
	shared/Microsoft.NETCore.App/%coreversion/createdump \
	shared/Microsoft.NETCore.App/%coreversion/libSystem.Security.Cryptography.Native.OpenSsl.so \
	shared/Microsoft.NETCore.App/%coreversion/libSystem.Net.Security.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/libSystem.Native.so \
	shared/Microsoft.NETCore.App/%coreversion/libSystem.IO.Compression.Native.so \
	sdk/%sdkversion/AppHostTemplate/apphost \
%ifarch x86_64
	packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/runtimes/linux-x64/native/libnethost.so \
	packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/runtimes/linux-x64/native/apphost \
%endif
%ifarch aarch64
	packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/runtimes/linux-arm64/native/libnethost.so \
	packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/runtimes/linux-arm64/native/apphost \
%endif
	host/fxr/%coreversion/libhostfxr.so \
	dotnet \
	#

%files
%dir %_libdir/%name/
%dir %_libdir/%name/templates/
%_libdir/%name/templates/%coreversion/
%dir %_libdir/%name/packs/
%dir %_libdir/%name/packs/Microsoft.AspNetCore.App.Ref
%_libdir/%name/packs/Microsoft.AspNetCore.App.Ref/5.0.0/
%ifarch aarch64
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-arm64/
%_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-arm64/%coreversion/
%else
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-x64/
%_libdir/%name/packs/Microsoft.NETCore.App.Host.linux-x64/%coreversion/
%endif
%dir %_libdir/%name/packs/Microsoft.NETCore.App.Ref/
%_libdir/%name/packs/Microsoft.NETCore.App.Ref/%apprefversion/
%dir %_libdir/%name/packs/NETStandard.Library.Ref/
%_libdir/%name/packs/NETStandard.Library.Ref/%netstandartversion/
%dir %_libdir/%name/host/
%dir %_libdir/%name/host/fxr/
%_libdir/%name/host/fxr/%coreversion/
%dir %_libdir/%name/sdk/
%_libdir/%name/sdk/%sdkversion/
%dir %_libdir/%name/shared/
%dir %_libdir/%name/shared/Microsoft.NETCore.App/
%_libdir/%name/shared/Microsoft.NETCore.App/%coreversion/
# TODO: drop from bootstrap
#dir %_libdir/%name/shared/Microsoft.AspNetCore.All/
%dir %_libdir/%name/shared/Microsoft.AspNetCore.App/
#_libdir/%name/shared/Microsoft.AspNetCore.All/%coreversion/
%_libdir/%name/shared/Microsoft.AspNetCore.App/%coreversion/
#_libdir/%name/store/
%_libdir/%name/LICENSE.txt
%_libdir/%name/ThirdPartyNotices.txt
%_libdir/%name/dotnet

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 5.0.17-alt1
- new version (5.0.17) with rpmgs script
- CVE-2022-29117: .NET Denial of Service Vulnerability
- CVE-2022-29145: .NET Denial of Service Vulnerability
- CVE-2022-23267: .NET Denial of Service Vulnerability

* Sat Apr 02 2022 Vitaly Lipatov <lav@altlinux.ru> 5.0.15-alt1
- The .NET 5.0.15 and .NET 5.0.406 SDK releases
- CVE-2022-24464 : .NET Denial of Service Vulnerability
- CVE-2022-24512 : .NET Remote Code Execution Vulnerability
- CVE-2020-8927 : .NET Remote Code Execution Vulnerability

* Sat Feb 12 2022 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt1
- .NET 5.0.14 - February 8, 2022
- CVE-2022-21986 : .NET Denial of Service Vulnerability
- CVE-2021-43877 : ASP.NET Core Elevation of privilege Vulnerability
- CVE-2021-41355 : .NET Core Information Disclosure Vulnerability
- CVE-2021-34485 : .NET Core Information Disclosure Vulnerability
- CVE-2021-26423 : .NET Core Denial of Service Vulnerability
- CVE-2021-34532 : ASP.NET Core Information Disclosure Vulnerability

* Wed Jun 30 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.7-alt1
- new version 5.0.7 (with rpmrb script)
- CVE-2021-31204: .NET Core Elevation of Privilege Vulnerability
- CVE-2021-31957: ASP.NET Denial of Service Vulnerability

* Sat Apr 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt1
- .NET 5.0.5 and .NET SDK 5.0.202
- CVE-2021-26701: .NET Core Remote Code Execution Vulnerability

* Wed Feb 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt1
- .NET 5.0.3 and .NET SDK 5.0.103
- CVE-2021-1721: .NET Core Denial of Service Vulnerability
- CVE-2021-24112: .NET 5 and .NET Core Remote Code Execution Vulnerability

* Thu Jan 14 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- .NET 5.0.2 and .NET SDK 5.0.102

* Sun Aug 02 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script) (ALT bug 38744)
- .NET Core 3.1.6 - July 14, 2020
- CVE-2020-1108: .NET Core Denial of Service Vulnerability
- CVE-2020-1147: NET Core Remote Code Execution Vulnerability

* Mon Dec 16 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version (3.1.0) with rpmgs script
- .NET Core 3.1.0 - December 3, 2019

* Fri Nov 08 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.0-alt1.qa1
- Dropped hack for ld-linux path on aarch64.

* Sat Oct 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script
- .NET Core 3.0.0 - September 23, 2019

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- new version 2.1.9 (with rpmrb script)
- includes .NET Core 2.1.9, ASP.NET Core 2.1.9 and .NET Core SDK 2.1.505
- CVE-2019-0657: .NET Core NuGet Tampering Vulnerability

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)
- includes .NET Core 2.1.6, ASP.NET Core 2.1.6 and .NET Core SDK 2.1.500

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: new version (2.1.5) (based on changes by lav@)
- includes .NET Core 2.1.5, ASP.NET Core 2.1.5 and .NET Core SDK 2.1.403

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version (2.1.4) with rpmgs script
- includes .NET Core 2.1.4, ASP.NET Core 2.1.4 and .NET Core SDK 2.1.402

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version (2.1.3) with rpmgs script
- includes .NET Core 2.1.3, ASP.NET Core 2.1.3 and .NET Core SDK 2.1.401

* Mon Feb 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- CVE-2018-0764, CVE-2018-0786

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- new version (2.0.0) with rpmgs script

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- enable autoreq for libs, shell
- fix buildreqs to correct generated requires

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview2
- add provides with .NET Core runtime/SDK versions

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Thu May 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1.005977
- .NET Core Runtime 2.0.0 Preview 1 build 002111
- .NET Core SDK 2.0.0 Preview 1 build 005977

* Fri Apr 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script (SDK 1.0.3)

* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
