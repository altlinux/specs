Name: cerbere
Version: 0.2
Release: alt1

Summary: service to relaunch Pantheon apps
Group: Graphical desktop/Other
License: GPLv2+
Url: https://launchpad.net/cerbere

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake vala glib2-devel libgio-devel libgee-devel gcc-c++

#Build-Depends: cmake,
#               debhelper (>= 7.0.50~),
#               libgee-dev (>= 0.5.3),
#               libglib2.0-dev (>= 2.28),
#               valac-0.16 | valac (>= 0.16)

%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a predefined
list of processes (configurable through dconf) and relaunches them if they
end. This is helpful to keep the panel, dock, and wallpaper running, even if
they crash or are killed by another process.

%prep
%setup -q

%build
%cmake_insource
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc INSTALL
%_bindir/*
%_desktopdir/cerbere.desktop
%_datadir/glib-2.0/schemas/org.pantheon.cerbere.gschema.xml

%changelog
* Tue Sep 10 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt1
- build for Sisyphus


