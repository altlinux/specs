Name: nvdock
Version: 1.03
Release: alt1.1

Summary: A tray icon to easily launch the nvidia-settings control panel

Group: System/Kernel and hardware
License: BSD

Url: https://github.com/LAKostis/nvdock

Source: %url/%name-%version.tar.bz2
Patch0: %name-nvctrl-revamp.patch
Patch1: %name-desktop-fix.patch

# Automatically added by buildreq on Sun Aug 19 2007
BuildRequires: libgtk+2-common-devel libgtk+2-devel
# Due NVCtrlLib
BuildRequires: nvidia-settings-devel
Requires: nvidia-settings

# we don't ship nvidia for other arches
ExclusiveArch: %ix86 x86_64

%description
A tray icon to easily launch the nvidia-settings control panel. Now with
temperature reading! Actually it always had temperature reading, nvidia-settings
did that for me.

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
RPM_OPT_FLAGS="%optflags" \
%make_build

%install
%makeinstall DESTDIR=%buildroot ROOT=$USER

%files
%doc COPYING README* TODO*
%_bindir/*
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Sat Apr 16 2022 L.A. Kostis <lakostis@altlinux.ru> 1.03-alt1.1
- Fix .desktop file categories.

* Wed Jun 23 2021 L.A. Kostis <lakostis@altlinux.ru> 1.03-alt1
- 1.03.
- revamp version with nvctrl support.

* Mon Jun 21 2021 L.A. Kostis <lakostis@altlinux.ru> 1.02-alt3
- update -alt patch (more -fno-common fixes).

* Mon Jun 21 2021 L.A. Kostis <lakostis@altlinux.ru> 1.02-alt2
- add exclusive arch.

* Sun Jun 20 2021 L.A. Kostis <lakostis@altlinux.ru> 1.02-alt1
- 1.02.
- Fix build with -fno-common.
- Combine from PCLinuxOS and Archlinux.

* Sun Dec 05 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.3
- fix Buildreg

* Thu Jul 29 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.2
- fix Buildreg

* Sun Aug 19 2007 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.1
- correct Group

* Sun Aug 19 2007 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1
- initial version
