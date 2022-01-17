Name: rtadmin
Version: 2.3
Release: alt1

Summary: Utility for format and administration Rutoken devices
License: Proprietary
URL: https://dev.rutoken.ru/pages/viewpage.action?pageId=7995615
#Download: https://download.rutoken.ru/Rutoken/Utilites/rtadmin/
Group: System/Configuration/Hardware

Source0: %name.zip
Source1: license.ru.html

ExclusiveArch: x86_64 aarch64 armh

BuildRequires: unzip

%description
Utility for format and administration of Rutoken devices: change label, PIN
codes, manage Flash partitions.

%prep
%setup -c %name-%version
cp %SOURCE1 .

%install
%ifarch x86_64
install -Dm 0755 linux-x64/rtadmin %buildroot%_bindir/%name
%endif
%ifarch aarch64
install -Dm 0755 linux-arm64/rtadmin %buildroot%_bindir/%name
%endif
%ifarch armh
install -Dm 0755 linux-armv32/rtadmin %buildroot%_bindir/%name
%endif

%files
%doc license.ru.html
%_bindir/%name

%changelog
* Mon Jan 17 2022 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- New version for x86_64 aarch64 and armh.

* Thu Apr 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- New version with non-truncuted executables

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
