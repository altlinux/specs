%define _unpackaged_files_terminate_build 1

%define _dotnet_major 10.0
%define _dotnet_coreversion 10.0.4
%define _dotnet_sdkversion 10.0.200

%define _dotnet_corerelease 10.0.4
%define _dotnet_corerelease1 10.0.4

#define _dotnet_sdkmanifestsrelease1 9.0.100
%define _dotnet_sdkmanifestsrelease 10.0.100
%define _dotnet_sdkrelease 10.0.200

%define _dotnet_templatesrelease %_dotnet_corerelease1
%define _dotnet_coreapprefrelease %_dotnet_corerelease
%define _dotnet_netstandartrelease 2.1.0

%define _dotnet_aspnetcorerelease %_dotnet_corerelease1
%define _dotnet_aspnetcoreapprefrelease %_dotnet_corerelease1


%define _dotnetdir %_libdir/%name

Name: dotnet-bootstrap-%_dotnet_major
Version: %_dotnet_sdkversion
Release: alt1

Summary: .NET 10 SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# Check actual releases here:
# from https://github.com/dotnet/core/tree/master/release-notes/10.0

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

BuildRequires: libunwind >= 1.1
BuildRequires: liblttng-ust >= 2.9.0
BuildRequires: libcurl
BuildRequires: libkrb5

# for System.Security.Cryptography.Native.OpenSsl.so
# but already required by libkrb5
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
%_dotnetdir/dnx
%dir %_dotnetdir/templates/
%_dotnet_templates/
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Host.%_dotnet_rid/
%_dotnet_coreapphost/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Ref/
%_dotnet_coreappref/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnet_aspnetcoreappref/
#%dir %_dotnetdir/packs/NETStandard.Library.Ref/
#%_dotnet_netstandart/
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
* Wed Apr 01 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.200-alt1
- new version (10.0.200)

* Mon Nov 17 2025 Vitaly Lipatov <lav@altlinux.ru> 10.0.100.rel-alt1
- The .NET 10.0.0 and .NET SDK 10.0.100 releases

* Wed Oct 15 2025 Vitaly Lipatov <lav@altlinux.ru> 10.0.100.rc2-alt1
- The .NET 10.0.0-rc.2 and .NET SDK 10.0.100-rc.2 release
