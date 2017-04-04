#ifarch %ix86
#set_verify_elf_method relaxed
#endif

Summary: Utility for format and administration Rutoken devices
Name: rtadmin
Version: 1.1
Release: alt1
License: Proprietary
URL: https://dev.rutoken.ru/pages/viewpage.action?pageId=7995615
#Download: https://download.rutoken.ru/Rutoken/Utilites/rtadmin/
Group: System/Configuration/Hardware
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

%description
Utility for format and administration of Rutoken devices: change label,
PIN codes, manage Flash partitions.

%prep
%setup

%install
%ifarch %ix86
install -Dm 0755 %name-i586 %buildroot%_bindir/%name
%else
install -Dm 0755  %name-x86_64 %buildroot%_bindir/%name
%endif

%files
%doc license.ru.html
%_bindir/%name

%changelog
* Thu Apr 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- New version with non-truncuted executables

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
