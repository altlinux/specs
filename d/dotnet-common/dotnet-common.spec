%define corerelease 2.0.0-preview2-25407-01

Name: dotnet-common
Version: 2.0.0
Release: alt3.preview2

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
NAME="GNU/Linux"
VERSION=""
ID=linux
VERSION_ID=""
EOF

cat <<EOF >fake-os-release-fedora
NAME="Fedora"
VERSION="24"
ID=fedora
VERSION_ID="24"
EOF

%install
mkdir -p %buildroot%_libdir/dotnet/
install -m644 fake-os-release %buildroot%_libdir/dotnet/fake-os-release
install -m644 fake-os-release-fedora %buildroot%_libdir/dotnet/fake-os-release-fedora

mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/%corerelease/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/%corerelease/

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

%changelog
* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- .NET Core 2.0.0 Preview 2 (2.0.0-preview2-25407-01)

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- use linux-64 in fake-os-release

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- use full corerelease

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
