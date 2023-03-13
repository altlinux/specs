%define _unpackaged_files_terminate_build 1

%define _dotnet_major 8.0
%define _dotnet_corerelease 8.0.0-preview.1.23110.8
%define _dotnet_sdkmanifestsrelease 8.0.100-preview.1
%define _dotnet_sdkrelease 8.0.100-preview.1.23115.2
%define _dotnet_aspnetcorerelease 8.0.0-preview.1.23112.2
%define _dotnet_templatesrelease 8.0.0-preview.1.23112.2
%define _dotnet_coreapprefrelease 8.0.0-preview.1.23110.8
%define _dotnet_aspnetcoreapprefrelease 8.0.0-preview.1.23112.2
%define _dotnet_netstandartrelease 2.1.0
%define preview .preview.1.23115.2
%define _dotnet_coreshortrelease 8.0.0%preview
%define _dotnet_sdkshortrelease 8.0.100%preview

%define _dotnetdir %_libdir/%name

Name: dotnet-bootstrap-%_dotnet_major
Version: 8.0.0%preview
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# To check we manually update download url
# from https://github.com/dotnet/core/tree/master/release-notes/6.0

# x86_64
# Source-url: https://download.visualstudio.microsoft.com/download/pr/e2578737-231b-493c-a6ee-f181496fe679/18038808d2621094ebe172ca011a7c22/dotnet-sdk-8.0.100-preview.1.23115.2-linux-x64.tar.gz
Source: %name-%version.tar

# aarch64
# Source2-url: https://download.visualstudio.microsoft.com/download/pr/57c316ef-4b1d-4b1e-b180-f38302132d3d/b938e1b373897fadfb25ff4b55ca32e6/dotnet-sdk-8.0.100-preview.1.23115.2-linux-arm64.tar.gz
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
%_dotnet_sdkmanifests/
%dir %_dotnetdir/shared/
%dir %_dotnetdir/shared/Microsoft.NETCore.App/
%_dotnet_coreapp/
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%_dotnet_aspnetcoreapp/
%_dotnetdir/LICENSE.txt
%_dotnetdir/ThirdPartyNotices.txt

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.preview.1.23115.2-alt1
- The .NET 8.0 and .NET SDK 8.0.0 preview
- initial release for ALT Sisyphus
