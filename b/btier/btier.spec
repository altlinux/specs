%define Name BTIER
Name: btier
%define module_name %name
Version: 0.9.9.9
%define rel 6
Release: alt2
Summary: %Name - a blockdevice that provides automated tiered storage
License: GPLv2
Group: System/Base
URL: http://sourceforge.net/projects/tier/
Source: %name-%version-%rel.tar
Patch: %name-%version-%release.patch
ExclusiveOS: Linux

BuildRequires: rpm-build-kernel

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
This package contains btier_setup - The setup utility for %name.


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
%setup -q -n %name-%version-%rel
%patch -p1


%build
%make_build CC="%__cc %optflags" clionly

gzip -9c Changelog > Changelog.gz


%install
install -d -m 0755 %buildroot{%_sbindir,%_man1dir,%_usrsrc/kernel/sources,%_docdir/%name-%version/examples/fio}
install -m 0755 cli/%{name}_setup %buildroot%_sbindir/
install -m 0644 man/*.1 %buildroot%_man1dir/
install -m 0644 tools/{show_*,writetest.c} %buildroot%_docdir/%name-%version/examples/
install -m 0644 tools/fio/* %buildroot%_docdir/%name-%version/examples/fio/
install -m 0644 Changelog.* TODO Documentation/* %buildroot%_docdir/%name-%version/

tar --transform='s,^.*/,/%module_name-%version/,' -cJf %kernel_srcdir/%module_name-%version.tar.xz kernel/%name/*


%files utils
%_sbindir/*
%_man1dir/*


%files doc
%_docdir/%name-%version


%files -n kernel-source-%name
%_usrsrc/kernel


%changelog
* Fri Apr 05 2013 Led <led@altlinux.ru> 0.9.9.9-alt2
- 0.9.9.9-6
- added doc subpackage

* Thu Mar 21 2013 Led <led@altlinux.ru> 0.9.9.9-alt1
- initial build
