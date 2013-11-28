%define Name BTIER
Name: btier
%define module_name %name
Version: 1.2.0
%define rel %nil
Release: alt1
Summary: %Name - a blockdevice that provides automated tiered storage
License: GPLv2
Group: System/Base
URL: http://sourceforge.net/projects/tier/
Source: %name-%version%rel.tar
Patch: %name-%version-%release.patch
ExclusiveOS: Linux

BuildRequires: rpm-build-kernel xz

%description
%name is a kernel block device that creates a tiered device out of multiple
smaller devices with automatic migration and smart placement of data chunks based
up-on access patterns.


%package utils
Summary: %name utilities
Group: System/Base
Provides: %{name}_setup = %version-%release

%description utils
%name is a kernel block device that creates a tiered device out of multiple
smaller devices with automatic migration and smart placement of data chunks based
up-on access patterns.
This package contains:
  - btier_setup - the setup utility for %name
  - btier_inspect - a tool that can be used to backup and restore btier metadata


%package doc
Summary: %name documentation
Group: Documentation
BuildArch: noarch

%description doc
%name is a kernel block device that creates a tiered device out of multiple
smaller devices with automatic migration and smart placement of data chunks based
up-on access patterns.
This package contains %name documentation.


%package -n kernel-source-%name
Summary: sources for %name kernel module
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
%name is a kernel block device that creates a tiered device out of multiple
smaller devices with automatic migration and smart placement of data chunks based
up-on access patterns.
This package contains sources for %name kernel module.


%prep
%setup -q -n %name-%version%rel
%patch -p1


%build
%make_build CC="%__cc %optflags" cli/btier_setup cli/btier_inspect


%install
install -d -m 0755 %buildroot{%_sbindir,%_man1dir,%_usrsrc/kernel/sources,%_docdir/%name-%version/examples/fio}
install -m 0755 cli/%{name}_{setup,inspect} %buildroot%_sbindir/
install -m 0755 tools/contributed/migrate_blocks_freq.py %buildroot%_sbindir/migrate_blocks_freq
install -m 0644 man/*.1 %buildroot%_man1dir/
install -m 0644 tools/{show_*,writetest.c} %buildroot%_docdir/%name-%version/examples/
install -m 0644 tools/fio/* %buildroot%_docdir/%name-%version/examples/fio/
install -m 0644 TODO Documentation/* tools/contributed/{EXAMPLE,README}* %buildroot%_docdir/%name-%version/
gzip -9c ChangeLog > %buildroot%_docdir/%name-%version/ChangeLog.gz

tar --transform='s,^.*/,/%module_name-%version/,' -cJf %kernel_srcdir/%module_name-%version.tar.xz kernel/%name/*


%files utils
%_sbindir/*
%_man1dir/*


%files doc
%_docdir/%name-%version


%files -n kernel-source-%name
%_usrsrc/kernel


%changelog
* Thu Nov 28 2013 Led <led@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Nov 16 2013 Led <led@altlinux.ru> 1.1.0-alt3
- upstream updates

* Thu Oct 17 2013 Led <led@altlinux.ru> 1.1.0-alt2
- 1.1.0 release

* Sun Aug 11 2013 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Jun 09 2013 Led <led@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue May 28 2013 Led <led@altlinux.ru> 1.0.0-alt1
- 1.0.0:
  + added migrate_blocks_freq - a data migration tool

* Mon Apr 22 2013 Led <led@altlinux.ru> 0.9.9.9-alt4
- 0.9.9.9-8:
  + added btier_inspect - a tool that can be used to backup and restore btier
    metadata

* Wed Apr 10 2013 Led <led@altlinux.ru> 0.9.9.9-alt3
- 0.9.9.9-7

* Fri Apr 05 2013 Led <led@altlinux.ru> 0.9.9.9-alt2
- 0.9.9.9-6
- added doc subpackage

* Thu Mar 21 2013 Led <led@altlinux.ru> 0.9.9.9-alt1
- initial build
