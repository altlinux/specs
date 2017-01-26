%define ver_major 0.2

Name: cerbere
Version: %ver_major.2
Release: alt1

Summary: service to relaunch Pantheon apps
Group: Graphical desktop/Other
License: GPLv2+
Url: https://launchpad.net/cerbere

Source: https://launchpad.net/%name/0.x/%version/+download/%name-%version.tar.xz

Requires: dconf

BuildRequires: cmake vala libgio-devel libgee0.8-devel gcc-c++

%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a predefined
list of processes (configurable through dconf) and relaunches them if they
end. This is helpful to keep the panel, dock, and wallpaper running, even if
they crash or are killed by another process.

%prep
%setup

%build
%cmake
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%doc INSTALL
%_bindir/*
%_desktopdir/cerbere.desktop
%_datadir/glib-2.0/schemas/org.pantheon.cerbere.gschema.xml

%changelog
* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

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


