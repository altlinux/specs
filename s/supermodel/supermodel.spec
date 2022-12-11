Name: supermodel
Version: 0.2a
Release: alt2
Summary: A cross-platform Sega Model 3 arcade machine emulator
Summary(ru_RU.UTF-8): Кросплатформенный эмулятор аркадного автомата Sega Model 3
Group: Emulators
License: GPLv2
Url: http://www.supermodel3.com/
Packager: Artyom Bystrov <arbars@altlinux.org>
Source: %name-%version.tar
Source1: %name.6
Source2: run_supermodel

BuildRequires: gcc-c++ libxcb libSDL2-devel libSDL2_net-devel zlib-devel libGLU-devel

%description
Supermodel emulates Sega's Model 3 arcade platform, allowing you
to play a number of ground-breaking arcade classics on your PC.
It uses OpenGL and the SDL library, and can run on Windows,
Linux, and Mac OS X. The source code is freely available under
the terms of the GNU General Public License.

%description -l ru_RU.UTF-8
Supermodel эмулирует аркадную платформу Sega Model 3, позволяя
играть в несколько сногшибательных аркадных игр на ПК.
Эмулятор использует OPenGL и библиотеки SDL, благодаря чему
эмулятор работает на Windows, Mac OS X и Linux. Исходный код
доступен на условиях лицензии GNU GPL.

%prep
%setup -n %name-%version

# Initial Elbrus support (thanks to ilyakurdyukov@)
%ifarch %e2k
sed -i 's/k_framePeriod/(int)&/g' Src/Model3/DSB.cpp
%endif 

%build
#%%make_build
%make -f Makefiles/Makefile.UNIX NET_BOARD=1 VERBOSE=1

%install
# %makeinstall_std
mkdir -p %buildroot%_datadir/%name/Config
mkdir -p %buildroot/%_man6dir
mv Config/* %buildroot%_datadir/%name/Config
install -D -m 755 bin/%name %buildroot%_libexecdir/%name
install -p -m 644 %SOURCE1  %buildroot/%_man6dir
install -D -m 755 %SOURCE2  %buildroot%_bindir/supermodel

%files
%_libexecdir/%name
%_bindir/%name
%_datadir/%name/Config/*
%doc Docs/*
%_man6dir/*

%changelog
* Sat Dec 10 2022 Artyom Bystrov <arbars@altlinux.org> 0.2a-alt2
- Initial Elbrus support (thanks to ilyakurdyukov@)

* Sat Dec 10 2022 Artyom Bystrov <arbars@altlinux.org> 0.2a-alt1
- Initial build for Sisyphus
