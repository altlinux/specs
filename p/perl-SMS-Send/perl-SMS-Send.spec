%define _unpackaged_files_terminate_build 1
%define module_name SMS-Send


Name:       perl-%module_name
Version:    1.07
Release:    alt1

Summary:    Driver-based API for sending SMS messages
License:    %perl_license
Group:      Development/Perl
Url:        %CPAN %module_name
Source0:    http://www.cpan.org/authors/id/E/ET/ETHER/%{module_name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-licenses

BuildRequires: perl-devel perl-Module-Pluggable perl-Params-Util perl-Class-Adapter

%description
'SMS::Send' is intended to provide a driver-based single API for sending
SMS and MMS messages. The intent is to provide a single API against which
to write the code to send an SMS message.

At the same time, the intent is to remove the limits of some of the
previous attempts at this sort of API, like "must be free internet-based
SMS services".

'SMS::Send' drivers are installed seperately, and might use the web, email
or physical SMS hardware. It could be a free or paid. The details shouldn't
matter.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%check
%make test

%install
%perl_vendor_install

%files
%doc README META.yml Changes CONTRIBUTING
%perl_vendor_privlib/*

%changelog
* Fri Jul 28 2023 Igor Vlasenko <viy@altlinux.org> 1.07-alt1
- automated CPAN update

* Thu Apr 07 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.06-alt4
- imported from autoimports
- spec's cleanups

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt3_6
- updated by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt3_5
- updated by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt3_4
- updated by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.06-alt3_3
- rebuilt to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_3
- mga update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_2
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 1.06-alt2_1
- rebuilt to get rid of unmets

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- converted for ALT Linux by srpmconvert tools from Mageia's srpm

