%define pre preview2

Name: dotnet-bootstrap
Version: 2.0.0
Release: alt0.%pre

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# Source-url: https://download.microsoft.com/download/F/A/A/FAAE9280-F410-458E-8819-279C5A68EDCF/dotnet-sdk-2.0.0-preview2-006497-linux-x64.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no
AutoProv: no

BuildRequires: libunwind

Requires: libcrypto10 libssl10 libunwind liblttng-ust

%description
This package contains full .NET Core SDK binaries, needed for bootstrap build.

https://github.com/dotnet/core/blob/master/release-notes/download-archives/2.0.0-%pre-download.md

%prep
%setup

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/libsosplugin.so
%__subst "s|.*libsosplugin.so.*||g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/*/Microsoft.NETCore.App.deps.json

%files
%_libdir/%name/

%changelog
* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview2
- .NET Core Runtime 2.0.0 Preview 2 build 25407-01
- .NET Core SDK 2.0.0 Preview 2 build 006497

* Thu May 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1.005977
- .NET Core Runtime 2.0.0 Preview 1 build 002111
- .NET Core SDK 2.0.0 Preview 1 build 005977

* Fri Apr 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script (SDK 1.0.3)

* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
