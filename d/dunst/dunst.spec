%define _unpackaged_files_terminate_build 1
%def_enable check

Name: dunst
Version: 1.5.0
Release: alt1
Summary: Lightweight replacement for the notification-daemons
License: BSD
Group: Graphical desktop/Other
URL: https://dunst-project.org
Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires: libdbus-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXft-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: glib2-devel
BuildRequires: libpango-devel
BuildRequires: libgtk+3-devel
BuildRequires: libnotify-devel
BuildRequires: /usr/bin/pod2man
BuildRequires: /bin/systemctl
BuildRequires: libsystemd-devel
%if_enabled check
BuildRequires: librsvg
%endif

%description
Dunst is a highly configurable and lightweight notification daemon.

%prep
%setup
%patch0 -p1

%build
%make_build PREFIX=%prefix

%install
%makeinstall_std PREFIX=%prefix

%check
%make_build test

%files
%doc AUTHORS CHANGELOG* LICENSE README* RELEASE_NOTES*
%_bindir/*
%_man1dir/*
%_datadir/dbus-1/services/*
%_datadir/%name
%_libexecdir/systemd/user/*

%changelog
* Wed Nov 25 2020 Danil Shein <dshein@altlinux.org> 1.5.0-alt1
- update version to 1.5.0
- using sources from github.com

* Tue Jun 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus (ALT #30120)

