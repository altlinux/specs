%def_with bootstrap
%define corerelease 2.0.0-preview1-002111-00
%define pre -preview1

Name: dotnet-corefx
Version: 2.0.0
Release: alt1.preview1

Summary: .NET Core foundational libraries, called CoreFX

License: MIT
Url: https://github.com/dotnet/corefx
Group: Development/Other

# Source-url: https://github.com/dotnet/corefx/archive/v%version%pre.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%if_with bootstrap
BuildRequires: dotnet-bootstrap
%else
BuildRequires: dotnet
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
%endif

#DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap ./build.sh x64 release managed verbose
#DOTNET_TOOL_DIR=%_libdir/dotnet-bootstrap ./build-native.sh x64 release verbose

%install
mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
cp -a %_libdir/dotnet-bootstrap/shared/Microsoft.NETCore.App/%version-*/{System*.so,*.dll} %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
# read during dotnet --version
cp -a %_libdir/dotnet-bootstrap/shared/Microsoft.NETCore.App/%version-*/System.Native.a %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/

# FIXME: possible hack
cp -a %_libdir/dotnet-bootstrap/shared/Microsoft.NETCore.App/%version-*/Microsoft.NETCore.App.deps.json %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/

# already in coreclr
rm -f %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/System.Globalization.Native.so

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
* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1

* Wed Apr 19 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
