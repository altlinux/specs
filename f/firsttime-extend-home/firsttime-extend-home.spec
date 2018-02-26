Name: firsttime-extend-home
Version: 0.0.1
Release: alt1

Summary: Auto extend /home FS.
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org
BuildArch: noarch
Source: %name-%version.tar

%description
Auto extend /home FS, using all unused space at the end of USB disk.
Runs only once, at first bootup.

%prep
%setup

%build

%install
mkdir -p %buildroot%_sysconfdir/firsttime.d
install -pm755 *.sh %buildroot%_sysconfdir/firsttime.d/

%files
%_sysconfdir/firsttime.d/*

%changelog
* Tue Aug 16 2011 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build.
