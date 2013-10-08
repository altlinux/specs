Name: pantheon-terminal
Version: 0.2.4.1
Release: alt1

Summary: Pantheon Terminal
Group: Terminals
License: GPLv3

Url: https://launchpad.net/pantheon-terminal

Source0: %name-%version.tgz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake gcc-c++ libnotify-devel libvte3-devel libgranite-devel libpixman-devel libXdmcp-devel vala libgranite-vala

%description
Pantheon Terminal (referred to simply as "Terminal" when installed) is a super
lightweight, beautiful, and simple terminal.

It's designed to be setup with sane defaults and little to no configuration.
It's just a terminal, nothing more, nothing less.

%prep
%setup -q

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS HACKING INSTALL README
%_bindir/*
%_desktopdir/pantheon-terminal.desktop
%_desktopdir/open-pantheon-terminal-here.desktop
%_datadir/glib-2.0/schemas/org.pantheon.terminal.gschema.xml

%changelog
* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4.1-alt1
- 0.2.3 -> 0.2.4.1

* Mon Aug 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

