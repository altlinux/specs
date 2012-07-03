%define geany_ver 0.21
Name: geany-plugins
Version: 0.21.1
Release: alt2

Summary: Plugins for Geany

License: GPLv2
Group: Development/Tools
Url: http://plugins.geany.org/

Source: %name-%version.tar.bz2
Obsoletes: geanygdb

BuildRequires(pre): geany geany-devel intltool

Requires: geany-plugins-vc

%description
This is Geany plugin collection

%package common
Group: Development/Tools
Requires: geany = %geany_ver
Summary: localization for geany-plugins

%description common
Common files of geany-plugins, including localization

%package vc
Group: Development/Tools
Requires: geany-plugins-common = %version-%release
Summary: Geany VC integration plugin

%description vc
Various VCS integration (Git, SVN, ...) for Geany

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name

%files
%doc %_defaultdocdir/%name
%_libdir/geany/*
%dir %_libexecdir/geany-plugins
%_libexecdir/geany-plugins/*
%exclude %_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la

%files common -f %name.lang
%files vc
%_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt2
- Remove release dependency

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt1
- Autobuild version bump to 0.21.1

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
- Add unpackaged files

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt4
- trying to fix build

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt3
- split by plugins

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt2
- first build for ALT Linux
