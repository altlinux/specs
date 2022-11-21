Name: rtl_433
Version: 22.11
Release: alt1

Summary: Generic radio data receiver
License: GPLv2
Group: Communications
Url: https://github.com/merbanan/rtl_433

Provides: rtl_433-devel = %version-%release
Obsoletes: rtl_433-devel

Source: %name-%version-%release.tar

BuildRequires: cmake libusb-devel rtl-sdr-devel

%description
%name (despite the name) is a generic data receiver, mainly
for the 433.92 MHz, 868 MHz (SRD), 315 MHz, and 915 MHz ISM bands.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
touch %buildroot%_sysconfdir/rtl_433/rtl_433.conf

%files
%doc AUTHORS COPYING *.md docs/*.md
%dir %_sysconfdir/rtl_433
%config(noreplace) %_sysconfdir/rtl_433/*.conf

%_bindir/rtl_433
%_man1dir/rtl_433.1*
%_includedir/rtl_433*.h

%changelog
* Mon Nov 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.11-alt1
- 22.11 released

* Mon Feb 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.12-alt1
- 21.12 released

* Thu Sep 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.05-alt1
- 21.05 released

* Mon Mar 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.11-alt1
- 20.11 released

* Sun Nov 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191101-alt1
- initial
