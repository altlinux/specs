Name:           cmospwd
Version:        5.0
Release:        alt2_3
Summary:        BIOS password cracker utility

Group:          System/Base
License:        GPLv2+
URL:            http://www.cgsecurity.org/wiki/CmosPwd
Source0:        http://www.cgsecurity.org/%{name}-%{version}.tar.bz2

# Fails to build on other arches and not useful there either, I think
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  dos2unix
Source44: import.info

%description
CmosPwd decrypts password stored in cmos used to access BIOS SETUP.
Works with the following BIOSes

    * ACER/IBM BIOS
    * AMI BIOS
    * AMI WinBIOS 2.5
    * Award 4.5x/4.6x/6.0
    * Compaq (1992)
    * Compaq (New version)
    * IBM (PS/2, Activa, Thinkpad)
    * Packard Bell
    * Phoenix 1.00.09.AC0 (1994), a486 1.03, 1.04, 1.10 A03, 4.05 rev 1.02.943,
      4.06 rev 1.13.1107
    * Phoenix 4 release 6 (User)
    * Gateway Solo - Phoenix 4.0 release 6
    * Toshiba
    * Zenith AMI

With CmosPwd, you can also backup, restore and erase/kill cmos.


%prep
%setup -q

rm src/%{name}

dos2unix %{name}.txt
iconv -f iso-8859-1 -t utf-8 %{name}.txt > %{name}.new
touch -r %{name}.txt %{name}.new
mv %{name}.new %{name}.txt


%build
cd src
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
install -D -m 755 src/%{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}


%files
%doc COPYING %{name}.txt
%{_sbindir}/%{name}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt2_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_3
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_2
- initial release by fcimport

