%def_without bootstrap
%define pre %nil

Name: dotnet
Version: 2.0.5
Release: alt1

Summary: Installer packages for the .NET Core runtime and libraries

License: MIT
Url: https://github.com/dotnet/core-setup
Group: Development/Other

# Source-url: %url/archive/v%version%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: clang4.0 llvm4.0

BuildRequires: cmake libstdc++-devel

BuildRequires: dotnet-common >= %version
BuildRequires: rpm-macros-dotnet >= %version

Requires: dotnet-common >= %version
Requires: dotnet-coreclr >= %version
Requires: dotnet-corefx >= %version
#Requires: dotnet-sdk >= %version

%if_with bootstrap
BuildRequires: dotnet-bootstrap
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif


%description
This repo contains the code to build the .NET Core runtime,
libraries and shared host (dotnet) installers for all supported platforms.
It does not contain the actual sources to .NET Core runtime;
this source is split across the dotnet/coreclr repo (runtime)
and dotnet/corefx repo (libraries).

%prep
%setup
# since glibc 2.26 xlocale.h is removed
%__subst "s|xlocale.h|locale.h|" src/corehost/cli/json/casablanca/include/cpprest/asyncrt_utils.h

find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_dotnetdir/fake-os-release|g"

%build
#DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap ./build.sh x64 release verbose
cd src/corehost
DOTNET_TOOL_DIR=%bootstrapdir sh -x ./build.sh \
    --arch x64 \
    --hostver %_dotnet_corerelease \
    --apphostver %_dotnet_corerelease \
    --fxrver %_dotnet_corerelease \
    --policyver %_dotnet_corerelease \
    -portable \
    --commithash 0 || make -C bin/obj/Linux.x64.Release
# (parallel generation fail workaround)

%install
mkdir -p %buildroot%_dotnetdir/
install -m755 src/corehost/cli/exe/dotnet/dotnet %buildroot%_dotnetdir/

mkdir -p %buildroot%_dotnet_shared/
install -m755 src/corehost/cli/dll/libhostpolicy.so %buildroot%_dotnet_shared/
#install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_dotnet_shared/
mkdir -p %buildroot%_dotnet_hostfxr/
install -m755 src/corehost/cli/fxr/libhostfxr.so %buildroot%_dotnet_hostfxr/

mkdir -p %buildroot%_bindir/
ln -sr %buildroot%_dotnetdir/dotnet %buildroot%_bindir/dotnet

%files
%doc THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md LICENSE.TXT
%_bindir/dotnet
%_dotnetdir/dotnet

%_dotnet_hostfxr/libhostfxr.so

%_dotnet_shared/libhostpolicy.so
#_dotnet_shared/libhostfxr.so

%changelog
* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3
- .NET Core Runtime 2.0.0 Release

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packaging

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
