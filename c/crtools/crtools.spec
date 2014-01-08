Name: crtools
Version: 1.1
%define pre -rc1
%define ver %version%{?pre:%pre}
Release: alt0.1
Summary: Utility to checkpoint/restore tasks
License: GPLv2
Group: System/Configuration/Other
URL: http://criu.org
Source: %name-%ver.tar
Patch: %name-%version-%release.patch
Provides: criu = %version-%release
ExclusiveArch: x86_64 %arm

BuildRequires: libprotobuf-c-devel asciidoc xmlto

%description
An utility to checkpoint/restore tasks.


%prep
%setup -q -n %name-%ver
%patch -p1


%build
export CFLAGS="%optflags"
%make_build PREFIX=%prefix all docs


%install
%makeinstall_std PREFIX=%prefix SYSTEMDUNITDIR=%_unitdir


%files
%doc README
%_sbindir/*
%_man8dir/*
%_unitdir/*


%changelog
* Wed Jan 08 2014 Led <led@altlinux.ru> 1.1-alt0.1
- 1.1-rc1

* Sat Dec 14 2013 Led <led@altlinux.ru> 1.0-alt5
- upstream fixes

* Sat Dec 07 2013 Led <led@altlinux.ru> 1.0-alt4
- upstream fixes

* Sun Dec 01 2013 Led <led@altlinux.ru> 1.0-alt3
- upstream fixes

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.0-alt2
- added TTY_MAJOR to known tty char devices group

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.0-alt1
- initial build
