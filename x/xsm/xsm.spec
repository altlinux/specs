Name: xsm
Version: 1.0.6
Release: alt1
Summary: X session manager
License: X11
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar.gz

# Automatically added by buildreq on Sun Dec 14 2025
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libgpg-error perl pkg-config python3 python3-base sh5 xorg-proto-devel
BuildRequires: libXaw-devel perl-parent
BuildRequires: xorg-util-macros

%description
xsm is a session manager.  A session is a group of applications, each
of which has a particular state.  xsm allows you to create arbitrary
sessions - for example, you might have a "light" session, a "development"
session, or an "xterminal" session.  Each session can have its own set of
applications.  Within a session, you can perform a "checkpoint" to save
application state, or a "shutdown" to save state and exit the session.  When
you log back in to the system, you can load a specific session, and you can
delete sessions you no longer want to keep.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README*
%_bindir/*
%_man1dir/*
%_x11appconfdir/XSm
%_x11sysconfdir/xsm/system.xsm

%changelog
* Sun Dec 14 2025 Fr. Br. George <george@altlinux.org> 1.0.6-alt1
- Autobuild version bump to 1.0.6

* Sun Dec 14 2025 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Ressurrect package
