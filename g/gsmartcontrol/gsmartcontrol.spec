Name:		gsmartcontrol
Summary:	GSmartControl is a graphical user interface for smartctl
Version:	0.8.6
Release:	alt2
Group:		Graphical desktop/Other
License:	GPL
Packager: 	Mikhail Pokidko <pma@altlinux.org>
URL:		http://gsmartcontrol.berlios.de/home/index.php/en/Downloads
Source:		%name-%version.tar.bz2
BuildRequires:	libgtkmm2-devel, gcc-c++, libpcre-devel gksu
Requires:	smartmontools

%description
GSmartControl is a graphical user interface for smartctl (from Smartmontools package), which is a tool for
querying and controlling SMART (Self-Monitoring, Analysis, and Reporting
Technology) data on modern hard disk drives. It allows you to inspect the
drive's SMART data to determine its health, as well as run various tests on
it.


%prep
%setup -q

%build
%configure --prefix=%prefix
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_defaultdocdir/%name
%_bindir/*
%_datadir/%name/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_man1dir/*.1*
%_desktopdir/%name.desktop


%changelog
* Thu May 03 2012 Mikhail Pokidko <pma@altlinux.org> 0.8.6-alt2
- fixed build with glib 2.31

* Tue Aug 23 2011 Mikhail Pokidko <pma@altlinux.org> 0.8.6-alt1
- version up

* Thu Nov 19 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.5-alt1
- Version up

* Wed Jun 10 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.4-alt1
- Version up. Fixed build errors.

* Fri Mar 13 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.3-alt1
- Initial build

