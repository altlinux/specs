Name: fortunes-shoo
Version: 20050822
Release: alt2

Summary: Funny statements about fictitious beast called "Shooshpunchik"
Group: Games/Other
License: distributable

BuildArch: noarch

Source: %name-%version.tar.bz2

PreReq: fortune-mod >= 1.0-ipl33mdk

%description
Funny statements about fictitious beast called "Shooshpunchik"

%prep
%setup -q

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__mv shoo %buildroot%_gamesdatadir/fortune
%__mv shoo.dat %buildroot%_gamesdatadir/fortune

%post
echo ""
echo "Warning! Risk of brain damage when read! Do not give it to kids! ;-)"
echo ""

%files
%_gamesdatadir/fortune/*
%doc THANKS

%changelog
* Sun Sep 04 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 20050822-alt2
- Fix stupid bug in script for generation "fortune"-files from plain text.

* Mon Aug 22 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 20050822-alt1
- Initial build for Sisyphus
