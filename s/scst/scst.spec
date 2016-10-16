Name: scst
Version: 3.1.0
Release: alt1
Summary: Generic SCSI target subsystem for Linux
License: GPLv2
Group: System/Kernel and hardware
URL: http://%name.sf.net
Source: %name-%version.tar.bz2

BuildRequires: rpm-build-kernel

%description
The generic SCSI target subsystem for Linux (SCST) allows creation of sophisticated
storage devices from any Linux box. Those devices can provide advanced functionality,
like replication, thin provisioning, deduplication, high availability, automatic backup, etc.

%package devel
Summary: SCST development files
Group: System/Kernel and hardware

%description devel
This package contains SCST development files

%package -n kernel-source-%name
Summary: SCST modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release

%description -n kernel-source-%name
This package contains SCST modules sources for Linux kernel.

%prep
%setup -q

tar -cJf %name-%version.tar.xz %name/src %name/README %name/README.*

%install
install -pD -m0644 %name-%version.tar.xz %kernel_srcdir/%name-%version.tar.xz
mkdir -p %buildroot%_includedir/%name
install -m0644 %name/include/* %buildroot%_includedir/%name/


%files devel
%doc %name/README %name/README.*
%_includedir/%name

%files -n kernel-source-%name
%_usrsrc/kernel

%changelog
* Sun Oct 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- initial release

