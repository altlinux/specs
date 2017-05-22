%define pre -preview1

Name: dotnet-sdk
Version: 2.0.0
Release: alt0.preview1

Summary: SDK for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: dotnet-bootstrap

%description
SDK for the .NET Core runtime and libraries.

Just copying binary now.

%prep
%setup

%install
mkdir -p %buildroot%_libdir/dotnet/sdk/%version%pre/
cp -a %_libdir/dotnet-bootstrap/sdk/%version-*/* %buildroot%_libdir/dotnet/sdk/%version%pre/

%files
%dir %_libdir/dotnet/sdk/
%_libdir/dotnet/sdk/%version%pre/

%changelog
* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
