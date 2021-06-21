Name: nvdock
Version: 1.02
Release: alt3

Summary: A tray icon to easily launch the nvidia-settings control panel

Group: System/Kernel and hardware
License: BSD

# Dead link! (
Url: http://www.opsat.net/user/bob/projects/nvdock

Source: %url/%name-%version.tar.bz2
Patch: %name-%version-alt.patch

# Automatically added by buildreq on Sun Aug 19 2007
BuildRequires: libgtk+2-common-devel libgtk+2-devel
Requires: nvidia-settings

# we don't ship nvidia for other arches
ExclusiveArch: %ix86 x86_64

%description
A tray icon to easily launch the nvidia-settings control panel. Now with
temperature reading! Actually it always had temperature reading, nvidia-settings
did that for me.

%prep
%setup
%patch -p1

%build
RPM_OPT_FLAGS="%optflags" \
%make_build

%install
%makeinstall DESTDIR=%buildroot ROOT=$USER

%files
%doc COPYING README TODO
%_bindir/*
%_pixmapsdir/*
%_desktopdir/*

%changelog
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
