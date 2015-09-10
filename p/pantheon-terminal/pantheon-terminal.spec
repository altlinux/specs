%define ver_major 0.3

Name: pantheon-terminal
Version: %ver_major.1.3
Release: alt1

Summary: Pantheon Terminal
Group: Terminals
License: GPLv3

Url: https://launchpad.net/pantheon-terminal

Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tgz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake gcc-c++ libnotify-devel libvte3_2.90-devel libgranite-devel libpixman-devel
BuildRequires: libXdmcp-devel vala libgranite-vala

%description
Pantheon Terminal (referred to simply as "Terminal" when installed) is a super
lightweight, beautiful, and simple terminal.

It's designed to be setup with sane defaults and little to no configuration.
It's just a terminal, nothing more, nothing less.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS HACKING INSTALL README
%_bindir/*
%_datadir/%name/
%_desktopdir/%name.desktop
%_desktopdir/open-%name-here.desktop
%_datadir/glib-2.0/schemas/org.pantheon.terminal.gschema.xml

%changelog
* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1.3-alt1
- 0.3.1.3

* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4.1-alt1
- 0.2.3 -> 0.2.4.1

* Mon Aug 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

