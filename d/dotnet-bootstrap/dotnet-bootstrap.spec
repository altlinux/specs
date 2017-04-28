Name: dotnet-bootstrap
Version: 1.1.1
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# Download URL from https://www.microsoft.com/net/download/linux
# 1.1.1 for Fedora 24
# TODO: use direct url
# Source-url: https://go.microsoft.com/fwlink/?linkid=847100
Source: %name-%version.tar

ExclusiveArch: x86_64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no
AutoProv: no

BuildRequires: libunwind libicu56

Requires: libicu56 libcrypto10 libssl10 libunwind libuv liblttng-ust

%description
This package contains full .NET Core SDK binaries, needed for bootstrap build.

%prep
%setup

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/

# due missed lldb
rm -f %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/1.1.1/libsosplugin.so
%__subst "s|.*libsosplugin.so.*||g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/1.1.1/Microsoft.NETCore.App.deps.json

%files
%_libdir/%name/

%changelog
* Fri Apr 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version (1.1.1) with rpmgs script (SDK 1.0.3)

* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
