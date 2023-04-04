Name: u-boot-tools
Version: 2023.04
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64 mipsel riscv64 %ix86 x86_64

Provides: uboot-tools = %version-%release
Obsoletes: uboot-tools

Source: %name-%version-%release.tar

BuildRequires: dtc flex libgnutls-devel libssl-devel libtinfo-devel libuuid-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(libfdt)

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains U-Boot tools.

%prep
%setup

%build
%make_build DTC=%_bindir/dtc NO_SDL=1 tools-only_defconfig tools-all

%install
mkdir -p %buildroot%_bindir
install -pm0644 -D tools/env/fw_env.config %buildroot%_sysconfdir/fw_env.config
install -pm0755 tools/{dumpimage,fdtgrep,gen_eth_addr,kwboot,mkimage,mkenvimage,env/fw_printenv} %buildroot%_bindir/
ln -s fw_printenv %buildroot%_bindir/fw_setenv

%files
%config(noreplace) %_sysconfdir/fw_env.config
%_bindir/*

%changelog
* Tue Apr 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.04-alt1
- 2023.04 released

* Tue Jan 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.01-alt1
- 2023.01 released

* Tue Oct 04 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.10-alt1
- 2022.10 released

* Wed Jul 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.07-alt1
- 2022.07 released

* Thu Apr 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.04-alt1
- 2022.04 released

* Thu Jan 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.01-alt1
- 2022.01 released

* Tue Oct 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.10-alt1
- 2021.10 released

* Wed Jul 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.07-alt1
- 2021.07 released

* Wed Apr 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt1
- 2021.04 released

* Mon Feb 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt2
- fw_setenv/fw_printenv and sample config packaged

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt1
- 2021.01 released

* Tue Oct 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.10-alt1
- 2020.10 released

* Fri Jul 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.07-alt1
- 2020.07 released

* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Fri Apr 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Fri Jan 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- initial
