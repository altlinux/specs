# TODO
# warning: Macro %_dotnet_corerelease not found
# error: line 26: Dependency tokens must not contain '%<=>' symbols: BuildRequires: dotnet-bootstrap-runtime = %_dotnet_corerelease
# hsh-rebuild: pkg.tar: failed to fetch build dependencies.
%define _dotnet_corerelease 2.0.3

# FIXME: build from sources
%def_with bootstrap
%define pre %nil

Name: dotnet-corefx
Version: 2.0.3
Release: alt1

Summary: .NET Core foundational libraries, called CoreFX

License: MIT
Url: https://github.com/dotnet/corefx
Group: Development/Other

# Source-url: https://github.com/dotnet/corefx/archive/v%{version}%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

BuildRequires(pre): rpm-macros-dotnet >= %version

%if_with bootstrap
BuildRequires: dotnet-bootstrap-runtime = %_dotnet_corerelease
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif


Requires: dotnet-common >= %version

BuildRequires: libcurl-devel

%description
This package contains the the .NET Core foundational libraries, called CoreFX.
It includes classes for collections, file systems, console, XML, async and many others.

Just copied binaries now.

%prep
%setup

#find -type f -name "*.sh" | xargs subst "s|/etc/os-release|%_libdir/dotnet/fake-os-release|g"

%build
%if_with bootstrap
#
%else
#DOTNET_TOOL_DIR=%bootstrapdir ./build.sh x64 release managed verbose
#DOTNET_TOOL_DIR=%bootstrapdir ./build-native.sh x64 release verbose
%endif

%install
mkdir -p %buildroot%_dotnet_shared/
%if_with bootstrap
# native
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System*.so %buildroot%_dotnet_shared/
# managed
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_shared/
# read during dotnet --version
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Native.a %buildroot%_dotnet_shared/

# FIXME: possible hack
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/Microsoft.NETCore.App.deps.json %buildroot%_dotnet_shared/

# already in coreclr
rm -fv %buildroot%_dotnet_shared/System.Globalization.Native.so
%endif


%files
%_dotnet_shared/Microsoft.NETCore.App.deps.json
%_dotnet_shared/System*.so
%_dotnet_shared/System.Native.a
%_dotnet_shared/*.dll

%changelog
* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) with rpmgs script

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core 2.0.0 Release

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- build with strict dotnet-bootstrap require

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- rebuild without bootstrap with RID linux.x64

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1

* Wed Apr 19 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
