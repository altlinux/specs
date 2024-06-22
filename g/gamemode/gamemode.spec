%define soversion 0
%define _sysusersdir /lib/sysusers.d

Name: gamemode
Version: 1.8.1
Release: alt2

Summary: Optimise Linux system performance on demand 
License: BSD
Group: Games/Other

Url: https://github.com/FeralInteractive/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

Requires: lib%{name}auto%soversion = %EVR

BuildRequires: cmake
BuildRequires: libdbus-devel
BuildRequires: libinih-devel
BuildRequires: libstdc++-devel
BuildRequires: libsystemd-devel
BuildRequires: meson

%description
GameMode is a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process.
GameMode was designed primarily as a stop-gap solution to problems with the Intel and AMD CPU powersave or ondemand governors, but is now host to a range of optimisation features and configurations.
Currently GameMode includes support for optimisations including:
- CPU governor
- I/O priority
- Process niceness
- Kernel scheduler (SCHED_ISO)
- Screensaver inhibiting
- GPU performance mode (NVIDIA and AMD), GPU overclocking (NVIDIA)
- Custom scripts

%package daemon
Summary: The GameMode daemon required by GameMode enabled games
Group: Games/Other

%description daemon
The GameMode daemon is installed as a D-Bus Service and will start
automatically on first access by a client.

%package -n lib%name%soversion
Summary: GameMode client library
Group: System/Libraries
Requires: %name-daemon = %EVR

%description -n lib%name%soversion
The client library used by games or libgamemodeauto to talk to the GameMode daemon.

%package -n lib%{name}auto%soversion
Summary: Helper library allowing to equip any game with GameMode support
Group: System/Libraries
Requires: lib%name%soversion = %EVR

%description -n lib%{name}auto%soversion
The helper library allows you to use GameMode with any Game by
preloading it into the game.

%package -n lib%name-devel
Summary: Development files for GameMode
Group: Development/C

%description -n lib%name-devel
Development files for GameMode

%prep
%setup

%build
%add_optflags -Wno-error=implicit-function-declaration
%meson -Dwith-systemd-group-dir=%_sysusersdir
%meson_build

%install
%meson_install
%__rm -f %buildroot%_libdir/lib%{name}auto.a

%files
%doc LICENSE.txt README.md
%_bindir/%{name}run
%_bindir/%{name}list
%_bindir/%{name}-simulate-game
%_man1dir/%{name}run*
%_man1dir/%{name}list*
%_man1dir/%{name}-simulate-game*

%files daemon
%_bindir/%{name}d
%_libexecdir/cpucorectl
%_libexecdir/cpugovctl
%_libexecdir/gpuclockctl
%_libexecdir/procsysctl
%config %_sysconfdir/security/limits.d/10-%name.conf
%config %_sysusersdir/%name.conf
%dir %_datadir/%name
%_datadir/%name/%name.ini
%_datadir/dbus-1/services/com.feralinteractive.GameMode.service
%_datadir/metainfo/io.github.feralinteractive.%name.metainfo.xml
%_datadir/polkit-1/actions/com.feralinteractive.GameMode.policy
%_datadir/polkit-1/rules.d/%name.rules
%_userunitdir/%{name}d.service
%_man8dir/%{name}d*

%files -n lib%name%soversion
%_libdir/lib%name.so.*

%files -n lib%{name}auto%soversion
%_libdir/lib%{name}auto.so.*

%files -n lib%name-devel
%_includedir/%{name}_client.h
%_pkgconfigdir/%name.pc
%_pkgconfigdir/lib%{name}auto.pc
%_libdir/lib%name.so
%_libdir/lib%{name}auto.so

%changelog
* Sat Jun 22 2024 Nazarov Denis <nenderus@altlinux.org> 1.8.1-alt2
- Fix FTBFS

* Tue Dec 12 2023 Nazarov Denis <nenderus@altlinux.org> 1.8.1-alt1
- New version 1.8.1.

* Thu Dec 07 2023 Nazarov Denis <nenderus@altlinux.org> 1.8-alt2
- Separate daemon and libraries

* Wed Dec 06 2023 Nazarov Denis <nenderus@altlinux.org> 1.8-alt1
- New version 1.8.

* Sat Jul 29 2023 Nazarov Denis <nenderus@altlinux.org> 1.7-alt1.1
- Fix FTBFS

* Fri Aug 05 2022 Nazarov Denis <nenderus@altlinux.org> 1.7-alt1
- Version (ALT #43455)

* Fri Feb 19 2021 Nazarov Denis <nenderus@altlinux.org> 1.6.1-alt1
- Version 1.6.1

* Fri Sep 11 2020 Nazarov Denis <nenderus@altlinux.org> 1.6-alt1
- Version 1.6

* Wed Mar 04 2020 Nazarov Denis <nenderus@altlinux.org> 1.5.1-alt1
- Version 1.5.1
- Use shared inih library

* Tue Feb 18 2020 Nazarov Denis <nenderus@altlinux.org> 1.5-alt1
- Initial build for ALT Linux
