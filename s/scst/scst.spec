Name: scst
Version: 3.10
Release: alt1
Summary: Generic SCSI target subsystem for Linux
License: GPL-2.0
Group: System/Kernel and hardware
URL: http://scst.sf.net
VCS: https://github.com/SCST-project/scst.git

Source: %name-%version.tar

BuildRequires: rpm-build-kernel

%description
The generic SCSI target subsystem for Linux (SCST) allows creation of
sophisticated storage devices from any Linux box. Those devices can provide
advanced functionality, like replication, thin provisioning, deduplication,
high availability, automatic backup, etc.

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
%setup
tar -cJf %name-%version.tar.xz %name/src iscsi-scst qla2x00t %name/README %name/README.*

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
* Tue Dec 30 2025 Andrey Cherepanov <cas@altlinux.org> 3.10-alt1
- New version.

* Mon Apr 21 2025 Andrey Cherepanov <cas@altlinux.org> 3.9-alt1
- New version.
- Packaged all sources in one kernel-source-scst.
- Built from https://github.com/SCST-project/scst.git

* Sat Oct 31 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version (ALT #38809).

* Sun Oct 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- initial release

