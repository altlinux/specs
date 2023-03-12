Name:    telegram-bot-api
Version: 6.6
Release: alt1

Summary: The Telegram Bot API provides an HTTP API for creating Telegram Bots.
License: Boost Software License
Group:   Other
Url:     https://github.com/tdlib/telegram-bot-api

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sun Mar 12 2023
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 libstdc++-devel pkg-config python3-base sh4
BuildRequires: cmake gcc-c++ gperf libssl-devel python3 zlib-devel

%description
The Telegram Bot API provides an HTTP API for creating Telegram Bots.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_bindir/*

%changelog
* Sun Mar 12 2023 Hihin Ruslan <ruslandh@altlinux.ru> 6.6-alt1
- Initial build for Sidyphus
