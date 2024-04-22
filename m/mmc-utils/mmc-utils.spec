Name: mmc-utils
Version: 0.0.20240329
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

%files
%doc README
%_bindir/mmc
%_man1dir/mmc.1*

%changelog
* Mon Apr 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.20240329-alt1
- manpage updated

* Thu Nov 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20230928-alt1
- initial
