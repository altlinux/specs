Name: mtproto-proxy
Version: 0.1
Release: alt1

Summary: MTProxy

Group: Networking/Instant messaging
License: GPLv2

Url: https://github.com/TelegramMessenger/MTProxy
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/TelegramMessenger/MTProxy.git
Source: %name-%version.tar

BuildRequires: gcc-c++

BuildRequires: zlib-devel libssl-devel > 1.0.0

ExclusiveArch: x86_64

%description
MTProxy.

%prep
%setup
%__subst "s|^COMMIT :=.*|COMMIT := %version-%release|g" Makefile

%build
%make_build

%install
install -D objs/bin/mtproto-proxy %buildroot%_bindir/mtproto-proxy

%files
%_bindir/mtproto-proxy


%changelog
* Thu May 31 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
