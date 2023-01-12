%define _unpackaged_files_terminate_build 1
%define dist Email-MessageID
Name: perl-%dist
Version: 1.408
Release: alt1

Summary: Generate world unique message-ids
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 28 2010
BuildRequires: perl-Email-Address perl-Test-Pod perl-Test-Pod-Coverage

%description
Message-ids are optional, but highly recommended, headers that identify
a message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.408-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 1.407-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.406-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.405-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.404-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.402-alt1
- automated CPAN update

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.401-alt1
- 1.35 -> 1.401

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- initial revision
