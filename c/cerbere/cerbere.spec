Name: cerbere
Version: 0.2
Release: alt5.r45

Summary: service to relaunch Pantheon apps
Group: Graphical desktop/Other
License: GPLv2+
Url: https://launchpad.net/cerbere

Source0: %name.tar.xz

Patch0: cerbere-0.2-alt-fix-desktop-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake vala glib2-devel libgio-devel libgee-devel gcc-c++

%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a predefined
list of processes (configurable through dconf) and relaunches them if they
end. This is helpful to keep the panel, dock, and wallpaper running, even if
they crash or are killed by another process.

%prep
%setup -q -n %name
%patch0 -p1

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%files
%doc INSTALL
%_bindir/*
%_desktopdir/cerbere.desktop
%_datadir/glib-2.0/schemas/org.pantheon.cerbere.gschema.xml

%changelog
* Sun Jan 05 2014 Igor Zubkov <icesik@altlinux.org> 0.2-alt5.r45
- r45

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt4.revno42
- Fix desktop file

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt3.revno42
- Make build verbose

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt2.revno42
- 0.2 revno 42

* Tue Sep 10 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt1
- build for Sisyphus


