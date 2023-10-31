Name: bcache-tools
Version: 1.1
Release: alt1
Epoch: 1

Summary: Tools for Linux kernel block layer cache
License: GPLv2
Group: System/Kernel and hardware
Url: http://bcache.evilpiepirate.org/

#git://git.kernel.org/pub/scm/linux/kernel/git/colyli/bcache-tools.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(smartcols)
BuildRequires: pkgconfig(uuid)

%package -n bcache-status
Summary: Display useful bcache statistics
Group: System/Kernel and hardware
Requires: %name
BuildArch: noarch

%description
Bcache is a Linux kernel block layer cache. It allows one or more fast disk
drives such as flash-based solid state drives (SSDs) to act as a cache for
one or more slower hard disk drives.
This package contains the utilities for manipulating bcache.

%description -n bcache-status
Display useful bcache statistics

%prep
%setup

%build
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README COPYING
%_udevrulesdir/*.rules
/lib/udev/bcache-register
/lib/udev/probe-bcache

%_sbindir/bcache
%_sbindir/bcache-super-show
%_sbindir/make-bcache

%_man8dir/bcache-super-show.*
%_man8dir/make-bcache.*
%_man8dir/probe-bcache.*

%files -n bcache-status
%_sbindir/bcache-status
%_man8dir/bcache-status.8.*

%changelog
* Tue Oct 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.1-alt1
- 1.1 released

* Thu May 20 2021 Slava Aseev <ptrnine@altlinux.org> 1:1.0.8-alt4
- Fix FTBFS due to missing rpm-build-python3

* Mon Jun 15 2020 Nikita Ermakov <arei@altlinux.org> 1:1.0.8-alt3
- Reorganize repo a little bit:
  + Move patches to the .gear/ subdirectory.
  + Remove bcache-status{,.8} as it is not needed.
  + Move bcache-status-20140220.tar.gz to .gear/ subdirectory.
  + Replace a patch, with man pages for the bcache-status, with a file.
  + Update .gear/rules.

* Mon Sep 04 2017 Lenar Shakirov <snejok@altlinux.ru> 1:1.0.8-alt2
- External bcache-status added (peeped from Fedora)

* Mon Aug 22 2016 Alexei Takaseev <taf@altlinux.org> 1:1.0.8-alt1
- 1.0.8
- fix build with gcc5

* Thu Jan 23 2014 Terechkov Evgenii <evg@altlinux.org> 1:0.9-alt1
- 0.9

* Fri Nov  8 2013 Terechkov Evgenii <evg@altlinux.org> 0-alt1.20131108
- git-20131108

* Mon Sep  9 2013 Terechkov Evgenii <evg@altlinux.org> 0-alt1.20130907
- Initial build for ALT Linux Sisyphus
