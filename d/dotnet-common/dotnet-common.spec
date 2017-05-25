%define pre -preview1

Name: dotnet-common
Version: 2.0.0
Release: alt0.preview1

Summary: Common dir and files for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

%description
Common dir and files for the .NET Core runtime and libraries.

%prep
%setup

# make scripts happy
cat <<EOF >fake-os-release
NAME="Fedora"
VERSION="24"
ID=fedora
VERSION_ID="24"
EOF

%install
mkdir -p %buildroot%_libdir/dotnet/
install -m644 fake-os-release %buildroot%_libdir/dotnet/fake-os-release

mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/%version%pre/

%files
%dir %_libdir/dotnet/
%_libdir/dotnet/fake-os-release

%dir %_libdir/dotnet/host/
%dir %_libdir/dotnet/host/fxr/
%dir %_libdir/dotnet/host/fxr/%version%pre/

%dir %_libdir/dotnet/shared/
%dir %_libdir/dotnet/shared/Microsoft.NETCore.App/
%dir %_libdir/dotnet/shared/Microsoft.NETCore.App/%version%pre/

%changelog
* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
