Name: perl-upstreamwatch
Version: 0.7.2.11.6
Release: alt1

Summary: Perl library for parsing watch files
Source0: upstreamwatch.pm

License: %gpl2plus
Group: Development/Perl

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses 
BuildRequires: rpm-build-licenses rpm-build-perl perl-libwww perl-devel perl-Crypt-SSLeay perl-RPM

%description
Upstreamwatch is a perl library for parsing watch files.
It used by uscan utility and several scripts of prometeus
project.

%prep

%build

%install
mkdir -p %buildroot/%perl_vendorlib
install %SOURCE0 %buildroot/%perl_vendorlib

%files
%perl_vendorlib/*

%changelog
* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.2.11.6-alt1
- improved any-archive

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.6-alt2
- more option checks

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.6-alt1
- sync with rpm-uscan 0.6.2.11.6
- interface 0.3 to return options

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.3-alt1
- sync with rpm-uscan 0.6.2.11.3

* Tue Nov 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.1-alt2
- synced versort with rpm-uscan 0.6.2.11.1 - (closes: 26651)

* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.1-alt1
- sync with rpm-uscan 0.6.2.11.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2.11.1-alt1
- sync with rpm-uscan 0.4.2.11.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2.11.1-alt1
- sync with rpm-uscan 0.3.2.11.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2.11.1-alt1
- sync with rpm-uscan 0.2.2.11.1

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2.11.1-alt1
- sync with uscan 2.11.1

* Mon Oct 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1
- restored copyright notices, bugfixes

* Fri Oct 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- multiple bugfixes

* Mon Dec 10 2007 Avramenko Andrew <liks@altlinux.ru> 0.1-alt1
- First draft

