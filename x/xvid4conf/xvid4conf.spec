Summary: This tool creates XviD configuration files
Name: xvid4conf
Version: 1.12
Release: alt1
URL: http://zebra.fh-weingarten.de/~transcode/xvid4conf/
Source0: %url/%{name}-%{version}.tar.bz2
License: GPL
Group: Video
Packager: Maxim Tyurin <mrkooll@altlinux.ru>

# Automatically added by buildreq on Thu Jun 10 2004
BuildRequires: glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig
Requires: xvid >= 1.0 transcode

%description 
This tool creates XviD configuration files. The generated
configuration file is meant to be read by transcodes xvid4 export
module. This module (and so the configuration file) is intended to be
used with XviD 1.0 (dev-api-4)

%prep
%setup -q

%build
%configure

%install
%makeinstall


%files
%_bindir/*
%doc AUTHORS COPYING ChangeLog README 

%changelog
* Mon Nov 14 2005 Maxim Tyurin <mrkooll@altlinux.ru> 1.12-alt1
- new version

* Thu Jun 10 2004 Maxim Tyurin <mrkooll@altlinux.ru> 1.9-alt1
- Initial build.


