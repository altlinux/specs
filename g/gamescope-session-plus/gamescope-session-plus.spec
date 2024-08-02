%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec
%define commit f8390d38c1347a3ad60540db95bcca284b0f1982

Name: gamescope-session-plus
Version: 0.0.1.gitf8390d
Release: alt1

Summary: Common files for sessions based on gamescope

License: MIT
Group: Games/Other
Url: https://github.com/ChimeraOS/gamescope-session

# Source-url: https://github.com/ChimeraOS/gamescope-session/archive/%commit.tar.gz?/gamescope-session-%commit.tar.gz
Source: %name-%version.tar
Patch1: shebang.patch

ExclusiveArch: x86_64

%add_findreq_skiplist %_datadir/%name/%name
Requires: gamescope
Requires: ibus

%description
Common files for Steam Big Picture Mode/Gamemode/ingame sessions based on gamescope

%prep
%setup
%patch1 -p1

%build

%install
mkdir -p %buildroot%_bindir/
cp -rv usr/bin/* %buildroot%_bindir/

mkdir -p %buildroot%_datadir/
cp -rv usr/share/* %buildroot%_datadir/

mkdir -p %buildroot%_userunitdir/
cp -v usr/lib/systemd/user/* %buildroot%_userunitdir/

mkdir -p %buildroot%_libexecdir/
cp -v usr/libexec/* %buildroot%_libexecdir/

%files
%doc README.md LICENSE
%_bindir/%name
%_bindir/export-gpu
%dir %_datadir/%name/
%_datadir/%name/%name
%_datadir/%name/device-quirks
%_userunitdir/%name@.service
%_libexecdir/gamescope-sdl-workaround

%changelog
* Fri Aug 02 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1.gitf8390d-alt1
- initial build for ALT Sisyphus
