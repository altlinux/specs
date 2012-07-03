Name: spt-profiles-ovz-1C
Version: 0.1
Release: alt2

AutoReq: yes, noshell

Summary: spt profiles for building OpenVZ VE containers fot 1C Linux Server
Group: Development/Other
License: GPL
Source: profiles-1C-%version.tar.bz2

BuildArch: noarch

Packager: Sergey Alembekov <rt@altlinux.ru>

%description
This package contains spt profiles for building OpenVZ isolated containers
used for creating appliances.

%prep
%setup -n profiles-1C-%version

%install
#profiles
%__install -dm755 %buildroot%_sysconfdir/spt/profiles/ovz
for i in * .;do
    cp -a $i %buildroot%_sysconfdir/spt/profiles/ovz
done

%files
%dir %_sysconfdir/spt/profiles/ovz
%config(noreplace) %_sysconfdir/spt/profiles/ovz/*
#%_sysconfdir/spt/profiles/ovz/.default

%changelog
* Fri Jan 18 2008 Sergey Alembekov <rt@altlinux.ru> 0.1-alt2
- profile for postgresql-server added

* Thu Jan 17 2008 Sergey Alembekov <rt@altlinux.ru> 0.1-alt1
- hook for setting ru_RU UTF-8 locale added

* Sat May 05 2007 Sergey Alembekov <rt@altlinux.ru> 0.1-alt0
-Initial realise

