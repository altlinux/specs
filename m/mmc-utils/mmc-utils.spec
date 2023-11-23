Name: mmc-utils
Version: 0.0.20230928
Release: alt1

Summary: Tool for configuring MMC storage devices from userspace
License: GPLv2
Group: System/Kernel and hardware
Url: https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%make_build prefix=%_prefix

%install
%make_install DESTDIR=%buildroot prefix=%_prefix install
install -pm0644 -D man/mmc.1 %buildroot%_man1dir/mmc.1

%files
%doc README
%_bindir/mmc
%_man1dir/mmc.1*

%changelog
* Thu Nov 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20230928-alt1
- initial
