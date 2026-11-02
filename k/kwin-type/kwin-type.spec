%define _unpackaged_files_terminate_build 1

Name: kwin-type
Version: 0.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Type text from standard input on KDE KWin Wayland
Url: https://git.zx2c4.com/kwin-type/
License: GPL-2.0-only

#Requires:       kwin >= 6.8

Source: %name-%version.tar

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libei-1.0)

%description
kwin-type sends UTF-8 text from standard input to KDE's KWin Wayland
compositor using its EIS text input interface.

%prep
%setup

%build
export CFLAGS="%optflags"
%make_build

%install
%make install DESTDIR=%buildroot PREFIX=%prefix MANDIR=%_mandir

%files
%doc COPYING README.md
%_bindir/kwin-type
%_man1dir/kwin-type.*

%changelog
* Mon Nov 02 2026 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- initial build
