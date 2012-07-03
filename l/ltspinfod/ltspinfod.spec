Name: ltspinfod
Version: 0.1
Release: alt2

Summary: Tool to get info from LTSP clients
License: GPL
Group: Networking/Other

Url: http://www.altlinux.org/LTSP
Source:	ftp://ltsp.mirrors.tds.net/pub/ltsp/tarballs/%name-%version.tar.bz2
Patch0: ltspinfod-0.1-help.patch
Patch1: ltspinfod-0.1-alt-fixes.patch

# Automatically added by buildreq on Fri Mar 30 2007
BuildRequires: libpopt-devel

%description
This service will run on a workstation, listening on a port (9200) for a
command to run. Initially, the first command will be a 'get' command,
for retrieving configuration things, like the sound service entry.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%define _optlevel s
cc %optflags -o %name %name.c -lpopt

%install
install -pDm755 %name %buildroot%_sbindir/%name

%files
%_sbindir/*

%changelog
* Tue Mar 06 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added patch by Valentin Nechaev to fill in netaddr properly
  (takes care for IPv4/v6 unification issues and corrects memset)

* Fri May 25 2007 Led <led@altlinux.ru> 0.1-alt1
- added %name-0.1-help.patch

* Fri Apr 06 2007 Led <led@altlinux.ru> 0.1-alt0.1
- initial build for Sisyphus
