%define module_name scst
%define module_version 3.1.0
%define module_release alt1

%define flavour std-def
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires: %module_name-devel

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Generic SCSI target subsystem for Linux
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2+
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://%module_name.sourceforge.net/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: kernel-source-iscsi-scst = %module_version
BuildRequires: kernel-source-qla2x00t = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

ExclusiveArch: %karch

%description
This package contains Generic SCSI target modules

%package -n kernel-modules-iscsi_scst-%flavour
Summary: iSCSI SCST target driver
Group: System/Kernel and hardware
Provides: kernel-modules-iscsi_scst-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-iscsi_scst-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-iscsi_scst-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease kernel-modules-%module_name-%kversion-%flavour-%krelease

%description -n kernel-modules-iscsi_scst-%flavour
This package contains iSCSI SCST target modules

%package -n kernel-modules-qla2x00t-%flavour
Summary: FC QLogic Target Driver modules
Group: System/Kernel and hardware
Provides: kernel-modules-qla2x00t-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-qla2x00t-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-qla2x00t-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease kernel-modules-%module_name-%kversion-%flavour-%krelease

%description -n kernel-modules-qla2x00t-%flavour
This package contains FC QLogic Target Driver for 22xx/23xx/24xx/25xx/26xx Adapters modules for Linux kernel


%prep
%setup -cT
tar -xf %kernel_src/%module_name-%module_version.tar*
tar -xf %kernel_src/iscsi-%module_name-%module_version.tar*
tar -xf %kernel_src/qla2x00t-%module_version.tar*

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
export CC="gcc${GCC_VERSION:+-$GCC_VERSION}"
%make -C %_usrsrc/linux-%kversion-%flavour SCST_INC_DIR=%_includedir/scst SUBDIRS=$(pwd)/scst/src modules

install -m0644 scst/src/Module.symvers scst/src/dev_handlers/
%make -C %_usrsrc/linux-%kversion-%flavour SCST_INC_DIR=%_includedir/scst SUBDIRS=$(pwd)/scst/src/dev_handlers modules

install -m0644 scst/src/Module.symvers kernel/
%make -C %_usrsrc/linux-%kversion-%flavour SCST_INC_DIR=%_includedir/scst SUBDIRS=$(pwd)/kernel modules
install -m0644 kernel/Module.symvers kernel/isert-scst/
%make -C %_usrsrc/linux-%kversion-%flavour SCST_INC_DIR=%_includedir/scst SUBDIRS=$(pwd)/kernel/isert-scst modules

install -m0644 scst/src/Module.symvers qla2x00t-%module_version/
BUILD_2X_MODULE=y CONFIG_SCSI_QLA_FC=y CONFIG_SCSI_QLA2XXX_TARGET=y \
    %make -C qla2x00t-%module_version KDIR=%_usrsrc/linux-%kversion-%flavour SCST_INC_DIR=%_includedir/scst
install -m0644 qla2x00t-%module_version/Module.symvers qla2x00t-%module_version/qla2x00-target/
BUILD_2X_MODULE=y CONFIG_SCSI_QLA_FC=y CONFIG_SCSI_QLA2XXX_TARGET=y \
    %make -C qla2x00t-%module_version/qla2x00-target KDIR=%_usrsrc/linux-%kversion-%flavour SCST_INC_DIR=%_includedir/scst

%install
mkdir -p %buildroot%module_dir
find -name \*.ko | while read m; do
    install -m0644 $m %buildroot%module_dir/
done

%files
%dir %module_dir
%module_dir/scst*.ko

%files -n kernel-modules-iscsi_scst-%flavour
%module_dir/i*-scst.ko

%files -n kernel-modules-qla2x00t-%flavour
%module_dir/qla*.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
