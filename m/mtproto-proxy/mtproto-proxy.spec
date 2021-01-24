Name: mtproto-proxy
Version: 0.1
Release: alt3.git.52254f3

Summary: Simple MT-Proto proxy

Group: Networking/Instant messaging
License: GPLv2

Url: https://github.com/TelegramMessenger/MTProxy
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/TelegramMessenger/MTProxy.git
Source: %name-%version.tar
Patch:  mtproto-proxy.gcc10.patch

BuildRequires: gcc-c++

BuildRequires: zlib-devel libssl-devel > 1.0.0

ExclusiveArch: x86_64

%description
Simple MT-Proto proxy.

%prep
%setup
%patch -p1
subst "s|^COMMIT :=.*|COMMIT := %version-%release|g" Makefile

%build
%make_build

%install
install -D objs/bin/mtproto-proxy %buildroot%_bindir/mtproto-proxy

%files
%_bindir/mtproto-proxy


%changelog
* Sat Jan 23 2021 Fr. Br. George <george@altlinux.ru> 0.1-alt3.git.52254f3
- build tag dc0c7f3de40530053189c572936ae4fd1567269b

* Sat Jan 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2.git.2c94211
- build tag 2c942119c4ee340c80922ba11d14fb3b10d5e654

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu May 31 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
