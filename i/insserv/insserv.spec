
Name:       insserv
Version:    1.14.0
Release:    alt1

Summary:    Tool for process controlling in System V boot scripts 
License:    GPLv2+
Group:      System/Configuration/Boot and Init
URL:        http://savannah.nongnu.org/projects/sysvinit

Packager:   Andrey Cherepanov <cas@altlinux.org>

Source0:    %name-%version.tar.bz2

BuildRequires: /proc

%description
This small package provides a tool for process controlling
in System V boot scripts.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/%name.conf
/lib/lsb/init-functions
/sbin/%name
%_libexecdir/lsb/*_initd
%_man8dir/%name.8.gz

%changelog
* Thu Feb 14 2013 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt1
- Initial import to ALT Linux

