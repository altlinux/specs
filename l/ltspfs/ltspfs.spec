%define cvs 20070117

Name: ltspfs
Version: 0.3
Release: alt4.%cvs

Summary: LTSP.org's %name
License: GPL
Group: System/Configuration/Hardware

Url: http://www.ltsp.org
# see also:
# http://www.archivesat.com/post1251692.htm
# http://www.archivesat.com/post1293963.htm
Source0: %name-%cvs.tar.bz2
# CVSROOT=:pserver:anonymous@cvs.ltsp.org:/usr/local/cvsroot cvs co lbussd
Patch: %name-0.3-error.patch
Source1: ltspfs.1
Source2: ltspfs.init

# Automatically added by buildreq on Wed Jan 17 2007
BuildRequires: libfuse-devel

%description
LTSP.org's %name (for local devices support)

%prep
%setup -n %name
%patch -p1

%build
%configure
%make

%install
%makeinstall bindir=%buildroot%_sbindir
install -pDm644 %SOURCE1 %buildroot%_man1dir/ltspfs.1
install -pDm755 %SOURCE2 %buildroot%_initdir/%name

%files
%_sbindir/*
%_man1dir/*
%_initdir/*

%post
%post_service %name

%preun
%preun_service %name

%changelog
* Tue Mar 02 2010 Michael Shigorin <mike@altlinux.org> 0.3-alt4.20070117
- added an initscript to work around #22929

* Mon Aug 06 2007 Led <led@altlinux.ru> 0.3-alt3.20070117.1
- added %name-0.3-error.patch
- fixed spec

* Mon Apr 23 2007 Michael Shigorin <mike@altlinux.org> 0.3-alt3.20070117
- removed ltspfsd(1) manpage since led@ has also added it 
  to ltspfsd package where it belongs

* Mon Apr 23 2007 Michael Shigorin <mike@altlinux.org> 0.3-alt2.20070117
- added ltspfsd(1) and ltspfs(1) manpages (thanks led@ again)

* Fri Apr 06 2007 Michael Shigorin <mike@altlinux.org> 0.3-alt1.20070117
- it's actually 0.3 (thanks led@; see #11384)

* Wed Jan 17 2007 Michael Shigorin <mike@altlinux.org> 0-alt1.20070117
- built for ALT Linux
- today's CVS off cvs.ltsp.org
- put binary to %_sbindir, not %_bindir

