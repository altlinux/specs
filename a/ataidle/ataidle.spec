Summary: Utility to sets the idle timer on ATA hard drives
Name: ataidle
Version: 2.5
Release: alt1
Source0: %name-%version.tar
License: BSD
Group: System/Kernel and hardware
Url: http://www.cran.org.uk/~brucec/blog/ataidle/

%description
ATAidle is a utility to set the power management features of ATA hard drives
in FreeBSD and Linux, including idle and standby timeouts, APM, and
acoustic level settings.

%prep
%setup -q

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT/%_sbindir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man8/
install $RPM_BUILD_DIR/%name-%version/ataidle $RPM_BUILD_ROOT/%_sbindir
install $RPM_BUILD_DIR/%name-%version/ataidle.8 $RPM_BUILD_ROOT/%_mandir/man8

%files
%_sbindir/ataidle
%_mandir/man8/*

%changelog
* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version

* Tue Sep 28 2010 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version

* Mon Mar 20 2006 Anton Farygin <rider@altlinux.ru> 0.9-alt2
- fixed build

* Fri Nov 18 2005 Anton Farygin <rider@altlinux.ru> 0.9-alt1
- new version

* Thu Sep 16 2004 Anton Farygin <rider@altlinux.ru> 0.6-alt1
- first build for Sisyphus
