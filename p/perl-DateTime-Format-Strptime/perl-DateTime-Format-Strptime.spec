%define _unpackaged_files_terminate_build 1
%define module DateTime-Format-Strptime

Name: perl-%module
Epoch: 1
Version: 1.75
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module to parse and format strp and strf time patterns
License: Artistic 2.0
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: perl-DateTime perl-devel perl(Test/Fatal.pm) perl(Package/DeprecationManager.pm) perl(Test/Warnings.pm) perl(Encode.pm)

%description
This module replicates most of Strptime for DateTime. Strptime is the unix
command that is the reverse of Strftime. While Strftime takes a DateTime and
outputs it in a given format, Strptime takes a DateTime and a format and
returns the DateTime object associated.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CONTRIBUTING.md README.md LICENSE Changes
%perl_vendor_privlib/DateTime

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.75-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.74-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.73-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.70-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.68-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.67-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.66-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.65-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.64-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.63-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.62-alt1
- automated CPAN update

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.61-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.60-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.57-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.56-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.55-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.54-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.52-alt1
- automated CPAN update

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 1.5000-alt1
- 1.5000

* Tue Jul 06 2010 Victor Forsiuk <force@altlinux.org> 1.4000-alt1
- 1.4000

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 1.2000-alt1
- 1.2000

* Thu Jul 16 2009 Victor Forsyuk <force@altlinux.org> 1.1000-alt1
- 1.1000

* Tue Mar 24 2009 Victor Forsyuk <force@altlinux.org> 1.0900-alt1
- 1.0900

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 1.0800-alt1
- 1.0800

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 1.0702-alt1
- Initial build.
