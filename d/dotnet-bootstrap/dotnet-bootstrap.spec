%define sdkversion 2.1.4
%define coreversion 2.0.5

Name: dotnet-bootstrap
Version: 2.0.5
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# broken due sdk/core versions mismatch
%define downloadversion 2.1.4
# from https://github.com/dotnet/core/blob/master/release-notes/download-archives/2.0.5-download.md
# SHA512 05fe90457a8b77ad5a5eb2f22348f53e962012a55077ac4ad144b279f6cad69740e57f165820bfd6104e88b30e93684bde3e858f781541d4f110f28cd52ce2b7
# Source-url: https://download.microsoft.com/download/1/1/5/115B762D-2B41-4AF3-9A63-92D9680B9409/dotnet-sdk-%downloadversion-linux-x64.tar.gz
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
Requires: libicu56

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

# due missed lldb
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|.*libsosplugin.so.*||g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

%files
%dir %_libdir/%name/
%_libdir/%name/additionalDeps/
%dir %_libdir/%name/host/
%dir %_libdir/%name/host/fxr/
%_libdir/%name/host/fxr/%coreversion/
%dir %_libdir/%name/sdk/
%_libdir/%name/sdk/%sdkversion/
%dir %_libdir/%name/shared/
%dir %_libdir/%name/shared/Microsoft.NETCore.App/
%_libdir/%name/shared/Microsoft.NETCore.App/%coreversion/
%_libdir/%name/store/
%_libdir/%name/LICENSE.txt
%_libdir/%name/ThirdPartyNotices.txt
%_libdir/%name/dotnet

%changelog
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
