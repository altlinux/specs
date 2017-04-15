Name: dotnet-bootstrap
Version: 1.0.4
Release: alt1

Summary: .NET Core SDK binaries

License: MIT
Url: https://github.com/dotnet
Group: Development/Other

# Download URL from https://www.microsoft.com/net/download/linux
# 1.0.4 LTS for Fedora 24
# Source-url: https://go.microsoft.com/fwlink/?linkid=843461
Source: %name-%version.tar

ExclusiveArch: x86_64

#Requires: /proc
#BuildPreReq: /proc

%set_verify_elf_method textrel=relaxed
AutoReq: no
AutoProv: no

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

%files
%_libdir/%name/

%changelog
* Fri Apr 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial release for ALT Sisyphus
