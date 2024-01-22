Name: opentabletdriver
Version: 0.6.4.0
Release: alt1

Summary: A cross-platform open source tablet driver
License: LGPLv3
Group: System/Kernel and hardware
URL: https://github.com/OpenTabletDriver/OpenTabletDriver

ExclusiveArch: x86_64

Source0: %name-%version.tar.gz
Source1: %name-%version-common.tar.gz
Patch0: %name-%version-alt-use-local-modules.patch
Patch1: %name-%version-alt-no-use-git.patch

Requires: dotnet-6.0
BuildRequires: dotnet-sdk-6.0
BuildRequires: jq
BuildRequires: /proc

%set_verify_elf_method relaxed

%description
OpenTabletDriver is an open source, cross platform, user mode tablet driver.The
goal of OpenTabletDriver is to be cross platform as possible with the highest
compatibility in an easily configurable graphical user interface.

%prep
%setup -a0 -a1 -n %name-%version
%patch0 -p1
%patch1 -p1

%build
./build.sh
./generate-rules.sh > ./70-%name.rules

%install
#makes dirs for files
mkdir -p %buildroot%_datadir
mkdir -p %buildroot%_udevrulesdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_prefix/lib/systemd/user/
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_datadir/applications
#install the commands, binaries, etc
mv bin/ %buildroot%_datadir/OpenTabletDriver/
mv scripts/* %buildroot%_bindir
install -D -m 0644 ./70-%name.rules %buildroot%_udevrulesdir/70-%name.rules
install -m 0644 ./%name.service %buildroot%_prefix/lib/systemd/user/%name.service
install -m 0755 ./OpenTabletDriver.UX/Assets/otd.png %buildroot%_datadir/pixmaps/otd.png
install -m 0755 ./OpenTabletDriver.desktop %buildroot%_datadir/applications/OpenTabletDriver.desktop

%post
#removes conflicting drivers
if lsmod | grep hid_uclogic > /dev/null ; then
     rmmod hid_uclogic || true
fi

if lsmod | grep wacom > /dev/null ; then
     rmmod wacom || true
fi
#enable systemd service
if [ $1 -eq 1 ] ; then
  systemctl --global enable %name.service >/dev/null 2>&1 || :
fi

%preun
#disable systemd service
if [ $1 -eq 0 ] ; then
    systemctl --global --no-reload disable %name.service > /dev/null 2>&1 || :
fi

%files
%_bindir/otd
%_bindir/otd-daemon
%_bindir/otd-gui
%_datadir/OpenTabletDriver/OpenTabletDriver.UX.Gtk
%_datadir/OpenTabletDriver/OpenTabletDriver.Daemon
%_datadir/OpenTabletDriver/OpenTabletDriver.Console
%_udevrulesdir/70-%name.rules
%_prefix/lib/systemd/user/%name.service
%_pixmapsdir/*.png
%_desktopdir/*.desktop

%changelog
* Sun Jan 21 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.4.0-alt1
- New version 0.6.4.0.

* Wed Dec 6 2023 Anton Kurachenko <srebrov@altlinux.org> 0.6.3.0-alt2
- Fixed post/preun scripts (#48657).

* Sat Sep 30 2023 Anton Kurachenko <srebrov@altlinux.org> 0.6.3.0-alt1
- Initial build for Sisyphus.
