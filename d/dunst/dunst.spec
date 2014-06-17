Name: dunst
Version: 1.0.0
Release: alt1
Summary: Lightweight replacement for the notification-daemons
License: BSD
Group: Graphical desktop/Other
Url: http://www.knopwob.org/dunst/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: libdbus-devel libXinerama-devel libXft-devel
BuildPreReq: libxdg-basedir-devel libpango-devel libXScrnSaver-devel
BuildPreReq: perl-podlators libgio-devel libnotify-devel

%description
Dunst is a lightweight replacement for the notification-daemons provided
by most desktop environments. It's very customizable, doesn't depend on
any toolkits and therefore fits in those windowmanager centric setups we
all love to customize to perfection.

Dunst is a part of the j4tools tools set.

%prep
%setup

%build
%make_build_ext PREFIX=%prefix

%install
%makeinstall_std PREFIX=%prefix

%files
%doc AUTHORS CHANGELOG LICENSE README* RELEASE_NOTES*
%_bindir/*
%_man1dir/*
%_datadir/dbus-1
%_datadir/%name

%changelog
* Tue Jun 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus (ALT #30120)

