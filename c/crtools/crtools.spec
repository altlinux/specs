Name: crtools
Version: 3.7
#define pre 
%define ver %version%{?pre:%pre}
Release: alt1
Summary: Utility to checkpoint/restore tasks
License: GPLv2
Group: System/Configuration/Other
URL: http://criu.org
Source: %name-%ver.tar
#Patch: %name-%version-%release.patch
Provides: criu = %version-%release
ExclusiveArch: x86_64 %arm

BuildRequires: libnet2-devel
BuildRequires: libprotobuf-c-devel %_bindir/protoc-c
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: asciidoc xmlto %_bindir/a2x

%description
An utility to checkpoint/restore tasks.


%package -n libcriu
Summary: Shared library of checkpoint/restore
Group: System/Libraries
License: LGPLv2

%description -n libcriu
Shared library of checkpoint/restore.


%package -n libcriu-devel
Summary: Files for development with libcriu
Group: Development/C
Requires: libcriu = %version-%release

%description -n libcriu-devel
Files for development with libcriu.


%package -n python-module-criu
Summary: Python library of checkpoint/restore
Group: System/Libraries
BuildArch: noarch
Requires: python
BuildRequires: python-devel
BuildRequires: glibc-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: libnl-devel
BuildRequires: libcap-devel
BuildRequires(pre): rpm-build-python
Provides: crit = %version-%release
Obsoletes: crtools-pycriu

%description -n python-module-criu
Python library library of checkpoint/restore.


%prep
%setup -q -n %name-%ver
#patch -p1


%build
export CFLAGS="%optflags"
%make_build PREFIX=%prefix V=1 all docs


%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir LIBEXECDIR=%_libexecdir SYSTEMDUNITDIR=%_unitdir


%files
%doc README.md COPYING CREDITS
%_sbindir/*
%_sbindir/*
%_libexecdir/criu/scripts/*
%_man1dir/*
%_man8dir/*


%files -n python-module-criu
%{_bindir}/crit
%{python_sitelibdir_noarch}/*


%files -n libcriu
%_libdir/*.so.*


%files -n libcriu-devel
%_bindir/compel
%_includedir/*
%_libdir/*.so
%dir %_libexecdir/compel
%_libexecdir/compel/*
%_libdir/libcompel.a
%_pkgconfigdir/*


%changelog
* Fri Feb 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7-alt1
- Updated to upstream version 3.7.

* Thu Sep 07 2017 Denis Pynkin <dans@altlinux.org> 3.4-alt1
- updated

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 3.3-alt1
- updated

* Thu Jun 29 2017 Denis Pynkin <dans@altlinux.org> 3.2.1-alt1
- updated

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.12-alt1
- updated

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.8-alt1
- updated

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.7-alt1
- updated

* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 2.6-alt1
- updated

* Mon Aug 29 2016 Denis Pynkin <dans@altlinux.org> 2.5-alt1
- updated

* Wed Apr 13 2016 Denis Pynkin <dans@altlinux.org> 2.1-alt1
- upstream updates and fixes

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt1
- Version update 

* Tue Mar 01 2016 Denis Pynkin <dans@altlinux.org> 1.8-alt1
- New upstream version

* Sat Apr 11 2015 Denis Pynkin <dans@altlinux.org> 1.5.1-alt1
- New upstream version
- Subpackage pycriu added
- New utility 'crit' added

* Sun Aug 17 2014 Led <led@altlinux.ru> 1.3-alt0.19
- upstream updates and fixes

* Sun Aug 10 2014 Led <led@altlinux.ru> 1.3-alt0.18
- upstream updates and fixes
- fixed build with protobuf-c >= 1.0

* Sat Jul 26 2014 Led <led@altlinux.ru> 1.3-alt0.17
- upstream updates and fixes

* Fri Jul 11 2014 Led <led@altlinux.ru> 1.3-alt0.16
- upstream updates and fixes

* Sun Jul 06 2014 Led <led@altlinux.ru> 1.3-alt0.15
- upstream updates and fixes

* Thu Jul 03 2014 Led <led@altlinux.ru> 1.3-alt0.14
- upstream updates and fixes

* Tue Jul 01 2014 Led <led@altlinux.ru> 1.3-alt0.13
- upstream updates and fixes

* Fri Jun 20 2014 Led <led@altlinux.ru> 1.3-alt0.12
- upstream updates and fixes

* Wed Jun 18 2014 Led <led@altlinux.ru> 1.3-alt0.11
- 1.3-rc2

* Thu Jun 12 2014 Led <led@altlinux.ru> 1.3-alt0.10
- upstream fixes

* Sun Jun 08 2014 Led <led@altlinux.ru> 1.3-alt0.9
- upstream fixes

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
