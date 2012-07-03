Name: fortunes-fido
Version: 20070503
Release: alt1

Summary: FidoNet members' quotes from many FidoNet conferences
Group: Games/Other
License: distributable

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

# Speed-up build process
AutoReqprov: off
%define _verify_elf_method skip
%define _strip_method none

%description
FidoNet members' quotes from many FidoNet conferences (especially from RU.(LINUX|UNIX) )

%prep
%setup -q

%install
install -pDm0644 fido %buildroot%_gamesdatadir/fortune/fido
strfile %buildroot%_gamesdatadir/fortune/fido %buildroot%_gamesdatadir/fortune/fido.dat

%files
%_gamesdatadir/fortune/*

%changelog
* Thu May 03 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 20070503-alt1
- +21 fortunes
- Speed up build process
- Set Packager tag
- Use tar archive instead of tar.bz2
- Generate .dat-file at build-time

* Sat Jul 23 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 20050721-alt1
- Initial build for Sisyphus
