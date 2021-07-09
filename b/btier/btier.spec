%define Name BTIER
%define module_name %name
%define rel %nil

Name:       btier
Version:    1.3.0
Release:    alt3

Summary:    %Name - a blockdevice that provides automated tiered storage
License:    GPLv2
Group:      System/Base
URL:        http://sourceforge.net/projects/tier/

Source:     %name-%version%rel.tar
Patch:      %name-%version-%release.patch
Patch1:     fix-code-style.patch

BuildRequires: rpm-build-python3
BuildRequires(pre): rpm-build-kernel
BuildRequires: python-tools-2to3 xz


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
%patch1 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

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
* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- add BR: rpm-build-python3

* Tue Jan 28 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- Porting on Python3.

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.3.0-alt1
- 1.3.0
- update to kernel API >= 3.14

* Tue Apr 15 2014 Led <led@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Wed Mar 12 2014 Led <led@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Sun Feb 16 2014 Led <led@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Sat Jan 18 2014 Led <led@altlinux.ru> 1.2.0-alt2
- upstream updates

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
