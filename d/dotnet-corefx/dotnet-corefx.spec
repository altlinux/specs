# FIXME: build from sources
%def_with bootstrap
%define corerelease 2.0.0-preview2-25407-01
%define pre preview2

Name: dotnet-corefx
Version: 2.0.0
Release: alt3.%pre

Summary: .NET Core foundational libraries, called CoreFX

License: MIT
Url: https://github.com/dotnet/corefx
Group: Development/Other

# Source-url: https://github.com/dotnet/corefx/archive/v%{version}-%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%if_with bootstrap
BuildRequires: dotnet-bootstrap-runtime = %corerelease
%define bootstrapdir %_libdir/dotnet-bootstrap
%else
BuildRequires: dotnet
%define bootstrapdir %_libdir/dotnet
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
mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
%if_with bootstrap
# native
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%version-*/System*.so %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
# managed
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%version-*/*.dll %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
# read during dotnet --version
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%version-*/System.Native.a %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/

# FIXME: possible hack
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%version-*/Microsoft.NETCore.App.deps.json %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/

# already in coreclr
rm -f %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/System.Globalization.Native.so
%endif

# FIXME: possible hack
cat <<EOF >%buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/.version
0
%corerelease
EOF

%files
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/.version
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/Microsoft.NETCore.App.deps.json
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/System*.so
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/System.Native.a
%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/*.dll

%changelog
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
