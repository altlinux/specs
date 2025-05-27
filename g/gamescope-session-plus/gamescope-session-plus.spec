%define _unpackaged_files_terminate_build 1
%define commit 35ac9fe5f22f3e8d98a34ecb032bc601c67bfe01

Name: gamescope-session-plus
Version: 0.0.2.git35ac9f
Release: alt1

Summary: Common files for sessions based on gamescope

License: MIT
Group: Games/Other
Url: https://github.com/ChimeraOS/gamescope-session

# Source-url: https://github.com/ChimeraOS/gamescope-session/archive/%commit.tar.gz?/gamescope-session-%commit.tar.gz
Source: %name-%version.tar

Patch1: shebang.patch
Patch2: use-systemctl.patch

ExclusiveArch: x86_64 aarch64

%add_findreq_skiplist %_datadir/%name/%name
Requires: gamescope
Requires: ibus

%description
Common files for Steam Big Picture Mode/Gamemode/ingame sessions based on gamescope

%prep
%setup
%patch1 -p1
%patch2 -p1

%build

%install
mkdir -p %buildroot%_bindir/
cp -rv usr/bin/* %buildroot%_bindir/

mkdir -p %buildroot%_datadir/
cp -rv usr/share/* %buildroot%_datadir/

mkdir -p %buildroot%_userunitdir/
cp -v usr/lib/systemd/user/* %buildroot%_userunitdir/

%files
%doc README.md LICENSE
%_bindir/%name
%_bindir/export-gpu
%dir %_datadir/%name/
%_datadir/%name/%name
%_datadir/%name/device-quirks
%_userunitdir/%name@.service

%changelog
* Tue May 27 2025 Mikhail Tergoev <fidel@altlinux.org> 0.0.2.git35ac9f-alt1
- updated to upstream git 35ac9f
- added build for aarch64
- fixed reboot and poweroff (thx boria138@) (ALT bug: 54447)

* Fri Aug 02 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1.gitf8390d-alt1
- initial build for ALT Sisyphus
