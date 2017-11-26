%define corerelease 2.0.3
%define sdkrelease 2.0.3

Name: dotnet-common
Version: 2.0.3
Release: alt1

Summary: Common dir and files for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

%description
Common dir and files for the .NET Core runtime and libraries.

%package -n rpm-macros-dotnet
Summary: RPM macros for build dotnet packages
Group: Development/Other

%description -n rpm-macros-dotnet
RPM macros for build dotnet packages.

%prep
%setup

# make scripts happy
cat <<EOF >fake-os-release
NAME="GNU/Linux"
VERSION=""
ID=linux
VERSION_ID=""
EOF

cat <<EOF >fake-os-release-fedora
NAME="Fedora"
VERSION="26"
ID=fedora
VERSION_ID="26"
EOF

cat <<EOF >macros
%%_dotnet_corerelease %corerelease
%%_dotnet_sdkrelease %sdkrelease
%%_dotnetdir %_libdir/dotnet
%%_dotnet_hostfxr %%_dotnetdir/host/fxr/%%_dotnet_corerelease/
%%_dotnet_shared %%_dotnetdir/shared/Microsoft.NETCore.App/%%_dotnet_corerelease/
%%_dotnet_sdk %%_dotnetdir/sdk/%%_dotnet_sdkrelease/
EOF

# FIXME: possible hack
cat <<EOF >.version
0
%corerelease
EOF


%install
mkdir -p %buildroot%_libdir/dotnet/
install -m644 fake-os-release %buildroot%_libdir/dotnet/fake-os-release
install -m644 fake-os-release-fedora %buildroot%_libdir/dotnet/fake-os-release-fedora

mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/%corerelease/

install -D -m644 macros %buildroot%_rpmmacrosdir/dotnet

install -D -m644 .version %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/.version

%files
%dir %_libdir/dotnet/
%_libdir/dotnet/fake-os-release
%_libdir/dotnet/fake-os-release-fedora

%dir %_libdir/dotnet/host/
%dir %_libdir/dotnet/host/fxr/
%dir %_libdir/dotnet/host/fxr/%corerelease/

%dir %_libdir/dotnet/shared/
%dir %_libdir/dotnet/shared/Microsoft.NETCore.App/
%dir %_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/.version

%files -n rpm-macros-dotnet
%_rpmmacrosdir/dotnet

%changelog
* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- build 2.0.3 release

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core 2.0.0 release
- add subpackage rpm-macros-dotnet

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- .NET Core 2.0.0 Preview 2 (2.0.0-preview2-25407-01)

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- use linux-64 in fake-os-release

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- use full corerelease

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
