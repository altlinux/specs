%define module_name dst
%define module_version %version
%define module_release alt4
%define module_source %module_name-%module_version.tar.gz
%define module_source_dir %module_name-%module_version

#### MODULE SOURCES ####
Version: 0.1
Name: kernel-source-%module_name-%module_version
Release: %module_release
Summary: Linux %module_name modules sources
License: GPL
Group: Development/Kernel
Url: http://tservice.net.ru/~s0mbre/blog/devel/dst/
BuildArch: noarch
Source0: %module_source

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name modules sources for Linux kernel

%prep
%setup -qc

%install
%__mkdir -p %buildroot%_usrsrc/kernel/sources/
%__mv %module_name-%module_version kernel-source-%module_name-%module_version
%__tar -c kernel-source-%module_name-%module_version | bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

%changelog
* Thu Nov 06 2008 Boris Savelev <boris@altlinux.org> 0.1-alt4
- update from upstream to 5 november.

* Wed Oct 01 2008 Boris Savelev <boris@altlinux.org> 0.1-alt3
- update from upstream from 20 september by 7 october.

* Sat Sep 20 2008 Boris Savelev <boris@altlinux.org> 0.1-alt2
- Free in node removal so node would be freed in process context and not in the receiving threads itself.
- Added cache name to the node. It is possible to have freed node still beaing alive while we register new node with the same name, so its cache name should be different.
- Use idr to manage minor numbers.
- Fixed memory leak in crypto thread initialization error path.
- Unprotected tree access (exceptionally stupid bug, I was made blind by the electronic equipment), and tricky bug_on catch in scsi code caused by incorrect bio flag initialization in the exporting node. 64bit alignment fix.
- Couple of bogus compilation warnings about unintialized variables cought by different compiler.
- Allow both hread and write permission, not only read or write in security config.

* Fri Aug 29 2008 Boris Savelev <boris@altlinux.org> 0.1-alt1
- initial build
