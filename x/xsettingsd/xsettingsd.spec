Summary: Provides settings to X11 applications via the XSETTINGS specification
Name: xsettingsd
Version: 1.0.0
Release: alt1
License: BSD-3-Clause
Group: Graphical desktop/Other
URL: https://github.com/derat/xsettingsd
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: scons gcc-c++ libX11-devel libstdc++-devel

%description
xsettingsd is a daemon that implements the XSETTINGS specification.

It is intended to be small, fast, and minimally dependent on other
libraries.  It can serve as an alternative to gnome-settings-daemon for
users who are not using the GNOME desktop environment but who still run
GTK+ applications and want to configure things such as themes, font
antialiasing/hinting, and UI sound effects.

Documentation is available at https://github.com/derat/xsettingsd/wiki.

%prep
%setup

%build
scons xsettingsd dump_xsettings

%install
install -pDm755 xsettingsd %buildroot%_bindir/xsettingsd
install -pDm755 dump_xsettings %buildroot%_bindir/dump_xsettings

%files
%_bindir/xsettingsd
%_bindir/dump_xsettings
%doc README


%changelog
* Tue Oct 30 2018 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus
- v1.0.0-2-g1b2bcca
