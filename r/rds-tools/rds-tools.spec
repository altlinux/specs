Summary: RDS support tools 
Name: rds-tools
Version: 2.0.4
Release: alt1
License: %gpl2only
Group: Networking/Other
URL: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Andriy Stepanov <stanv@altlinux.ru>

BuildRequires: rpm-build-licenses

%description
%name is a collection of support tools for the RDS socket API.


%package -n rds-devel
Summary: User space interface for RDS
Group: Development/C
Requires: glibc-devel

%description -n rds-devel
User space interface for RDS.

%prep
%setup -n %name-%version

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*


%files -n rds-devel
%_includedir/net/*
%_man7dir/*

%changelog
* Thu Dec 16 2010 Timur Aitov <timonbl4@altlinux.org> 2.0.4-alt1
- New version

* Thu Aug 12 2010 Andriy Stepanov <stanv@altlinux.ru> 1.5-alt1
- 1.5-1

* Wed Apr 15 2009 Led <led@altlinux.ru> 1.4-alt1
- 1.4-1

* Mon Oct 27 2008 Led <led@altlinux.ru> 1.2-alt1
- initial build for ALTLinux

* Sun Nov 25 2007 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Use DESTDIR
* Mon Oct 27 2006 Zach Brown <zach.brown@oracle.com>
- initial version
