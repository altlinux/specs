Name: fortunes-kernelcookies
Version: 9
Release: alt2

Summary: A collection of funny (or strange) lines from the Linux kernel
Group: Games/Other
License: distributable

URL: http://www.schwarzvogel.de/software-misc.shtml
BuildArch: noarch

Source: kernelcookies-%version.tar

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%description
A collection of funny (or strange) lines from the Linux kernel

%prep
%setup -n kernelcookies-%version

%install
install -pDm0644 kernelcookies %buildroot%_gamesdatadir/fortune/kernelcookies
strfile %buildroot%_gamesdatadir/fortune/kernelcookies %buildroot%_gamesdatadir/fortune/kernelcookies.dat

%files
%_gamesdatadir/fortune/*
%doc CHANGES README THANKS

%changelog
* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 9-alt2
- Rebuilt.

* Fri Aug 10 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 9-alt1
- New version

* Thu Jul 21 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 8-alt1
- Initial build for Sisyphus
