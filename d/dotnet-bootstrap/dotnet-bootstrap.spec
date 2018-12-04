%define _unpackaged_files_terminate_build 1

%define sdkversion 2.1.500
%define coreversion 2.1.6

Name: dotnet-bootstrap
Version: 2.1.6
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# FIXME: broken due sdk/core versions mismatch
#%define downloadversion 2.1.403
# from https://www.microsoft.com/net/download/dotnet-core/2.1
# SHA512 
# Source-url: https://download.visualstudio.microsoft.com/download/pr/e5eef3df-d2e3-429b-8204-f58372eb6263/20c825ddcc6062e93ff0c60e8354d3af/dotnet-sdk-%sdkversion-linux-x64.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

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

Provides: dotnet-bootstrap-runtime = %coreversion
Provides: dotnet-bootstrap-sdk = %sdkversion

%description
This package contains full .NET Core SDK binaries, needed for bootstrap build.

https://github.com/dotnet/core/blob/master/release-notes/download-archives/%version-download.md

%prep
%setup

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb (TODO)
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|libsosplugin.so|libsos.so|g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

%files
%dir %_libdir/%name/
#_libdir/%name/additionalDeps/
%dir %_libdir/%name/host/
%dir %_libdir/%name/host/fxr/
%_libdir/%name/host/fxr/%coreversion/
%dir %_libdir/%name/sdk/
%_libdir/%name/sdk/%sdkversion/
%dir %_libdir/%name/shared/
%dir %_libdir/%name/shared/Microsoft.NETCore.App/
%_libdir/%name/shared/Microsoft.NETCore.App/%coreversion/
# TODO: drop from bootstrap
%dir %_libdir/%name/shared/Microsoft.AspNetCore.All/
%dir %_libdir/%name/shared/Microsoft.AspNetCore.App/
%_libdir/%name/shared/Microsoft.AspNetCore.All/%coreversion/
%_libdir/%name/shared/Microsoft.AspNetCore.App/%coreversion/
#_libdir/%name/store/
%_libdir/%name/LICENSE.txt
%_libdir/%name/ThirdPartyNotices.txt
%_libdir/%name/dotnet

%changelog
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
