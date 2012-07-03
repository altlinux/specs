Name:           0xFFFF
Version:        0.3.9
Release:        alt2_6
Summary:        The Open Free Fiasco Firmware Flasher

Group:          File tools
License:        GPLv3
URL:            http://www.nopcode.org/0xFFFF/
Source0:        http://www.nopcode.org/0xFFFF/get/%{name}-%{version}.tar.gz

BuildRequires:  libusb-compat-devel libusb-devel
Source44: import.info

%description
The 'Open Free Fiasco Firmware Flasher' aka 0xFFFF utility implements
a free (GPL3) userspace handler for the NOLO bootloader and related
utilities for the Nokia Internet Tablets like flashing setting device
options, packing/unpacking FIASCO firmware format and more.

%prep
%setup -q
sed -i /^LDFLAGS/d config.mk
sed -i "s/^CFLAGS+=.*/CFLAGS+=$RPM_OPT_FLAGS/" config.mk

%build
make -C src %{?_smp_mflags}
make -C logotool CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 src/0xFFFF $RPM_BUILD_ROOT%{_bindir}/0xFFFF
install -m0755 logotool/logotool $RPM_BUILD_ROOT%{_bindir}/logotool



%files
%doc COPYING README INSTALL
%{_bindir}/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1_6
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.9-alt1_5
- new version

