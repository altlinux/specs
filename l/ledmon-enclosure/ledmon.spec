# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: perl(Config.pm) perl(English.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(Time/Local.pm) python-devel
# END SourceDeps(oneline)
BuildRequires: libsgutils-devel
%define oldname ledmon
Summary: Enclosure LED Utilities
Name: ledmon-enclosure
Version: 0.74
Release: alt1_3
License: GPLv2+
Group: System/Kernel and hardware
URL: http://sourceforge.net/projects/ledmon/
Source0: http://download.sourceforge.net/%{oldname}/%{oldname}-%{version}.tar.bz2
Patch0: ledmon_cflags.patch
Patch1: ledmon-0.74-coverity-fixes.patch
BuildRequires: perl
BuildRequires: libsgutils-devel
Obsoletes: ledctl = 0.1-1
Provides: ledctl = %{version}-%{release}
Requires: libsgutils
Source44: import.info
Patch33: ledmon-0.74-alt-as-needed.patch

%description
The ledmon and ledctl are user space applications design to control LED
associated with each slot in an enclosure or a drive bay. There are two
types of system: 2-LED system (Activity LED, Status LED) and 3-LED system
(Activity LED, Locate LED, Fail LED). User must have root privileges to
use this application.

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1 -b .cflags
%patch1 -p1 -b .coverity
%patch33 -p1

%build
# can't use smp_flags because -j4 makes the build fail
make CFLAGS="$RPM_OPT_FLAGS --std=c99"

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT SBIN_DIR=$RPM_BUILD_ROOT/%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%files
%doc README COPYING
%{_sbindir}/ledctl
%{_sbindir}/ledmon
%{_mandir}/*/*

%changelog
* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1_3
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1_2
- fc import

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1_1
- fc import

