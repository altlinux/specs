Name: crtools
Version: 1.0
Release: alt3
Summary: Utility to checkpoint/restore tasks
License: GPLv2
Group: System/Configuration/Other
URL: http://criu.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Provides: criu = %version-%release
ExclusiveArch: x86_64 %arm

BuildRequires: libprotobuf-c-devel asciidoc xmlto

%description
An utility to checkpoint/restore tasks.


%prep
%setup -q
%patch -p1


%build
export CFLAGS="%optflags"
%make_build PREFIX=%prefix all docs


%install
%makeinstall_std PREFIX=%prefix


%files
%doc README
%_sbindir/*
%_man8dir/*


%changelog
* Sun Dec 01 2013 Led <led@altlinux.ru> 1.0-alt3
- upstream fixes

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.0-alt2
- added TTY_MAJOR to known tty char devices group

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.0-alt1
- initial build
