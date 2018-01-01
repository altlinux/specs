%define _unpackaged_files_terminate_build 1
%define dist Net-Amazon-EC2
Name: perl-%dist
Version: 0.35
Release: alt1

Summary: Perl interface to the Amazon Elastic Compute Cloud (EC2)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MALLEN/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Digest-HMAC perl-Moose perl-Params-Validate perl-XML-Simple perl-devel perl-libwww perl(Test/Exception.pm) perl(LWP/Protocol/https.pm) perl(inc/Module/Install.pm)

%description
This module is a Perl interface to Amazon's Elastic Compute Cloud.
It uses the Query API to communicate with Amazon's Web Services framework.

%prep
%setup -q -n %{dist}-%{version}
rm -fv lib/Net/Amazon/._EC2.pm
rm -rf inc

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changelog
%perl_vendor_privlib/Net

%changelog
* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt3
- updated build dependencies

* Wed Sep 15 2010 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt2
- remove MacOS X resource fork file

* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt1
- initial build for ALT Linux Sisyphus
