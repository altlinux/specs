Name: rtl_433
Version: 21.05
Release: alt1

Summary: Generic radio data receiver
License: GPLv2
Group: Communications
Url: https://github.com/merbanan/rtl_433

Source: %name-%version-%release.tar

BuildRequires: libusb-devel rtl-sdr-devel

%package devel
Summary: Generic radio data receiver
Group: Development/C

%description
%name (despite the name) is a generic data receiver, mainly
for the 433.92 MHz, 868 MHz (SRD), 315 MHz, and 915 MHz ISM bands.

%description devel
%name (despite the name) is a generic data receiver, mainly
for the 433.92 MHz, 868 MHz (SRD), 315 MHz, and 915 MHz ISM bands.
This  package contains development part of %name

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pm0644 -D man/man1/rtl_433.1 %buildroot%_man1dir/rtl_433.1
mkdir -p %buildroot%_sysconfdir/rtl_433
cp -a conf/*.conf %buildroot%_sysconfdir/rtl_433
touch %buildroot%_sysconfdir/rtl_433/rtl_433.conf

%files
%doc AUTHORS COPYING *.md docs/*.md
%dir %_sysconfdir/rtl_433
%config(noreplace) %_sysconfdir/rtl_433/*.conf

%_bindir/rtl_433
%_man1dir/rtl_433.1*

%files devel
%_includedir/rtl_433*.h
%_pkgconfigdir/rtl433.pc

%changelog
* Thu Sep 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.05-alt1
- 21.05 released

* Mon Mar 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.11-alt1
- 20.11 released

* Sun Nov 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191101-alt1
- initial
