Name: tinymount
Version: 0.2.6
Release: alt1

Summary: Simple GUI tool for disks mounting
Group: System/Kernel and hardware
License: GPL2
URL: http://github.com/limansky/tinymount

Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: %name-%version.tar
Patch0:%name-%version-alt.patch

BuildRequires: gcc-c++ libudev-devel libqt4-devel

%description
TinyMount is a little GUI tool for mount/unmount devices, using
UDisks.

TinyMount is inspired by internal KDE mounter, but has no dependencies
on KDE libs (but it Qt based, sorry) and can be used with lightweight
window managers like awesome, *boxes, etc. with internal tray support,
or with separate tray applications (like stalonetray) if your manager
doesn't support tray.

%prep
%setup
%patch0 -p1

%build
qmake-qt4 PREFIX=/usr
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%_bindir/%name
%_datadir/%name
%doc ChangeLog README.md

%changelog
* Sun Dec  2 2012 Terechkov Evgenii <evg@altlinux.org> 0.2.6-alt1
- Initial build for ALT Linux Sisyphus
