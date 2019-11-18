Name: rawgl
Version: 0.2.1
Release: alt1

Summary: Another World/Out of This World engine reimplementation
Summary(ru_RU.UTF-8): Воссоздание движка Another World/Out of This World

License: GPLv2+
Group: Games/Arcade
Url: https://github.com/cyxx/rawgl

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Aug 12 2019
# optimized out: libSDL2-devel libstdc++-devel python-base python-modules python3 python3-base
BuildRequires: gcc-c++ libxcb libGL-devel libSDL2_mixer-devel unzip zlib-devel

%description
raw(gl) is a rewrite of the engine used in the game
Another World/Out of this World from Eric Chahi.

This program is designed as a cross-platform
replacement for the original executable.

You need the original game datafiles (Amiga, DOS,
15th/20th anniversary editions, Win31 or 3DO).

%description -l ru_RU.UTF-8
raw(gl) - воссозданый движок, используемый в играх
Another World/Out of this World авторства Eric Chahi.

Программа создана как кросс-платформенная замена
оригинального движка.

Для запуска игры необходимы файлы данных оригинальной игры
(Amiga, DOS, 15th/20th anniversary editions, Win31 или 3DO).

%prep
%setup 

%build
%make_build OPTIMISE="%optflags"

%install
install -Dm0755 %name %buildroot%_bindir/%name

%find_lang %name

%files -f %name.lang
%doc README.md docs/*
%_bindir/*


%changelog
* Mon Nov 18 2019 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt1
- initial build for ALT Sisyphus

