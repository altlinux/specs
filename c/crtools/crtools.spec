Name: crtools
Version: 1.3
%define pre -rc1
%define ver %version%{?pre:%pre}
Release: alt0.8
Summary: Utility to checkpoint/restore tasks
License: GPLv2
Group: System/Configuration/Other
URL: http://criu.org
Source: %name-%ver.tar
Patch: %name-%version-%release.patch
Provides: criu = %version-%release
ExclusiveArch: x86_64 %arm

BuildRequires: libprotobuf-c-devel asciidoc xmlto %_bindir/a2x

%description
An utility to checkpoint/restore tasks.


%package -n libcriu
Summary: Shared library of checkpoint/restore
Group: System/Libraries

%description -n libcriu
Shared library of checkpoint/restore.


%package -n libcriu-devel
Summary: Files for development with libcriu
Group: Development/C
Requires: libcriu = %version-%release

%description -n libcriu-devel
Files for development with libcriu.


%prep
%setup -q -n %name-%ver
%patch -p1


%build
export CFLAGS="%optflags"
%make_build PREFIX=%prefix all docs


%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir SYSTEMDUNITDIR=%_unitdir


%files
%doc README
%_sbindir/*
%_man8dir/*
%_unitdir/*
%_logrotatedir/*


%files -n libcriu
%_libdir/*.so.*


%files -n libcriu-devel
%_includedir/*
%_libdir/*.so


%changelog
* Fri Jun 06 2014 Led <led@altlinux.ru> 1.3-alt0.8
- mnt: Relax checks for top-mount in validate_mounts
- mnt: Fix validation of dumpable mountpoints

* Wed Jun 04 2014 Led <led@altlinux.ru> 1.3-alt0.7
- mnt: Devpts options get corrupted on dump (v2)

* Sat May 31 2014 Led <led@altlinux.ru> 1.3-alt0.6
- upstream fixes

* Sun May 25 2014 Led <led@altlinux.ru> 1.3-alt0.5
- upstream fixes

* Thu May 15 2014 Led <led@altlinux.ru> 1.3-alt0.4
- upstream fixes

* Mon May 12 2014 Led <led@altlinux.ru> 1.3-alt0.3
- upstream fixes

* Thu May 08 2014 Led <led@altlinux.ru> 1.3-alt0.2
- upstream fixes

* Sat Apr 26 2014 Led <led@altlinux.ru> 1.3-alt0.1
- 1.3-rc1

* Wed Feb 26 2014 Led <led@altlinux.ru> 1.2-alt1
- 1.2

* Sat Feb 01 2014 Led <led@altlinux.ru> 1.1-alt1
- 1.1 release

* Sat Jan 25 2014 Led <led@altlinux.ru> 1.1-alt0.3
- upstream fixes

* Thu Jan 23 2014 Led <led@altlinux.ru> 1.1-alt0.2
- 1.1-rc2

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
