# TODO: build from sources
%define _unpackaged_files_terminate_build 1
%def_disable netstandart
%def_enable dotnet_host

%define _dotnet_major 11.0
%define preview ~rc.1.26425.128
%define _dotnet_coreversion 11.0.0%preview
%define _dotnet_sdkversion 11.0.100%preview

%define _dotnet_corerelease 11.0.0-rc.1.26425.128
%define _dotnet_corerelease1 11.0.0-rc.1.26425.128

%define _dotnet_sdkmanifestsrelease1 11.0.100-preview.6
%define _dotnet_sdkmanifestsrelease 11.0.100-rc.1
%define _dotnet_sdkrelease 11.0.100-rc.1.26425.128

%define _dotnet_templatesrelease %_dotnet_corerelease1
%define _dotnet_coreapprefrelease %_dotnet_corerelease
%define _dotnet_netstandartrelease 2.1.0

%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major

Name: dotnet-sdk-%_dotnet_major
Version: %_dotnet_sdkversion
Release: alt1

Summary: SDK for the .NET 11

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

# This optional AOT SDK library is prebuilt; without it the muxer uses dotnet.dll.
rm -f %buildroot%_dotnet_sdk/libdotnet-aot.so

# RC1 ships the ASP.NET CLI tools only as prebuilt NativeAOT binaries.
# Do not package them until dotnet-aspnetcore builds aspnetcoretools from source.
rm -rf %buildroot%_dotnet_sdk/DotnetTools/aspnetcoretools

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

%ifdef _dotnet_sdkmanifestsrelease0
mkdir -p %buildroot%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease0/
cp -a %bootstrapdir/sdk-manifests/%_dotnet_sdkmanifestsrelease0/* %buildroot%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease0/
%endif

# apphost used as executable, f.i. dotnet tool install --global paket will install it in $HOME/.dotnet/tools as paket
# rewrite one with our binary
rm -vf %buildroot%_dotnet_sdk/AppHostTemplate/apphost
cp -v %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost %buildroot%_dotnet_sdk/AppHostTemplate/apphost

# Replace prebuilt launchers with the apphost built by dotnet-runtime.
# This is a shell implementation of CreateAppHost.
PLACEHOLDER="c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2"
for i in %buildroot%_dotnet_sdk/MSBuild \
         %buildroot%_dotnet_sdk/Roslyn/bincore/{VBCSCompiler,csc,vbc} ; do
    cp -v %buildroot%_dotnet_sdk/AppHostTemplate/apphost $i
    APP_DLL="$(basename $i).dll\x0"
    PADDED_APP_DLL=$(printf "%%-${#PLACEHOLDER}s" "$APP_DLL")
    subst "s|${PLACEHOLDER}|${PADDED_APP_DLL}zz|" $i
done

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
%ifdef _dotnet_sdkmanifestsrelease0
%_dotnetdir/sdk-manifests/%_dotnet_sdkmanifestsrelease0/
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
* Thu Sep 24 2026 Vitaly Lipatov <lav@altlinux.ru> 11.0.100~rc.1.26425.128-alt1
- Update to .NET SDK 11.0.100-rc.1.26425.128.

* Tue Sep 01 2026 Vitaly Lipatov <lav@altlinux.ru> 11.0.100~rpreview.7.26381.103-alt1
- .NET 11 preview.7 SDK.
- Update SDK manifests paths.
- Replace prebuilt launchers and remove prebuilt NativeAOT tools.

* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 11.0.100~rc1-alt1
- .NET SDK 11.0.100 rc 1
- initial build for ALT Sisyphus
