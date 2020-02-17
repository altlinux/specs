%define soversion 0
%define inih_commit 745ada6724038cde32ff6390b32426cbdd5e532b

Name: gamemode
Version: 1.5
Release: alt1

Summary: Optimise Linux system performance on demand 
License: BSD
Group: Games/Other

Url: https://github.com/FeralInteractive/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: https://github.com/FeralInteractive/%name/archive/%version/%name-%version.tar.gz
Source1: https://github.com/FeralInteractive/inih/archive/%inih_commit/inih-%inih_commit.tar.gz

Requires: lib%name%soversion = %EVR

BuildRequires: cmake
BuildRequires: libdbus-devel
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

%package -n lib%name%soversion
Summary: Libraries for GameMode
Group: System/Libraries

%description -n lib%name%soversion
Libraries for GameMode
   
%package -n lib%name-devel
Summary: Development files for GameMode
Group: Development/C

%description -n lib%name-devel
Development files for GameMode

%prep
%setup -b 1
%__mv -Tf ../inih-%inih_commit subprojects/inih

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE.txt README.md
%_bindir/gamemoded
%_bindir/gamemoderun
%_datadir/dbus-1/services/com.feralinteractive.GameMode.service
%_datadir/polkit-1/actions/com.feralinteractive.GameMode.policy
%_libexecdir/cpugovctl
%_libexecdir/gpuclockctl
%_libexecdir/systemd/user/gamemoded.service
%_man8dir/%{name}d.8*

%files -n lib%name%soversion
%_libdir/lib%name.so.*
%_libdir/lib%{name}auto.so.*

%files -n lib%name-devel
%_includedir/%{name}_client.h
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-auto.pc
%_libdir/lib%name.so
%_libdir/lib%{name}auto.so

%changelog
* Tue Feb 18 2020 Nazarov Denis <nenderus@altlinux.org> 1.5-alt1
- Initial build for ALT Linux

