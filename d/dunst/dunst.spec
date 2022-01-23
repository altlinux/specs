%define _unpackaged_files_terminate_build 1
%def_enable check

Name: dunst
Version: 1.7.3
Release: alt1
Summary: Lightweight replacement for the notification-daemons
License: BSD
Group: Graphical desktop/Other
Url: https://dunst-project.org
Source: %name-%version.tar.gz

%if_enabled check
BuildRequires: librsvg wayland-protocols dbus
%endif

# Automatically added by buildreq on Sun Jan 23 2022
# optimized out: bash4 dbus fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXext-devel libXrender-devel libcairo-devel libcairo-gobject libcap-ng libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libwayland-client libwayland-client-devel libwayland-cursor perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators pkg-config python3 python3-base sh4 shared-mime-info wayland-devel xorg-proto-devel
BuildRequires: libXScrnSaver-devel libXinerama-devel libXrandr-devel libnotify-devel libpango-devel libwayland-cursor-devel perl-Pod-Usage

%description
Dunst is a highly configurable and lightweight notification daemon.

%prep
%setup

%build
%make_build PREFIX=%prefix SYSCONFDIR=%_sysconfdir SYSTEMD=1

%install
%makeinstall_std PREFIX=%prefix SYSCONFDIR=%_sysconfdir SYSTEMD=1

%check
%make_build test

%files
%doc AUTHORS CHANGELOG* LICENSE README* RELEASE_NOTES*
%_bindir/*
%_man1dir/*
%_man5dir/*
%_datadir/dbus-1/services/*
%_libexecdir/systemd/user/*
%_sysconfdir/%name

%changelog
* Sun Jan 23 2022 Fr. Br. George <george@altlinux.ru> 1.7.3-alt1
- Autobuild version bump to 1.7.3

* Sun Jan 23 2022 Fr. Br. George <george@altlinux.ru> 1.7.2-alt1
- Update to 1.7.2
- Introduce Wayland support

* Wed Nov 25 2020 Danil Shein <dshein@altlinux.org> 1.5.0-alt1
- update version to 1.5.0
- using sources from github.com

* Tue Jun 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus (ALT #30120)

