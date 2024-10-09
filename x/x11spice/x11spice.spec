Name: x11spice
Version: 1.2
Release: alt2
Summary: x11spice connects a running X server as a Spice server
Group: Networking/Remote access
License: GPL-3.0+
Url: https://gitlab.freedesktop.org/spice/x11spice/
Source0: %name-%version.tar

Patch1: %name-alt-show-ip-address.patch
Patch2: %name-allow-access-in-config.patch
Patch3: %name-alt-crash.patch
Patch4: %name-alt-desktop-l10n.patch
Patch5: %name-alt-build.patch

BuildRequires(pre): rpm-build-xdg
BuildRequires: libxcb-devel libxcbutil-devel libgtk+3-devel libspice-server-devel libpixman-devel libaudit-devel
BuildRequires: xorg-util-macros

ExcludeArch: %ix86

%description
It owes a debt to the excellent x11vnc project,
from the libvncserver project. That project proved that
this could be done, and done well.  Some of the logic,
notably that of scan.c, was inspired by the code in x11vnc.

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p1
%patch4 -p2
%patch5 -p1

%build
%ifarch %ix86
#hack, excuse me, plz
#export CFLAGS="-Wno-error=address -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -Wno-format"
%endif
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%config(noreplace) %_xdgconfigdir/%name
%_bindir/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_man1dir/*

%changelog
* Wed Oct 09 2024 Andrey Kovalev <ded@altlinux.org> 1.2-alt2
- Fixed build.
- Updated URL to the current one.

* Fri Mar 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version.

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt6
- Add Russian localization to desktop file.

* Thu Mar 07 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt5
- Fixed crash on shutdown.

* Wed Feb 06 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt4
- Do not build on i586.

* Thu Dec 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3
- Run with password spicey and allow control by default.

* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Show IP address(es) in dialog.

* Wed Feb 28 2018 Lenar Shakirov <snejok@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

