%define sdkrelease 2.0.0-preview1-005977
%define pre -preview1

Name: dotnet-sdk
Version: 2.0.0
Release: alt2.preview1

Summary: SDK for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: dotnet-bootstrap

Requires: dotnet-common >= %version

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%description
SDK for the .NET Core runtime and libraries.

Just copying binary now.

%prep
%setup

%install
mkdir -p %buildroot%_libdir/dotnet/sdk/%sdkrelease/
cp -a %_libdir/dotnet-bootstrap/sdk/%version-*/* %buildroot%_libdir/dotnet/sdk/%sdkrelease/
# dotnet --info get RID string from this .version, line 3
cp -a %_libdir/dotnet-bootstrap/sdk/%version-*/.version %buildroot%_libdir/dotnet/sdk/%sdkrelease/

%files
%dir %_libdir/dotnet/sdk/
%_libdir/dotnet/sdk/%sdkrelease/

%changelog
* Wed May 31 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2.preview1
- fix requires, provides
- add missed .version

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- fix packing

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
